# 📘 Plan d'Étude AZ-104 — Administrateur Azure
## 8 Semaines Vers la Certification

**Préparé pour:** Examen AZ-104 (Microsoft Azure Administrator)  
**Durée:** 8 semaines  
**Format:** Guide structuré avec labs, ressources et quiz  
**Objectif:** Certifier administrateur Azure avec expertise pratique

---

## 📋 Table des Matières

1. [Vue d'ensemble](#vue-densemble)
2. [Structure de l'examen](#structure-de-lexamen)
3. [Plan par Semaine](#plan-par-semaine)
4. [Labs Pratiques](#labs-pratiques)
5. [Ressources Microsoft Learn](#ressources-microsoft-learn)
6. [Vidéos Sarah Kong](#vidéos-sarah-kong)
7. [Quiz Hebdomadaires](#quiz-hebdomadaires)
8. [Calendrier 8 Semaines](#calendrier-8-semaines)
9. [Checklists de Préparation](#checklists-de-préparation)

---

## 🎯 Vue d'ensemble {#vue-densemble}

### Informations de l'Examen

```
Examen:           AZ-104 (Microsoft Azure Administrator)
Durée:            120 minutes
Questions:        40-60 questions
Format:           Choix multiples, drag-drop, labs interactifs
Langue:           Français disponible
Score requis:     700/1000 (70%)
Coût:             99-165 USD
Validité:         3 ans
Plateforme:       Pearson VUE
```

### Compétences Évaluées

```
✅ Identités et Gouvernance (25-30%)
   • Azure AD / Entra ID
   • Rôles et permissions (RBAC)
   • Gouvernance Azure

✅ Stockage (15-20%)
   • Azure Storage
   • Managed Disks
   • Backup & Recovery

✅ Réseaux Virtuels (20-25%)
   • VNets et Subnets
   • Network Security Groups (NSGs)
   • VPN & ExpressRoute
   • Load Balancers

✅ Calcul (20-25%)
   • Virtual Machines
   • Containers (ACR, AKS)
   • App Service
   • Azure Functions

✅ Surveillance (10-15%)
   • Azure Monitor
   • Alerts & Logs
   • Application Insights
```

### Prérequis

```
Requis:
• Compte Azure gratuit (créer maintenant: azure.microsoft.com/free)
• PC/Mac avec accès internet
• Connaissances de base en IT

Recommandé:
• 6+ mois d'expérience Azure
• PowerShell/Azure CLI basique
• Concepts réseau (IP, subnets, firewalls)
```

---

## 📚 Structure de l'Examen {#structure-de-lexamen}

### Domaines Testés (% pondération)

```
┌─────────────────────────────────────────────────────┐
│         AZ-104 — DOMAINES D'EXAMEN                 │
├─────────────────────────────────────────────────────┤
│                                                     │
│ 1. Identités & Gouvernance (25-30%)                │
│    └─ Azure AD, RBAC, Policies, Subscriptions      │
│                                                     │
│ 2. Stockage (15-20%)                               │
│    └─ Storage, Disks, Backup, Replication         │
│                                                     │
│ 3. Réseaux (20-25%)                                │
│    └─ VNets, NSGs, VPN, Load Balancers            │
│                                                     │
│ 4. Calcul (20-25%)                                 │
│    └─ VMs, Containers, App Service, Functions    │
│                                                     │
│ 5. Surveillance (10-15%)                           │
│    └─ Monitor, Alerts, Logs, Insights             │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Format des Questions

```
Type 1: Choix Multiples (SC, MC)
  • Scénario court + 4 réponses
  • Sélectionner 1 réponse correcte

Type 2: Choix Multiples (Plusieurs réponses)
  • Scénario + 4-5 réponses
  • Sélectionner 2+ réponses
  • Message spécifie le nombre

Type 3: Drag & Drop
  • Associer concepts, paramètres
  • Relier colonnes, ordonner

Type 4: Labs Interactifs (1-2 par examen)
  • Environnement Azure sandbox
  • Compléter des tâches pratiques
  • 30 minutes max par lab

Type 5: Case à Cocher (Hot Spot)
  • Identifier zones d'images/diagrammes
  • Cliquer points critiques
```

---

## 📅 Plan par Semaine {#plan-par-semaine}

## SEMAINE 1: Fondamentals & Identités {#semaine-1}

### Objectifs

```
□ Comprendre architecture Azure (subscriptions, resource groups)
□ Maîtriser Azure Active Directory / Entra ID
□ Configurer utilisateurs, groupes, rôles
□ Implémenter Azure RBAC
```

### Contenu Théorique

#### 1.1 Concepts Fondamentaux Azure

```
Hiérarchie Azure:
┌──────────────────────────────────┐
│  Management Group (Enterprise)   │
│  ├─ Subscription 1 (Dev)         │
│  │  ├─ Resource Group (App1)     │
│  │  │  ├─ VM, Storage, Network   │
│  │  ├─ Resource Group (App2)     │
│  │  │  └─ ...                     │
│  ├─ Subscription 2 (Prod)        │
│  │  └─ ...                        │
│  ├─ Subscription 3 (HR)          │
│  │  └─ ...                        │
└──────────────────────────────────┘

Terminologie:
• Subscription: Contrat de facturation
• Resource Group: Conteneur logique
• Région: Localisation géographique
• Availability Zone: Isolation physique dans région
```

#### 1.2 Azure AD / Entra ID

```
Qu'est-ce que Azure AD?
• Service d'identité et d'accès cloud
• Annuaire centralisé (utilisateurs, groupes, applications)
• Authentification (vérifier qui vous êtes)
• Autorisation (vérifier ce que vous pouvez faire)

Éditions:
┌──────────────┬──────────────┬──────────────┬──────────────┐
│    Free      │   Premium P1 │   Premium P2 │   Premium P2 │
├──────────────┼──────────────┼──────────────┼──────────────┤
│ Utilisateurs │ Utilisateurs │ Utilisateurs │ Tous + MFA   │
│ Groupes      │ + MFA        │ + Conditional│ + Risk-based │
│ SSO          │ + Self-Pass  │   Access     │   Access     │
│ B2B Collab   │ + PIM        │ + PIM        │ + Analytics  │
└──────────────┴──────────────┴──────────────┴──────────────┘

Concepts:
• Directory (annuaire)
• Tenant (locataire/organisation)
• Object ID (identifiant unique)
• User Principal Name (UPN) = email style
• Managed Identity (identité pour ressources Azure)
```

#### 1.3 Azure RBAC (Role-Based Access Control)

```
3 Éléments:
1. Principal (Qui?)
   • User
   • Group
   • Service Principal
   • Managed Identity

2. Role Definition (Quoi?)
   • Owner: Contrôle total
   • Contributor: Créer/modifier, pas accès
   • Reader: Lecture seule
   • Custom roles (personnalisés)

3. Scope (Où?)
   • Management Group
   • Subscription
   • Resource Group
   • Resource

EXEMPLE:
Attribuer "Virtual Machine Contributor" 
au groupe "Operations"
pour le Resource Group "Production"

→ Operations peut gérer VMs en Production
→ Mais pas les networks ou storage
→ Scope limité à ce Resource Group
```

#### 1.4 Gouvernance & Policies

```
Azure Policy:
• Lois de l'organisation
• Appliqué automatiquement
• Enforce, Audit, Deny

Exemples:
- Tous les storage must have encryption
- Tous les VMs must have monitoring
- Seulement 2 régions autorisées
- Seulement SKU Standard/Premium

Azure Blueprints:
• Collections de policies + templates
• Deploy cohésif (multi-resource)
• Versioning & update tracking

Initiative:
• Groupes de policies
• Deploy plusieurs policies ensemble
```

### Labs Semaine 1

#### Lab 1.1: Créer Utilisateurs & Groupes

```
Durée: 45 minutes

Tâches:
1. Créer 3 utilisateurs dans Azure AD
   → alice@yourdomain.onmicrosoft.com
   → bob@yourdomain.onmicrosoft.com
   → charlie@yourdomain.onmicrosoft.com

2. Créer 2 groupes
   → Groupe "Administrators" (alice, bob)
   → Groupe "Users" (charlie)

3. Configurer MFA pour alice
   → Microsoft Authenticator app

4. Définir password policy
   → Minimum 14 characters
   → Must change password every 90 days

5. Vérifier accès Azure Portal
   → Chaque utilisateur se connecte

Validation:
□ 3 utilisateurs créés
□ 2 groupes avec membres
□ MFA actif
□ Tous peuvent accéder Portal
```

#### Lab 1.2: Implémenter RBAC

```
Durée: 60 minutes

Tâches:
1. Créer Resource Group "Lab-RG"

2. Créer 2 VMs dans ce group
   → VM1 (Windows Server 2022)
   → VM2 (Linux Ubuntu)

3. Assigner rôles:
   → Alice: Owner on Lab-RG
   → Bob: Virtual Machine Contributor on VM1
   → Charlie: Reader on Lab-RG

4. Tester permissions:
   → Alice: Can do everything ✅
   → Bob: Can restart VM1 but not VM2 ✅
   → Charlie: Can view but not modify ✅

5. Créer custom role
   → "VM Viewer": Can list, view, but not modify
   → Assigner à 1 utilisateur

Validation:
□ 3 rôles assignés correctement
□ Permissions testées
□ Custom role créé et fonctionnel
```

### Ressources Microsoft Learn (Semaine 1)

```
Module 1: Azure Fundamentals
https://learn.microsoft.com/en-us/training/modules/
  describe-cloud-compute

Durée: 30 min

Module 2: Azure AD Concepts
https://learn.microsoft.com/en-us/training/modules/
  explore-basic-services-identity-types

Durée: 45 min

Module 3: RBAC Implementation
https://learn.microsoft.com/en-us/training/modules/
  manage-identity-and-access

Durée: 60 min

Module 4: Azure Policy
https://learn.microsoft.com/en-us/training/modules/
  define-compliance-requirements-deploy-azure-policy

Durée: 45 min

TOTAL: ~3 heures
```

### Vidéos Sarah Kong (Semaine 1)

```
Sarah Kong sur YouTube: "AZ-104 Administrator"

Video 1: Azure AD Overview
https://www.youtube.com/watch?v=... (rechercher)
Durée: 22 minutes
Topics: Users, Groups, Roles

Video 2: RBAC Deep Dive
Durée: 18 minutes
Topics: Role definitions, scopes, effective permissions

Video 3: Best Practices Identities
Durée: 15 minutes
Topics: Security, naming conventions, governance
```

### Quiz Semaine 1

**Quiz 1.1: Concepts Fondamentaux (10 questions)**

```
1. Quelle est la hiérarchie correcte de containment?
   a) Subscription > Management Group > Resource Group
   b) Management Group > Subscription > Resource Group
   c) Resource Group > Subscription > Management Group
   ✓ RÉPONSE: b

2. Azure AD est utilisé pour:
   a) Gérer les machines physiques
   b) Gérer les identités et accès
   c) Gérer les machines virtuelles
   d) Tous les précédents
   ✓ RÉPONSE: b

3. Quel rôle RBAC permet tout contrôle?
   a) Contributor
   b) Owner
   c) Administrator
   ✓ RÉPONSE: b

