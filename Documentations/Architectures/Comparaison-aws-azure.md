# Architecture VPC haute disponibilité
## 1. AWS
Voici un schéma textuel détaillé d'une architecture VPC haute disponibilité (HA) sur AWS, incluant VPC, IGW, SG, NAT Gateway, sous-réseaux publics/privés, tables de routage, etc. Il utilise un format ASCII art pour une visualisation claire, avec 2 AZ (Zones de Disponibilité) dans une région.

```
Internet
    |
    v
+--------------------------------+  
| Route 53 (DNS + Health Checks) |
+--------------------------------+
                |
                v
       +-------------------------+
       | Internet Gateway (IGW)  |  <- Attaché au VPC
       +-------------------------+
                   |
                   |  VPC (CIDR: 10.0.0.0/16)
                   |  Security Groups (SG): web-sg, app-sg, db-sg
                   |
                   v
         +--------------------------------------------+
         |                                            |
      AZ1 (eu-west-1a)                              AZ2 (eu-west-1b)
         |                                            |
         v                                            v
    +----------------+                      +----------------+
    | Public Subnet1 |                      | Public Subnet2 |
    | 10.0.1.0/24    |                      | 10.0.2.0/24    |
    |                |                      |                |
    | NAT Gateway1   |                      | NAT Gateway2   |
    | (EIP)          |                      | (EIP)          |
    +----------------+                      +----------------+
            |                                       |
            | Route Table Public:                   | Route Table Public:
            | 0.0.0.0/0 -> IGW                      | 0.0.0.0/0 -> IGW
            |                                       |
            v                                       v
    +-----------------+                   +----------------+
    | ALB (Application|                   | Load Balancer) |  <- Multi-AZ
    +-----------------+                   +----------------+
           |                                      |
           +--------------------------------------+
                             |
                             v
                    +---------------------+
                    | Auto Scaling Group  |
                    | EC2 Instances (App) |  <- SG: app-sg
                    +---------------------+
                             |
                             | Route Table Private:
                             | 0.0.0.0/0 -> NAT (local)
                             |
                    +---------------------+     +---------------------+
                    | Private Subnet1 App |     | Private Subnet2 App |
                    | 10.0.3.0/24         |     | 10.0.4.0/24         |
                    +---------------------+     +---------------------+
                             |                        |
                             |                        |
                             v                        v
                    +------------------------------------------+
                    | RDS Multi-AZ (Primary AZ1 + Standby AZ2) |
                    | Private Subnet DB: 10.0.5.0/24 (AZ1)     |
                    |                  10.0.6.0/24 (AZ2)       |
                    | SG: db-sg                                |
                    +------------------------------------------+
                                       |
                                       v
                            +----------------------+
                            | S3 (via VPC Endpoint)|  <- Pas de NAT nécessaire
                            +----------------------+
```
## Explications des Composants
- **VPC** : Réseau isolé (10.0.0.0/16), spanning 2+ AZ pour HA.
- **IGW** : Accès Internet sortant/entrant pour sous-réseaux publics.
- **NAT Gateway** : Un par AZ (coût ~32$/mois/AZ), permet aux instances privées d'accéder à Internet (mises à jour) sans exposition inbound.
- **Sous-réseaux** : Publics pour ALB/NAT, privés pour apps/DB (au moins /24 par rôle/AZ).
- **Route Tables** : Séparées public (IGW) et privé (NAT) ; propagation automatique.
- **Security Groups (SG)** : Stateful, web-sg (HTTP/HTTPS), app-sg (port app), db-sg (port DB depuis app-sg seulement).
- **Autres** : NACL optionnels pour stateless filtering ; VPC Endpoints pour S3 (privé, gratuit).

