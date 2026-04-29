# Guide Complet AZ-104 – Microsoft Azure Administrator
> Guide de préparation personnalisé – Profil DevOps expérimenté

---

## 📋 Table des matières

1. [Stratégie d'examen](#stratégie-dexamen)
2. [Domaine 1 – Identités et gouvernance (15-20%)](#domaine-1--identités-et-gouvernance)
3. [Domaine 2 – Stockage (15-20%)](#domaine-2--stockage)
4. [Domaine 3 – Calcul (20-25%)](#domaine-3--calcul)
5. [Domaine 4 – Réseau virtuel (20-25%)](#domaine-4--réseau-virtuel)
6. [Domaine 5 – Surveillance et sauvegarde (10-15%)](#domaine-5--surveillance-et-sauvegarde)
7. [Pièges classiques à l'examen](#pièges-classiques)
8. [Questions style examen](#questions-style-examen)

---

## Stratégie d'examen

### Format de l'examen
- **Durée** : 120 minutes
- **Questions** : 40 à 60 (QCM, cas pratiques, drag & drop, scénarios)
- **Score minimum** : 700 / 1000
- **Prix** : ~165 € en France
- **Validité** : 1 an (renouvellement gratuit en ligne via Microsoft Learn)

### Plan de révision recommandé (3 semaines)

| Semaine | Focus | Priorité |
|---|---|---|
| S1 | Identités (Entra ID, RBAC, PIM) + Stockage | 🔴 Critique |
| S2 | Réseau (détails avancés) + Monitoring | 🟠 Important |
| S3 | Examens blancs + révision des lacunes | 🟡 Consolidation |

### Ressources indispensables
- **John Savill – AZ-104 Study Cram** (YouTube) → 4h qui résument tout
- **Microsoft Learn** → parcours officiel, gratuit
- **MeasureUp ou Whizlabs** → examens blancs (faire minimum 3 passages)
- **Azure Portal** → pratiquer en live, créer un compte Free Tier

---

## Domaine 1 – Identités et gouvernance

> ⚠️ **Domaine le plus piégeux de l'examen. Ne pas négliger.**

### 1.1 Microsoft Entra ID (ancien Azure Active Directory)

C'est l'**annuaire d'identités cloud** de Microsoft. Il gère **qui tu es** et **à quoi tu as accès**.

#### Objets principaux

| Objet | Description | Points clés |
|---|---|---|
| **User** | Personne physique | Peut être membre ou invité (B2B) |
| **Group** | Ensemble d'users/SPs | Assigned ou Dynamic |
| **Service Principal** | Identité d'une application | Créé automatiquement quand une app est enregistrée |
| **Managed Identity** | SP géré par Azure | Pas de credentials à gérer |
| **Application Registration** | Définition d'une app dans Entra | Crée un Service Principal associé |

#### Licences Entra ID

| Licence | Fonctionnalités clés |
|---|---|
| **Free** | Gestion users/groupes basique, SSO limité |
| **P1** | Conditional Access, groupes dynamiques, MFA avancé, Self-Service Password Reset |
| **P2** | PIM (Privileged Identity Management), Identity Protection, Access Reviews |

> 💡 **À retenir** : Les groupes dynamiques et Conditional Access nécessitent **P1 minimum**.

---

### 1.2 Types de groupes

#### Assigned
- Tu ajoutes les membres **manuellement**
- Disponible avec la licence Free

#### Dynamic (User ou Device)
- Les membres sont ajoutés **automatiquement** selon des règles
- Exemple de règle : `user.department -eq "IT"`
- Nécessite une licence **P1**
- ⚠️ Un utilisateur ne peut pas être ajouté manuellement dans un groupe Dynamic

---

### 1.3 Managed Identity

Permet à une ressource Azure (VM, App Service, Function…) de s'authentifier auprès d'autres services Azure **sans gérer de secrets**.

#### System-assigned
```
VM <──── Managed Identity (liée à la VM)
         ↓
         Si la VM est supprimée → l'identité est supprimée aussi
```
- Liée à **une seule ressource**
- Cycle de vie lié à la ressource

#### User-assigned
```
App Service ──┐
              ├──── Managed Identity (indépendante)
VM ───────────┘
```
- Créée **indépendamment** des ressources
- Peut être attachée à **plusieurs ressources**
- Survit à la suppression des ressources

> 💡 **Cas d'usage typique** : Ta VM doit accéder à Key Vault → tu lui assigne une Managed Identity, tu lui donnes le rôle **Key Vault Secrets User** sur le Key Vault. Plus besoin de stocker de secret.

---

### 1.4 RBAC – Role Based Access Control

Système qui gère **ce que tu peux faire** sur les ressources Azure.

#### La formule fondamentale
```
QUI          +    QUOI       +    OÙ
(Principal)       (Rôle)          (Scope)
User/Group/SP     Owner/Contributor/Reader    Subscription/RG/Resource
```

#### Les 4 rôles built-in fondamentaux

| Rôle | Lire | Créer/Modifier | Supprimer | Gérer les accès |
|---|---|---|---|---|
| **Owner** | ✅ | ✅ | ✅ | ✅ |
| **Contributor** | ✅ | ✅ | ✅ | ❌ |
| **Reader** | ✅ | ❌ | ❌ | ❌ |
| **User Access Administrator** | ✅ | ❌ | ❌ | ✅ |

#### Autres rôles importants à connaître

| Rôle | Usage |
|---|---|
| **Virtual Machine Contributor** | Gérer les VMs sans accès réseau/stockage |
| **Network Contributor** | Gérer les ressources réseau |
| **Storage Blob Data Contributor** | Lire/écrire dans Blob Storage |
| **Key Vault Secrets Officer** | Gérer les secrets dans Key Vault |

---

### 1.5 Le Scope – héritage du RBAC

```
Management Group        ← Niveau le plus haut
    └── Subscription
            └── Resource Group
                    └── Resource   ← Niveau le plus bas
```

**Règles d'héritage :**
- Les rôles s'héritent **du haut vers le bas**
- Un rôle au niveau Subscription s'applique à tous les RG et ressources dedans
- Le RBAC est **additif** : si tu as Reader via un groupe et Contributor via un autre → tu as **Contributor**

> ⚠️ **Piège d'examen** : Tu ne peux **pas bloquer** un accès hérité avec RBAC classique. Si quelqu'un hérite d'Owner sur une Subscription, tu ne peux pas lui retirer sur un RG spécifique. Seules les **Deny Assignments** le permettent (cas très rare).

---

### 1.6 Azure Policy vs RBAC

Confusion très fréquente à l'examen :

| | RBAC | Azure Policy |
|---|---|---|
| **Contrôle** | Ce que l'user **peut faire** | Ce qui **peut exister** |
| **Exemple** | "Tu peux créer des VMs" | "Les VMs doivent être en West Europe" |
| **Bloque** | Les actions non autorisées | Les ressources non conformes |
| **Portée** | Identité (who) | Ressource (what) |

#### Effets des Policies

| Effet | Description |
|---|---|
| **Deny** | Bloque la création/modification |
| **Audit** | Journalise la non-conformité sans bloquer |
| **DeployIfNotExists** | Déploie automatiquement une ressource associée si absente |
| **Modify** | Modifie les propriétés lors de la création |
| **Append** | Ajoute des champs lors de la création |

---

### 1.7 Conditional Access

> Requiert une licence **P1**

Logique : **Si [Conditions] → Alors [Contrôles]**

#### Conditions possibles
- Utilisateur ou groupe ciblé
- Application ciblée
- Localisation (pays, plage IP)
- Plateforme (Windows, iOS, Android…)
- Risque de connexion (nécessite P2)
- Device compliance

#### Contrôles d'accès
- **Bloquer l'accès**
- **Autoriser avec MFA**
- **Autoriser uniquement depuis un device compliant**
- **Autoriser uniquement depuis un device joint à Azure AD**

> 💡 **Exemple typique examen** : *"Les utilisateurs qui se connectent depuis un pays inconnu doivent faire le MFA"* → Conditional Access avec condition Location + contrôle MFA requis.

---

### 1.8 PIM – Privileged Identity Management

> Requiert une licence **P2**

**Concept clé** : Personne ne doit avoir des droits élevés **en permanence**.

#### Deux types d'assignation

| Type | Description |
|---|---|
| **Eligible** | Le rôle est disponible mais pas actif. L'user doit l'activer manuellement. |
| **Active** | Le rôle est actif en permanence (comme le RBAC classique) |

#### Processus d'activation PIM
1. L'user demande l'activation du rôle
2. Il fournit une justification
3. (Optionnel) Un approbateur valide la demande
4. Le rôle est actif pour une durée définie (ex: 8h)
5. Le rôle expire automatiquement

> 💡 **À retenir pour l'examen** : PIM = **Just-In-Time (JIT) access**

---

### 1.9 Gouvernance – Management Groups et Subscriptions

```
Root Management Group
├── Management Group "Production"
│   ├── Subscription "Prod-West"
│   └── Subscription "Prod-East"
└── Management Group "Dev"
    └── Subscription "Dev-All"
```

- **Management Groups** : conteneurs logiques pour organiser plusieurs subscriptions
- Les policies et RBAC assignés sur un Management Group s'appliquent à **toutes les subscriptions** en dessous
- Maximum **6 niveaux** de hiérarchie (sans compter la racine)
- Chaque subscription n'appartient qu'à **un seul** Management Group

---

### 1.10 Azure AD B2B vs B2C

| | B2B | B2C |
|---|---|---|
| **Usage** | Collaboration avec des partenaires/externes | Authentification clients d'une app |
| **Qui l'utilise** | Employés d'autres entreprises | Clients finaux |
| **Exemple** | Inviter un consultant externe | Login avec Google/Facebook sur ton app |

---

## Domaine 2 – Stockage

### 2.1 Types de comptes de stockage

| Type | Usage | Redondance dispo |
|---|---|---|
| **StorageV2 (General Purpose v2)** | Blob, File, Queue, Table | LRS, ZRS, GRS, GZRS |
| **BlockBlobStorage** | Blob hautes performances | LRS, ZRS |
| **FileStorage** | Azure Files hautes performances | LRS, ZRS |

> 💡 **À l'examen** : Toujours choisir **StorageV2** sauf si une performance spécifique est demandée.

---

### 2.2 Redondance du stockage

| Option | Description | Réplication |
|---|---|---|
| **LRS** – Locally Redundant Storage | 3 copies dans 1 datacenter | Même région, même DC |
| **ZRS** – Zone Redundant Storage | 3 copies dans 3 zones | Même région, 3 zones |
| **GRS** – Geo-Redundant Storage | LRS + 3 copies dans une région secondaire | 2 régions |
| **GZRS** – Geo-Zone Redundant | ZRS + 3 copies dans une région secondaire | 2 régions + 3 zones |
| **RA-GRS** | GRS + lecture possible sur la région secondaire | 2 régions |
| **RA-GZRS** | GZRS + lecture possible sur la région secondaire | 2 régions + 3 zones |

> ⚠️ **Piège** : Avec GRS/GZRS, la région secondaire n'est **pas accessible en lecture par défaut**. Pour ça il faut **RA-GRS** ou **RA-GZRS**.

---

### 2.3 Niveaux d'accès Blob (Access Tiers)

| Tier | Coût stockage | Coût accès | Usage |
|---|---|---|---|
| **Hot** | Élevé | Faible | Données accédées fréquemment |
| **Cool** | Moyen | Moyen | Données accédées peu fréquemment (>30 jours) |
| **Cold** | Faible | Élevé | Données accédées rarement (>90 jours) |
| **Archive** | Très faible | Très élevé + délai de réhydratation | Archivage long terme (>180 jours) |

> ⚠️ **Important** : Les blobs en **Archive** ne sont **pas accessibles directement**. Il faut les **réhydrater** vers Hot ou Cool (peut prendre plusieurs heures).

#### Lifecycle Management
Permet d'automatiser le passage entre les tiers :
```
Blob créé → après 30 jours → Cool
            après 90 jours → Cold
            après 365 jours → Archive
            après 2 ans → Supprimer
```

---

### 2.4 SAS – Shared Access Signatures

Permet de donner un **accès temporaire et limité** à du stockage sans partager la clé du compte.

#### Types de SAS

| Type | Description |
|---|---|
| **Account SAS** | Accès à plusieurs services du compte |
| **Service SAS** | Accès à un seul service (Blob, File, Queue, Table) |
| **User Delegation SAS** | Basé sur les credentials Entra ID (plus sécurisé) |

#### Ce qu'on peut contrôler dans un SAS
- Date/heure d'expiration
- Adresses IP autorisées
- Protocoles autorisés (HTTPS only)
- Permissions (read, write, delete, list…)
- Conteneur ou blob spécifique

> 💡 **Bonne pratique** : Toujours préférer **User Delegation SAS** car basé sur Entra ID. Si la clé du compte est compromise, un Account SAS est compromis aussi.

---

### 2.5 Azure Files

Service de partage de fichiers SMB/NFS managé dans le cloud.

#### Méthodes d'authentification
- **Active Directory Domain Services (AD DS)** – on-premise
- **Azure AD DS** – domaine managé dans Azure
- **Azure AD Kerberos** – pour les clients hybrides
- **Clé de compte de stockage** (moins sécurisé)

#### Niveaux de performance

| Tier | Stockage sous-jacent | Usage |
|---|---|---|
| **Standard (Transaction Optimized)** | HDD | Workloads généraux |
| **Premium** | SSD | Applications I/O intensives |

---

### 2.6 Azure Blob – Types de blobs

| Type | Description | Usage |
|---|---|---|
| **Block Blob** | Optimisé pour upload/download | Fichiers, images, vidéos |
| **Append Blob** | Optimisé pour ajout de données | Logs |
| **Page Blob** | Accès aléatoire par pages de 512 bytes | Disques de VMs (VHD) |

---

### 2.7 Soft Delete et Versioning

| Fonctionnalité | Description |
|---|---|
| **Blob Soft Delete** | Conserve les blobs supprimés pendant X jours |
| **Container Soft Delete** | Conserve les conteneurs supprimés pendant X jours |
| **Blob Versioning** | Conserve automatiquement chaque version d'un blob |
| **Point-in-time restore** | Restaurer les blobs à un point dans le temps |

---

### 2.8 Clés d'accès vs Entra ID pour le stockage

| Méthode | Sécurité | Recommandation |
|---|---|---|
| **Clé de compte** | ❌ Accès total, difficile à révoquer | À éviter si possible |
| **SAS** | 🟡 Limité mais peut être compromis | Pour accès externes temporaires |
| **Rôles RBAC Entra ID** | ✅ Granulaire, révocable | Méthode recommandée |

---

## Domaine 3 – Calcul

### 3.1 Virtual Machines

#### Tailles de VMs – familles importantes

| Famille | Usage |
|---|---|
| **B** (Burstable) | Dev/test, charges variables |
| **D** (General Purpose) | Web apps, bases de données légères |
| **E** (Memory Optimized) | Bases de données en mémoire |
| **F** (Compute Optimized) | Calcul intensif |
| **N** (GPU) | Machine learning, rendu graphique |

#### Disponibilité des VMs

| Option | Protection contre | SLA |
|---|---|---|
| **Availability Set** | Pannes matérielles (rack) dans un même DC | 99.95% |
| **Availability Zone** | Pannes d'un datacenter entier | 99.99% |
| **VMSS (Scale Set)** | Charge + pannes | Variable |

> 💡 **Availability Set** utilise :
> - **Fault Domains** (FD) : racks physiques séparés (max 3)
> - **Update Domains** (UD) : groupes mis à jour séparément lors des maintenances (max 20)

---

### 3.2 Azure Disk Storage

| Type | IOPS max | Usage |
|---|---|---|
| **Standard HDD** | Faible | Dev/test, non-critique |
| **Standard SSD** | Moyen | Web apps, faible trafic |
| **Premium SSD** | Élevé | Production, bases de données |
| **Ultra Disk** | Très élevé | Workloads critiques, SAP HANA |

#### Types de disques

| Type | Description |
|---|---|
| **OS Disk** | Disque système (C: sur Windows) |
| **Data Disk** | Disques supplémentaires pour les données |
| **Temp Disk** | Disque temporaire local (D: sur Windows) – **données perdues si VM redémarre** |

> ⚠️ **Piège** : Le **disque temporaire** n'est **pas sauvegardé** et les données sont perdues lors des redémarrages/redéploiements. Ne jamais y stocker de données importantes.

---

### 3.3 App Service

#### Plans App Service

| Plan | VMs dédiées | Scale out | Usage |
|---|---|---|---|
| **Free/Shared** | Non (partagé) | ❌ | Dev/test |
| **Basic** | Oui | Manuel | Apps de test |
| **Standard** | Oui | Auto (10 instances max) | Production |
| **Premium** | Oui | Auto (30 instances max) | Production haute perf |
| **Isolated** | Oui (VNet dédié) | Auto (100 instances max) | Haute sécurité |

#### Deployment Slots
Disponibles à partir du plan **Standard**.

```
Slot Production ←──── swap ────→ Slot Staging
```

- Permet de déployer sans interruption (**zero-downtime deployment**)
- Possibilité de tester sur Staging avant le swap
- En cas de problème → swap back immédiat
- **Les paramètres de connexion peuvent être "sticky"** (ne pas swapper avec le slot)

---

### 3.4 Azure Container Instances (ACI)

- Exécuter des conteneurs **sans gérer d'infrastructure**
- Idéal pour des tâches courtes ou des workloads burst
- Facturation à la **seconde**
- Pas de haute disponibilité native (contrairement à AKS)

---

### 3.5 Azure Kubernetes Service (AKS)

Points clés pour l'examen :
- **Node Pools** : groupes de VMs avec la même configuration
- **System Node Pool** : obligatoire, exécute les pods système Kubernetes
- **User Node Pool** : optionnel, pour les workloads applicatifs
- Intégration avec **Azure Container Registry (ACR)** pour les images
- Intégration avec **Entra ID** pour l'authentification

---

### 3.6 Azure Container Registry (ACR)

| SKU | Géo-réplication | Webhooks | Rétention |
|---|---|---|---|
| **Basic** | ❌ | ✅ | Non configurable |
| **Standard** | ❌ | ✅ | Non configurable |
| **Premium** | ✅ | ✅ | Configurable |

---

## Domaine 4 – Réseau virtuel

> Tu connais déjà bien cette partie. Focus sur les détails théoriques piégeux.

### 4.1 VNet – Concepts fondamentaux

- Un VNet est **régional** (limité à une région Azure)
- Un VNet peut avoir **plusieurs espaces d'adressage**
- Les **subnets** divisent le VNet en segments plus petits
- Azure **réserve 5 adresses IP** dans chaque subnet :
  - `.0` : Adresse réseau
  - `.1` : Gateway Azure
  - `.2` et `.3` : Réservées Azure DNS
  - `.255` : Broadcast

> 💡 **Exemple** : Subnet `10.0.0.0/24` → 256 adresses - 5 réservées = **251 utilisables**

---

### 4.2 NSG – Network Security Group

Pare-feu de niveau 4 (TCP/UDP) qui filtre le trafic.

#### Règles par défaut (toujours présentes, non supprimables)

**Inbound :**
| Priorité | Nom | Source | Destination | Action |
|---|---|---|---|---|
| 65000 | AllowVnetInBound | VirtualNetwork | VirtualNetwork | Allow |
| 65001 | AllowAzureLoadBalancerInBound | AzureLoadBalancer | Any | Allow |
| 65500 | DenyAllInBound | Any | Any | Deny |

**Outbound :**
| Priorité | Nom | Source | Destination | Action |
|---|---|---|---|---|
| 65000 | AllowVnetOutBound | VirtualNetwork | VirtualNetwork | Allow |
| 65001 | AllowInternetOutBound | Any | Internet | Allow |
| 65500 | DenyAllOutBound | Any | Any | Deny |

> ⚠️ **Priorité** : Plus le nombre est **petit**, plus la règle est prioritaire. Une règle en priorité 100 est appliquée avant une règle en priorité 200.

#### Application Flow Logs
- Permet de logger tout le trafic qui passe par le NSG
- Stocké dans un compte de stockage
- Analysable avec **Traffic Analytics** (Log Analytics Workspace)

---

### 4.3 VNet Peering

Connecte deux VNets pour qu'ils communiquent via le réseau backbone d'Azure.

#### Types
- **Regional Peering** : même région
- **Global Peering** : régions différentes

#### Points importants
- Le peering **n'est pas transitif** par défaut
  ```
  VNet A ←──── peering ────→ VNet B ←──── peering ────→ VNet C
  A ne peut PAS parler à C sans peering direct ou hub (NVA/VPN Gateway)
  ```
- Adresses IP **ne doivent pas se chevaucher** entre les VNets peerés
- Peering doit être créé **des deux côtés**

---

### 4.4 VPN Gateway

Connecte des réseaux on-premise à Azure via un tunnel VPN chiffré (IPSec/IKE).

#### Types de connexions

| Type | Description |
|---|---|
| **Site-to-Site (S2S)** | Réseau on-premise → Azure (connexion permanente) |
| **Point-to-Site (P2S)** | Machine individuelle → Azure (VPN client) |
| **VNet-to-VNet** | Deux VNets dans des régions différentes via VPN |
| **ExpressRoute** | Connexion privée (non internet) via un opérateur |

#### SKUs Gateway importantes

| SKU | Débit max | Usage |
|---|---|---|
| **Basic** | 100 Mbps | Dev/test (legacy, à éviter) |
| **VpnGw1** | 650 Mbps | Production légère |
| **VpnGw5** | 10 Gbps | Haute performance |

---

### 4.5 Azure DNS

- Hébergement de zones DNS dans Azure
- **Zone DNS publique** : résolution internet
- **Zone DNS privée** : résolution interne aux VNets

#### DNS privé – Auto-registration
- Quand activé sur un VNet, les VMs enregistrent automatiquement leur nom DNS
- Chaque VNet peut être lié à **plusieurs** zones DNS privées
- Une zone DNS privée peut être liée à **plusieurs** VNets

---

### 4.6 Load Balancer

| Type | Niveau OSI | Trafic | Usage |
|---|---|---|---|
| **Azure Load Balancer** | Layer 4 (TCP/UDP) | Interne ou public | Distribution trafic bas niveau |
| **Application Gateway** | Layer 7 (HTTP/HTTPS) | Interne ou public | Web apps, URL routing, WAF |
| **Traffic Manager** | DNS (Layer 7) | Public uniquement | Distribution géographique |
| **Front Door** | Layer 7 global | Public uniquement | CDN + WAF + global load balancing |

#### Application Gateway – fonctionnalités clés
- **URL-based routing** : route selon l'URL (`/api/*` → backend API)
- **Multi-site hosting** : plusieurs sites sur une même gateway
- **SSL termination** : déchiffre HTTPS à la gateway
- **WAF (Web Application Firewall)** : protection contre OWASP Top 10
- **Cookie-based session affinity** : même client → même backend

---

### 4.7 Azure Firewall

Pare-feu managé de niveau enterprise, entièrement stateful.

#### Différence avec NSG

| | NSG | Azure Firewall |
|---|---|---|
| **Niveau** | Layer 4 | Layer 4 + 7 |
| **Scope** | Subnet ou NIC | VNet centralisé |
| **FQDN filtering** | ❌ | ✅ |
| **Threat Intelligence** | ❌ | ✅ |
| **Coût** | Gratuit | Payant (environ 900€/mois) |

---

### 4.8 Private Endpoint vs Service Endpoint

| | Service Endpoint | Private Endpoint |
|---|---|---|
| **Description** | Accès optimisé au service via le backbone Azure | IP privée dans ton VNet pour le service |
| **Trafic** | Reste sur le backbone mais via IP publique | IP privée, jamais internet |
| **DNS** | Pas de changement | Besoin de zone DNS privée |
| **Coût** | Gratuit | Payant (environ 7€/mois par endpoint) |
| **Accès depuis on-premise** | ❌ Difficile | ✅ Oui (via ExpressRoute/VPN) |

> 💡 **Tendance** : Les Private Endpoints sont la solution recommandée pour sécuriser l'accès aux services PaaS (Storage, SQL, Key Vault…).

---

## Domaine 5 – Surveillance et sauvegarde

### 5.1 Azure Monitor – Vue d'ensemble

```
Sources de données
├── VMs, App Services, Containers
├── Azure Activity Log
├── Metrics (toutes les ressources)
└── Application Insights (SDK dans le code)
         ↓
Azure Monitor
├── Metrics → Metric Explorer / Alertes
├── Logs → Log Analytics Workspace (KQL)
└── Alertes → Action Groups (email, SMS, webhook, runbook…)
```

---

### 5.2 Azure Monitor Metrics vs Logs

| | Metrics | Logs |
|---|---|---|
| **Type** | Données numériques (CPU, RAM…) | Données structurées (événements, traces) |
| **Rétention** | 93 jours par défaut | Configurable (30 jours par défaut, jusqu'à 2 ans) |
| **Requêtes** | Metric Explorer | KQL dans Log Analytics |
| **Fréquence** | 1 minute par défaut | Envoi batch |

---

### 5.3 Log Analytics Workspace

Stocke les logs de toutes les ressources Azure.

#### KQL – Kusto Query Language (bases à connaître)

```kql
-- Chercher dans les logs des VMs les 24 dernières heures
Heartbeat
| where TimeGenerated > ago(24h)
| summarize count() by Computer

-- Top 10 des erreurs
Event
| where EventLevelName == "Error"
| summarize count() by Source
| top 10 by count_

-- Logs d'activité
AzureActivity
| where OperationNameValue == "Microsoft.Compute/virtualMachines/delete"
| project TimeGenerated, Caller, ResourceGroup
```

---

### 5.4 Alertes Azure Monitor

#### Composants d'une alerte

```
Signal (Metric/Log/Activity)
    ↓
Condition (seuil dépassé, etc.)
    ↓
Action Group (qui notifier, comment)
    ↓
Actions : Email, SMS, Voice, Webhook, Logic App, Runbook, ITSM
```

#### Types de signaux

| Type | Exemple |
|---|---|
| **Metric** | CPU > 80% pendant 5 minutes |
| **Log** | Plus de 100 erreurs en 1 heure |
| **Activity Log** | Une VM a été supprimée |
| **Resource Health** | Une VM est marquée "Unavailable" |

---

### 5.5 Application Insights

Monitoring applicatif (APM). Nécessite un SDK dans le code ou une instrumentation auto.

#### Ce qu'il collecte
- Requêtes HTTP (durée, succès/échec)
- Exceptions et erreurs
- Dépendances (appels SQL, API externes…)
- Métriques custom
- Logs de traces

#### Fonctionnalités clés
- **Live Metrics** : vue temps réel
- **Application Map** : cartographie des dépendances
- **Availability Tests** : pings réguliers depuis plusieurs régions
- **Smart Detection** : détection automatique d'anomalies

---

### 5.6 Azure Backup

Service de sauvegarde managé.

#### Recovery Services Vault
Conteneur pour stocker les sauvegardes. Doit être **dans la même région** que les ressources à sauvegarder.

#### Ce qu'on peut sauvegarder

| Ressource | Agent requis |
|---|---|
| **Azure VMs** | Non (extension automatique) |
| **SQL Server dans VM** | Agent dans la VM |
| **Azure Files** | Non (snapshots) |
| **Azure Blobs** | Non (backup opérationnel) |
| **Machines on-premise** | MARS Agent ou Azure Backup Server |

#### Types de rétention
- **GFS (Grandfather-Father-Son)** : politique de rétention hebdo/mensuelle/annuelle
- **Instant Restore** : restauration rapide depuis les snapshots récents

---

### 5.7 Azure Site Recovery (ASR)

Disaster Recovery as a Service (DRaaS).

- Réplique des VMs vers une **région secondaire** en continu
- **RPO** (Recovery Point Objective) : jusqu'à 30 secondes pour les VMs Azure
- **RTO** (Recovery Time Objective) : quelques minutes
- Peut être utilisé pour les migrations (lift & shift)

> 💡 **À l'examen** :
> - **Azure Backup** = sauvegarde et restauration de données
> - **Azure Site Recovery** = continuité d'activité et disaster recovery

---

## Pièges classiques

### RBAC & Identités

| ❌ Erreur fréquente | ✅ Réalité |
|---|---|
| "Global Admin = Owner sur la subscription" | Ce sont deux systèmes séparés. Un Global Admin Entra ID n'a pas de droits Azure par défaut |
| "Contributor peut gérer les accès" | Non, seulement Owner et User Access Administrator |
| "Le RBAC peut refuser un accès hérité" | Non, le RBAC est additif. Utiliser Deny Assignment (rare) |
| "Les groupes Dynamic sont gratuits" | Non, nécessitent une licence P1 |
| "Un user peut être dans un groupe Dynamic et Assigned" | Un groupe est soit l'un soit l'autre |

### Stockage

| ❌ Erreur fréquente | ✅ Réalité |
|---|---|
| "GRS permet de lire depuis la région secondaire" | Non, il faut RA-GRS pour avoir un accès en lecture |
| "Les blobs Archive sont accessibles immédiatement" | Non, il faut les réhydrater (peut prendre des heures) |
| "Le disque temporaire de la VM est sauvegardé" | Non, les données sont perdues si la VM redémarre |

### Réseau

| ❌ Erreur fréquente | ✅ Réalité |
|---|---|
| "Le VNet Peering est transitif" | Non, A↔B et B↔C ne signifie pas A↔C |
| "NSG = Azure Firewall" | NSG est Layer 4 et gratuit, Firewall est Layer 7 et payant |
| "Service Endpoint = IP privée" | Non, Service Endpoint optimise le routage mais reste via IP publique |
| "Un subnet a 256 adresses utilisables en /24" | Non, Azure en réserve 5 → 251 utilisables |

### Calcul

| ❌ Erreur fréquente | ✅ Réalité |
|---|---|
| "Availability Set protège contre la panne de datacenter" | Non, seulement contre les pannes de rack. Pour le datacenter → Availability Zone |
| "Les Deployment Slots sont dispo sur le plan Basic" | Non, à partir du plan Standard |
| "Les données du disque temporaire survivent aux redémarrages" | Non, elles sont perdues |

---

## Questions style examen

### Question 1 – RBAC
**Scénario** : Alice est membre du groupe "Dev-Team" qui a le rôle Contributor sur le Resource Group "RG-App". Alice est aussi directement assignée au rôle Reader sur la subscription.
**Question** : Que peut faire Alice sur le Resource Group "RG-App" ?

<details>
<summary>Réponse</summary>

**Contributor sur RG-App.**
Le RBAC est additif. Alice hérite du Reader de la subscription sur tous les RGs, mais elle a aussi Contributor sur RG-App spécifiquement. Le rôle le plus permissif s'applique → Contributor.

</details>

---

### Question 2 – Stockage
**Scénario** : Tu dois stocker des fichiers de logs qui seront accédés rarement après 90 jours, et jamais après 1 an.
**Question** : Quelle configuration de lifecycle policy est optimale ?

<details>
<summary>Réponse</summary>

```
Après 90 jours → déplacer vers le tier Cold (ou Archive)
Après 365 jours → supprimer le blob
```
Si les logs ne seront plus jamais accédés après 90 jours → directement Archive après 90 jours pour minimiser les coûts.

</details>

---

### Question 3 – Réseau
**Scénario** : Tu as VNet-A et VNet-B peerés. VNet-B et VNet-C sont peerés. Une VM dans VNet-A doit communiquer avec une VM dans VNet-C.
**Question** : Que dois-tu faire ?

<details>
<summary>Réponse</summary>

Créer un **peering direct entre VNet-A et VNet-C**. Le peering n'est pas transitif. Il faut soit :
1. Un peering direct A↔C
2. Ou une architecture Hub & Spoke avec une NVA/VPN Gateway qui route le trafic

</details>

---

### Question 4 – Managed Identity
**Scénario** : Plusieurs App Services doivent accéder au même Key Vault. Tu veux centraliser la gestion de l'identité.
**Question** : Quel type de Managed Identity utiliser ?

<details>
<summary>Réponse</summary>

**User-assigned Managed Identity.**
Elle peut être partagée entre plusieurs ressources. Tu crées une seule identité, tu lui donnes le rôle Key Vault Secrets User sur le Key Vault, puis tu l'attaches à chaque App Service.

</details>

---

### Question 5 – Backup vs ASR
**Scénario** : Ton entreprise veut s'assurer que si la région Azure West Europe tombe complètement, les applications peuvent redémarrer en North Europe en moins de 30 minutes.
**Question** : Quelle solution utiliser ?

<details>
<summary>Réponse</summary>

**Azure Site Recovery (ASR).**
ASR est conçu pour le disaster recovery avec réplication continue et failover rapide. Azure Backup est pour la restauration de données mais le RTO est bien plus long (plusieurs heures).

</details>

---

### Question 6 – Conditional Access
**Scénario** : Tu veux que les utilisateurs doivent faire le MFA uniquement quand ils se connectent depuis l'extérieur du réseau de l'entreprise.
**Question** : Comment configurer cela ?

<details>
<summary>Réponse</summary>

1. Créer une **Named Location** dans Entra ID avec les plages IP de l'entreprise
2. Créer une **Conditional Access policy** :
   - **Condition** : Location → exclure la Named Location de l'entreprise
   - **Contrôle** : Require MFA

</details>

---

## Checklist finale avant l'examen

### Entra ID & RBAC
- [ ] Je connais la différence entre System-assigned et User-assigned Managed Identity
- [ ] Je sais que Contributor ne peut pas gérer les accès
- [ ] Je comprends l'héritage du RBAC (top-down, additif)
- [ ] Je connais la différence entre rôles Entra ID et rôles RBAC Azure
- [ ] Je sais ce que nécessite P1 et P2
- [ ] Je comprends PIM (Just-In-Time access)
- [ ] Je sais configurer Conditional Access

### Stockage
- [ ] Je connais LRS, ZRS, GRS, GZRS et leurs différences
- [ ] Je sais que GRS ≠ RA-GRS pour l'accès en lecture
- [ ] Je connais les tiers Hot/Cool/Cold/Archive et leurs implications
- [ ] Je comprends les SAS et leurs types
- [ ] Je sais que l'Archive nécessite une réhydratation

### Calcul
- [ ] Je connais la différence Availability Set vs Availability Zone
- [ ] Je comprends les Fault Domains et Update Domains
- [ ] Je sais à partir de quel plan les Deployment Slots sont disponibles
- [ ] Je sais que le disque temporaire n'est pas persistant

### Réseau
- [ ] Je sais que le VNet Peering n'est pas transitif
- [ ] Je connais les 5 adresses réservées par subnet
- [ ] Je comprends la différence NSG vs Azure Firewall
- [ ] Je connais la différence Service Endpoint vs Private Endpoint
- [ ] Je connais les types de Load Balancer (L4 vs L7)

### Monitoring & Backup
- [ ] Je comprends la différence Metrics vs Logs
- [ ] Je sais ce qu'est un Action Group
- [ ] Je connais la différence Azure Backup vs Azure Site Recovery
- [ ] Je sais que Recovery Services Vault doit être dans la même région

---

*Guide créé pour la préparation à l'examen AZ-104 – Microsoft Azure Administrator*
*Complémentaire au guide de révision chapitré Entra ID & RBAC détaillé*