[... 7 autres questions]
```

**Quiz 1.2: Identités & RBAC (15 questions)**

```
Scénarios pratiques avec permissions RBAC...

[Complet dans document)
```

### Résumé Semaine 1

```
✅ Complété:
   □ Concepts fondamentaux Azure
   □ Azure AD / Entra ID
   □ RBAC implementation
   □ Gouvernance & Policies
   □ 2 labs pratiques
   □ Quiz hebdomadaire

⏭️  Prochaine:
   Stockage, Disks, Backup
```

---

## SEMAINE 2: Stockage Azure {#semaine-2}

### Objectifs

```
□ Maîtriser Azure Storage (Blob, Queue, Table, File)
□ Gérer Managed Disks
□ Implémenter replication & disaster recovery
□ Configurer Storage Accounts
```

### Contenu Théorique

#### 2.1 Azure Storage

```
Composants:
┌────────────────────────────────────────────┐
│        Azure Storage Account               │
├────────────────────────────────────────────┤
│                                            │
│ 1. Blob Storage                            │
│    Stockage de fichiers non structurés     │
│    • Hot (accès fréquent)                  │
│    • Cool (accès rare)                     │
│    • Archive (long-term)                   │
│                                            │
│ 2. Queue Storage                           │
│    Messages pour applications              │
│    • Async communication                   │
│    • Decoupling                            │
│                                            │
│ 3. Table Storage                           │
│    Base de données NoSQL                   │
│    • Key-value storage                     │
│    • Queries                               │
│                                            │
│ 4. File Shares                             │
│    SMB shares (NAS)                        │
│    • Mount on VMs                          │
│    • Cross-platform                        │
│                                            │
│ 5. Disk Storage                            │
│    Disks pour VMs                          │
│    • OS disks                              │
│    • Data disks                            │
│                                            │
└────────────────────────────────────────────┘

Types de Compte:
┌──────────────────┬────────────────────────────┐
│ Standard         │ Blob, Queue, Table, Files  │
│ Premium          │ High-perf (VMs, databases) │
│ BlockBlobStorage │ Blob optimized              │
│ FileStorage      │ File shares optimized       │
└──────────────────┴────────────────────────────┘
```

#### 2.2 Managed Disks

```
Types de Disks:
┌──────────────┬────────────────┬──────────────┐
│ Premium SSD  │ Standard SSD   │ Standard HDD │
├──────────────┼────────────────┼──────────────┤
│ IOPS: 120k   │ IOPS: 6k       │ IOPS: 500    │
│ Latence: 1ms │ Latence: 5ms   │ Latence: 10ms│
│ Production   │ Standard       │ Archive      │
│ $$$$         │ $$             │ $            │
└──────────────┴────────────────┴──────────────┘

Tailles disponibles:
P1: 4 GB (128 IOPS)
P2: 8 GB (256 IOPS)
...
P80: 32 TB (20,000 IOPS)

OS Disk:
• Premium par défaut (Windows Server 2022)
• Standard possible pour dev/test

Data Disks:
• Attachables à VM
• Up to 64 per VM
• Max 32 TB per disk
```

#### 2.3 Replication & Disaster Recovery

```
Stratégies de Replication:
┌────────────────────────────────────────────┐
│          REPLICATION STRATEGIES            │
├────────────────────────────────────────────┤
│                                            │
│ LRS (Locally Redundant Storage)            │
│ • 3 copies dans 1 datacenter               │
│ • Protection: défaillance matériel         │
│ • Coût: $ (moins cher)                    │
│ • Cas: dev/test, non-critique             │
│                                            │
│ ZRS (Zone-Redundant Storage)               │
│ • 3 copies dans 3 availability zones       │
│ • Protection: zone failure                 │
│ • Coût: $$ (moyen)                        │
│ • Cas: application importante              │
│                                            │
│ GRS (Geo-Redundant Storage)                │
│ • 3 copies locally + 3 dans autre région   │
│ • Protection: région failure               │
│ • Coût: $$$ (cher)                        │
│ • Cas: données critiques                   │
│                                            │
│ RA-GRS (Read-Access GRS)                   │
│ • GRS + accès lecture à replica             │
│ • Permet failover + lecture cross-region   │
│ • Coût: $$$$ (très cher)                   │
│                                            │
└────────────────────────────────────────────┘

Choisir:
• Non-critical: LRS
• Standard: ZRS
• Mission-critical: GRS/RA-GRS
```

### Labs Semaine 2

#### Lab 2.1: Créer Storage Account

```
Durée: 45 minutes

Tâches:
1. Créer Storage Account
   → Name: labstg123456 (unique globally)
   → Region: France Central
   → Redundancy: GRS
   → Performance: Standard
   → Access tier: Hot

2. Créer containers Blob
   → "documents" (private)
   → "public-data" (public)
   → "uploads" (private)

3. Uploader fichiers
   → 5 PDFs dans "documents"
   → 1 image dans "public-data"
   → Vérifier access

4. Configurer lifecycle
   → 90 jours → Cool tier
   → 180 jours → Archive tier
   → 365 jours → Delete

5. Configurer network access
   → Allow Azure Portal
   → Deny tout autre par défaut
   → Add whitelist IP

Validation:
□ Storage account créé
□ Containers & files présents
□ Lifecycle policy active
□ Network rules appliquées
□ Accès fonctionne correctement
```

#### Lab 2.2: Managed Disks & Snapshots

```
Durée: 60 minutes

Tâches:
1. Créer VM Windows avec Premium disk

2. Créer 2 disks (Premium SSD)
   → Disk1: 256 GB (P15)
   → Disk2: 512 GB (P20)
   → Attach à VM

3. Initialiser disks
   → Format NTFS
   → Assign drive letters (D:, E:)
   → Create folders, files

4. Créer snapshots
   → Snapshot1 de Disk1 (D:)
   → Snapshot2 de Disk2 (E:)

5. Tester recovery
   → Créer new disk from Snapshot1
   → Attach à second VM
   → Vérifier data intégrité

6. Monitor performance
   → Check IOPS metrics
   → Check throughput (MB/s)
   → Verify Premium SSD performance

Validation:
□ Disks created & formatted
□ Snapshots successful
□ Recovery tested
□ Performance metrics captured
```

### Ressources Microsoft Learn (Semaine 2)

```
Module 1: Azure Storage Architecture
https://learn.microsoft.com/en-us/training/modules/
  configure-storage-accounts

Durée: 50 min

Module 2: Blob Storage
https://learn.microsoft.com/en-us/training/modules/
  configure-blob-storage

Durée: 45 min

Module 3: Managed Disks
https://learn.microsoft.com/en-us/training/modules/
  configure-virtual-machine-storage

Durée: 55 min

Module 4: Replication & Recovery
https://learn.microsoft.com/en-us/training/modules/
  configure-storage-security

Durée: 60 min

TOTAL: ~3.5 heures
```

### Quiz Semaine 2

**Quiz 2.1: Azure Storage (12 questions)**

```
1. Quel tier est approprié pour archived data?
   a) Hot tier
   b) Cool tier
   c) Archive tier
   ✓ RÉPONSE: c

2. Combien de copies pour LRS?
   a) 1 copy
   b) 3 copies locally
   c) 6 copies (3 local + 3 geo)
   ✓ RÉPONSE: b

[... 10 autres questions]
```

**Quiz 2.2: Disk & Replication (15 questions)**

```
Scénarios avec choix de replication strategy...
Performance requirements...
Cost optimization...

[Complet dans document)
```

---

## SEMAINE 3: Réseaux Virtuels {#semaine-3}

### Objectifs

```
□ Concevoir Virtual Networks et Subnets
□ Implémenter Network Security Groups (NSGs)
□ Configurer Network Interfaces (NICs)
□ Gérer connectivité (VPN, ExpressRoute, Peering)
```

### Contenu Théorique

#### 3.1 Virtual Networks (VNets)

```
Composants VNet:
┌────────────────────────────────────────────┐
│           Azure Virtual Network            │
├────────────────────────────────────────────┤
│                                            │
│ Address Space (CIDR):                      │
│ • 10.0.0.0/16 (65,536 IPs)                │
│ • Non-routable on Internet (Private)       │
│                                            │
│ Subnets:                                   │
│ • 10.0.1.0/24 (256 IPs)                   │
│ • 10.0.2.0/24 (256 IPs)                   │
│ • 10.0.3.0/24 (256 IPs)                   │
│                                            │
│ Network Interfaces (NICs):                 │
│ • VMs attach via NIC                       │
│ • Multiple NICs possible                   │
│ • 1 public IP optional                     │
│                                            │
│ Resources in Subnets:                      │
│ • VMs, App Services, Databases             │
│ • Load Balancers                           │
│ • Network Appliances                       │
│                                            │
└────────────────────────────────────────────┘