Ce design assure 99.99% uptime : trafic via ALB multi-AZ, DB bascule auto, pas de SPOF. [devopssec](https://devopssec.fr/article/construire-infrastructure-aws-hautement-disponible-terraform)

---

## 2. AZURE



### Ton architecture AWS traduite en Azure

```
Internet
    |
    v
+---------------------------+
| Azure DNS (+ Traffic Mgr) |   ← Route 53
+---------------------------+
           |
           v
    +-------------------------+
    |   (natif au VNet)       |   ← Internet Gateway (implicite dans Azure)
    +-------------------------+
                |
    VNet (CIDR: 10.0.0.0/16)
    NSG : web-nsg, app-nsg, db-nsg  ← Security Groups
                |
    +-------------------------------+
    |                               |
  Zone 1 (AZ1)               Zone 2 (AZ2)
    |                               |
+----------------+         +----------------+
| Public Subnet1 |         | Public Subnet2 |
| 10.0.1.0/24    |         | 10.0.2.0/24    |
|                |         |                |
| NAT Gateway1   |         | NAT Gateway2   |  ← même nom dans Azure !
+----------------+         +----------------+
         |                         |
         | Route Table:            | Route Table:
         | 0.0.0.0/0 -> Internet   | 0.0.0.0/0 -> Internet
         |                         |
         v                         v
  +------------------+     +------------------+
  | Application      |     |    Gateway       |  ← ALB = Application Gateway
  | Gateway (WAF)    |     |                  |
  +------------------+     +------------------+
              |                   |
              +--------+----------+
                       |
                       v
             +---------------------+
             |  VM Scale Set (VMSS)|  ← Auto Scaling Group + EC2
             |  + NSG : app-nsg    |
             +---------------------+
                       |
              +--------+--------+
              |                 |
   +------------------+  +------------------+
   | Private Subnet1  |  | Private Subnet2  |  ← mêmes subnets privés
   | 10.0.3.0/24      |  | 10.0.4.0/24      |
   +------------------+  +------------------+
              |                 |
              v                 v
   +---------------------------------------+
   | Azure SQL Flexible Server (HA)        |  ← RDS Multi-AZ
   | Private Subnet DB 10.0.5.0/24 (AZ1)   |
   |                   10.0.6.0/24 (AZ2)   |
   | NSG : db-nsg                          |
   +---------------------------------------+
              |
              v
   +---------------------------+
   | Blob Storage              |  ← S3
   | (via Service/Private      |
   |  Endpoint, sans NAT)      |  ← VPC Endpoint
   +---------------------------+
```

---

## 3. Équivalences AWS ↔ Azure

| Concept | AWS | Azure |
|---|---|---|
| Réseau virtuel | VPC | VNet |
| Sous-réseau | Subnet | Subnet |
| Accès Internet | Internet Gateway (IGW) | pas d'objet explicite (natif au VNet) |
| IP publique sortante | NAT Gateway + EIP | NAT Gateway ou IP publique |
| Firewall réseau (L4) | Security Group + NACL | NSG (Network Security Group) |
| Firewall avancé (L7) | AWS Network Firewall | Azure Firewall |
| DNS | Route 53 | Azure DNS + Private DNS Zone |
| Load Balancer HTTP | ALB | Application Gateway |
| Load Balancer TCP | NLB | Azure Load Balancer |
| Accès privé aux services | VPC Endpoint | Private Endpoint / Service Endpoint |
| Accès SSH/RDP sécurisé | AWS Systems Manager Session Manager | Azure Bastion |
| Peering réseau | VPC Peering | VNet Peering |
| Réseau étendu/hybride | Transit Gateway | Virtual WAN / VNet Hub |
| Multi-AZ | Availability Zones | Availability Zones |
| Auto Scaling + EC2 | Auto Scaling Group | VMSS (VM Scale Set) |
| Base de données managée | RDS Multi-AZ | Azure SQL / Flexible Server |
| Stockage objet | S3 | Blob Storage |

---

## 4. Les différences notables

**1. Internet Gateway**
- AWS → objet **explicite** à créer et attacher au VPC
- Azure → **implicite**, le VNet a un accès internet natif, tu le contrôles via les NSG et routes

**2. Sécurité réseau à deux niveaux sur AWS**
- AWS a **Security Groups** (stateful) + **NACL** (stateless)
- Azure n'a que les **NSG** (stateful) — plus simple

**3. Bastion**
- AWS → **Session Manager** (SSM, sans port ouvert)
- Azure → **Azure Bastion** (RDP/SSH via HTTPS dans le browser)

**4. Endpoint vers les services managés**
- AWS → **VPC Endpoint** (Gateway pour S3/DynamoDB, Interface pour le reste)
- Azure → **Service Endpoint** (simple) ou **Private Endpoint** (IP privée dédiée, plus sécurisé)

---

>En résumé : **les concepts sont quasi identiques**, seuls les noms et quelques subtilités d'implémentation changent. Si tu maîtrises l'un, tu comprends l'autre rapidement ! Tu veux qu'on approfondisse un composant en particulier ?


---

## 5. Détails des différences AWS vs Azure

---

### 1. Internet Gateway

#### AWS — Objet explicite

```
VPC (pas d'accès internet par défaut)
    |
    |  Tu dois :
    |  1. Créer un IGW
    |  2. L'attacher au VPC
    |  3. Ajouter une route 0.0.0.0/0 → IGW dans la route table
    |  4. Assigner une IP publique à l'instance
    |
    v
Internet Gateway (IGW)
    |
    v
Internet
```

Si tu oublies **une seule** de ces étapes → pas d'accès internet. C'est volontaire, AWS part du principe **"tout privé par défaut"**.

---

#### Azure — Implicite

```
VNet (accès internet natif, toujours présent)
    |
    |  Azure crée un "System Route" automatique :
    |  0.0.0.0/0 → Internet  (existe déjà sans rien faire)
    |
    v
Internet (accessible si le NSG le permet)
```

> Dans Azure, **toute VM avec une IP publique peut accéder à internet** sans configuration de routing. Tu **restreins** plutôt que tu **autorises**.

#### Comparaison

| | AWS | Azure |
|---|---|---|
| Accès internet par défaut | ❌ Non | ✅ Oui (si IP publique) |
| Objet à créer | IGW obligatoire | Rien |
| Route à ajouter | Obligatoire | Automatique (System Route) |
| Philosophie | **Opt-in** | **Opt-out** |
| Bloquer internet | Supprimer la route IGW | NSG règle `DenyInternet` ou UDR |

---

### 2. Sécurité réseau — Double couche AWS vs NSG Azure

#### AWS — 2 couches distinctes

```
Trafic entrant
      |
      v
+------------------+
|   NACL           |  ← Couche 1 : au niveau du SUBNET
|  (stateless)     |     - Évalué dans l'ordre des règles (n°100, 200…)
|                  |     - DOIT avoir règle Allow ET la réponse aussi !
|  ex: Allow 443   |     - Bloque → le paquet est détruit
+------------------+
      |
      v
+------------------+
|  Security Group  |  ← Couche 2 : au niveau de l'INSTANCE
|  (stateful)      |     - Si tu autorises l'entrée → retour automatique
|                  |     - Deny implicite sur tout ce qui n'est pas listé
|  ex: Allow 443   |
+------------------+
      |
      v
   EC2 Instance
```

**Exemple concret NACL (stateless) :**
```
# Si tu autorises le port 443 en entrée sur le NACL...
Inbound:  Allow TCP 443 ✅

# ...tu DOIS aussi autoriser les ports éphémères en sortie pour la réponse !
Outbound: Allow TCP 1024-65535 ✅  ← sinon la réponse est bloquée !
```

**Exemple Security Group (stateful) :**
```
# Si tu autorises le port 443 en entrée...
Inbound: Allow TCP 443 ✅

# La réponse passe automatiquement, pas besoin de règle sortante
Outbound: (rien à faire) ✅
```

---

#### Azure — 1 seule couche (NSG)

```
Trafic entrant
      |
      v
+------------------+
|      NSG         |  ← Peut s'appliquer sur le SUBNET ou sur la NIC
|   (stateful)     |     - Toujours stateful (comme SG AWS)
|                  |     - Priorité numérique (100 = priorité haute)
|                  |     - Règles Allow ET Deny explicites possibles
+------------------+
      |
      v
   VM Azure
```

> Azure n'a **pas d'équivalent NACL**. Le NSG fait tout, mais il est **stateful** — donc plus simple à gérer.

#### Comparaison

| | AWS Security Group | AWS NACL | Azure NSG |
|---|---|---|---|
| Niveau | Instance (ENI) | Subnet | Subnet **ou** NIC |
| Stateful | ✅ Oui | ❌ Non | ✅ Oui |
| Règles Deny explicites | ❌ Non (deny implicite) | ✅ Oui | ✅ Oui |
| Ordre d'évaluation | Toutes évaluées | Ordre numérique (stop au 1er match) | Ordre numérique (stop au 1er match) |
| Gérer le retour | Automatique | Manuel (ports éphémères) | Automatique |

---

### 3. Bastion

#### AWS — Session Manager (SSM)

```
Ta machine
    |
    | HTTPS (port 443 uniquement)
    v
AWS Systems Manager
    |
    | Agent SSM installé sur l'EC2
    v
EC2 Instance (AUCUN port 22/3389 ouvert !)
```

**Avantages SSM :**
- Zéro port ouvert sur le Security Group
- Pas d'IP publique nécessaire sur l'EC2
- Logs de session dans CloudWatch / S3
- Pas de serveur à gérer

```bash
# Connexion SSH via SSM sans clé .pem
aws ssm start-session --target i-0123456789abcdef0

# Tunnel pour RDP
aws ssm start-session \
  --target i-0123456789abcdef0 \
  --document-name AWS-StartPortForwardingSession \
  --parameters '{"portNumber":["3389"],"localPortNumber":["3389"]}'
```

---

#### Azure — Bastion

```
Ta machine (browser)
    |
    | HTTPS (port 443)
    v
Azure Bastion (VM dédiée dans subnet "AzureBastionSubnet")
    |
    | RDP/SSH via le VNet (IP privée)
    v
VM cible (AUCUN port 22/3389 exposé à internet)
```

**Particularité Azure Bastion :**
- C'est un **service PaaS managé** mais qui tourne dans **ton VNet**
- Nécessite un **subnet dédié** nommé obligatoirement `AzureBastionSubnet` avec un `/26` minimum
- Interface graphique directement dans le **portail Azure**

---

#### Comparaison

| | AWS Session Manager | Azure Bastion |
|---|---|---|
| Infrastructure à déployer | Aucune (service AWS) | Subnet dédié `/26` dans ton VNet |
| Port ouvert requis | Aucun | Aucun (sur la VM cible) |
| IP publique sur la VM | Non requise | Non requise |
| Mode de connexion | CLI `aws ssm` ou console | Navigateur (portail Azure) |
| Logs de session | CloudWatch / S3 | Azure Monitor |
| Coût | Gratuit (SSM) + coût data | Facturation horaire du Bastion |
| Agent requis | ✅ SSM Agent sur l'instance | ❌ Rien sur la VM |

---

### 4. Endpoints vers les services managés

#### AWS — VPC Endpoint (2 types)

**Type 1 : Gateway Endpoint** (S3 et DynamoDB uniquement)
```
EC2 (subnet privé)
    |
    | Trafic reste dans le réseau AWS
    v
+------------------+
| Gateway Endpoint |  ← Entrée dans la Route Table du subnet
|  (gratuit)       |     Route: pl-xxxxx → vpce-xxxxx
+------------------+
    |
    v
   S3 / DynamoDB  (sans passer par NAT Gateway)
```

**Type 2 : Interface Endpoint (PrivateLink)**
```
EC2 (subnet privé)
    |
    v
+----------------------+
| Interface Endpoint   |  ← Crée une ENI avec IP privée dans ton subnet
| (= PrivateLink)      |     ex: ec2.eu-west-1.vpce.amazonaws.com
| Coût : ~$7/mois/AZ  |
+----------------------+
    |
    v
  Tous les autres services AWS (RDS, SQS, Lambda, etc.)
```

---

#### Azure — Service Endpoint vs Private Endpoint

**Service Endpoint (simple)**
```
VM (subnet privé)
    |
    | Trafic passe par le backbone Azure (optimisé)
    | MAIS l'IP source reste l'IP privée du VNet
    v
+----------------------+
| Service Endpoint     |  ← Activé sur le subnet, pas d'IP dédiée
| (gratuit)            |     ex: Microsoft.Storage, Microsoft.Sql
+----------------------+
    |
    v
  Blob Storage / Azure SQL
  (accessible depuis ce subnet uniquement)
```

**Private Endpoint (le plus sécurisé)**
```
VM (subnet privé)
    |
    v
+----------------------+
| Private Endpoint     |  ← Crée une IP privée dans ton subnet
| (~$7/mois)           |     ex: monstockage.blob.core.windows.net
|                      |         → résolu en 10.0.5.4 (IP privée !)
+----------------------+
    |
    | Trafic 100% privé, jamais sur internet
    v
  Blob Storage / Azure SQL / etc.
```

---

#### Comparaison globale

| | AWS Gateway Endpoint | AWS Interface Endpoint | Azure Service Endpoint | Azure Private Endpoint |
|---|---|---|---|---|
| IP privée dédiée | ❌ | ✅ | ❌ | ✅ |
| Résolution DNS privée | ❌ | ✅ | ❌ | ✅ |
| Coût | Gratuit | ~$7/mois/AZ | Gratuit | ~$7/mois |
| Services supportés | S3, DynamoDB | Tous | Limité (Storage, SQL…) | Tous |
| Trafic sort d'internet | ❌ | ❌ | ❌ | ❌ |
| Niveau de sécurité | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |

> **Règle d'or :** Pour la production, privilégie toujours **Private Endpoint (Azure)** ou **Interface Endpoint (AWS)** — le trafic ne sort jamais d'internet et tu as une IP privée dédiée résolvable par DNS.
