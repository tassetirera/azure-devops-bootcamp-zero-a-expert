# 🌐 Architecture Réseau Haute Disponibilité — AWS vs Azure

**Objectif du cours :** Comprendre et comparer les architectures réseau VPC/VNet entre AWS et Azure, leurs équivalences, leurs différences notables, et les bonnes pratiques à appliquer en production.

---

## 📋 Sommaire

1. [Architecture VPC Haute Disponibilité sur AWS](#1-architecture-vpc-haute-disponibilite-sur-aws)
2. [Architecture VNet Haute Disponibilité sur Azure](#2-architecture-vnet-haute-disponibilite-sur-azure)
3. [Tableau des Équivalences AWS ↔ Azure](#3-equivalences-aws-azure)
4. [Les Différences Notables](#4-les-differences-notables)
5. [Détails approfondis des différences](#5-details-approfondis-des-differences)
6. [Bonnes pratiques & Pièges courants](#6-bonnes-pratiques-pieges-courants)
7. [Outils de diagnostic réseau](#7-outils-de-diagnostic-reseau)
8. [Infrastructure as Code](#8-infrastructure-as-code)
9. [Checklist de sécurité réseau](#9-checklist-de-securite-reseau)
10. [Pour aller plus loin](#10-pour-aller-plus-loin)
11. [Conclusion](#conclusion)

---

## 1. 🟠 Architecture VPC Haute Disponibilité sur AWS {#1-architecture-vpc-haute-disponibilite-sur-aws}

Voici un schéma textuel détaillé d'une architecture VPC haute disponibilité (HA) sur AWS, incluant VPC, IGW, SG, NAT Gateway, sous-réseaux publics/privés, tables de routage, etc. L'exemple utilise **2 Zones de Disponibilité (AZ)** dans une région.

```text
Internet
    |
    v
+---------------------------+  
| Route 53 (DNS + Health Checks) |
+---------------------------+
           |
           v
    +-------------------------+
    | Internet Gateway (IGW)  |  <- Attaché au VPC
    +-------------------------+
           |
           |  VPC (CIDR: 10.0.0.0/16)
           |  Security Groups (SG): web-sg, app-sg, db-sg
           |
    +--------------------------------------------+
    |                                            |
    | AZ1 (eu-west-1a)                  AZ2 (eu-west-1b)
    |                                            |
    +----------------+                 +----------------+
    | Public Subnet1 |                 | Public Subnet2 |
    | 10.0.1.0/24    |                 | 10.0.2.0/24    |
    |                |                 |                |
    | NAT Gateway1   |                 | NAT Gateway2   |
    | (EIP)          |                 | (EIP)          |
    +----------------+                 +----------------+
         |                                   |
         | Route Table Public:              | Route Table Public:
         | 0.0.0.0/0 -> IGW                 | 0.0.0.0/0 -> IGW
         |                                   |
         v                                   v
    +----------------+                 +----------------+
    | ALB (Application|                 | Load Balancer) |  <- Multi-AZ
    +----------------+                 +----------------+
         |                                   |
         +---------------------------+-------+
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
                             v                        v
                    +-------------------------------------+
                    | RDS Multi-AZ (Primary AZ1 + Standby AZ2) |
                    | Private Subnet DB: 10.0.5.0/24 (AZ1)   |
                    |                  10.0.6.0/24 (AZ2)    |
                    | SG: db-sg                              |
                    +-------------------------------------+
                             |
                             v
                    +---------------------+
                    | S3 (via VPC Endpoint)|  <- Pas de NAT nécessaire
                    +---------------------+
```

### 🔍 Explication des Composants

- 🏗️ **VPC** : Réseau isolé (10.0.0.0/16), spanning 2+ AZ pour HA.
- 🌍 **IGW** : Accès Internet sortant/entrant pour sous-réseaux publics.
- 🔁 **NAT Gateway** : Un par AZ (coût ~32$/mois/AZ), permet aux instances privées d'accéder à Internet (mises à jour) sans exposition inbound.
- 🗂️ **Sous-réseaux** : Publics pour ALB/NAT, privés pour apps/DB (au moins /24 par rôle/AZ).
- 🗺️ **Route Tables** : Séparées public (IGW) et privé (NAT) ; propagation automatique.
- 🔒 **Security Groups (SG)** : Stateful, web-sg (HTTP/HTTPS), app-sg (port app), db-sg (port DB depuis app-sg seulement).
- ℹ️ **Autres** : NACL optionnels pour stateless filtering ; VPC Endpoints pour S3 (privé, gratuit).

> - ✅ Ce design assure **99.99% uptime** : trafic via ALB multi-AZ, DB bascule auto, pas de SPOF.
>
>
> - 💡 **Suggestion :** Pour aller encore plus loin en HA, envisage **3 AZ** au lieu de 2 — certaines régions AWS comme `eu-west-1` en proposent jusqu'à 3. Une panne d'AZ sur 3 est mieux absorbée qu'une panne sur 2.

---

## 2. 🔵 Architecture VNet Haute Disponibilité sur Azure {#2-architecture-vnet-haute-disponibilite-sur-azure}

Voici l'architecture AWS traduite dans l'écosystème Azure :

```text
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
   | Private Subnet DB 10.0.5.0/24 (AZ1)  |
   |                   10.0.6.0/24 (AZ2)  |
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

> 💡 **Suggestion Azure :** Ajoute un **Azure DDoS Protection Standard** sur ton VNet en production. La version Basic est gratuite mais limitée — la version Standard (~2900$/mois) offre une protection adaptative et des rapports d'attaque.

---

## 3. 🔄 Équivalences AWS ↔ Azure {#3-equivalences-aws-azure}

| Concept | 🟠 AWS | 🔵 Azure |
| --- | --- | --- |
| Réseau virtuel | VPC | VNet |
| Sous-réseau | Subnet | Subnet |
| Accès Internet | Internet Gateway (IGW) | Pas d'objet explicite (natif au VNet) |
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

> 💡 **Suggestion :** Il existe un concept sans équivalent direct que tu dois connaître : le **AWS Transit Gateway** (et son équivalent Azure **Virtual WAN**). C'est indispensable dès que tu as **plusieurs VPC/VNets** à interconnecter — sans ça, tu te retrouves avec un maillage de peerings ingérable.

---

## 4. ⚠️ Les Différences Notables {#4-les-differences-notables}

### **4.1. 🌍 Internet Gateway**

- 🟠 AWS → objet **explicite** à créer et attacher au VPC
- 🔵 Azure → **implicite**, le VNet a un accès internet natif, tu le contrôles via les NSG et routes

### **4.2. 🔒 Sécurité réseau à deux niveaux sur AWS**

- 🟠 AWS a **Security Groups** (stateful) + **NACL** (stateless)
- 🔵 Azure n'a que les **NSG** (stateful) — plus simple

### **4.3. 🛡️ Bastion**

- 🟠 AWS → **Session Manager** (SSM, sans port ouvert)
- 🔵 Azure → **Azure Bastion** (RDP/SSH via HTTPS dans le browser)

### **4.4. 🔗 Endpoint vers les services managés**

- 🟠 AWS → **VPC Endpoint** (Gateway pour S3/DynamoDB, Interface pour le reste)
- 🔵 Azure → **Service Endpoint** (simple) ou **Private Endpoint** (IP privée dédiée, plus sécurisé)

---

## 5. 🔬 Détails approfondis des différences {#5-details-approfondis-des-differences}

---

### 5.1 🌍 Internet Gateway

#### 🟠 AWS — Objet explicite

```text
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

> ⚠️ Si tu oublies **une seule** de ces étapes → pas d'accès internet. C'est volontaire, AWS part du principe **"tout privé par défaut"**.

#### 🔵 Azure — Implicite

```text
VNet (accès internet natif, toujours présent)
    |
    |  Azure crée un "System Route" automatique :
    |  0.0.0.0/0 → Internet  (existe déjà sans rien faire)
    |
    v
Internet (accessible si le NSG le permet)
```

> 💡 Dans Azure, **toute VM avec une IP publique peut accéder à internet** sans configuration de routing. Tu **restreins** plutôt que tu **autorises**.

#### 📊 Comparaison

| | 🟠 AWS | 🔵 Azure |
| --- | --- | --- |
| Accès internet par défaut | ❌ Non | ✅ Oui (si IP publique) |
| Objet à créer | IGW obligatoire | Rien |
| Route à ajouter | Obligatoire | Automatique (System Route) |
| Philosophie | **Opt-in** | **Opt-out** |
| Bloquer internet | Supprimer la route IGW | NSG règle `DenyInternet` ou UDR |

> - 🧠 **À savoir — Egress-Only IGW (AWS) :** Pour les ressources en IPv6 qui doivent accéder à internet en sortie seulement (sans être joignables depuis l'extérieur), AWS propose un **Egress-Only Internet Gateway**. C'est l'équivalent IPv6 du NAT Gateway, et beaucoup l'ignorent.
>
> - 🧠 **À savoir — UDR Azure (User Defined Routes) :** Dans Azure, si tu veux forcer tout le trafic sortant à passer par un **Azure Firewall** ou un **NVA (Network Virtual Appliance)**, tu crées une UDR avec `0.0.0.0/0 → IP du Firewall`. C'est le mécanisme clé pour inspecter tout le trafic est/ouest et nord/sud.

---

### 5.2 🔒 Sécurité réseau — Double couche AWS vs NSG Azure

#### 🟠 AWS — 2 couches distinctes

```text
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

**⚠️ Exemple concret NACL (stateless) :**

```text
# Si tu autorises le port 443 en entrée sur le NACL...
Inbound:  Allow TCP 443 ✅

# ...tu DOIS aussi autoriser les ports éphémères en sortie pour la réponse !
Outbound: Allow TCP 1024-65535 ✅  ← sinon la réponse est bloquée !
```

**✅ Exemple Security Group (stateful) :**

```text
# Si tu autorises le port 443 en entrée...
Inbound: Allow TCP 443 ✅

# La réponse passe automatiquement, pas besoin de règle sortante
Outbound: (rien à faire) ✅
```

#### 🔵 Azure — 1 seule couche (NSG)

```text
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

> 💡 Azure n'a **pas d'équivalent NACL**. Le NSG fait tout, mais il est **stateful** — donc plus simple à gérer.

##### 📊 **Comparaison**

| | 🟠 AWS Security Group | 🟠 AWS NACL | 🔵 Azure NSG |
| --- | --- | --- | --- |
| Niveau | Instance (ENI) | Subnet | Subnet **ou** NIC |
| Stateful | ✅ Oui | ❌ Non | ✅ Oui |
| Règles Deny explicites | ❌ Non (deny implicite) | ✅ Oui | ✅ Oui |
| Ordre d'évaluation | Toutes évaluées | Ordre numérique (stop au 1er match) | Ordre numérique (stop au 1er match) |
| Gérer le retour | Automatique | Manuel (ports éphémères) | Automatique |

> - 🧠 **À savoir — NSG Flow Logs (Azure) :** Azure permet d'activer les **NSG Flow Logs** → les logs sont envoyés dans un Storage Account et analysables avec **Traffic Analytics** (dans Network Watcher). C'est indispensable pour auditer qui communique avec qui dans ton réseau.
>
> - 🧠 **À savoir — VPC Flow Logs (AWS) :** Équivalent AWS : les **VPC Flow Logs**, activables au niveau du VPC, subnet ou ENI. Envoi vers CloudWatch Logs ou S3. Utile pour détecter des connexions anormales ou déboguer des refus de trafic.
>
> - ⚠️ **Piège fréquent sur Azure :** Si tu appliques un NSG **à la fois sur le subnet ET sur la NIC**, les deux sont évalués. Une règle permissive sur le subnet ne suffit pas si la NIC a un Deny. Les deux doivent autoriser le trafic.

---

### 5.3 🛡️ Bastion

#### 🟠 AWS — Session Manager (SSM)

```text
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

**✅ Avantages SSM :**

- 🔒 Zéro port ouvert sur le Security Group
- 🚫 Pas d'IP publique nécessaire sur l'EC2
- 📋 Logs de session dans CloudWatch / S3
- 🛠️ Pas de serveur à gérer

```bash
# 💻 Connexion SSH via SSM sans clé .pem
aws ssm start-session --target i-0123456789abcdef0

# 🖥️ Tunnel pour RDP
aws ssm start-session \
  --target i-0123456789abcdef0 \
  --document-name AWS-StartPortForwardingSession \
  --parameters '{"portNumber":["3389"],"localPortNumber":["3389"]}'
```

#### 🔵 Azure — Bastion

```text
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

##### **⚙️ Particularités Azure Bastion :**

- 🏗️ C'est un **service PaaS managé** mais qui tourne dans **ton VNet**
- 📐 Nécessite un **subnet dédié** nommé obligatoirement `AzureBastionSubnet` avec un `/26` minimum
- 🖥️ Interface graphique directement dans le **portail Azure**

##### **📊 Comparaison**

| | 🟠 AWS Session Manager | 🔵 Azure Bastion |
| --- | --- | --- |
| Infrastructure à déployer | Aucune (service AWS) | Subnet dédié `/26` dans ton VNet |
| Port ouvert requis | Aucun | Aucun (sur la VM cible) |
| IP publique sur la VM | Non requise | Non requise |
| Mode de connexion | CLI `aws ssm` ou console | Navigateur (portail Azure) |
| Logs de session | CloudWatch / S3 | Azure Monitor |
| Coût | Gratuit (SSM) + coût data | Facturation horaire du Bastion |
| Agent requis | ✅ SSM Agent sur l'instance | ❌ Rien sur la VM |

> - 🧠 **À savoir — Azure Bastion SKU :** Il existe deux SKUs pour Azure Bastion :
>
>   - **Basic** : RDP/SSH depuis le portail uniquement
>   - **Standard** : ajoute le tunneling natif (`az network bastion ssh`), le support des VMs sans IP publique depuis CLI, et le peering VNet. En production, préfère le **Standard**.
>
> - 🧠 **À savoir — Just-In-Time (JIT) Access (Azure) :** Une alternative légère à Bastion pour les environnements de dev — le **JIT Access** dans Microsoft Defender for Cloud ouvre le port SSH/RDP temporairement (ex: 3h) uniquement pour ton IP. Pas aussi sécurisé que Bastion, mais pratique et peu coûteux.
>
> - 🧠 **À savoir — AWS Instance Connect :** Alternative plus légère à SSM sur AWS, **EC2 Instance Connect** permet une connexion SSH temporaire en poussant une clé publique éphémère (valable 60 secondes). Nécessite une IP publique ou un endpoint dédié, mais pas d'agent supplémentaire.

---

### 5.4 🔗 Endpoints vers les services managés

#### 🟠 AWS — VPC Endpoint (2 types)

**Type 1 : Gateway Endpoint** *(S3 et DynamoDB uniquement)*

```text
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

#### **Type 2 : Interface Endpoint (PrivateLink)**

```text
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

#### 🔵 Azure — Service Endpoint vs Private Endpoint

##### **Service Endpoint (simple)**

```text
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

##### **Private Endpoint (le plus sécurisé) 🔐**

```text
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

#### 📊 Comparaison globale

| | 🟠 AWS Gateway Endpoint | 🟠 AWS Interface Endpoint | 🔵 Azure Service Endpoint | 🔵 Azure Private Endpoint |
| --- | --- | --- | --- | --- |
| IP privée dédiée | ❌ | ✅ | ❌ | ✅ |
| Résolution DNS privée | ❌ | ✅ | ❌ | ✅ |
| Coût | Gratuit | ~$7/mois/AZ | Gratuit | ~$7/mois |
| Services supportés | S3, DynamoDB | Tous | Limité (Storage, SQL…) | Tous |
| Trafic sort d'internet | ❌ | ❌ | ❌ | ❌ |
| Niveau de sécurité | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |

> - 🏆 **Règle d'or :** Pour la production, privilégie toujours **Private Endpoint (Azure)** ou **Interface Endpoint (AWS)** — le trafic ne sort jamais d'internet et tu as une IP privée dédiée résolvable par DNS.
>
> - ⚠️ **Piège DNS avec Private Endpoint (Azure) :** Quand tu crées un Private Endpoint, le nom DNS public du service (ex: `moncompte.blob.core.windows.net`) doit être résolu vers l'IP privée **depuis ton VNet**. Pour ça, tu dois créer une **Private DNS Zone** et la lier à ton VNet. Sans cette étape, le DNS continue de résoudre vers l'IP publique même si le Private Endpoint existe !
>
> - 🧠 **À savoir — AWS PrivateLink pour ses propres services :** AWS PrivateLink ne sert pas qu'aux services AWS — tu peux l'utiliser pour **exposer ton propre service** (derrière un NLB) de façon privée à d'autres VPCs ou comptes AWS. Très utilisé en architecture multi-comptes ou pour des éditeurs SaaS.

---

## 6. 🏗️ Bonnes pratiques & Pièges courants {#6-bonnes-pratiques-pieges-courants}

### 6.1 📐 Plan d'adressage IP — Ne pas bâcler le CIDR

> ⚠️ **Le plus gros regret des équipes cloud :** avoir mal planifié leur plage IP au départ.

```text
✅ Bonnes pratiques CIDR :

- VPC/VNet principal     : /16  (65 534 IPs)  → suffisant pour grandir
- Subnet par rôle/AZ     : /24  (254 IPs)     → standard
- AzureBastionSubnet     : /26  minimum       → obligatoire Azure
- GatewaySubnet (Azure)  : /27  minimum       → pour VPN/ExpressRoute
- Subnet de transit/hub  : /28                → juste assez

❌ Erreurs fréquentes :
- Utiliser 10.0.0.0/8 pour tout → impossible à filtrer proprement
- Subnets /29 ou /30 → trop petits, bloquent la scalabilité
- Chevauchement de CIDRs entre VPCs → impossible de peerer ensuite
```

> 💡 **Suggestion :** Utilise un outil comme **[ipplan.io](https://ipplan.io)** ou une simple feuille Excel pour documenter ton plan d'adressage AVANT de créer quoi que ce soit. Une fois les ressources déployées, changer le CIDR d'un VNet/VPC est extrêmement douloureux.

### 6.2 🔒 Principe du moindre privilège sur les Security Groups / NSG

```text
❌ Mauvaise pratique (trop permissive) :
Inbound : Allow ALL from 0.0.0.0/0

✅ Bonne pratique (least privilege) :
Inbound : Allow TCP 443 from ALB-SG (référencer le SG source, pas une IP)
Inbound : Allow TCP 5432 from App-SG only
```

> - 💡 **Suggestion AWS :** Utilise les **Security Group References** plutôt que des plages IP. En référençant un SG source (`app-sg → db-sg`), la règle s'adapte automatiquement quand des instances entrent/sortent du groupe, sans maintenance manuelle des IPs.
>
> - 💡 **Suggestion Azure :** Utilise les **Application Security Groups (ASG)** — l'équivalent Azure des SG References. Tu tagges tes VMs dans un ASG (`asg-web`, `asg-app`) et tu écris des règles NSG en ciblant les ASGs, pas les IPs.

### 6.3 💸 Optimisation des coûts réseau

| Source de coût | 🟠 AWS | 🔵 Azure |
| --- | --- | --- |
| NAT Gateway | ~32$/mois + 0.045$/GB | ~32$/mois + 0.045$/GB |
| Data Transfer inter-AZ | 0.01$/GB dans les 2 sens | Gratuit dans la même région |
| VPC Peering data transfer | 0.01$/GB | Gratuit (même région) |
| Endpoints | Gratuit (Gateway) / ~7$/mois (Interface) | Gratuit (Service) / ~7$/mois (Private) |

> - 💡 **Suggestion AWS :** Le **data transfer inter-AZ** est souvent une surprise sur la facture. Si ton ALB dans AZ1 redirige vers une instance en AZ2, tu paies 0.01$/GB. Active l'option **"Cross-Zone Load Balancing"** avec précaution et préfère l'affinité de zone quand possible.
>
> - 💡 **Suggestion :** Si tes instances privées font beaucoup de téléchargements (ex: mises à jour de paquets), un **Gateway Endpoint S3 (AWS)** ou un **Service Endpoint Storage (Azure)** peut économiser des centaines d'euros/mois en évitant de passer par le NAT Gateway.

### 6.4 🌐 Connectivité hybride (On-Premise ↔ Cloud)

| Méthode | 🟠 AWS | 🔵 Azure | Usage |
| --- | --- | --- | --- |
| VPN chiffré | Site-to-Site VPN | VPN Gateway | Connexion chiffrée, <1 Gbps |
| Lien dédié | AWS Direct Connect | Azure ExpressRoute | Haute bande passante, SLA |
| Réseau étendu | Transit Gateway | Virtual WAN | Multi-sites, hub-and-spoke |

> 💡 **Suggestion :** Pour un environnement hybride, opte pour **ExpressRoute (Azure)** ou **Direct Connect (AWS)** dès que tu as des charges de travail sensibles ou à haute volumétrie. Le VPN IPSec passe par internet et a une latence variable — problématique pour les bases de données ou les appels applicatifs fréquents.

---

## 7. 🔧 Outils de diagnostic réseau {#7-outils-de-diagnostic-reseau}

### 7.1 🟠 AWS — Outils natifs

```bash
# 🔍 VPC Reachability Analyzer
# Vérifie la connectivité entre deux ressources AWS sans envoyer de trafic réel
aws ec2 start-network-insights-analysis \
  --network-insights-path-id nip-xxxx

# 📊 VPC Flow Logs — Activer sur un VPC
aws ec2 create-flow-logs \
  --resource-type VPC \
  --resource-ids vpc-xxxx \
  --traffic-type ALL \
  --log-destination-type cloud-watch-logs \
  --log-group-name /aws/vpc/flowlogs

# 🧪 Tester la connectivité depuis une instance
# (via SSM, sans ouvrir de port)
aws ssm send-command \
  --instance-ids i-xxxx \
  --document-name "AWS-RunShellScript" \
  --parameters 'commands=["curl -v telnet://10.0.3.5:5432"]'
```

### 7.2 🔵 Azure — Outils natifs

```powershell
# 🔍 IP Flow Verify — Savoir si un NSG bloque le trafic
az network watcher test-ip-flow \
  --vm myVM \
  --direction Inbound \
  --protocol TCP \
  --local 10.0.0.4:* \
  --remote 20.58.66.84:5500 \
  --resource-group myRG

# 🗺️ Topology — Vue graphique du réseau
# Azure Portal → Network Watcher → Topology

# 📊 Connection Monitor — Test de connectivité continu
az network watcher connection-monitor create \
  --name myMonitor \
  --resource-group myRG \
  --source-resource myVM \
  --dest-address 10.0.1.5 \
  --dest-port 443

# 🔎 Next Hop — Quelle route est utilisée ?
az network watcher show-next-hop \
  --vm myVM \
  --resource-group myRG \
  --source-ip 10.0.0.4 \
  --dest-ip 10.0.1.5
```

> 💡 **Suggestion :** L'outil **"Next Hop"** de Network Watcher est sous-utilisé mais extrêmement puissant. Il te dit exactement quelle route sera suivie par un paquet (System Route, UDR, VPN, etc.) — parfait pour déboguer un problème de routage sans avoir à lancer de vrai trafic.

---

## 8. 🤖 Infrastructure as Code {#8-infrastructure-as-code}

> 💡 **Suggestion forte :** Ne crée **jamais** une architecture réseau manuellement en production. Utilise toujours de l'IaC pour la reproductibilité, l'auditabilité et la gestion des changements.

### 8.1 🟠 AWS — Terraform (exemple VPC)

```hcl
# VPC avec subnets publics et privés sur 2 AZ
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"

  name = "prod-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["eu-west-1a", "eu-west-1b"]
  public_subnets  = ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnets = ["10.0.3.0/24", "10.0.4.0/24"]

  enable_nat_gateway     = true
  single_nat_gateway     = false  # Un NAT par AZ pour HA
  enable_vpn_gateway     = false
  enable_dns_hostnames   = true

  # Tags recommandés pour EKS si utilisé
  public_subnet_tags  = { "kubernetes.io/role/elb" = 1 }
  private_subnet_tags = { "kubernetes.io/role/internal-elb" = 1 }
}
```

### 8.2 🔵 Azure — Terraform (exemple VNet)

```hcl
# VNet avec subnets et NSG
resource "azurerm_virtual_network" "main" {
  name                = "prod-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = "westeurope"
  resource_group_name = azurerm_resource_group.main.name
}

resource "azurerm_subnet" "app" {
  name                 = "app-subnet"
  resource_group_name  = azurerm_resource_group.main.name
  virtual_network_name = azurerm_virtual_network.main.name
  address_prefixes     = ["10.0.3.0/24"]
}

resource "azurerm_network_security_group" "app" {
  name                = "app-nsg"
  location            = "westeurope"
  resource_group_name = azurerm_resource_group.main.name

  security_rule {
    name                       = "Allow-HTTPS"
    priority                   = 100
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "443"
    source_address_prefix      = "10.0.1.0/24"
    destination_address_prefix = "*"
  }
}

# Association NSG ↔ Subnet
resource "azurerm_subnet_network_security_group_association" "app" {
  subnet_id                 = azurerm_subnet.app.id
  network_security_group_id = azurerm_network_security_group.app.id
}
```

> 💡 **Suggestion :** Pour AWS, le module **terraform-aws-modules/vpc** est un standard de l'industrie — inutile de réinventer la roue. Pour Azure, explore les **Azure Verified Modules** (AVM) sur le registry Terraform, maintenus directement par Microsoft.

---

## 9. ✅ Checklist de sécurité réseau {#9-checklist-de-securite-reseau}

### 9.1 🟠 AWS

- [ ] Aucune instance avec `0.0.0.0/0` en inbound sur le port 22 ou 3389
- [ ] Toutes les instances de prod dans des **subnets privés**
- [ ] **VPC Flow Logs** activés et archivés (min. 90 jours)
- [ ] **S3 Gateway Endpoint** configuré pour éviter le transit par NAT
- [ ] **GuardDuty** activé (détection d'anomalies réseau)
- [ ] Aucun Security Group avec une règle `Allow ALL Outbound 0.0.0.0/0` en prod
- [ ] **AWS Config** activé pour détecter les changements de SG non conformes
- [ ] Accès admin via **SSM Session Manager** uniquement (pas de bastion SSH classique)

### 9.2 🔵 Azure

- [ ] Aucune VM avec RDP/SSH exposé directement sur internet (NSG)
- [ ] **NSG Flow Logs** activés + **Traffic Analytics** configuré
- [ ] **Azure Defender for Cloud** activé (niveau Standard en prod)
- [ ] Tous les services managés (SQL, Storage) avec **Private Endpoint** en prod
- [ ] **Azure Firewall** ou **NVA** pour inspecter le trafic est/ouest
- [ ] **DDoS Protection Basic** au minimum, **Standard** pour les environnements critiques
- [ ] Accès admin via **Azure Bastion Standard** uniquement
- [ ] **Private DNS Zones** configurées pour chaque Private Endpoint

---

## 10. 📚 Pour aller plus loin {#10-pour-aller-plus-loin}

### 10.1 🎓 Certifications recommandées

| Niveau | 🟠 AWS | 🔵 Azure |
| --- | --- | --- |
| Débutant | AWS Cloud Practitioner | AZ-900 Azure Fundamentals |
| Intermédiaire | **AWS Solutions Architect Associate** | **AZ-104 Azure Administrator** |
| Réseau spécialisé | AWS Advanced Networking Specialty | AZ-700 Azure Network Engineer |
| Sécurité | AWS Security Specialty | AZ-500 Security Engineer |

> 💡 **Suggestion :** Si tu travailles déjà sur Azure au quotidien (comme on le voit dans notre contexte), commence par **AZ-104** — il couvre exactement les sujets de ce cours (VNet, NSG, Bastion, Load Balancer, Private Endpoint). Compte 2-3 mois de préparation.

### 10.2 🛠️ Outils utiles à connaître

| Outil | Usage |
| --- | --- |
| **draw.io / Diagrams.net** | Schémas d'architecture réseau (templates AWS/Azure natifs) |
| **CloudMapper (AWS)** | Visualisation automatique de ton VPC en graphe |
| **Azure Network Watcher** | Diagnostic réseau natif Azure (topology, flow verify, next hop) |
| **Wireshark + VPC Tap** | Capture de paquets sur instances EC2 (via Traffic Mirroring) |
| **nmap** | Scanner de ports pour valider l'exposition d'une machine |
| **mtr / traceroute** | Diagnostic de routage et de latence |
| **infracost** | Estimation du coût d'une infrastructure Terraform avant déploiement |

### 10.3 📖 Ressources officielles

- 📘 **AWS** : [docs.aws.amazon.com/vpc](https://docs.aws.amazon.com/vpc/latest/userguide/)
- 📘 **Azure** : [learn.microsoft.com/azure/virtual-network](https://learn.microsoft.com/azure/virtual-network/)
- 📘 **Well-Architected Framework AWS** : [aws.amazon.com/architecture/well-architected](https://aws.amazon.com/architecture/well-architected/)
- 📘 **Well-Architected Framework Azure** : [learn.microsoft.com/azure/well-architected](https://learn.microsoft.com/azure/well-architected/)

---

## ✅ 11. Conclusion {#conclusion}

Les concepts réseau entre AWS et Azure sont **quasi identiques** — seuls les noms et quelques subtilités d'implémentation changent.

| 💡 Ce qu'il faut retenir | |
| --- | --- |
| 🟠 AWS part du principe **"tout privé par défaut"** (opt-in) | 🔵 Azure est **ouvert par défaut**, tu restreins (opt-out) |
| 🟠 AWS a **2 couches** de sécurité réseau (SG + NACL) | 🔵 Azure n'en a qu'**une seule** (NSG, plus simple) |
| 🟠 SSM = **sans infrastructure**, sans agent visible | 🔵 Bastion = **service dans ton VNet**, subnet dédié requis |
| 🟠 Gateway Endpoint = **gratuit** mais limité à S3/DynamoDB | 🔵 Service Endpoint = **gratuit** mais sans IP privée dédiée |
| ⚠️ **Planifie tes CIDRs avant tout** | Un mauvais plan IP coûte très cher à corriger |
| 🤖 **Toujours de l'IaC en production** | Terraform, Bicep ou CloudFormation — jamais à la main |
| 🔍 **Active les Flow Logs dès le départ** | Impossibles à activer rétrospectivement sur un incident passé |

---

Dans Azure, un **SKU** (Stock Keeping Unit) désigne une offre ou un niveau de service spécifique pour un produit cloud, définissant ses performances, fonctionnalités et tarification. [learn.microsoft](https://learn.microsoft.com/fr-fr/azure/load-balancer/skus)
Contrairement au SKU logistique (précédemment discuté), il identifie des configurations comme les VM, Load Balancer ou stockage, par exemple "Standard_LRS" pour du stockage standard localement redondant. [learn.microsoft](https://learn.microsoft.com/fr-fr/rest/api/storagerp/srp_sku_types)

## Exemples par service  

- **Load Balancer** : SKU Basic (retiré), Standard (HA, diagnostics) et Gateway, avec Standard nécessitant des IP publiques Standard. [learn.microsoft](https://learn.microsoft.com/fr-fr/azure/load-balancer/skus)
- **VM et clusters** : Familles comme Dsv3-Type1 (calcul optimisé), Easv5 (stockage Premium) ; disponibilité varie par région/abonnement. [learn.microsoft](https://learn.microsoft.com/fr-fr/azure/data-explorer/manage-cluster-choose-sku)
- **Stockage** : Standard_LRS/GRS/ZRS (redondance), Premium_LRS (hautes perf.). [learn.microsoft](https://learn.microsoft.com/fr-fr/rest/api/storagerp/srp_sku_types)

## Gestion pratique  

Utilisez `az vm list-skus` ou l'API ListSkus pour lister les SKU disponibles par région ; passez au scale-up via Portail/CLI pour changer. [learn.microsoft](https://learn.microsoft.com/fr-fr/azure/data-explorer/manage-cluster-choose-sku)
Azure Advisor recommande les SKU optimaux selon charge/charge. [learn.microsoft](https://learn.microsoft.com/fr-fr/azure/data-explorer/manage-cluster-choose-sku)

> 🚀 **Si tu maîtrises l'un, tu comprends l'autre rapidement — et avec ce cours, tu maîtrises les deux !**