Best Practices:
✅ Use RFC 1918 addresses (10.0.0.0/8, etc.)
✅ Plan subnets carefully (future growth)
✅ Document CIDR ranges
✅ Isolate by function (web, app, db)
```

#### 3.2 Network Security Groups (NSGs)

```
NSG Rules:
┌────────────────────────────────────────────┐
│      Inbound Security Rules (Input)        │
├────────────────────────────────────────────┤
│                                            │
│ Priority: 100-65535 (lower = first)        │
│ Source: IP, CIDR, Service Tag, *           │
│ Protocol: TCP, UDP, ICMP, *                │
│ Port Range: 22, 80, 443, *, 3389:3390      │
│ Action: Allow, Deny                        │
│ Direction: Inbound                         │
│                                            │
│ Example:                                   │
│ Priority: 100                              │
│ Source: 10.0.0.0/24                        │
│ Protocol: TCP                              │
│ Port: 3306 (MySQL)                         │
│ Action: Allow                              │
│ → Allow MySQL from app subnet              │
│                                            │
└────────────────────────────────────────────┘

Service Tags (groupes de IPs):
• VirtualNetwork: Toutes IPs in VNet
• Internet: Toutes IPs publiques
• Storage: IP ranges de Azure Storage
• SQL: IP ranges de Azure SQL
• AppService: IP ranges de App Service
• AzureKeyVault: Etc.

Outbound Rules:
• Par défaut: All traffic allowed out
• Peut être restrictif pour sécurité
```

#### 3.3 VPN & ExpressRoute

```
VPN Gateway (Site-to-Site):
┌────────────────────────────────────────────┐
│       On-Premises ←→ Azure VNet           │
│                                            │
│ On-premises (Corporate):                   │
│ 192.168.0.0/16                             │
│                                            │
│           ↓ VPN Tunnel (IPSec)             │
│                                            │
│ Azure VNet:                                │
│ 10.0.0.0/16                                │
│                                            │
│ Gateway Subnet (GatewaySubnet):            │
│ 10.0.255.0/24                              │
│                                            │
│ VPN Gateway (SKU: VpnGw1-5):               │
│ • Public IP address                        │
│ • VPN type: Route-based/Policy-based       │
│ • Throughput: 100 Mbps - 10 Gbps           │
│                                            │
└────────────────────────────────────────────┘

Point-to-Site (Client VPN):
• Utilisateurs distants → Azure VNet
• Download VPN client
• Certificate-based or Password-based
• IKEv2, SSTP, OpenVPN

ExpressRoute:
• Connexion dédiée (non-Internet)
• Partenaires: AT&T, Vodafone, Level3, etc.
• Bande passante: 50 Mbps - 100 Gbps
• Latence: Très basse
• Coût: Plus cher que VPN
```

#### 3.4 Load Balancers

```
Azure Load Balancer (L4 - Transport):
┌────────────────────────────────────────────┐
│         Incoming Traffic                   │
│              ↓                             │
│    Azure Load Balancer (Stateless)         │
│    • Distributes across backend VMs        │
│    • Round-robin, Least connections, etc.  │
│    • Health probes                         │
│              ↓                             │
│    ┌──────────┬──────────┬──────────┐     │
│    ↓          ↓          ↓          ↓     │
│    VM1        VM2        VM3        VM4   │
│    80/443     80/443     80/443     80/443│
│                                            │
└────────────────────────────────────────────┘

Application Gateway (L7 - Application):
• URL-based routing
• Hostname-based routing
• WAF (Web Application Firewall)
• SSL/TLS termination
• Cookies, headers inspection
```

### Labs Semaine 3

#### Lab 3.1: VNet & Subnets

```
Durée: 50 minutes

Tâches:
1. Créer VNet
   → Name: Lab-VNet
   → Address space: 10.0.0.0/16

2. Créer subnets
   → WebSubnet: 10.0.1.0/24
   → AppSubnet: 10.0.2.0/24
   → DbSubnet: 10.0.3.0/24
   → GatewaySubnet: 10.0.255.0/24

3. Créer Network Interfaces
   → WebNIC (in WebSubnet)
   → AppNIC (in AppSubnet)
   → DbNIC (in DbSubnet)

4. Assigner public IPs
   → WebNIC gets static public IP
   → AppNIC, DbNIC remain private

5. Document design
   → Diagram of VNet, subnets
   → IP ranges, purposes
   → NIC assignments

Validation:
□ VNet created with correct address space
□ 3 subnets in correct ranges
□ NICs created and assigned
□ Public IP assigned to WebNIC only
□ Design documented
```

#### Lab 3.2: NSG & Rules

```
Durée: 60 minutes

Tâches:
1. Créer 2 NSGs
   → WebNSG (for WebSubnet)
   → AppNSG (for AppSubnet)

2. Configurer WebNSG rules:
   → Inbound: Allow HTTP (80) from Internet
   → Inbound: Allow HTTPS (443) from Internet
   → Inbound: Allow RDP (3389) from AdminIP only
   → Outbound: Allow to AppSubnet (10.0.2.0/24)
   → Outbound: Deny all else

3. Configurer AppNSG rules:
   → Inbound: Allow from WebSubnet (10.0.1.0/24) port 8080
   → Inbound: Allow from DbSubnet (10.0.3.0/24) port 1433
   → Outbound: Allow all

4. Appliquer NSGs
   → WebNSG → WebSubnet
   → AppNSG → AppSubnet

5. Tester règles
   → Verify correct traffic allowed
   → Verify incorrect traffic blocked
   → Check NSG flow logs

Validation:
□ 2 NSGs created
□ Rules configured correctly
□ NSGs applied to correct subnets
□ Traffic testing successful
```

#### Lab 3.3: VPN Gateway (Optional Advanced)

```
Durée: 90 minutes (advanced)

Tâches:
1. Créer VPN Gateway
   → SKU: VpnGw1
   → Type: Route-based
   → In GatewaySubnet

2. Créer Local Network Gateway
   → Represents on-premises network
   → Address space: 192.168.0.0/16
   → Gateway IP: x.x.x.x (simulated)

3. Créer VPN Connection
   → Connect VPN Gateway to Local Gateway
   → Shared key (pre-shared secret)

4. Créer test VPN client
   → Download VPN client
   → Install on test machine
   → Connect to VNet

5. Test connectivity
   → Ping VM in VNet from on-prem
   → Verify bidirectional

Validation:
□ VPN Gateway deployed
□ Connection established
□ Clients can connect
□ Ping test successful
```

### Ressources Microsoft Learn (Semaine 3)

```
Module 1: Azure Virtual Networks
https://learn.microsoft.com/en-us/training/modules/
  configure-virtual-networks

Durée: 60 min

Module 2: Network Security Groups
https://learn.microsoft.com/en-us/training/modules/
  configure-network-security-groups

Durée: 50 min

Module 3: VPN Gateway
https://learn.microsoft.com/en-us/training/modules/
  configure-vpn-gateway

Durée: 45 min

Module 4: Load Balancers
https://learn.microsoft.com/en-us/training/modules/
  configure-azure-load-balancer

Durée: 55 min

TOTAL: ~3 heures
```

### Quiz Semaine 3

**Quiz 3.1: VNets & NSGs (12 questions)**

```
1. Quelle est la plus grande IPv4 address space?
   a) 10.0.0.0/8 (16M IPs)
   b) 172.16.0.0/12 (1M IPs)
   c) 192.168.0.0/16 (65k IPs)
   ✓ RÉPONSE: a

2. NSG inbound rule - priorité?
   a) Lower number = higher priority
   b) Higher number = higher priority
   ✓ RÉPONSE: a

[... 10 autres questions]
```

**Quiz 3.2: VPN & Load Balancing (15 questions)**

```
Scénarios avec design requirements...
Connectivity decisions...
Traffic routing...

[Complet dans document)
```

---

## SEMAINE 4: Virtual Machines {#semaine-4}

### Objectifs

```
□ Créer et configurer VMs Windows & Linux
□ Gérer disks et storage pour VMs
□ Implémenter auto-scaling & load balancing
□ Configurer monitoring & diagnostics
```

### Contenu Théorique

#### 4.1 VM Compute Options

```
VM Sizes (SKUs):
┌──────────────┬────────────┬───────────┬──────────────┐
│ General      │ Compute    │ Memory    │ Storage      │
│ Purpose      │ Optimized  │ Optimized │ Optimized    │
├──────────────┼────────────┼───────────┼──────────────┤
│ B-series     │ F-series   │ E-series  │ L-series     │
│ D-series     │ (CPU)      │ (RAM)     │ (NVMe/SSD)   │
│ E-series     │            │           │              │
│ Standard     │ 2-128 vCPU │ 2-432 GB  │ Up to 30 TB  │
│              │            │ RAM       │              │
└──────────────┴────────────┴───────────┴──────────────┘

Burstable VMs (B-series):
• Dev/test environments
• Low baseline, can burst to high
• Cost-effective
• Example: B1s, B2s, B4ms

General Purpose (D-series):
• Balanced CPU/Memory
• Production workloads
• Most common
• Example: D2s_v3, D4s_v3

Compute Optimized (F-series):
• High CPU
• Batch processing
• Scientific simulation
• Example: F2s, F4s

Memory Optimized (E-series):
• High RAM
• In-memory databases (SAP, Oracle)
• Example: E4s_v3, E32s_v3
```

#### 4.2 Images & Extensions

```
Operating System Images:
• Windows Server 2019/2022 (Licensed)
• Linux (Ubuntu, CentOS, Red Hat, SUSE)
• Custom images (VHD upload)
• Marketplace images (third-party)

