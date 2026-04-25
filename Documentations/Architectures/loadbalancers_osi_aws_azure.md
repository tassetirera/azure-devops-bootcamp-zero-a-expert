# ⚖️ Load Balancers en Haute Disponibilité — AWS & Azure

## Positionnement dans le modèle OSI & cas d'usage

> **Objectif :** Comprendre les différents types de load balancers disponibles sur AWS et Azure, les couches du modèle OSI auxquelles ils opèrent, et comment ils s'intègrent dans une architecture haute disponibilité.

---

## 📋 Sommaire

1. [Rappel — Le modèle OSI en bref](#1-rappel-le-modele-osi-en-bref)
2. [Pourquoi un Load Balancer en haute disponibilité ?](#2-pourquoi-un-load-balancer-en-haute-disponibilite)
3. [Les Load Balancers AWS](#3-les-load-balancers-aws)
4. [Les Load Balancers Azure](#4-les-load-balancers-azure)
5. [Load balancer par AZ](#5-load-balancer-par-az)
6. [Terminaison TLS](#6-terminaison-tls)
7. [Tableau comparatif AWS ↔ Azure](#7-tableau-comparatif-aws-azure)
8. [Positionnement OSI — Vue synthétique](#8-positionnement-osi-vue-synthetique)
9. [Intégration dans l'architecture haute disponibilité](#9-integration-dans-larchitecture-haute-disponibilite)
10. [Choisir le bon Load Balancer](#10-choisir-le-bon-load-balancer)
11. [Bonnes pratiques & pièges courants](#11-bonnes-pratiques-pieges-courants)

---

## 1. Rappel — Le modèle OSI en bref {#1-rappel-le-modele-osi-en-bref}

Le modèle OSI (*Open Systems Interconnection*) décrit en **7 couches** comment les données transitent sur un réseau. Les load balancers interviennent principalement aux **couches 4 et 7**.

```text
┌─────────────────────────────────────────────────────────────────┐
│  Couche 7 — APPLICATION   HTTP, HTTPS, gRPC, WebSocket          │ ← ALB / Application Gateway
├─────────────────────────────────────────────────────────────────┤
│  Couche 6 — PRÉSENTATION  TLS/SSL, encodage, compression        │
├─────────────────────────────────────────────────────────────────┤
│  Couche 5 — SESSION       Gestion des sessions                  │
├─────────────────────────────────────────────────────────────────┤
│  Couche 4 — TRANSPORT     TCP, UDP, ports source/destination    │ ← NLB / Azure Load Balancer
├─────────────────────────────────────────────────────────────────┤
│  Couche 3 — RÉSEAU        IP, routage, ICMP                     │
├─────────────────────────────────────────────────────────────────┤
│  Couche 2 — LIAISON       Ethernet, MAC, VLAN                   │
├─────────────────────────────────────────────────────────────────┤
│  Couche 1 — PHYSIQUE      Câbles, fibres, ondes                 │
└─────────────────────────────────────────────────────────────────┘
```

| Couche | Nom | Données manipulées | Load Balancer concerné |
| -------- | ----- | ------------------- | ------------------------ |
| **4** | Transport | Port TCP/UDP, flux | NLB (AWS), Azure Load Balancer |
| **7** | Application | URL, headers HTTP, cookies | ALB (AWS), Application Gateway (Azure) |

> 💡 **L'essentiel :** Plus on monte dans les couches OSI, plus le load balancer a de **contexte** sur le trafic — et donc plus il peut prendre des **décisions intelligentes** de routage. En contrepartie, la **latence est légèrement plus élevée** (plus d'inspection à faire).

---

## 2. Pourquoi un Load Balancer en haute disponibilité ? {#2-pourquoi-un-load-balancer-en-haute-disponibilite}

Dans une architecture multi-AZ (Availability Zones) comme décrite dans notre cours, le load balancer est le **point d'entrée unique** qui distribue le trafic vers plusieurs instances réparties sur plusieurs zones de disponibilité.

```text
                        Internet
                           |
                           v
              ┌────────────────────────┐
              │      Load Balancer     │  ← Point d'entrée unique
              │      (multi-AZ)        │
              └────────────────────────┘
                    /              \
                   /                \
    ┌─────────────────┐      ┌─────────────────┐
    │   AZ1           │      │   AZ2           │
    │  Instance(s)    │      │  Instance(s)    │
    └─────────────────┘      └─────────────────┘
```

**Sans load balancer**, si une instance ou une AZ tombe :

- ❌ Les utilisateurs reçoivent une erreur
- ❌ Le service est indisponible (SPOF — *Single Point of Failure*)

**Avec un load balancer multi-AZ** :

- ✅ Le trafic est automatiquement redirigé vers les instances saines
- ✅ Les health checks détectent et isolent les instances défaillantes
- ✅ L'auto-scaling peut ajouter des instances à la volée
- ✅ Le SLA atteint **99,99% de disponibilité**

---

## 3. 🟠 Les Load Balancers AWS  {#3-les-load-balancers-aws}

AWS propose **trois types** de load balancers regroupés sous le service *Elastic Load Balancing (ELB)*, chacun opérant à une couche OSI différente.

---

### 3.1 ALB — Application Load Balancer (Couche 7)

L'ALB est le load balancer **HTTP/HTTPS** d'AWS. Il opère à la **couche 7 (Application)** du modèle OSI, ce qui signifie qu'il peut **lire et interpréter le contenu de la requête**.

```text
Client
  |
  | HTTPS (port 443)
  v
┌──────────────────────────────────────────┐
│         ALB — Couche 7 (HTTP)            │
│                                          │
│  Lecture de :                            │
│  • URL path  → /api/*  → Target Group A  │
│  • Host      → app.monsite.com → TG B    │
│  • Headers   → X-User-Type: premium      │
│  • Cookies   → session_id=xyz            │
│  • Méthode   → GET, POST, PUT…           │
└──────────────────────────────────────────┘
          |                |
          v                v
   ┌────────────┐   ┌────────────┐
   │ Target     │   │ Target     │
   │ Group A    │   │ Group B    │
   │ (EC2, ECS, │   │ (Lambda,   │
   │  Fargate)  │   │  EC2)      │
   └────────────┘   └────────────┘
```

**Capacités de routage de l'ALB :**

| Règle de routage | Exemple | Cible |
| ----------------- | --------- | ------- |
| **Path-based** | `/api/*` → microservice API | Target Group A |
| **Host-based** | `admin.monsite.com` → backend admin | Target Group B |
| **Header-based** | `X-Version: v2` → nouvelle version | Target Group C |
| **Query string** | `?env=staging` → environnement de test | Target Group D |
| **HTTP method** | `POST /upload` → service d'upload | Target Group E |

**Fonctionnalités clés de l'ALB :**

- 🔐 **Terminaison TLS/SSL** : le certificat est géré au niveau de l'ALB (via ACM — AWS Certificate Manager)
- 🍪 **Sticky sessions** : les requêtes d'un même client sont routées vers la même instance (via cookie)
- 🛡️ **Intégration WAF** : AWS WAF peut être attaché directement à l'ALB pour filtrer les attaques L7 (injection SQL, XSS…)
- 🔄 **Redirection HTTP → HTTPS** : règle native sans toucher aux instances
- 🐳 **Support conteneurs** : port mapping dynamique pour ECS/Fargate
- 🌐 **Support WebSocket et HTTP/2**

**Cas d'usage typique :**

```text
# Architecture microservices derrière un ALB
ALB
├── /api/users  → ECS Service "user-service"
├── /api/orders → ECS Service "order-service"
├── /admin      → EC2 "back-office"  (règle header: X-Admin: true)
└── /*          → EC2 "frontend"     (règle par défaut)
```

---

### 3.2 NLB — Network Load Balancer (Couche 4)

Le NLB opère à la **couche 4 (Transport)** du modèle OSI. Il travaille au niveau des **ports TCP/UDP** et ne lit **pas** le contenu applicatif des paquets. C'est un load balancer **ultra-performant** conçu pour les cas où la vitesse prime.

```text
Client
  |
  | TCP Port 443 (ou UDP, ou TLS)
  v
┌──────────────────────────────────────────┐
│         NLB — Couche 4 (TCP/UDP)         │
│                                          │
│  Lit uniquement :                        │
│  • IP source / destination               │
│  • Port TCP/UDP                          │
│  • Protocole (TCP, UDP, TLS, TCP_UDP)    │
│                                          │
│  Ne lit PAS :                            │
│  • URL, headers HTTP, cookies            │
│  • Corps de la requête                   │
└──────────────────────────────────────────┘
          |
          v
   ┌──────────────────┐
   │   Target Group   │
   │  EC2 / IP / ALB  │
   └──────────────────┘
```

**Caractéristiques techniques du NLB :**

- ⚡ **Ultra-faible latence** : traitement en microsecondes, sans inspection applicative
- 📌 **IP statique** : le NLB possède une IP fixe par AZ (EIP possible) — indispensable pour les firewall clients
- 🔒 **TLS Passthrough** : le NLB peut laisser passer le TLS sans le déchiffrer (terminaison sur les instances)
- 📦 **Préservation de l'IP source** : les instances voient la vraie IP du client (pas l'IP du LB)
- 🔢 **Millions de requêtes/seconde** : conçu pour des charges extrêmes

**Cas d'usage typiques du NLB :**

- Jeux en ligne (UDP, faible latence)
- VoIP, streaming (protocoles temps-réel)
- Services financiers (FIX protocol, TCP brut)
- Exposition d'un ALB avec une IP fixe (double stacking NLB → ALB)
- Endpoints PrivateLink (NLB obligatoire en frontal)

---

### 3.3 GLB — Gateway Load Balancer (Couche 3)

> ℹ️ Le GLB est un cas spécifique. Il opère à la **couche 3 (Réseau)** et sert exclusivement à intégrer des **appliances réseau tierces** (pare-feux, IDS/IPS) dans le flux de trafic.

```text
Trafic entrant
      |
      v
┌──────────────────┐
│ Gateway LB (L3)  │  ← Couche 3 — Encapsulation GENEVE
│                  │
│  Distribue vers  │
│  des appliances  │
│  (Palo Alto,     │
│   Check Point…)  │
└──────────────────┘
      |
      v (trafic inspecté)
Destination finale
```

---

### 3.4 CLB — Classic Load Balancer (déprécié)

L'ancien *Classic Load Balancer* d'AWS opérait à la fois sur les couches 4 et 7, mais de façon limitée. **Il ne doit plus être utilisé** — AWS encourage la migration vers ALB ou NLB.

---

## 4. 🔵 Les Load Balancers Azure  {#4-les-load-balancers-azure}

Azure propose également deux types principaux de load balancers, avec une logique similaire à AWS.

---

### 4.1 Application Gateway (Couche 7)

L'**Application Gateway** est l'équivalent Azure de l'ALB. Il opère à la **couche 7 (Application)** et offre des fonctionnalités de routage HTTP avancées.

```text
Client
  |
  | HTTPS (port 443)
  v
┌──────────────────────────────────────────────┐
│     Application Gateway — Couche 7 (HTTP)    │
│                                              │
│  Fonctionnalités :                           │
│  • Routage par URL path / hostname           │
│  • Terminaison SSL/TLS                       │
│  • WAF intégré (OWASP 3.x)                  │
│  • Réécriture de headers HTTP                │
│  • Affinité de session (cookie)              │
│  • Redirection HTTP → HTTPS                  │
│  • Auto-scaling (v2)                         │
└──────────────────────────────────────────────┘
          |              |
          v              v
   ┌───────────┐   ┌───────────┐
   │  Backend  │   │  Backend  │
   │  Pool A   │   │  Pool B   │
   │ (VMs/VMSS)│   │ (App Svc) │
   └───────────┘   └───────────┘
```

**SKUs disponibles :**

| SKU | Caractéristiques | Usage |
| ----- | ----------------- | ------- |
| **Standard v2** | Auto-scaling, zone-redundant, IP statique | Production moderne |
| **WAF v2** | Standard v2 + WAF OWASP intégré | Production avec protection L7 |
| Standard v1 *(déprécié)* | Pas d'auto-scaling | À migrer |
| WAF v1 *(déprécié)* | WAF sans auto-scaling | À migrer |

**Composants clés de l'Application Gateway :**

```text
┌──────────────────────────────────────────────────────────────┐
│                    Application Gateway                       │
│                                                              │
│  ┌─────────────┐   ┌─────────────┐   ┌──────────────────┐    │
│  │  Frontend   │   │  Listener   │   │  Routing Rules   │    │
│  │  IP / Port  │ → │ HTTP/HTTPS  │ → │  path, host...   │    │
│  └─────────────┘   └─────────────┘   └──────────────────┘    │
│                                               |              │
│                          ┌────────────────────┘              │
│                          v                                   │
│                 ┌─────────────────┐                          │
│                 │  HTTP Settings  │  ← Timeout, protocol,    │
│                 │  (Backend cfg)  │     port backend         │
│                 └─────────────────┘                          │
│                          |                                   │
│                          v                                   │
│                 ┌─────────────────┐                          │
│                 │  Backend Pool   │  ← VMs, VMSS, FQDN,      │
│                 │                 │     App Service, IP      │
│                 └─────────────────┘                          │
└──────────────────────────────────────────────────────────────┘
```

**WAF intégré :** L'Application Gateway WAF v2 implémente les règles OWASP (Open Web Application Security Project) pour bloquer les attaques applicatives les plus courantes (injection SQL, XSS, inclusion de fichiers, etc.) — sans modifier le code de l'application.

---

### 4.2 Azure Load Balancer (Couche 4)

L'**Azure Load Balancer** est l'équivalent du NLB AWS. Il opère à la **couche 4 (Transport)** et distribue le trafic TCP/UDP sans inspecter le contenu applicatif.

```text
Client
  |
  | TCP/UDP
  v
┌──────────────────────────────────────────┐
│     Azure Load Balancer — Couche 4       │
│                                          │
│  Lit uniquement :                        │
│  • IP source/destination                 │
│  • Port TCP/UDP                          │
│  • Protocole                             │
│                                          │
│  Types :                                 │
│  • Public  → IP publique en frontal      │
│  • Interne → IP privée (interne VNet)    │
└──────────────────────────────────────────┘
          |
          v
   ┌─────────────────────┐
   │   Backend Pool      │
   │  VMs / VMSS / IP    │
   └─────────────────────┘
```

**SKUs disponibles :**

| SKU | Zone-redundant | SLA | Usage |
| ----- | --------------- | ----- | ------- |
| **Standard** | ✅ Oui | 99,99% | Production (obligatoire pour HA) |
| Basic *(déprécié)* | ❌ Non | Pas de SLA | Développement uniquement |

> ⚠️ **Important :** Le SKU **Basic** sera **retiré le 30 septembre 2025** par Microsoft. Toutes les architectures de production doivent utiliser le SKU **Standard**.

**Modes de l'Azure Load Balancer :**

```text
# Load Balancer Public (frontal Internet)
Internet → IP Publique (Frontend) → Load Balancer → VMs (Backend Pool)

# Load Balancer Interne (frontal privé, dans le VNet)
VMs tier 1 → IP Privée (Frontend) → Load Balancer → VMs tier 2 (Backend Pool)
             ↑
             Utilisé pour le trafic inter-couches (ex: web → app)
```

---

### 4.3 Azure Traffic Manager (Couche DNS — Couche 7 applicatif)

L'**Azure Traffic Manager** est un cas particulier : il ne load-balance pas les paquets réseau mais fonctionne au niveau **DNS** pour rediriger les utilisateurs vers la région la plus proche ou la plus disponible.

```text
Client
  |
  | DNS Query → monapp.trafficmanager.net
  v
┌───────────────────────────────────────────┐
│         Azure Traffic Manager             │
│         (DNS-based, Global)               │
│                                           │
│  Méthodes de routage :                    │
│  • Priority   → failover région           │
│  • Weighted   → A/B testing (%)           │
│  • Performance → région la plus proche    │
│  • Geographic → RGPD, géo-restriction     │
└───────────────────────────────────────────┘
     |                       |
     v                       v
┌──────────────┐      ┌──────────────┐
│  Région      │      │  Région      │
│  West Europe │      │  East US     │
│  (Primary)   │      │  (Failover)  │
└──────────────┘      └──────────────┘
```

> 💡 Traffic Manager est l'équivalent d'**AWS Route 53** en mode *routing policy*. Il intervient avant que la connexion TCP ne soit établie — la décision de routage se fait au niveau de la résolution DNS.

---

## 5. Load balancer par AZ {#5-load-balancer-par-az}

---

### Un load balancer par AZ ?

Non, c'est l'inverse — c'est justement **l'un des grands intérêts** d'un load balancer managé : tu déploies **un seul load balancer logique**, et le cloud le rend automatiquement présent dans toutes tes AZ.

```text
        TON ALB / Application Gateway
        (1 seul objet dans la console)
               /           \
    ┌──────────────────────────────────┐
    |     AZ1                  AZ2     |
    |  [nœud ALB]          [nœud ALB]  |  ← Le cloud instancie
    |      |                    |      |     automatiquement un
    |  Instance A          Instance B  |     nœud par AZ
    └──────────────────────────────────┘
```

Ce que tu fais toi, c'est simplement **indiquer dans quels subnets** le load balancer peut opérer — un subnet public par AZ suffit. Le reste est géré par AWS/Azure.

Si l'AZ1 tombe, le nœud de l'AZ2 prend le relais sans intervention manuelle. C'est précisément ce qui garantit le **99,99% de disponibilité** mentionné dans ton cours.

> À ne pas confondre avec le **NAT Gateway**, lui, doit être déployé **un par AZ** manuellement — c'est une exception notable dans l'architecture.
---

## 6. Terminaison TLS {#6-terminaison-tls}

### La terminaison TLS

TLS c'est le protocole qui chiffre ta connexion HTTPS. "Terminer" TLS signifie **déchiffrer la connexion à un endroit précis** de la chaîne.

```text
# Avec terminaison TLS sur le Load Balancer (recommandé)

Client ──[HTTPS chiffré]──► Load Balancer ──[HTTP clair]──► Instance
                                  ↑
                         Le LB déchiffre ici.
                         Il lit la requête, route, puis
                         envoie en HTTP simple vers l'instance.
```

Concrètement, ça veut dire que c'est **le load balancer qui possède le certificat SSL** (le fameux cadenas 🔒 dans le navigateur). Les instances derrière n'ont pas à gérer le chiffrement — elles reçoivent du HTTP brut, ce qui est plus simple et plus performant.

Sans terminaison TLS, le chiffrement irait jusqu'à l'instance, et tu devrais gérer un certificat sur chaque serveur individuellement. C'est là que ça devient vite un cauchemar en production.

---

## 7. 🔄 Tableau comparatif AWS ↔ Azure  {#7-tableau-comparatif-aws-azure}

| Critère | 🟠 AWS ALB | 🟠 AWS NLB | 🔵 Azure Application Gateway | 🔵 Azure Load Balancer |
| --------- | ----------- | ----------- | ------------------------------ | ------------------------ |
| **Couche OSI** | 7 (Application) | 4 (Transport) | 7 (Application) | 4 (Transport) |
| **Protocoles** | HTTP, HTTPS, WebSocket, gRPC | TCP, UDP, TLS | HTTP, HTTPS, WebSocket | TCP, UDP |
| **Routage intelligent** | ✅ URL, headers, cookies | ❌ IP/Port uniquement | ✅ URL, headers, cookies | ❌ IP/Port uniquement |
| **Terminaison TLS** | ✅ Oui (ACM) | ✅ Oui ou passthrough | ✅ Oui (Key Vault) | ❌ Non |
| **WAF intégré** | Via AWS WAF (addon) | ❌ | ✅ WAF v2 natif | ❌ |
| **IP statique** | ❌ DNS uniquement | ✅ EIP par AZ | ✅ IP publique statique | ✅ IP publique statique |
| **IP source préservée** | Header X-Forwarded-For | ✅ Oui (nativement) | Header X-Forwarded-For | ✅ Oui (nativement) |
| **Sticky sessions** | ✅ Cookie LB | ❌ | ✅ Cookie | ✅ Hash IP/Port |
| **Auto-scaling** | ✅ Automatique | ✅ Automatique | ✅ v2 (automatique) | ✅ Automatique |
| **Multi-AZ (zone-redundant)** | ✅ Natif | ✅ Natif | ✅ v2 natif | ✅ Standard SKU |
| **Health checks** | HTTP, HTTPS, gRPC | TCP, HTTP, HTTPS | HTTP, HTTPS | TCP, HTTP |
| **Backends supportés** | EC2, ECS, Lambda, IP | EC2, IP, ALB | VMs, VMSS, App Service, IP | VMs, VMSS, IP |
| **Cas d'usage principal** | Applications web, microservices | Hautes perfs, jeux, VoIP | Applications web, microservices | Hautes perfs, TCP brut |

---

## 8. 🗺️ Positionnement OSI — Vue synthétique {#8-positionnement-osi-vue-synthetique}

```text
Modèle OSI                    AWS                          Azure
─────────────────────────────────────────────────────────────────────────────

Couche 7      ┌─────────────────────┐       ┌───────────────────────────┐
APPLICATION   │  ALB                │       │  Application Gateway      │
              │  (HTTP, HTTPS,      │       │  (HTTP, HTTPS,            │
              │  WebSocket, gRPC)   │       │  WebSocket + WAF natif)   │
              │                     │       │                           │
              │  Route 53           │       │  Traffic Manager          │
              │  (DNS routing)      │       │  (DNS routing global)     │
              └─────────────────────┘       └───────────────────────────┘

Couche 4      ┌─────────────────────┐       ┌───────────────────────────┐
TRANSPORT     │  NLB                │       │  Azure Load Balancer      │
              │  (TCP, UDP, TLS)    │       │  (TCP, UDP)               │
              │  IP statique        │       │  Public ou Interne        │
              └─────────────────────┘       └───────────────────────────┘

Couche 3      ┌─────────────────────┐
RÉSEAU        │  GLB                │       (Pas d'équivalent direct Azure)
              │  (Appliances NVA)   │
              └─────────────────────┘

─────────────────────────────────────────────────────────────────────────────
```

### Règle de décision simple

```text
┌─────────────────────────────────────────────────────────────┐
│               Quel load balancer choisir ?                  │
└─────────────────────────────────────────────────────────────┘
                           │
          ┌────────────────┴────────────────┐
          │                                 │
    Trafic HTTP/HTTPS ?              Trafic TCP/UDP brut ?
    Besoin de WAF ?                  Jeux, VoIP, FIX ?
    Routage par URL ?                Latence ultra-faible ?
    Microservices ?                  IP fixe obligatoire ?
          │                                 │
          v                                 v
  ┌───────────────┐               ┌─────────────────────┐
  │ Couche 7      │               │ Couche 4             │
  │ AWS : ALB     │               │ AWS : NLB            │
  │ Azure: App GW │               │ Azure: Azure LB      │
  └───────────────┘               └─────────────────────┘
```

---

## 9. 🏗️ Intégration dans l'architecture haute disponibilité  {#9-integration-dans-larchitecture-haute-disponibilite}

### 9.1 Architecture AWS avec ALB multi-AZ

D'après notre cours, voici comment l'ALB s'intègre dans un VPC haute disponibilité :

```text
Internet
    |
    v
Route 53 (DNS + Health Checks)
    |
    v
Internet Gateway (IGW)
    |
    ┌───────────────────────────────────────────┐
    │              VPC 11.0.0.0/16              │
    │                                           │
    │  Public Subnet AZ1     Public Subnet AZ2  │
    │  11.0.1.0/24           11.0.2.0/24        │
    │  ┌──────────────┐      ┌──────────────┐   │
    │  │  ALB Node 1  │      │  ALB Node 2  │   │  ← ALB déployé dans les
    │  │  (L7)        │      │  (L7)        │   │     subnets publics, multi-AZ
    │  └──────────────┘      └──────────────┘   │
    │         │                    │            │
    │         └────────┬───────────┘            │
    │                  │                        │
    │  Private Subnet AZ1    Private Subnet AZ2 │
    │  11.0.3.0/24           11.0.4.0/24        │
    │  ┌──────────────┐      ┌──────────────┐   │
    │  │   EC2 App1   │      │   EC2 App2   │   │  ← Target Group : instances
    │  │ (Auto Scaling│      │ (Auto Scaling│   │     privées, health-checkées
    │  │   Group)     │      │   Group)     │   │
    │  └──────────────┘      └──────────────┘   │
    │         │                    │            │
    │         v                    v            │
    │  ┌────────────────────────────────────┐   │
    │  │  RDS Multi-AZ (Primary + Standby)  │   │
    │  │  Private Subnet DB                 │   │
    │  └────────────────────────────────────┘   │
    └───────────────────────────────────────────┘
```

**Flux d'une requête :**

1. L'utilisateur résout `monapp.com` → Route 53 retourne l'IP du ALB
2. La requête HTTPS arrive sur l'ALB (Couche 7) — le TLS est terminé ici
3. L'ALB lit l'URL path et les headers, applique les règles de routage
4. La requête est forwardée (HTTP) vers l'instance EC2 saine dans le Target Group
5. Si l'instance AZ1 est unhealthy → l'ALB bascule automatiquement sur AZ2

---

### 9.2 Architecture Azure avec Application Gateway multi-AZ

```text
Internet
    |
    v
Azure DNS / Traffic Manager
    |
    |
    ┌─────────────────────────────────────────────┐
    │                VNet 11.0.0.0/16             │
    │                                             │
    │  Public Subnet AZ1      Public Subnet AZ2   │
    │  11.0.1.0/24            11.0.2.0/24         │
    │  ┌──────────────────────────────────────┐   │
    │  │   Application Gateway v2 (WAF)       │   │  ← App GW déployé dans
    │  │   Zone-redundant (AZ1 + AZ2)         │   │     un subnet dédié,
    │  │   Couche 7, WAF OWASP activé         │   │     avec IP statique
    │  └──────────────────────────────────────┘   │
    │                  │                          │
    │  Private Subnet AZ1    Private Subnet AZ2   │
    │  11.0.3.0/24           11.0.4.0/24          │
    │  ┌──────────────┐      ┌──────────────┐     │
    │  │   VM/VMSS    │      │   VM/VMSS    │     │  ← Backend Pool
    │  │   (app-nsg)  │      │   (app-nsg)  │     │
    │  └──────────────┘      └──────────────┘     │
    │         │                    │              │
    │  ┌───────────────────────────────────────┐  │
    │  │  Azure SQL Flexible Server (HA)       │  │
    │  │  Subnet DB                            │  │
    │  └───────────────────────────────────────┘  │
    └─────────────────────────────────────────────┘
```

---

### 9.3 Pattern double load balancer (L7 + L4)

Dans certaines architectures, les deux types de load balancer sont combinés :

```text
# AWS — NLB devant ALB (IP fixe obligatoire + routing intelligent)
Internet → NLB (L4, IP statique) → ALB (L7, routing HTTP) → EC2

# Azure — Load Balancer interne entre couches applicatives
App GW (L7) → VMs Web → Azure LB Interne (L4) → VMs App → Azure SQL
                                    ↑
                     Utilisé pour le trafic est/ouest
                     entre la couche web et la couche app
```

---

## 10. 🎯 Choisir le bon Load Balancer {#10-choisir-le-bon-load-balancer}

### Arbre de décision complet

```text
Mon trafic est de type HTTP/HTTPS ?
├─ OUI
│   ├─ J'ai besoin d'un WAF intégré ?
│   │   ├─ OUI (AWS)   → ALB + AWS WAF
│   │   ├─ OUI (Azure) → Application Gateway WAF v2
│   │   └─ NON → ALB (AWS) ou Application Gateway Standard v2 (Azure)
│   │
│   ├─ Je dois router selon l'URL path ou le hostname ?
│   │   └─ OUI → ALB (AWS) ou Application Gateway (Azure)  [Couche 7 obligatoire]
│   │
│   └─ J'ai besoin de sticky sessions par cookie ?
│       └─ OUI → ALB (AWS) ou Application Gateway (Azure)  [Couche 7]
│
└─ NON (TCP/UDP brut, jeux, VoIP, FIX…)
    ├─ J'ai besoin d'une IP fixe ?
    │   └─ OUI → NLB (AWS) ou Azure Load Balancer Standard (Azure)  [Couche 4]
    │
    ├─ Latence ultra-faible obligatoire ?
    │   └─ OUI → NLB (AWS) ou Azure Load Balancer (Azure)  [Couche 4]
    │
    └─ Je load-balance des appliances réseau (firewall, IDS) ?
        └─ OUI (AWS) → Gateway Load Balancer  [Couche 3]
```

### Tableau de synthèse par cas d'usage

| Cas d'usage | Load Balancer recommandé | Couche OSI |
| ------------- | -------------------------- | ----------- |
| Application web (HTTP/HTTPS) | ALB / Application Gateway | **7** |
| API Gateway / Microservices | ALB / Application Gateway | **7** |
| Multi-tenant (virtualhosting) | ALB / Application Gateway | **7** |
| Protection WAF incluse | ALB+WAF / App GW WAF v2 | **7** |
| Jeux en ligne temps-réel | NLB / Azure LB | **4** |
| VoIP / streaming UDP | NLB / Azure LB | **4** |
| Services financiers (FIX) | NLB / Azure LB | **4** |
| PrivateLink / Endpoint | NLB (obligatoire) | **4** |
| IP statique obligatoire | NLB / Azure LB | **4** |
| Appliances réseau (firewall) | GLB (AWS uniquement) | **3** |
| Failover multi-régions | Route 53 / Traffic Manager | DNS |

---

## 11. ⚠️ Bonnes pratiques & pièges courants {#11-bonnes-pratiques-pieges-courants}

### 11.1 Health Checks — Ne jamais les négliger

```yaml
# Exemple de health check ALB
HealthCheckConfig:
  Protocol: HTTP
  Path: /health           # Endpoint dédié (ne pas utiliser /)
  Port: traffic-port
  HealthyThresholdCount: 2   # 2 succès → instance healthy
  UnhealthyThresholdCount: 3 # 3 échecs → instance retirée du pool
  Interval: 30               # Vérification toutes les 30s
  Timeout: 5                 # Timeout de 5s
```

> ⚠️ **Piège fréquent :** Utiliser `/` comme endpoint de health check. Si la page d'accueil dépend d'une BDD ou d'un service tiers, une panne externe peut marquer toutes vos instances comme unhealthy alors qu'elles fonctionnent. Créez un endpoint `/health` qui ne vérifie que la santé locale de l'instance.

### 11.2 Gestion du TLS

```text
# ✅ Bonne pratique : terminaison TLS au niveau du load balancer
Client → [HTTPS] → ALB/App GW (terminaison TLS) → [HTTP] → Instances
                         ↑
           Certificat géré centralement (ACM / Key Vault)
           Renouvellement automatique
           Une seule configuration à maintenir

# ❌ Mauvaise pratique : TLS end-to-end sans raison
Client → [HTTPS] → Load Balancer → [HTTPS] → Instances
                                        ↑
              Double déchiffrement, gestion des certs sur chaque instance,
              certificats à renouveler manuellement → overhead inutile
              (sauf contraintes de conformité strictes ex: PCI-DSS)
```

### 11.3 Sticky Sessions — Avec précaution

Les sticky sessions (affinité de session par cookie) maintiennent un utilisateur sur la même instance backend. C'est utile pour les applications **stateful** — mais elles **réduisent l'efficacité du load balancing** :

```text
# Sans sticky sessions (recommandé pour applications stateless)
Requête 1 → Instance A
Requête 2 → Instance B   ← Distribution équitable
Requête 3 → Instance C

# Avec sticky sessions (applications stateful legacy)
Requête 1 → Instance A
Requête 2 → Instance A   ← Toujours la même instance
Requête 3 → Instance A   ← Si A tombe → session perdue !
```

> 💡 **Recommandation :** Préférez les applications **stateless** avec une session centralisée (Redis, ElastiCache / Azure Cache for Redis). Le load balancer peut alors distribuer librement sans état à maintenir.

### 11.4 Cross-Zone Load Balancing (AWS)

```text
# Sans Cross-Zone (par défaut sur NLB)
AZ1 : 2 instances → reçoivent 50% du trafic chacune
AZ2 : 8 instances → reçoivent 7.25% du trafic chacune
                ↑ Déséquilibre si le nombre d'instances est inégal entre AZ

# Avec Cross-Zone (par défaut sur ALB)
AZ1 + AZ2 : 10 instances → reçoivent 10% du trafic chacune
                ↑ Distribution équitable, mais data transfer inter-AZ facturé
                  (0.01$/GB sur AWS — surveiller la facture)
```

### 11.5 Sécurité — Restreindre l'accès aux instances backend

```text
# ✅ Bonne pratique : les instances n'acceptent le trafic QUE du load balancer

# AWS — Security Group Reference
Inbound rule sur app-sg :
  Allow TCP 8080 from <sg-id-de-l-ALB>   ← Référence le SG de l'ALB, pas une IP

# Azure — Application Security Group
NSG rule sur app-nsg :
  Allow TCP 8080 from <asg-app-gateway>   ← Référence l'ASG de l'App Gateway
```

> ⚠️ **Piège Azure :** Ne pas oublier que l'Application Gateway possède ses propres IPs dans son subnet. Autoriser ces IPs (ou le subnet de l'App GW) dans le NSG du backend est indispensable.

### 11.6 Checklist de mise en production

- [ ] Health check configuré sur un endpoint `/health` dédié
- [ ] Terminaison TLS au niveau du load balancer avec certificat valide
- [ ] Logs d'accès activés (ALB access logs vers S3 / App GW via Azure Monitor)
- [ ] Auto-scaling configuré sur le Target Group / Backend Pool
- [ ] Load balancer déployé en multi-AZ (zone-redundant)
- [ ] Instances backend dans des subnets **privés** (pas d'IP publique)
- [ ] Security Groups / NSG restreignant le trafic au seul load balancer
- [ ] WAF activé si exposition publique d'une application web
- [ ] Timeout de connexion adapté à l'application (défaut 60s sur ALB, 30s App GW)
- [ ] Monitoring des métriques clés : `TargetResponseTime`, `HTTP5xxCount`, `HealthyHostCount`

---

## 📌 Synthèse finale

| | 🟠 AWS | 🔵 Azure | Couche OSI |
| --- | --- | --- | --- |
| **Load Balancer HTTP** | ALB (Application LB) | Application Gateway | **7** |
| **WAF** | AWS WAF (addon ALB) | App GW WAF v2 (natif) | **7** |
| **Load Balancer TCP/UDP** | NLB (Network LB) | Azure Load Balancer | **4** |
| **Load Balancer réseau/appliances** | GLB (Gateway LB) | — | **3** |
| **DNS Routing global** | Route 53 | Traffic Manager | DNS |

> 🧠 **À retenir :** La couche OSI d'un load balancer détermine sa **capacité d'inspection** — plus la couche est haute, plus le load balancer est intelligent (et légèrement plus lent). La couche 7 permet le routage applicatif fin ; la couche 4 offre la performance brute. Dans une architecture haute disponibilité, les deux types sont souvent complémentaires : un load balancer L7 en frontal public, un load balancer L4 pour le trafic est/ouest interne.

---

## 📚 Pour aller plus loin

| Ressource | Lien |
| ----------- | ------ |
| AWS ALB — Documentation officielle | [docs.aws.amazon.com/elasticloadbalancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/) |
| AWS NLB — Documentation officielle | [docs.aws.amazon.com/elasticloadbalancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/) |
| Azure Application Gateway | [learn.microsoft.com/azure/application-gateway](https://learn.microsoft.com/azure/application-gateway/) |
| Azure Load Balancer | [learn.microsoft.com/azure/load-balancer](https://learn.microsoft.com/azure/load-balancer/) |
| Azure Traffic Manager | [learn.microsoft.com/azure/traffic-manager](https://learn.microsoft.com/azure/traffic-manager/) |
| Certifications réseau AWS | AWS Advanced Networking Specialty |
| Certifications réseau Azure | AZ-700 Azure Network Engineer |
