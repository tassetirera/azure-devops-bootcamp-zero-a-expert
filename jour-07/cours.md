# Cours Pratique : Serveur Bastion avec accès Internet pour VM privée via NAT Gateway

## Sommaire

1. [Objectifs et architecture](#1-objectifs-et-architecture)
2. [Prérequis](#2-prérequis)
3. [Création du groupe de ressources](#3-création-du-groupe-de-ressources)
4. [Création du réseau virtuel (VNet) et des sous-réseaux](#4-création-du-réseau-virtuel-vnet-et-des-sous-réseaux)
5. [Création et configuration du groupe de sécurité réseau (NSG) unique](#5-création-et-configuration-du-groupe-de-sécurité-réseau-nsg-unique)
6. [Création des machines virtuelles](#6-création-des-machines-virtuelles)
   - 6.1 VM publique (bastion)
   - 6.2 VM privée
7. [Installation de Nginx sur la VM publique](#7-installation-de-nginx-sur-la-vm-publique)
8. [Connexion à la VM privée via la VM publique (transfert de clé SSH)](#8-connexion-à-la-vm-privée-via-la-vm-publique-transfert-de-clé-ssh)
9. [Problème d’accès Internet sur la VM privée](#9-problème-daccès-internet-sur-la-vm-privée)
10. [Mise en place d’une NAT Gateway pour le subnet privé](#10-mise-en-place-dune-nat-gateway-pour-le-subnet-privé)
11. [Vérification de l’accès Internet sur la VM privée](#11-vérification-de-laccès-internet-sur-la-vm-privée)
12. [Nettoyage des ressources](#12-nettoyage-des-ressources)
13. [Conclusion et bonnes pratiques](#13-conclusion-et-bonnes-pratiques)


## 1. Objectifs et architecture

Dans ce TP, nous allons construire une infrastructure réseau sécurisée sur Azure :

- Un **Virtual Network (VNet)** avec deux sous-réseaux : **public** (pour une VM bastion) et **privé** (pour une VM interne).
- Un **groupe de sécurité réseau (NSG) unique** appliqué aux deux sous-réseaux, avec des règles fines pour autoriser :
  - SSH depuis votre IP publique vers la VM publique.
  - SSH depuis la VM publique vers la VM privée.
- Une **VM publique** (bastion) avec une IP publique, sur laquelle nous installerons Nginx.
- Une **VM privée** sans IP publique, accessible uniquement via la VM publique.
- Nous montrerons que la VM privée ne peut pas accéder à Internet (échec de `apt update`).
- Nous résoudrons ce problème en configurant une **NAT Gateway** pour le sous-réseau privé, permettant ainsi aux VM privées d’avoir un accès sortant vers Internet.

Toutes les étapes seront réalisées avec **Azure CLI** en ligne de commande.

---

## 2. Prérequis

- Un compte Azure avec un abonnement actif.
- Azure CLI installé et configuré (ou utilisation du [Cloud Shell](https://shell.azure.com) directement depuis le portail).
- Connaissances de base en ligne de commande Linux et SSH.
- Votre adresse IP publique (pour la restreindre dans les règles SSH). Vous pouvez l’obtenir avec `curl ifconfig.me`.

---

## 3. Création du groupe de ressources

Nous allons créer un groupe de ressources pour regrouper toutes les ressources du TP.

```bash
# Définir des variables (personnalisez si nécessaire)
RESOURCE_GROUP="rg-bastion-nat"
LOCATION="francecentral"

# Créer le groupe de ressources
az group create --name $RESOURCE_GROUP --location $LOCATION
```

---

## 4. Création du réseau virtuel (VNet) et des sous-réseaux

Nous créons un VNet avec l’espace d’adressage `10.0.0.0/16`, puis deux sous-réseaux :

- **public-subnet** : `10.0.1.0/24` (pour la VM bastion)
- **private-subnet** : `10.0.2.0/24` (pour la VM privée)

```bash
VNET_NAME="vnet-bastion"
SUBNET_PUBLIC="public-subnet"
SUBNET_PRIVATE="private-subnet"

# Créer le VNet
az network vnet create \
  --resource-group $RESOURCE_GROUP \
  --name $VNET_NAME \
  --address-prefix 10.0.0.0/16

# Créer le sous-réseau public
az network vnet subnet create \
  --resource-group $RESOURCE_GROUP \
  --vnet-name $VNET_NAME \
  --name $SUBNET_PUBLIC \
  --address-prefixes 10.0.1.0/24

# Créer le sous-réseau privé
az network vnet subnet create \
  --resource-group $RESOURCE_GROUP \
  --vnet-name $VNET_NAME \
  --name $SUBNET_PRIVATE \
  --address-prefixes 10.0.2.0/24
```

---

## 5. Création et configuration du groupe de sécurité réseau (NSG) unique

Nous allons créer un seul NSG que nous associerons aux deux sous-réseaux. Les règles seront les suivantes :

| Priorité | Nom | Source | Destination | Port | Protocole | Action |
| ---------- | ----- | -------- | ------------- | ------ | ----------- | -------- |
| 100 | AllowSSHFromInternet | Votre IP publique | 10.0.1.0/24 (subnet public) | 22 | TCP | Allow |
| 110 | AllowSSHFromPublicSubnet | 10.0.1.0/24 | 10.0.2.0/24 (subnet privé) | 22 | TCP | Allow |
| 120 | AllowHTTP | Internet | 10.0.1.0/24 | 80 | TCP | Allow |

**Création du NSG :**

```bash
NSG_NAME="nsg-bastion"
az network nsg create \
  --resource-group $RESOURCE_GROUP \
  --name $NSG_NAME
```

**Ajout des règles :**

```bash
# Récupérer votre IP publique (remplacez si nécessaire)
MY_IP=$(curl -s ifconfig.me)

# Règle 100 : SSH depuis votre IP vers le subnet public
az network nsg rule create \
  --resource-group $RESOURCE_GROUP \
  --nsg-name $NSG_NAME \
  --name AllowSSHFromInternet \
  --priority 100 \
  --source-address-prefixes $MY_IP/32 \
  --destination-address-prefixes 10.0.1.0/24 \
  --destination-port-ranges 22 \
  --protocol Tcp \
  --access Allow

# Règle 110 : SSH depuis le subnet public vers le subnet privé
az network nsg rule create \
  --resource-group $RESOURCE_GROUP \
  --nsg-name $NSG_NAME \
  --name AllowSSHFromPublicSubnet \
  --priority 110 \
  --source-address-prefixes 10.0.1.0/24 \
  --destination-address-prefixes 10.0.2.0/24 \
  --destination-port-ranges 22 \
  --protocol Tcp \
  --access Allow

# Règle 120 : HTTP depuis Internet vers le subnet public (pour Nginx)
az network nsg rule create \
  --resource-group $RESOURCE_GROUP \
  --nsg-name $NSG_NAME \
  --name AllowHTTP \
  --priority 120 \
  --source-address-prefixes Internet \
  --destination-address-prefixes 10.0.1.0/24 \
  --destination-port-ranges 80 \
  --protocol Tcp \
  --access Allow
```

**Association du NSG aux deux sous-réseaux :**

```bash
az network vnet subnet update \
  --resource-group $RESOURCE_GROUP \
  --vnet-name $VNET_NAME \
  --name $SUBNET_PUBLIC \
  --network-security-group $NSG_NAME

az network vnet subnet update \
  --resource-group $RESOURCE_GROUP \
  --vnet-name $VNET_NAME \
  --name $SUBNET_PRIVATE \
  --network-security-group $NSG_NAME
```

---

## 6. Création des machines virtuelles

Nous allons créer deux VM Ubuntu 22.04 LTS. La VM publique aura une IP publique, la VM privée non.

### 6.1 VM publique (bastion)

```bash
# Créer une IP publique
az network public-ip create \
  --resource-group $RESOURCE_GROUP \
  --name bastion-pip \
  --sku Standard

# Créer la VM publique dans le subnet public
az vm create \
  --resource-group $RESOURCE_GROUP \
  --name vm-bastion \
  --image Ubuntu2204 \
  --vnet-name $VNET_NAME \
  --subnet $SUBNET_PUBLIC \
  --public-ip-address bastion-pip \
  --admin-username azureuser \
  --generate-ssh-keys \
  --size Standard_B1s
```

La clé SSH publique générée automatiquement est installée sur la VM. La clé privée reste sur votre machine locale (dans `~/.ssh/id_rsa`).

### 6.2 VM privée

```bash
# Créer la VM privée sans IP publique
az vm create \
  --resource-group $RESOURCE_GROUP \
  --name vm-private \
  --image Ubuntu2204 \
  --vnet-name $VNET_NAME \
  --subnet $SUBNET_PRIVATE \
  --public-ip-address "" \
  --admin-username azureuser \
  --generate-ssh-keys \
  --size Standard_B1s
```

**Récupération des adresses IP :**

```bash
# IP publique de la VM bastion
BASTION_PUBLIC_IP=$(az vm show --resource-group $RESOURCE_GROUP --name vm-bastion --show-details --query publicIps -o tsv)
echo "Bastion public IP: $BASTION_PUBLIC_IP"

# IP privée de la VM privée
PRIVATE_IP=$(az vm show --resource-group $RESOURCE_GROUP --name vm-private --show-details --query privateIps -o tsv)
echo "Private VM IP: $PRIVATE_IP"
```

Notez ces adresses, nous en aurons besoin.

---

## 7. Installation de Nginx sur la VM publique

Connectez-vous à la VM publique via SSH :

```bash
ssh azureuser@$BASTION_PUBLIC_IP
```

Une fois connecté, installez Nginx :

```bash
sudo apt update
sudo apt install nginx -y
sudo systemctl enable nginx
```

Vérifiez que Nginx fonctionne en ouvrant un navigateur sur `http://$BASTION_PUBLIC_IP`. Vous devriez voir la page d’accueil par défaut.

Quittez la session (tapez `exit`).

---

## 8. Connexion à la VM privée via la VM publique (transfert de clé SSH)

Pour accéder à la VM privée, nous allons utiliser la VM publique comme passerelle. Nous allons copier notre clé privée SSH sur la VM publique (attention : en environnement de test uniquement). En production, on préfère utiliser l’agent forwarding (`ssh -A`).

**Copie de la clé privée sur la VM publique :**

```bash
scp ~/.ssh/id_rsa azureuser@$BASTION_PUBLIC_IP:~/.ssh/
```

**Connexion à la VM publique :**

```bash
ssh azureuser@$BASTION_PUBLIC_IP
```

**Depuis la VM publique, se connecter à la VM privée en utilisant la clé copiée :**

```bash
# Sur la VM publique
ssh -i ~/.ssh/id_rsa azureuser@$PRIVATE_IP
```

Vous êtes maintenant connecté à la VM privée. Vérifiez avec `hostname`.

Pour revenir sur la VM publique, tapez `exit`. Pour revenir sur votre machine locale, tapez `exit` à nouveau.

---

## 9. Problème d’accès Internet sur la VM privée

Depuis la VM privée, essayez de faire une mise à jour des paquets :

```bash
sudo apt update
```

La commande échoue avec une erreur de résolution DNS ou de connexion. En effet, la VM privée n’a pas d’IP publique et, par défaut, Azure ne fournit pas d’accès Internet sortant aux VM sans IP publique.

Nous allons résoudre cela en configurant une **NAT Gateway** pour le subnet privé.

---

## 10. Mise en place d’une NAT Gateway pour le subnet privé

Une NAT Gateway permet aux ressources d’un subnet sans IP publique d’accéder à Internet en utilisant une adresse IP publique partagée.

**Étapes :**

1. Créer une IP publique pour la NAT Gateway.
2. Créer la ressource NAT Gateway.
3. Associer la NAT Gateway au subnet privé.

**Commandes Azure CLI (depuis votre machine locale ou Cloud Shell) :**

```bash
# Créer une IP publique standard
az network public-ip create \
  --resource-group $RESOURCE_GROUP \
  --name nat-pip \
  --sku Standard

# Créer la NAT Gateway
az network nat gateway create \
  --resource-group $RESOURCE_GROUP \
  --name nat-gateway \
  --public-ip-addresses nat-pip \
  --idle-timeout 10

# Associer la NAT Gateway au subnet privé
az network vnet subnet update \
  --resource-group $RESOURCE_GROUP \
  --vnet-name $VNET_NAME \
  --name $SUBNET_PRIVATE \
  --nat-gateway nat-gateway
```

> **Explication** : L’association de la NAT Gateway modifie automatiquement la table de routage du subnet privé. Azure ajoute une route par défaut (0.0.0.0/0) pointant vers la NAT Gateway.

---

## 11. Vérification de l’accès Internet sur la VM privée

Retournez sur la VM privée (via la VM publique) et réessayez la mise à jour :

```bash
# Depuis votre machine locale, reconnectez-vous à la VM publique
ssh azureuser@$BASTION_PUBLIC_IP

# Puis à la VM privée
ssh -i ~/.ssh/id_rsa azureuser@$PRIVATE_IP

# Maintenant, sur la VM privée
sudo apt update
```

La commande devrait réussir. Vous pouvez même installer un paquet pour confirmer :

```bash
sudo apt install curl -y
```

Le trafic sortant de la VM privée est maintenant NATé vers l’IP publique de la NAT Gateway.

---

## 12. Nettoyage des ressources

Pour éviter des frais inutiles, supprimez le groupe de ressources à la fin du TP :

```bash
az group delete --name $RESOURCE_GROUP --yes --no-wait
```

---

## 13. Conclusion et bonnes pratiques

Nous avons réalisé une architecture complète avec :

- Un **VNet** segmenté en deux sous-réseaux.
- Un **NSG unique** appliqué aux deux sous-réseaux, avec des règles fines pour contrôler les flux.
- Une **VM bastion** avec IP publique pour l’administration.
- Une **VM privée** sans IP publique, accessible uniquement via le bastion.
- Une **NAT Gateway** pour permettre à la VM privée d’accéder à Internet (mises à jour, téléchargements).

**Points de sécurité importants :**

- L’accès SSH à la VM publique est restreint à votre IP uniquement.
- L’accès à la VM privée n’est possible que depuis le subnet public.
- La VM privée n’a pas d’IP publique, donc elle est invisible depuis Internet.
- La NAT Gateway utilise une IP publique statique, ce qui facilite la configuration des pare-feu en aval.

**Pour aller plus loin :**

- Remplacez la VM bastion par le service managé **Azure Bastion** pour un accès sans IP publique.
- Ajoutez un **Azure Firewall** pour un contrôle plus avancé du trafic sortant (filtrage par FQDN).
- Utilisez des **Application Security Groups (ASG)** pour regrouper les VM et simplifier les règles NSG.

Ce TP vous a permis de manipuler les composants réseau fondamentaux d’Azure et de comprendre le pattern du bastion associé à une NAT Gateway pour les accès sortants.