VM Extensions:
• Custom Script Extension
  → Run scripts (PowerShell, Bash)
  → Install software, configure
  
• Desired State Configuration (DSC)
  → PowerShell automation
  → Infrastructure as Code
  
• Dependency Agent
  → Monitor VM dependencies
  → With Azure Monitor

• Guest Configuration
  → Compliance checking
  → Policy enforcement

Example:
{
  "publisher": "Microsoft.Compute",
  "type": "CustomScriptExtension",
  "typeHandlerVersion": "1.10",
  "settings": {
    "commandToExecute": "powershell -Command 'Install-WindowsFeature -Name Web-Server'"
  }
}
```

#### 4.3 Auto-Scaling & VMSS

```
Virtual Machine Scale Sets (VMSS):
┌────────────────────────────────────────────┐
│    Virtual Machine Scale Set               │
│    (Collection of identical VMs)           │
├────────────────────────────────────────────┤
│                                            │
│ Base Configuration:                        │
│ • Image (OS)                               │
│ • Size (SKU)                               │
│ • Network config                           │
│ • Storage config                           │
│                                            │
│ VMSS automatically:                        │
│ • Creates N identical VMs                  │
│ • Distributes across zones                 │
│ • Adds to Load Balancer                    │
│ • Can auto-scale (0-1000 VMs)              │
│                                            │
│ Scaling Policies:                          │
│ • Scale-out: CPU > 80% → Add VMs           │
│ • Scale-in: CPU < 20% → Remove VMs        │
│ • Custom metrics: Application metrics     │
│                                            │
└────────────────────────────────────────────┘

Auto-Scale Rules:
• Monitor CPU, Memory, Network
• Threshold-based or time-based
• Cool-down period (prevent flapping)
• Min/Max instances
```

### Labs Semaine 4

#### Lab 4.1: Créer VMs Windows & Linux

```
Durée: 60 minutes

Tâches:
1. Créer VM Windows
   → Image: Windows Server 2022 Datacenter
   → Size: Standard D2s_v3 (2 vCPU, 8 GB RAM)
   → Network: WebSubnet
   → Public IP: Yes (static)
   → Name: Web-VM-01

2. Créer VM Linux
   → Image: Ubuntu 20.04 LTS
   → Size: Standard B2s (2 vCPU, 4 GB RAM)
   → Network: AppSubnet
   → Public IP: No
   → Name: App-VM-01
   → SSH key authentication

3. Ajouter data disks
   → Web-VM: 1x 256GB Premium SSD (D:)
   → App-VM: 1x 128GB Premium SSD (/data)

4. Configurer Network Interfaces
   → Static private IPs
   → NSG assignments
   → Public IP for Web-VM only

5. Test connectivity
   → RDP to Web-VM (Windows)
   → SSH to App-VM (Linux, via Web-VM)
   → Ping between VMs

Validation:
□ 2 VMs created and running
□ Disks formatted and mounted
□ Network connectivity tested
□ Both VMs accessible
```

#### Lab 4.2: VMSS & Auto-Scaling

```
Durée: 90 minutes

Tâches:
1. Créer Azure Load Balancer
   → Public IP: Yes
   → SKU: Standard
   → Backend pool: empty (will add VMSS)

2. Créer VMSS
   → Name: WebServerScaleSet
   → Image: Windows Server 2022
   → Size: Standard B2s
   → Initial instances: 2

3. Configurer auto-scaling
   → Min instances: 2
   → Max instances: 10
   → Scale-out: CPU > 75% (add 2 VMs)
   → Scale-in: CPU < 25% (remove 1 VM)
   → Cool-down: 5 minutes

4. Install web server
   → Custom Script Extension
   → Install IIS (Internet Information Services)
   → Deploy sample website

5. Load test
   → Generate traffic (curl loop)
   → Monitor CPU metrics
   → Observe auto-scaling
   → Should scale-out to 4+ VMs

6. Monitor scaling activity
   → Check VMSS activity log
   → Verify instances added
   → Verify health probes passing

Validation:
□ VMSS created with 2 instances
□ Load Balancer routing traffic
□ Web server responding on all instances
□ Auto-scaling triggered and working
□ Instances scale-out under load
□ Instances scale-in after load reduction
```

### Ressources Microsoft Learn (Semaine 4)

```
Module 1: Virtual Machine Basics
https://learn.microsoft.com/en-us/training/modules/
  configure-virtual-machines

Durée: 60 min

Module 2: VM Storage & Images
https://learn.microsoft.com/en-us/training/modules/
  configure-virtual-machine-storage

Durée: 50 min

Module 3: VMSS & Auto-Scaling
https://learn.microsoft.com/en-us/training/modules/
  configure-scale-sets

Durée: 55 min

Module 4: VM Extensions
https://learn.microsoft.com/en-us/training/modules/
  manage-virtual-machine-extensions

Durée: 40 min

TOTAL: ~3 heures
```

### Quiz Semaine 4

**Quiz 4.1: VMs & Sizing (12 questions)**

```
1. Pour une application avec haute CPU, quel size?
   a) Memory optimized (E-series)
   b) Compute optimized (F-series)
   c) General purpose (D-series)
   ✓ RÉPONSE: b

[... 11 autres questions]
```

---

## SEMAINE 5: Container & App Services {#semaine-5}

### Objectifs

```
□ Gérer Azure App Service (Web Apps, API Apps)
□ Configurer Azure Functions
□ Utiliser Container Registries (ACR)
□ Déployer containers via AKS
```

### Contenu Théorique

#### 5.1 App Service

```
Azure App Service Plans:
┌──────────────┬────────────┬──────────────┬──────────────┐
│ Free         │ Shared     │ Standard     │ Premium      │
├──────────────┼────────────┼──────────────┼──────────────┤
│ 1 GB Storage │ 1 GB       │ 50 GB        │ 500 GB       │
│ Shared CPU   │ Shared CPU │ Dedicated    │ Dedicated    │
│ Dev/Test     │ Dev/Test   │ Production   │ Production   │
│ No SLA       │ No SLA     │ 99.95% SLA   │ 99.95% SLA   │
│ $0           │ $10/month  │ $100+/month  │ $250+/month  │
└──────────────┴────────────┴──────────────┴──────────────┘

Runtimes:
• .NET 6, 7, 8
• Node.js 18, 20
• Python 3.8+
• Java 11, 17
• PHP 7.4, 8.0+
• Ruby 2.7, 3.0+

Deployment Methods:
• Zip/WAR file
• Git (GitHub, Azure DevOps)
• Docker container
• CI/CD pipeline
```

#### 5.2 Azure Functions

```
Triggers & Bindings:
┌────────────────────────────────┐
│   TRIGGER (Events)             │
│                                │
│ HTTP: REST API calls           │
│ Timer: Scheduled (CRON)        │
│ Blob Storage: File upload      │
│ Queue: Message received        │
│ Event Hub: Stream events       │
│ Service Bus: Message queue     │
│ Cosmos DB: Document changed    │
│                                │
├────────────────────────────────┤
│   OUTPUT BINDING (Results)     │
│                                │
│ HTTP: Return response          │
│ Blob: Write file               │
│ Queue: Send message            │
│ Database: Save record          │
│ Email: Send notification       │
│ Table Storage: Save data       │
│                                │
└────────────────────────────────┘

Pricing Models:
• Consumption: Pay per execution (~$0.20/million)
• Premium: Reserved instance (dedicated)
• App Service Plan: Shared with App Service
```

#### 5.3 Containers & ACR

```
Azure Container Registry:
• Private Docker registry
• Geo-replication
• Image scanning
• Build tasks

ACR Tasks:
• Build images on push
• CI/CD without external pipeline
• Multi-step builds
• Schedule builds

Registry Tiers:
• Basic: $5/month (storage only)
• Standard: $50/month (geo-replication)
• Premium: $250+/month (advanced security)
```

#### 5.4 Azure Kubernetes Service (AKS)

```
AKS Architecture:
┌──────────────────────────────┐
│   Azure Kubernetes Service   │
├──────────────────────────────┤
│ Control Plane (Microsoft     │
│ managed - no charge)         │
│  • API Server                │
│  • Scheduler                 │
│  • etcd (database)           │
│                              │
│ Node Pools:                  │
│  • System node pool (1+)     │
│  • User node pools (0+)      │
│  • Each pool: VMs, auto-scale│
│                              │
│ Pods (containers):           │
│  • Smallest unit in K8s      │
│  • 1+ containers per pod     │
│  • Share storage, network    │
│                              │
│ Services (networking):       │
│  • ClusterIP (internal)      │
│  • LoadBalancer (public)     │
│  • NodePort (debug)          │
│                              │
└──────────────────────────────┘

Pricing:
• Control Plane: Free
• Nodes: Pay per VM
• Typical: $50-500/month (depending on node pool size)
```

### Labs Semaine 5

#### Lab 5.1: App Service Deployment

```
Durée: 60 minutes

Tâches:
1. Créer App Service Plan
   → Name: LabAppServicePlan
   → OS: Windows
   → SKU: Standard S1
   → Region: France Central

2. Créer 2 Web Apps
   → WebApp1: .NET application
   → WebApp2: Node.js application

3. Déployer applications
   → WebApp1: Deploy from GitHub (dotnet sample)
   → WebApp2: Deploy from GitHub (nodejs sample)

4. Configurer Custom Domain (simulation)
   → Add binding (local hosts file or simulated)

5. Configure SSL/TLS
   → Enable HTTPS
   → Add free TLS certificate

6. Test applications
   → Browse both web apps
   → Verify functionality

7. Configure auto-scale
   → Min instances: 2
   → Max instances: 5
   → Scale on CPU > 80%

Validation:
□ App Service Plan created
□ 2 Web Apps deployed
□ Both responding to HTTP/HTTPS
□ Auto-scale configured
```

#### Lab 5.2: Azure Functions

```
Durée: 75 minutes

