# 🚀 Cours Complet Azure CLI☁️

## 📚 Table des matières

1. [🎯 Introduction](#introduction)
2. [💿 Installation](#installation)
3. [⚙️ Configuration initiale](#configuration-initiale)
4. [🎮 Commandes de base](#commandes-de-base)
5. [🏗️ Gestion des ressources](#gestion-des-ressources)
6. [💾 Stockage](#stockage)
7. [🌐 Réseaux](#reseaux)
8. [🔐 Sécurité et identité](#securite-et-identite)
9. [📊 Surveillance et logs](#surveillance-et-logs)
10. [🎯 Bonnes pratiques](#bonnes-pratiques)
11. [🚀 Commandes avancées](#commandes-de-base)
12. [📚 Ressources supplémentaires](#ressources-supplementaires)
13. [🎉 Conclusion](#conclusion)

---

## 🎯 Introduction {#introduction}

### Qu'est-ce qu'Azure CLI ?

**Azure CLI** (Command-Line Interface) est un outil en ligne de commande multiplateforme qui permet de gérer les ressources Azure. 💻

#### ✨ Avantages principaux

- 🔄 **Automatisation** : Scriptez vos tâches répétitives
- 🌐 **Multiplateforme** : Windows, macOS, Linux
- ⚡ **Rapidité** : Plus rapide que le portail Azure pour certaines tâches
- 🔧 **Flexibilité** : Intégration avec bash, PowerShell, etc.
- 📦 **Infrastructure as Code** : Gérez votre infrastructure comme du code

---

## 💿 Installation {#installation}

### Windows

```bash
# Téléchargez le MSI depuis le site officiel Microsoft
# Ou utilisez winget
winget install -e --id Microsoft.AzureCLI
```

### macOS 🍎

```bash
# Avec Homebrew
brew update && brew install azure-cli
```

### Linux 🐧

```bash
# Ubuntu/Debian
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# Red Hat/CentOS
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

### Vérification de l'installation ✅

```bash
az --version
```

---

## ⚙️ Configuration initiale {#configuration-initiale}

### 🔐 Connexion à Azure

```bash
# Connexion interactive (ouvre le navigateur)
az login

# Connexion avec un service principal
az login --service-principal -u <app-id> -p <password> --tenant <tenant-id>

# Connexion avec un device code (pour les environnements sans navigateur)
az login --use-device-code
```

### 📋 Lister vos abonnements

```bash
az account list --output table
```

### 🎯 Définir l'abonnement par défaut

```bash
az account set --subscription "Nom de votre abonnement"
# ou
az account set --subscription <subscription-id>
```

### 🔍 Voir l'abonnement actuel

```bash
az account show
```

### 🌍 Configurer la région par défaut

```bash
az configure --defaults location=westeurope
```

---

## 🎮 Commandes de base

### 📖 Aide et documentation

```bash
# Aide générale
az --help

# Aide sur une commande spécifique
az vm --help

# Aide sur une sous-commande
az vm create --help

# Rechercher des commandes
az find "virtual machine"
```

### 🎨 Formats de sortie

```bash
# JSON (par défaut)
az group list

# Table (lisible)
az group list --output table

# YAML
az group list --output yaml

# TSV (pour le scripting)
az group list --output tsv

# Définir le format par défaut
az configure --defaults output=table
```

### 🔎 Requêtes JMESPath

```bash
# Filtrer les résultats
az vm list --query "[?location=='westeurope']"

# Sélectionner des colonnes spécifiques
az vm list --query "[].{Name:name, Location:location, State:powerState}"

# Compter les ressources
az vm list --query "length([])"
```

---

## 🏗️ Gestion des ressources {#gestion-des-ressources}

### 📁 Groupes de ressources

```bash
# Créer un groupe de ressources
az group create \
  --name MonGroupeRG \
  --location westeurope

# Lister tous les groupes de ressources
az group list --output table

# Afficher les détails d'un groupe
az group show --name MonGroupeRG

# Lister les ressources dans un groupe
az resource list --resource-group MonGroupeRG --output table

# Supprimer un groupe de ressources (⚠️ attention!)
az group delete --name MonGroupeRG --yes --no-wait
```

### 💻 Machines virtuelles

#### Créer une VM

```bash
# Créer une VM Linux simple
az vm create \
  --resource-group MonGroupeRG \
  --name MaVM \
  --image Ubuntu2204 \
  --admin-username azureuser \
  --generate-ssh-keys \
  --size Standard_B2s

# Créer une VM Windows
az vm create \
  --resource-group MonGroupeRG \
  --name MaVMWindows \
  --image Win2022Datacenter \
  --admin-username azureuser \
  --admin-password 'MotDePasse123!' \
  --size Standard_B2s
```

#### Gérer les VMs

```bash
# Lister toutes les VMs
az vm list --output table

# Démarrer une VM 🟢
az vm start --resource-group MonGroupeRG --name MaVM

# Arrêter une VM 🔴
az vm stop --resource-group MonGroupeRG --name MaVM

# Redémarrer une VM 🔄
az vm restart --resource-group MonGroupeRG --name MaVM

# Supprimer une VM 🗑️
az vm delete --resource-group MonGroupeRG --name MaVM --yes

# Obtenir l'IP publique
az vm list-ip-addresses --resource-group MonGroupeRG --name MaVM

# Voir l'état de la VM
az vm get-instance-view \
  --resource-group MonGroupeRG \
  --name MaVM \
  --query instanceView.statuses[1]
```

#### Redimensionner une VM 📏

```bash
# Lister les tailles disponibles
az vm list-sizes --location westeurope --output table

# Redimensionner
az vm resize \
  --resource-group MonGroupeRG \
  --name MaVM \
  --size Standard_B4ms
```

### 🌐 App Services

```bash
# Créer un plan App Service
az appservice plan create \
  --name MonPlanAppService \
  --resource-group MonGroupeRG \
  --sku B1 \
  --is-linux

# Créer une Web App
az webapp create \
  --resource-group MonGroupeRG \
  --plan MonPlanAppService \
  --name MonAppUnique123 \
  --runtime "NODE|18-lts"

# Déployer du code
az webapp deployment source config \
  --name MonAppUnique123 \
  --resource-group MonGroupeRG \
  --repo-url https://github.com/user/repo \
  --branch main \
  --manual-integration

# Voir les logs en temps réel 📊
az webapp log tail --name MonAppUnique123 --resource-group MonGroupeRG
```

### 🐳 Azure Container Instances

```bash
# Créer un conteneur
az container create \
  --resource-group MonGroupeRG \
  --name MonConteneur \
  --image mcr.microsoft.com/azuredocs/aci-helloworld \
  --dns-name-label mon-conteneur-unique \
  --ports 80

# Voir les logs
az container logs --resource-group MonGroupeRG --name MonConteneur

# Supprimer le conteneur
az container delete --resource-group MonGroupeRG --name MonConteneur --yes
```

---

## 💾 Stockage {#stockage}

### 📦 Comptes de stockage

```bash
# Créer un compte de stockage
az storage account create \
  --name monstockageunique123 \
  --resource-group MonGroupeRG \
  --location westeurope \
  --sku Standard_LRS

# Obtenir les clés d'accès 🔑
az storage account keys list \
  --resource-group MonGroupeRG \
  --account-name monstockageunique123

# Obtenir la chaîne de connexion
az storage account show-connection-string \
  --name monstockageunique123 \
  --resource-group MonGroupeRG
```

### 📁 Blob Storage

```bash
# Créer un conteneur blob
az storage container create \
  --name monconteneur \
  --account-name monstockageunique123

# Uploader un fichier ⬆️
az storage blob upload \
  --account-name monstockageunique123 \
  --container-name monconteneur \
  --name monfichier.txt \
  --file ./monfichier.txt

# Lister les blobs
az storage blob list \
  --account-name monstockageunique123 \
  --container-name monconteneur \
  --output table

# Télécharger un blob ⬇️
az storage blob download \
  --account-name monstockageunique123 \
  --container-name monconteneur \
  --name monfichier.txt \
  --file ./monfichier-downloaded.txt

# Générer une URL SAS (Shared Access Signature) 🔗
az storage blob generate-sas \
  --account-name monstockageunique123 \
  --container-name monconteneur \
  --name monfichier.txt \
  --permissions r \
  --expiry 2024-12-31T23:59:00Z
```

### 📂 File Shares

```bash
# Créer un partage de fichiers
az storage share create \
  --name monpartage \
  --account-name monstockageunique123

# Uploader un fichier
az storage file upload \
  --share-name monpartage \
  --source ./monfichier.txt \
  --account-name monstockageunique123
```

---

## 🌐 Réseaux {#reseaux}

### 🔌 Réseaux virtuels (VNet)

```bash
# Créer un réseau virtuel
az network vnet create \
  --resource-group MonGroupeRG \
  --name MonVNet \
  --address-prefix 10.0.0.0/16 \
  --subnet-name MonSousReseau \
  --subnet-prefix 10.0.1.0/24

# Créer un sous-réseau supplémentaire
az network vnet subnet create \
  --resource-group MonGroupeRG \
  --vnet-name MonVNet \
  --name AutreSousReseau \
  --address-prefix 10.0.2.0/24

# Lister les VNets
az network vnet list --output table
```

### 🔒 Groupes de sécurité réseau (NSG)

```bash
# Créer un NSG
az network nsg create \
  --resource-group MonGroupeRG \
  --name MonNSG

# Créer une règle de sécurité (ouvrir le port SSH) 🚪
az network nsg rule create \
  --resource-group MonGroupeRG \
  --nsg-name MonNSG \
  --name AllowSSH \
  --protocol tcp \
  --priority 1000 \
  --destination-port-range 22 \
  --access Allow

# Lister les règles
az network nsg rule list \
  --resource-group MonGroupeRG \
  --nsg-name MonNSG \
  --output table
```

### 🌍 IP publiques

```bash
# Créer une IP publique
az network public-ip create \
  --resource-group MonGroupeRG \
  --name MonIPPublique \
  --allocation-method Static \
  --sku Standard

# Voir les détails
az network public-ip show \
  --resource-group MonGroupeRG \
  --name MonIPPublique
```

### ⚖️ Load Balancer

```bash
# Créer un load balancer
az network lb create \
  --resource-group MonGroupeRG \
  --name MonLoadBalancer \
  --sku Standard \
  --public-ip-address MonIPPublique \
  --frontend-ip-name MonFrontend \
  --backend-pool-name MonBackendPool
```

---

## 🔐 Sécurité et identité {#securite-et-identite}

### 👤 Azure Active Directory (Entra ID)

```bash
# Lister les utilisateurs
az ad user list --output table

# Créer un utilisateur
az ad user create \
  --display-name "Jean Dupont" \
  --user-principal-name jean.dupont@votredomaine.com \
  --password "MotDePasse123!" \
  --force-change-password-next-sign-in true

# Lister les groupes
az ad group list --output table

# Créer un groupe
az ad group create \
  --display-name "Développeurs" \
  --mail-nickname developpeurs
```

### 🎫 RBAC (Role-Based Access Control)

```bash
# Lister les rôles disponibles
az role definition list --output table

# Assigner un rôle à un utilisateur 👥
az role assignment create \
  --assignee user@example.com \
  --role "Contributor" \
  --scope /subscriptions/<subscription-id>/resourceGroups/MonGroupeRG

# Lister les attributions de rôles
az role assignment list \
  --resource-group MonGroupeRG \
  --output table

# Supprimer une attribution
az role assignment delete \
  --assignee user@example.com \
  --role "Contributor" \
  --resource-group MonGroupeRG
```

### 🔑 Key Vault

```bash
# Créer un Key Vault
az keyvault create \
  --name MonKeyVaultUnique123 \
  --resource-group MonGroupeRG \
  --location westeurope

# Ajouter un secret 🤫
az keyvault secret set \
  --vault-name MonKeyVaultUnique123 \
  --name MonSecret \
  --value "ValeurSecrete123"

# Récupérer un secret
az keyvault secret show \
  --vault-name MonKeyVaultUnique123 \
  --name MonSecret

# Lister les secrets
az keyvault secret list \
  --vault-name MonKeyVaultUnique123 \
  --output table
```

---

## 📊 Surveillance et logs {#surveillance-et-logs}

### 📈 Azure Monitor

```bash
# Lister les métriques disponibles pour une VM
az monitor metrics list-definitions \
  --resource /subscriptions/<sub-id>/resourceGroups/MonGroupeRG/providers/Microsoft.Compute/virtualMachines/MaVM

# Obtenir des métriques
az monitor metrics list \
  --resource /subscriptions/<sub-id>/resourceGroups/MonGroupeRG/providers/Microsoft.Compute/virtualMachines/MaVM \
  --metric "Percentage CPU" \
  --start-time 2024-01-01T00:00:00Z \
  --end-time 2024-01-02T00:00:00Z
```

### 📝 Logs

```bash
# Créer un Log Analytics Workspace
az monitor log-analytics workspace create \
  --resource-group MonGroupeRG \
  --workspace-name MonWorkspace

# Exécuter une requête
az monitor log-analytics query \
  --workspace MonWorkspace \
  --analytics-query "AzureActivity | limit 10"
```

### 🚨 Alertes

```bash
# Créer une alerte métrique
az monitor metrics alert create \
  --name AlerteCPU \
  --resource-group MonGroupeRG \
  --scopes /subscriptions/<sub-id>/resourceGroups/MonGroupeRG/providers/Microsoft.Compute/virtualMachines/MaVM \
  --condition "avg Percentage CPU > 80" \
  --description "Alerte quand le CPU dépasse 80%"
```

---

## 🎯 Bonnes pratiques {#bonnes-pratiques}

### 1. 🔒 Sécurité

- ✅ Utilisez toujours Azure Key Vault pour les secrets
- ✅ Activez l'authentification multi-facteurs (MFA)
- ✅ Appliquez le principe du moindre privilège (RBAC)
- ✅ Utilisez des identités managées plutôt que des mots de passe
- ❌ Ne stockez jamais de credentials dans vos scripts

### 2. 💰 Optimisation des coûts

```bash
# Analyser les coûts
az consumption usage list \
  --start-date 2024-01-01 \
  --end-date 2024-01-31

# Arrêter les VMs non utilisées
az vm deallocate --resource-group MonGroupeRG --name MaVM
```

### 3. 📝 Scripting et automatisation

```bash
#!/bin/bash
# Exemple de script pour créer une infrastructure complète

# Variables
RESOURCE_GROUP="MonInfra"
LOCATION="westeurope"
VM_NAME="WebServer"

# Créer le groupe de ressources
echo "🏗️ Création du groupe de ressources..."
az group create --name $RESOURCE_GROUP --location $LOCATION

# Créer un réseau virtuel
echo "🌐 Création du réseau virtuel..."
az network vnet create \
  --resource-group $RESOURCE_GROUP \
  --name MyVNet \
  --address-prefix 10.0.0.0/16 \
  --subnet-name MySubnet \
  --subnet-prefix 10.0.1.0/24

# Créer la VM
echo "💻 Création de la VM..."
az vm create \
  --resource-group $RESOURCE_GROUP \
  --name $VM_NAME \
  --image Ubuntu2204 \
  --admin-username azureuser \
  --generate-ssh-keys \
  --vnet-name MyVNet \
  --subnet MySubnet

echo "✅ Infrastructure créée avec succès!"
```

### 4. 🏷️ Tagging des ressources

```bash
# Ajouter des tags lors de la création
az group create \
  --name MonGroupeRG \
  --location westeurope \
  --tags Environment=Production Owner=TeamA CostCenter=IT

# Ajouter des tags à une ressource existante
az resource tag \
  --tags Environment=Development \
  --resource-group MonGroupeRG \
  --name MaVM \
  --resource-type Microsoft.Compute/virtualMachines

# Lister les ressources par tag
az resource list --tag Environment=Production
```

### 5. 🔄 Mode interactif

```bash
# Lancer le mode interactif (plus convivial)
az interactive

# Avantages:
# - Auto-complétion intelligente
# - Documentation intégrée
# - Historique des commandes
# - Colorisation syntaxique
```

### 6. 💡 Astuces de productivité

```bash
# Créer des alias
alias azl='az login'
alias azls='az account list --output table'
alias azvm='az vm list --output table'

# Utiliser des variables d'environnement
export RESOURCE_GROUP="MonGroupeRG"
export LOCATION="westeurope"
az vm create --resource-group $RESOURCE_GROUP --location $LOCATION --name MaVM

# Utiliser des fichiers de configuration
az configure --defaults group=MonGroupeRG location=westeurope

# Exporter les résultats dans un fichier
az vm list > mes-vms.json
```

### 7. 🧪 Tester avant de déployer

```bash
# Mode "what-if" pour les déploiements ARM
az deployment group what-if \
  --resource-group MonGroupeRG \
  --template-file template.json

# Valider un template sans le déployer
az deployment group validate \
  --resource-group MonGroupeRG \
  --template-file template.json
```

---

## 🚀 Commandes avancées {#commandes-de-base}

### Infrastructure as Code avec ARM Templates

```bash
# Déployer un template ARM
az deployment group create \
  --resource-group MonGroupeRG \
  --template-file azuredeploy.json \
  --parameters azuredeploy.parameters.json

# Exporter un template depuis une ressource existante
az group export \
  --name MonGroupeRG \
  --include-parameter-default-value > template.json
```

### 🔄 Gestion multi-abonnements

```bash
# Exécuter une commande sur tous les abonnements
az account list --query "[].id" -o tsv | while read sub; do
  az account set --subscription $sub
  echo "📋 Abonnement: $(az account show --query name -o tsv)"
  az vm list --query "[].name" -o table
done
```

### 🐚 Extensions Azure CLI

```bash
# Lister les extensions disponibles
az extension list-available --output table

# Installer une extension
az extension add --name azure-devops

# Mettre à jour les extensions
az extension update --name azure-devops

# Lister les extensions installées
az extension list --output table
```

---

## 📚 Ressources supplémentaires {#ressources-supplementaires}

### 🔗 Liens utiles

- 📖 [Documentation officielle Azure CLI](https://docs.microsoft.com/cli/azure/)
- 🎓 [Microsoft Learn - Azure CLI](https://learn.microsoft.com/training/modules/control-azure-services-with-cli/)
- 💬 [Forums de la communauté](https://learn.microsoft.com/answers/topics/azure-cli.html)
- 🐛 [Signaler des bugs](https://github.com/Azure/azure-cli/issues)

### 🎓 Certifications Azure

- ☁️ **AZ-900**: Azure Fundamentals
- 🏗️ **AZ-104**: Azure Administrator
- 🔧 **AZ-305**: Azure Solutions Architect

---

## 🎉 Conclusion {#conclusion}

Azure CLI est un outil puissant qui vous permet de :

- ⚡ Automatiser vos tâches Azure
- 🚀 Déployer rapidement des infrastructures
- 🔧 Gérer vos ressources de manière programmatique
- 📊 Intégrer Azure dans vos pipelines CI/CD

### 💪 Prochaines étapes

1. 🔨 Pratiquez avec les commandes de base
2. 🏗️ Créez des scripts d'automatisation
3. 📝 Explorez les templates ARM ou Bicep
4. 🔄 Intégrez Azure CLI dans vos workflows DevOps
5. 🎯 Passez une certification Azure

---