Tâches:
1. Créer Function App
   → Runtime: .NET 6 or Node.js
   → Storage Account: Create new
   → Plan: Consumption

2. Créer HTTP-triggered function
   → HTTP function (GET/POST)
   → Return JSON response
   → Test with curl

3. Créer Timer-triggered function
   → Run every 5 minutes
   → Log timestamp to Application Insights

4. Créer Queue-triggered function
   → Listen to Storage Queue
   → Process messages
   → Write to output binding (Table)

5. Configure Application Insights
   → Connect to Function App
   → View logs and traces

6. Test all functions
   → HTTP: Call endpoint
   → Timer: Wait for trigger
   → Queue: Send test messages

7. Deploy
   → Deploy to Azure Function App
   → Verify running in cloud

Validation:
□ Function App created
□ 3 functions working
□ Application Insights collecting data
□ All functions triggered successfully
```

#### Lab 5.3: Azure Container Registry & AKS

```
Durée: 120 minutes (advanced)

Tâches:
1. Créer Azure Container Registry
   → Name: labacr123456 (unique)
   → SKU: Standard
   → Enable admin user

2. Build container image
   → Create Dockerfile (Node.js app)
   → Build locally or in ACR
   → Tag: labacr.azurecr.io/webapp:v1

3. Push to ACR
   → docker push labacr.azurecr.io/webapp:v1
   → Verify in ACR portal

4. Créer AKS Cluster
   → Name: labaks-cluster
   → Nodes: 2 (Standard B2s VMs)
   → Network: Advanced (integrate with VNet)
   → Auto-scale: Min 2, Max 5

5. Connect kubectl
   → az aks get-credentials
   → kubectl get nodes

6. Déployer application
   → Create deployment.yaml
   → Create service.yaml (LoadBalancer)
   → kubectl apply -f deployment.yaml

7. Expose application
   → Service type: LoadBalancer
   → Get public IP
   → Access via browser

8. Scale deployment
   → kubectl scale deployment
   → Observe pod scaling

Validation:
□ ACR created and image pushed
□ AKS cluster running
□ Application deployed
□ Service accessible via public IP
□ Scaling working
```

### Ressources Microsoft Learn (Semaine 5)

```
Module 1: App Service
https://learn.microsoft.com/en-us/training/modules/
  configure-app-services

Durée: 60 min

Module 2: Azure Functions
https://learn.microsoft.com/en-us/training/modules/
  develop-cloud-applications

Durée: 55 min

Module 3: Containers (ACR)
https://learn.microsoft.com/en-us/training/modules/
  publish-container-image-to-azure-container-registry

Durée: 45 min

Module 4: Kubernetes (AKS)
https://learn.microsoft.com/en-us/training/modules/
  aks-deployment-best-practices

Durée: 60 min

TOTAL: ~3.5 heures
```

### Quiz Semaine 5

**Quiz 5.1: App Services & Functions (12 questions)**

```
1. Quel plan App Service inclut SSL?
   a) Free
   b) Shared
   c) Standard+
   ✓ RÉPONSE: c

[... 11 autres questions]
```

---

## SEMAINE 6: Monitoring & Diagnostics {#semaine-6}

### Objectifs

```
□ Configurer Azure Monitor
□ Créer alertes et actions
□ Utiliser Application Insights
□ Analyser logs (Log Analytics)
□ Configurer diagnostics
```

### Contenu Théorique

#### 6.1 Azure Monitor

```
Azure Monitor Platform:
┌────────────────────────────────────────────┐
│        Azure Monitor                       │
├────────────────────────────────────────────┤
│                                            │
│ Data Collection:                           │
│ • Metrics (CPU, Memory, Disk)             │
│ • Logs (Events, Diagnostics)              │
│ • Traces (Application telemetry)          │
│                                            │
│ Storage:                                   │
│ • Metrics: Time-series DB (30 days)       │
│ • Logs: Log Analytics workspace           │
│ • Long-term: Storage Account              │
│                                            │
│ Analysis:                                  │
│ • Alerts (conditions)                      │
│ • Dashboards (visualizations)              │
│ • Workbooks (interactive reports)          │
│ • Queries (KQL)                            │
│                                            │
│ Actions:                                   │
│ • Email notifications                      │
│ • SMS/Push                                 │
│ • Webhooks                                 │
│ • Logic Apps                               │
│ • Runbooks                                 │
│                                            │
└────────────────────────────────────────────┘

Metric Types:
• Host metrics: CPU, Memory, Disk I/O
• Guest OS metrics: Requires agent
• Application metrics: Custom (via SDK)
• Availability: Synthetic tests
```

#### 6.2 Alerting

```
Alert Rule Components:
1. Target
   • Resource (VM, Web App, etc.)
   • Metric or Log

2. Condition
   • Threshold (CPU > 80%)
   • Time aggregation (Last 5 minutes)
   • Frequency (Check every 1 minute)
   • Severity (0-4)

3. Action
   • Notification (Email, SMS)
   • Webhook
   • Logic App
   • Runbook

4. Suppression
   • Maintenance window
   • Prevent alert storm

Example:
Alert: "High CPU on Production VMs"
Target: VMs in Prod resource group
Condition: CPU > 80% for 5 minutes
Action: Email ops@company.com
Severity: 2 (warning)
```

#### 6.3 Application Insights

```
Application Insights Capabilities:
┌────────────────────────────────────────────┐
│    Application Insights                    │
├────────────────────────────────────────────┤
│                                            │
│ Request Tracking:                          │
│ • Page views, response times               │
│ • Failed requests                          │
│ • Performance counters                     │
│                                            │
│ Dependency Tracking:                       │
│ • Database calls (latency)                 │
│ • External API calls                       │
│ • Cache hits/misses                        │
│                                            │
│ Exception Tracking:                        │
│ • Unhandled exceptions                     │
│ • Stack traces                             │
│ • User impact analysis                     │
│                                            │
│ Performance Monitoring:                    │
│ • Slow queries                             │
│ • Slow requests                            │
│ • Memory usage                             │
│                                            │
│ Availability Monitoring:                   │
│ • Web tests (synthetic monitoring)         │
│ • Global test locations                    │
│ • Alert on failures                        │
│                                            │
│ Integration:                               │
│ • Azure Functions, App Service             │
│ • Custom apps (SDK)                        │
│ • On-premises apps (TelemetryClient)      │
│                                            │
└────────────────────────────────────────────┘
```

#### 6.4 Log Analytics & KQL

```
Kusto Query Language (KQL):
• Time-series data queries
• Performance analysis
• Trend identification
• Custom dashboards

Common Queries:

# CPU usage over time
Perf
| where ObjectName == "Processor"
| where CounterName == "% Processor Time"
| where TimeGenerated > ago(1h)
| summarize AvgCPU = avg(CounterValue) by bin(TimeGenerated, 5m)

# Failed requests in App Insights
requests
| where success == false
| where timestamp > ago(24h)
| summarize FailureCount = count() by resultCode

# Exceptions by operation
exceptions
| where timestamp > ago(7d)
| summarize Count = count() by outerMessage
| order by Count desc
```

### Labs Semaine 6

#### Lab 6.1: Azure Monitor Setup

```
Durée: 60 minutes

Tâches:
1. Créer Log Analytics Workspace
   → Name: lab-logs-workspace
   → Region: France Central

2. Ajouter VMs to monitoring
   → Install Log Analytics Agent
   → Connect to workspace

3. Créer alert rules
   → Alert: CPU > 85% for 5 minutes
   → Alert: Available memory < 1 GB
   → Alert: Disk usage > 90%

4. Configurer actions
   → Notification: Email (your account)
   → Action: Create ticket (simulation)

5. Create metrics dashboard
   → Pin CPU chart
   → Pin Memory chart
   → Pin Disk chart

6. Test alerts
   → Generate high CPU load (stress test)
   → Verify alert triggered
   → Verify email received

Validation:
□ Workspace created
□ Agents installed
□ 3 alert rules working
□ Dashboard created
□ Alerts triggered successfully
```

#### Lab 6.2: Application Insights

```
Durée: 75 minutes

Tâches:
1. Créer Application Insights resource
   → Name: lab-insights
   → Application type: Web
   → Connection: To App Service

2. Enable Application Insights on Web App
   → Connect to resource
   → Enable monitoring

3. Instrument application
   → Add instrumentation key to code
   → Send custom events
   → Send custom metrics

4. Create Web Tests
   → HTTP test to /api/health endpoint
   → Run every 5 minutes from 3 locations
   → Alert if any location fails

5. Analyze Performance
   → View request/response times
   → Identify slow pages
   → Check dependencies (database, APIs)

6. Exception Handling
   → Trigger test exception
   → View in Application Insights
   → Check stack trace

7. Create Alerts
   → Alert on failed requests > 5%
   → Alert on availability < 95%

Validation:
□ Application Insights connected
□ Data flowing in
□ Web tests running
□ Performance metrics visible
□ Alerts configured
```

#### Lab 6.3: Log Analytics Queries

```
Durée: 60 minutes

Tâches:
1. Write KQL queries
   → Query 1: CPU usage trends
   → Query 2: Memory by computer
   → Query 3: Failed processes

2. Create saved queries
   → Save top 5 queries
   → Add descriptions

3. Create workbook
   → Visualize CPU trends
   → Visualize disk usage
   → Compare multiple VMs

4. Pin to dashboard
   → Pin 3 custom charts
   → Create monitoring dashboard

5. Export reports
   → Export query results
   → PDF format (concept)

Validation:
□ Multiple queries written
□ Queries saved
□ Workbook created
□ Dashboard configured
```

### Ressources Microsoft Learn (Semaine 6)

```
Module 1: Azure Monitor Basics
https://learn.microsoft.com/en-us/training/modules/
  configure-azure-monitor

Durée: 60 min

Module 2: Alerting
https://learn.microsoft.com/en-us/training/modules/
  create-performance-alerts

Durée: 45 min

Module 3: Application Insights
https://learn.microsoft.com/en-us/training/modules/
  monitor-performance-using-azure-application-insights

Durée: 55 min

Module 4: Log Analytics & KQL
https://learn.microsoft.com/en-us/training/modules/
  analyze-infrastructure-with-azure-monitor-logs

Durée: 60 min

TOTAL: ~3 heures
```

---

## SEMAINE 7: Governance & Backup {#semaine-7}

### Objectifs

```
□ Implémenter Azure Policies
□ Configurer Resource Locks
□ Gérer Backups & Recovery
□ Implémenter Disaster Recovery
□ Cost Management
```

### Contenu Théorique

#### 7.1 Azure Policy

```
Policy Components:
┌────────────────────────────────────────────┐
│        Azure Policy Framework              │
├────────────────────────────────────────────┤
│                                            │
│ Policy Definition:                         │
│ • Rules (allow, deny, audit)               │
│ • Scope (conditions)                       │
│ • Effects (what happens)                   │
│                                            │
│ Example Policy:                            │
│ "Require tags on all resources"            │
│ • Scan resources without tags              │
│ • Deny creation of untagged resources      │
│ • Report non-compliance                    │
│                                            │
│ Built-in Policies:                         │
│ • 200+ provided by Microsoft               │
│ • Common compliance scenarios              │
│ • Industries (HIPAA, PCI-DSS, SOC2)        │
│                                            │
│ Initiative:                                │
│ • Collection of policies                   │
│ • Deploy multiple at once                  │
│ • Example: "Azure Security Benchmark"      │
│                                            │
└────────────────────────────────────────────┘

Policy Effects:
• Deny: Prevent non-compliant resource
• Audit: Log non-compliance (allow)
• AuditIfNotExists: Complex logic
• DeployIfNotExists: Auto-remediate
• Disabled: Testing
```

#### 7.2 Resource Locks

```
Lock Types:
┌──────────────────────────────────────────┐
│          Resource Locks                  │
├──────────────────────────────────────────┤
│                                          │
│ CanNotDelete Lock:                       │
│ • Can read & modify                      │
│ • Cannot delete                          │
│ • Use case: Production databases         │
│                                          │
│ ReadOnly Lock:                           │
│ • Can read only                          │
│ • Cannot modify or delete                │
│ • Use case: Compliance, audit            │
│                                          │
│ Scope:                                   │
│ • Resource level (1 resource)            │
│ • Resource Group level (all resources)   │
│ • Subscription level (all RGs)           │
│                                          │
│ Inheritance:                             │
│ • Child resources inherit locks          │
│ • RG lock affects all resources          │
│                                          │
└──────────────────────────────────────────┘

Example:
Production Database:
• CanNotDelete lock (whole RG)
• Prevents accidental deletion
• Can still modify database
• Requires unlock to delete
```

#### 7.3 Backup & Recovery

```
Azure Backup Service:
┌────────────────────────────────────────────┐
│         Azure Backup Architecture          │
├────────────────────────────────────────────┤
│                                            │
│ Sources:                                   │
│ • VMs (full, incremental)                  │
│ • SQL/MySQL (transaction logs)             │
│ • File Shares (snapshots)                  │
│ • On-premises (via MARS agent)             │
│                                            │
│ Backup Vault:                              │
│ • Geo-redundant storage                    │
│ • Immutable backups                        │
│ • Long-term retention                      │
│                                            │
│ Restore Options:                           │
│ • Full VM restore                          │
│ • File restore (from snapshot)             │
│ • Point-in-time (any point in retention)   │
│                                            │
│ Retention Policies:                        │
│ • Daily: 7-180 days                        │
│ • Weekly: 1-260 weeks                      │
│ • Monthly: 1-1200 months                   │
│ • Yearly: 1-99 years                       │
│                                            │
└────────────────────────────────────────────┘

Backup Process:
VM → Incremental Snapshots → Backup Vault → Recovery Services Vault
     (Every 24 hours)      (Geo-replicated)

RPO (Recovery Point Objective): 24 hours (usually)
RTO (Recovery Time Objective): 30 minutes (restore new VM)
```

#### 7.4 Site Recovery & DR

```
Azure Site Recovery (ASR):
┌────────────────────────────────────────────┐
│    Disaster Recovery (DR)                  │
├────────────────────────────────────────────┤
│                                            │
│ Primary Region ←→ DR Region                │
│ (Production)    (Standby)                  │
│                                            │
│ Replication:                               │
│ • Continuous (real-time)                   │
│ • RPO: Minutes to seconds                  │
│ • Async writes                             │
│                                            │
│ Failover Types:                            │
│ • Test: No production impact               │
│ • Planned: Maintenance window              │
│ • Unplanned: Disaster recovery             │
│                                            │
│ RTO: 2-15 minutes                          │
│ RPO: 5-300 seconds                         │
│                                            │
└────────────────────────────────────────────┘

Use Cases:
• VMware → Azure
• Hyper-V → Azure
• Physical → Azure
• Azure → Azure (secondary region)
```

### Labs Semaine 7

#### Lab 7.1: Azure Policy & Locks

```
Durée: 60 minutes

Tâches:
1. Créer custom policy
   → Require tag "Environment"
   → Values: Dev, Test, Prod
   → Deny resources without tag

2. Assign policy
   → Scope: Lab resource group
   → Effect: Deny

3. Test policy
   → Try to create VM without tag
   → Should be denied ✓
   → Create with tag
   → Should succeed ✓

4. Create initiative
   → Require "Environment" tag
   → Require "CostCenter" tag
   → Require "Owner" tag
   → Apply to entire subscription

5. Add locks
   → CanNotDelete on critical resources
   → ReadOnly on audit resources
   → Test lock enforcement

6. Report compliance
   → View non-compliant resources
   → Generate compliance report

Validation:
□ Custom policy created
□ Policy tested and working
□ Initiative deployed
□ Locks applied
□ Compliance report generated
```

#### Lab 7.2: Backup Configuration

```
Durée: 75 minutes

Tâches:
1. Créer Recovery Services Vault
   → Name: lab-backup-vault
   → Region: France Central
   → SKU: Standard

2. Configure backup policy
   → Daily backups: 7 AM
   → Retention: 30 days (daily)
   → Weekly: 52 weeks
   → Monthly: 12 months

3. Backup VMs
   → Select 2 VMs to backup
   → Apply policy
   → Start initial backup

4. Monitor backups
   → Check backup status
   → View backup jobs
   → Verify completion

5. Test restore
   → Restore files from VM backup
   → Restore full disk
   → Verify data integrity

6. Configure off-site backup
   → Export to Storage Account
   → Geo-redundant copy
   → Long-term archive

Validation:
□ Backup Vault created
□ Policy configured
□ 2 VMs backing up
□ Backups completed
□ Restore tested successfully
```

#### Lab 7.3: Disaster Recovery (Optional Advanced)

```
Durée: 120 minutes (advanced)

Tâches:
1. Créer second region resources
   → Secondary VNet in different region
   → Setup mirror infrastructure

2. Enable Site Recovery
   → Select source VMs
   → Target: Secondary region
   → Replication policy: 5-min RPO

3. Monitor replication
   → Check sync status
   → View replication health
   → Monitor RPO/RTO

4. Test failover
   → Run test failover
   → Production not affected
   → Verify application works in secondary region
   → Cleanup test

5. Document failover runbook
   → Steps to execute failover
   → Contact information
   → Recovery procedures

Validation:
□ Site Recovery configured
□ VMs replicating to secondary region
□ Test failover successful
□ Failover runbook documented
```

### Ressources Microsoft Learn (Semaine 7)

```
Module 1: Azure Policy
https://learn.microsoft.com/en-us/training/modules/
  define-compliance-requirements-deploy-azure-policy

Durée: 55 min

Module 2: Resource Management
https://learn.microsoft.com/en-us/training/modules/
  control-and-organize-with-azure-resource-manager

Durée: 50 min

Module 3: Backup & Recovery
https://learn.microsoft.com/en-us/training/modules/
  protect-virtual-machines-backups

Durée: 65 min

Module 4: Site Recovery
https://learn.microsoft.com/en-us/training/modules/
  protect-infrastructure-disaster-recovery

Durée: 60 min

TOTAL: ~3.5 heures
```

---

## SEMAINE 8: Révision & Examen {#semaine-8}

### Objectifs

```
□ Réviser tous les domaines
□ Compléter practice tests
□ Déboguer points faibles
□ Passer l'examen AZ-104
```

### Calendrier Révision

#### Jours 1-2: Identités & Gouvernance

```
Réviser:
• Azure AD/Entra ID concepts
• RBAC implementation
• Azure Policies
• Resource Locks
• Subscriptions & Management Groups

Practice:
• 15 practice questions
• 1 lab (RBAC scenario)
• Review flashcards
```

#### Jours 3-4: Stockage

```
Réviser:
• Storage accounts (types, tiers)
• Blob lifecycle management
• Managed Disks & Snapshots
• Replication strategies
• Security & encryption

Practice:
• 15 practice questions
• 1 lab (Storage configuration)
```

#### Jours 5-6: Réseaux

```
Réviser:
• VNets & Subnets
• NSGs & routing
• VPN Gateway
• Load Balancers
• Firewall, DNS, CDN

Practice:
• 20 practice questions (most complex)
• 2 labs (VNet design, NSG rules)
```

#### Jours 7-8: Calcul & Monitoring

```
Réviser:
• VMs & VMSS
• App Service
• Containers & AKS
• Azure Monitor
• Alerts & Diagnostics

Practice:
• 20 practice questions
• 2 labs (VM deployment, monitoring)

Full Practice Exam:
• Simulate real exam (40-60 questions)
• 120 minutes
• Review incorrect answers
```

### Practice Tests & Resources

#### Microsoft Learn Assessments

```
Interactive assessments (FREE):
• Module completion tests
• Knowledge checks
• Practice problems

Available at:
https://learn.microsoft.com/en-us/certifications/
```

#### Third-Party Practice Tests

```
Recommended:
1. MeasureUp Practice Tests
   • Most accurate simulation
   • Official Microsoft partner
   • $99 for 2 attempts
   • Link: https://www.measureup.com/

2. Whizlabs
   • 1000+ questions
   • Video explanations
   • $30-50
   • Link: https://www.whizlabs.com/

3. ExamTopics
   • Free/paid questions
   • Community discussions
   • Link: https://www.examtopics.com/

Recommendation:
✅ Do MeasureUp + Microsoft Learn free tests
✅ Score 80%+ before exam
```

#### Sarah Kong Video Review Series

```
Recommended final review videos:
- AZ-104 60-minute crash course
- Top 20 exam questions explained
- Common mistakes to avoid
- Last-minute tips

Watch 1-2 days before exam
```

### Pre-Exam Checklist (2 jours avant)

```
48 Hours Before Exam:
□ Schedule exam officially
□ Know exam center location
□ Prepare ID documents
□ Test equipment (if remote)
□ Know exam code (AZ-104)

24 Hours Before:
□ No heavy studying (rest!)
□ Review summary notes
□ Sleep 8 hours
□ Review logistics again

Day of Exam:
□ Eat well
□ Arrive 30 minutes early
□ Bring ID + proof of address
□ Check-in procedure
□ Clear mind
```

### Exam Strategy

```
DURING EXAM:

1. Read questions carefully
   • Identify what's being asked
   • Note key details (scenario context)
   • Look for "which of the following"

2. Multi-select questions:
   • Usually 2-3 correct answers
   • Instructions say how many
   • All must be selected for credit

3. Flag for review:
   • Unsure questions → flag
   • Continue to end
   • Return to flagged
   • Final review before submit

4. Time management:
   • 120 minutes total
   • ~2 minutes per question
   • Labs may take 10-15 minutes
   • Leave 5 minutes for review

5. Labs (if present):
   • Read instructions thoroughly
   • Take notes on requirements
   • Complete step-by-step
   • Verify each step before moving on
   • Don't skip validation

6. Common trap answers:
   • More expensive option (not always right)
   • Newest feature (not always applicable)
   • "All of the above" (usually too broad)
   • Highly specific (might not match scenario)
```

### Post-Exam

```
After Exam:
• Score released immediately (at testing center)
• If pass: Certificate usually within 24 hours
• Detailed report sent to email

If Failed:
• Review weak areas from report
• Wait 24 hours before retake
• Focus on gaps identified
• Re-study and retest

If Passed:
🎉 Congratulations!
✓ Add to LinkedIn
✓ Share on resume
✓ Update professional profiles
✓ Consider next cert (AZ-900, AZ-305, etc.)

Next Steps:
• Maintain certification (valid 3 years)
• Renew with continuing education
• Pursue higher certs:
  - AZ-305 (Architect)
  - AZ-700 (Network)
  - AZ-500 (Security)
```

---

## 📚 Ressources Microsoft Learn {#ressources-microsoft-learn}

### Tous les Modules (Resume)

```
Total: ~30 modules
Duration: ~30 heures
All FREE on Microsoft Learn

IDENTITIES (5 modules)
1. Azure AD Concepts
2. Manage Identities
3. Azure RBAC
4. Implement Azure Policies
5. Manage Subscriptions

STORAGE (5 modules)
1. Storage Accounts
2. Blob Storage
3. File Shares
4. Managed Disks
5. Backup & Recovery

NETWORKING (6 modules)
1. VNets & Subnets
2. NSGs
3. VPN Gateway
4. Load Balancers
5. Application Gateway
6. DNS & CDN

COMPUTE (5 modules)
1. VMs
2. VMSS
3. App Service
4. Containers
5. Serverless

MONITORING (4 modules)
1. Azure Monitor
2. Alerts
3. Application Insights
4. Log Analytics

All available at:
https://learn.microsoft.com/en-us/training/
```

### Learning Paths (Curated)

```
Official AZ-104 Learning Path:
"Prepare for AZ-104"
~30 hours
All modules aligned with exam

Link:
https://learn.microsoft.com/en-us/training/paths/
  az-104-administrator-labs/
```

---

## 📹 Vidéos Sarah Kong {#vidéos-sarah-kong}

### Channel & Playlists

```
YouTube Channel: Sarah Kong
URL: https://www.youtube.com/c/...

Playlist: AZ-104 Administrator Certification
Videos: 30+ videos
Duration: 15-30 min each
Topics: All exam domains + labs

Topics covered:
1. Azure fundamentals refresher
2. Identities deep dive
3. RBAC hands-on
4. Storage configuration
5. VNet design
6. NSG rules explained
7. VPN setup
8. Load balancing
9. VMs and VMSS
10. App Service
11. Containers basics
12. Azure Monitor
13. Alerts configuration
14. Backup & DR
15. Common exam questions
16. Exam day tips
17. Troubleshooting scenarios

Recommendation:
Watch videos that match weekly topics
Take notes on key points
Pause and practice along
```

---

## 🎯 Quiz Hebdomadaires {#quiz-hebdomadaires}

### Quiz Framework

```
Each week:
• 1 x 10-question quiz (quick)
• 1 x 15-20 question quiz (comprehensive)
• 1 x scenario-based quiz (practical)
• Total: 35-50 questions per week

Scoring:
• 70% = passing
• 80%+ = good
• 90%+ = excellent

Review incorrect answers thoroughly!
Understanding why is more important than just passing.
```

### Accès aux Quiz

```
Microsoft Learn Built-in Assessments:
• Free with module completion

Recommended Platforms:
1. ExamTopics.com
   • 2000+ AZ-104 questions
   • Free community version
   • Paid verified answers

2. Udemy Practice Tests
   • $10-15 during sales
   • 500+ questions
   • Video explanations

3. MeasureUp
   • Most realistic
   • $99 for 2 exams
   • Recommended!

4. Whizlabs
   • 1000+ questions
   • Lab simulations
   • $30
```

---

## 📅 Calendrier 8 Semaines {#calendrier-8-semaines}

### Structure Globale

```
WEEK 1: Identities & Governance
├─ Mon-Wed: Théorie (6h)
├─ Thu-Fri: Labs (2h)
├─ Sat: Review (2h)
└─ Sun: Quiz (1h)
   TOTAL: 11 heures

WEEK 2: Storage
├─ Mon-Wed: Théorie (6h)
├─ Thu-Fri: Labs (2h)
├─ Sat: Review (2h)
└─ Sun: Quiz (1h)
   TOTAL: 11 heures

WEEK 3: Networking
├─ Mon-Wed: Théorie (7h) *plus complexe
├─ Thu-Fri: Labs (3h) *plus labs
├─ Sat: Review (2h)
└─ Sun: Quiz (1h)
   TOTAL: 13 heures

WEEK 4: Compute (VMs)
├─ Mon-Wed: Théorie (6h)
├─ Thu-Fri: Labs (3h)
├─ Sat: Review (2h)
└─ Sun: Quiz (1h)
   TOTAL: 12 heures

WEEK 5: Containers & App Service
├─ Mon-Wed: Théorie (7h)
├─ Thu-Fri: Labs (3h)
├─ Sat: Review (2h)
└─ Sun: Quiz (1h)
   TOTAL: 13 heures

WEEK 6: Monitoring
├─ Mon-Wed: Théorie (6h)
├─ Thu-Fri: Labs (3h)
├─ Sat: Review (2h)
└─ Sun: Quiz (1h)
   TOTAL: 12 heures

WEEK 7: Governance & Backup
├─ Mon-Wed: Théorie (6h)
├─ Thu-Fri: Labs (2h)
├─ Sat: Review (2h)
└─ Sun: Quiz (1h)
   TOTAL: 11 heures

WEEK 8: Revision & Exam
├─ Mon-Fri: Full Revision (10h)
│  • Review all domains
│  • Practice tests
│  • Weak areas
├─ Sat: Practice exam (2h)
├─ Sun: Rest + Light Review (2h)
└─ Exam Day: PASS! 🎉
   TOTAL: 14 heures

━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOTAL STUDY TIME: ~96 hours over 8 weeks
Average per week: 12 hours
Weekday: 2 hours/day
Weekend: 3 hours/day
```

### Horaire Recommandé

```
OPTION 1: Flexible (Work around schedule)
• 2 hours/weekday (after work)
• 3-4 hours/weekend
• Total: 10-14 hours/week

OPTION 2: Intensive (Dedicated learning)
• 3-4 hours/weekday
• 5-6 hours/weekend
• Total: 20-30 hours/week
• Exam ready in 4 weeks

OPTION 3: Minimal (Part-time)
• 1 hour/weekday
• 2 hours/weekend
• Total: 7-9 hours/week
• Extend to 12+ weeks

Recommendation:
→ OPTION 1 (Most realistic for working professionals)
→ Start Monday
→ Exam date: 8 weeks later
```

### Sample Week Schedule (Option 1)

```
MONDAY:
└─ Evening (7-9 PM): Learn module 1 (2h)

TUESDAY:
└─ Evening (7-9 PM): Learn module 1 continued + quiz (2h)

WEDNESDAY:
└─ Evening (7-9 PM): Learn module 2 (2h)

THURSDAY:
└─ Evening (7-8:30 PM): Start Lab 1 (1.5h)

FRIDAY:
└─ Evening (7-8 PM): Complete Lab 1 + setup Lab 2 (1h)
└─ Evening (8-9 PM): Lab 2 (1h)

SATURDAY:
└─ Morning (9-11 AM): Lab completion + review (2h)

SUNDAY:
└─ Morning (10-11 AM): Weekly quiz + cleanup (1h)

TOTAL: ~11 hours
```

---

## ✅ Checklists de Préparation {#checklists-de-préparation}

### Pre-Exam (2 weeks)

```
DOMAIN 1: Identities & Governance (25-30%)

Content Checklist:
□ Azure AD/Entra ID fundamentals
□ User & group management
□ Custom domains
□ Self-service password reset
□ MFA & authentication methods
□ Azure RBAC (roles, scope, assignments)
□ Custom roles (creation)
□ Azure Policies (built-in & custom)
□ Policy effects (deny, audit, etc.)
□ Resource locks
□ Subscriptions & Management Groups
□ Resource tagging strategy
□ Cost analysis by tag
□ Budgets & alerts

Skills Checklist:
□ Create users in Azure AD
□ Assign RBAC roles
□ Create custom RBAC role
□ Create & assign policies
□ Apply resource locks
□ Create management structure
□ Tag resources consistently

Labs Completed:
□ User & group creation
□ RBAC implementation
□ Custom role creation
□ Policy enforcement
□ Resource locking

Score Target: 80%+
```

```
DOMAIN 2: Storage (15-20%)

Content Checklist:
□ Storage account types & tiers
□ Blob lifecycle policies
□ Azure Files (SMB shares)
□ Queue & Table storage
□ Managed Disks (types, sizes)
□ Disk encryption (SSE, BYOK)
□ Snapshots & images
□ Replication strategies (LRS, ZRS, GRS)
□ Failover & failback
□ Backup & recovery
□ Soft delete & immutability

Skills Checklist:
□ Create storage accounts
□ Configure lifecycle policies
□ Mount file shares
□ Create disk snapshots
□ Configure replication
□ Setup backup policies
□ Restore from backups

Labs Completed:
□ Storage account creation
□ Disk & snapshot management
□ Replication configuration

Score Target: 85%+
```

```
DOMAIN 3: Networking (20-25%)

Content Checklist:
□ VNet architecture
□ Subnets & address space planning
□ Network Interfaces (NICs)
□ Network Security Groups (inbound/outbound)
□ Service tags & application security groups
□ User-Defined Routes (UDRs)
□ Route tables
□ VPN Gateway types (route-based, policy-based)
□ Point-to-site, site-to-site configurations
□ VNet peering & global peering
□ VNet service endpoints
□ Private endpoints
□ Load Balancer (Layer 4)
□ Application Gateway (Layer 7)
□ WAF (Web Application Firewall)
□ Azure Firewall
□ DNS (Azure DNS)
□ Traffic Manager
□ Content Delivery Network (CDN)
□ DDoS Protection

Skills Checklist:
□ Design VNet architecture
□ Create & configure NSG rules
□ Setup VPN connections
□ Configure load balancers
□ Setup traffic routing
□ Configure firewall rules
□ Implement disaster recovery networking

Labs Completed:
□ VNet & subnet creation
□ NSG rule configuration
□ VPN Gateway setup
□ Load balancer configuration

Score Target: 75%+ (hardest domain!)
```

```
DOMAIN 4: Compute (20-25%)

Content Checklist:
□ VM creation (Windows & Linux)
□ Image selection & custom images
□ VM sizing & performance optimization
□ Virtual Machine Scale Sets (VMSS)
□ Auto-scaling policies
□ VM networking (NICs, public IPs)
□ Availability sets & zones
□ Extension types
□ Custom Script Extension
□ Desired State Configuration (DSC)
□ App Service fundamentals
□ App Service plans (tiers)
□ Deployment slots
□ Azure Functions (serverless)
□ Triggers & bindings
□ Consumption vs Premium
□ Container Registries (ACR)
□ Docker images & tags
□ Azure Kubernetes Service (AKS)
□ Pod management
□ Services & networking in K8s

Skills Checklist:
□ Deploy VMs (Windows & Linux)
□ Configure VMSS
□ Setup auto-scaling
□ Deploy applications to App Service
□ Create & test Azure Functions
□ Push images to ACR
□ Deploy to AKS
□ Configure service endpoints

Labs Completed:
□ VM creation & configuration
□ VMSS & auto-scaling
□ App Service deployment
□ Functions development
□ Container registry setup
□ AKS deployment

Score Target: 80%+
```

```
DOMAIN 5: Monitoring (10-15%)

Content Checklist:
□ Azure Monitor platform
□ Metrics vs Logs
□ Metric aggregation & time ranges
□ Log Analytics Workspace
□ Data collection rules
□ KQL (Kusto Query Language) basics
□ Alert rules (structure & conditions)
□ Action groups & notifications
□ Application Insights setup
□ Application Insights features
□ Dependency tracking
□ Performance monitoring
□ Availability tests (web tests)
□ Diagnostic settings
□ Guest diagnostics
□ Boot diagnostics
□ Serial console
□ Activity logs

Skills Checklist:
□ Configure monitoring on resources
□ Create alert rules
□ Write basic KQL queries
□ Setup Application Insights
□ Configure web tests
□ Monitor application performance
□ Analyze logs

Labs Completed:
□ Azure Monitor setup
□ Alert creation
□ Application Insights configuration
□ Log Analytics queries

Score Target: 85%+
```

### Final Week Checklist

```
Monday (Start of Week 8):
□ Review all module notes
□ Identify weak topics
□ Plan revision schedule

Tuesday-Thursday:
□ Day 1: Deep dive weak areas
□ Day 2: More weak areas
□ Day 3: Mixed review

Friday:
□ Full practice exam
□ 2-3 hours
□ Target: 70%+

Saturday:
□ Review incorrect answers
□ Study explanations
□ Fix knowledge gaps

Sunday (Day Before):
□ Light review (1-2h max)
□ Prepare exam day logistics
□ Get good sleep

Exam Day:
□ Arrive 30 min early
□ Relax & focus
□ Read questions carefully
□ Pass! 🎉
```

### Post-Exam Success Checklist

```
If Passed ✓:
□ Screenshot score
□ Take LinkedIn photo with certificate
□ Update resume
□ Update LinkedIn profile
□ Post on social media
□ Celebrate! 🎉

If Failed ✗:
□ Review score report
□ Identify weak domains
□ Study those topics extra
□ Take practice tests
□ Schedule retake (24h+ later)
□ Don't get discouraged!
   • Retry with focus
   • Most people pass 2nd time
```

---

## 🎯 Ressources Supplémentaires {#ressources-supplémentaires}

### Sites Officiels

```
Microsoft Learn:
https://learn.microsoft.com/

Azure Free Account:
https://azure.microsoft.com/free/

Certification Dashboard:
https://learn.microsoft.com/credentials/

Practice Exams Schedule:
https://learn.microsoft.com/certifications/
```

### Communautés & Support

```
Reddit:
• r/AzureCertification
• r/learnprogramming

Stack Overflow:
• Tag: azure
• Tag: az-104

Microsoft Tech Community:
https://techcommunity.microsoft.com/

Local User Groups:
• Azure Meetups
• Cloud Developer Groups
• Networking events
```

### Livres & Guides

```
Recommended Books:
1. "AZ-104 Study Guide" by William Panek
2. "Microsoft Azure Administrator" by Scott Duffy

Online Guides:
• Microsoft Azure Documentation
• Azure best practices
• Architecture Center
```

### Coût Total de Préparation

```
Microsoft Learn Modules:        FREE
Azure Free Account (labs):      FREE (1 year, $200 credit)
Sarah Kong Videos:              FREE (YouTube)
ExamTopics (free tier):         FREE
MeasureUp Practice Tests:        $99
Exam Registration:              $99-165
─────────────────────────────────────
TOTAL:                          $198-264

With paid extras:
+ Udemy course:                 $15
+ Whizlabs:                     $30
+ Books:                        $50-80
─────────────────────────────────────
TOTAL (with extras):            ~$300-400
```

---

## 🏁 Conclusion & Conseils Finaux {#conclusion}

### Points Clés à Retenir

```
1. Azure AD is everywhere
   • Understand it deeply
   • Know RBAC inside out
   • This covers 25-30% of exam

2. NETWORKING is complex
   • NSGs, VNets, subnets
   • VPN, Load Balancers
   • Study thoroughly (20-25%)

3. HANDS-ON LABS are critical
   • Don't just watch videos
   • Do every lab
   • Build muscle memory
   • Exams have interactive labs

4. Practice Tests matter
   • Take MeasureUp or ExamTopics
   • Aim for 80%+ before real exam
   • Review every wrong answer
   • Understand the "why"

5. Time management in exam
   • Read carefully
   • Flag tough questions
   • Return to flagged later
   • Don't get stuck on one question
   • Leave 5 minutes to review

6. Fail gracefully
   • If you fail, it's OK!
   • Most people pass 2nd attempt
   • Identify gaps
   • Retry with focus
```

### Final Words

```
Preparing for AZ-104 is an investment:
✓ In your career
✓ In your skills
✓ In your Azure knowledge
✓ In your professional growth

This exam will:
✓ Validate your Azure admin skills
✓ Boost your resume
✓ Increase job opportunities
✓ Improve salary prospects
✓ Build confidence in cloud

You've got this! 💪

Follow this plan:
→ Stay consistent
→ Do all labs
→ Practice regularly
→ Ask questions
→ Review failures
→ Believe in yourself

See you on the other side with your AZ-104 certification! 🎉
```

---

## 📄 Document Info

```
Plan Name:         AZ-104 Study Plan 8 Weeks
Target Audience:   IT Professionals, Cloud Beginners
Duration:          56-112 hours (depending on pace)
Created:           2024
Last Updated:      2024
Status:            Ready for Exam

Exam Details:
Title:             Microsoft Azure Administrator Certified Associate
Code:              AZ-104
Duration:          120 minutes
Questions:         40-60
Passing Score:     700/1000 (70%)
Cost:              $99-165 USD
Validity:          3 years
```

---

## Link

### Vidéos

  - [IT - CLUB D'EXPERTS](https://www.youtube.com/watch?v=tewhcoPAJ4Q&list=PLV_MjE7oovbVkM4MooDXhhNUigK2AfQor&index=1)


