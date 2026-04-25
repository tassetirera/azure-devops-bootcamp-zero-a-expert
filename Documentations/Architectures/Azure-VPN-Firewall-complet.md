# 🔐 Azure VPN & Azure Firewall — Cours Complet du Débutant à l'Expert

**Objectif du cours :** Maîtriser les concepts fondamentaux et avancés d'Azure VPN Gateway et Azure Firewall, comprendre leurs architectures, cas d'usage, et les intégrer dans une infrastructure cloud sécurisée et hautement disponible.

---

## 📋 Sommaire

1. [Concepts Fondamentaux](#1-concepts-fondamentaux)
2. [Azure VPN Gateway — Guide Complet](#2-azure-vpn-gateway-guide-complet)
3. [Azure Firewall — Guide Complet](#3-azure-firewall-guide-complet)
4. [Comparaison AWS vs Azure](#4-comparaison-aws-vs-azure)
5. [Architectures Intégrées](#5-architectures-integrees)
6. [Cas d'Usage Réels](#6-cas-dusage-reels)
7. [Configuration Pas à Pas](#7-configuration-pas-a-pas)
8. [Infrastructure as Code](#8-infrastructure-as-code)
9. [Sécurité & Bonnes Pratiques](#9-securite-bonnes-pratiques)
10. [Diagnostic & Dépannage](#10-diagnostic-depannage)
11. [Exercices Pratiques](#11-exercices-pratiques)
12. [Ressources & Références](#12-ressources-references)

---

## 1. 🎓 Concepts Fondamentaux {#1-concepts-fondamentaux}

### 1.1 Qu'est-ce qu'une VPN (Virtual Private Network) ?

Une **VPN** établit un tunnel chiffré entre deux réseaux (ou un utilisateur et un réseau) sur Internet public, permettant une communication sécurisée comme si les deux réseaux étaient directement connectés.

#### Les 3 Types de VPN sur Azure

| Type | Description | Use Case |
| --- | --- | --- |
| **Site-to-Site (S2S)** | Connecte deux réseaux (ex: locaux ↔ Azure) | Hybride cloud, filiale à HQ |
| **Point-to-Site (P2S)** | Connecte un utilisateur/client à un réseau Azure | Télétravail, accès à distance |
| **VNet-to-VNet** | Connecte deux VNets Azure | Multi-région, isolement réseau |

### 1.2 Qu'est-ce qu'un Firewall ?

Un **Firewall** inspecte le trafic réseau entrant/sortant et applique des règles pour autoriser ou bloquer les connexions.

#### Les 2 Niveaux de Firewall sur Azure

```text
┌─────────────────────────────────────────────────────────┐
│ COUCHE 7 (Application Layer)                            │
│ → Azure Firewall (avec règles applicatives)             │
│ → Application Gateway (WAF)                             │
├─────────────────────────────────────────────────────────┤
│ COUCHE 4 (Transport Layer)                              │
│ → Network Security Groups (NSG)                         │
│ → Azure Firewall (règles réseau)                        │
├─────────────────────────────────────────────────────────┤
│ COUCHE 3 (Network Layer)                                │
│ → Routing, règles réseau                                │
└─────────────────────────────────────────────────────────┘
```

### 1.3 VPN vs Firewall — Quelle différence ?

| Aspect | VPN | Firewall |
| --- | --- | --- |
| **Objectif** | **Connexion sécurisée** entre réseaux | **Filtrage** du trafic autorisé/bloqué |
| **Chiffrement** | ✅ Chiffre tout le trafic | ❌ Ne chiffre pas (but du chiffrement : confidentialité) |
| **Utilisation** | Connecter réseaux distants | Protéger un réseau de menaces |
| **Couche OSI** | L3-L4 (Network/Transport) | L3-L7 (Network à Application) |
| **Exemple combiné** | VPN crée le tunnel → Firewall inspecte le trafic dedans | Connexion sécurisée + contrôle d'accès |

---

## 2. 🚪 Azure VPN Gateway — Guide Complet {#2-azure-vpn-gateway-guide-complet}

### 2.1 Architecture & Composants

```text
Internet (Public)
       |
       v
+──────────────────────────────+
|  VPN Gateway (SKU: Basic/    |
|  Standard/HighPerformance)   |
|  Public IP: 203.0.113.45     |
+──────────────────────────────+
       |
       | Tunnel chiffré (IPSec/IKEv2)
       v
+──────────────────────────────+
|   VNet Azure                 |
| 10.0.0.0/16                  |
+──────────────────────────────+
       |
       v (Routage interne)
+──────────────────────────────+
|   Subnet App: 10.0.1.0/24    |
|   Subnet DB: 10.0.2.0/24     |
+──────────────────────────────+
```

### 2.2 Types de VPN Gateway

#### VPN Gateway Modes

```text
┌────────────────────────────────────────┐
│         VPN GATEWAY MODES              │
├────────────────────────────────────────┤
│ 1. ROUTE-BASED (Dynamic Routing)       │
│    • Utilise la table de routage       │
│    • IPSec/IKEv2                       │
│    • À PRIVILÉGIER (moderne)           │
│                                        │
│ 2. POLICY-BASED (Static Routing)       │
│    • Définit les testes sur IP         │
│    • Moins flexible                    │
│    • Hérité (legacy)                   │
└────────────────────────────────────────┘
```

#### SKU Disponibles (Prix & Performance)

| SKU | Débit (Mbps) | Connexions | Prix/mois* | Use Case |
| --- | --- | --- | --- | --- |
| **Basic** | ~100 | 10 S2S | ~15€ | Développement/test, faible traffic |
| **Standard** | ~1,000 | 20 S2S | ~50€ | Production, trafic moyen |
| **HighPerformance** | ~10,000 | 30 S2S | ~150€ | Mission-critique, haut trafic |
| **VpnGw1/2/3** | 650/1,300/2,600 | 32/128/128 | Varié | Nouvelle génération, meilleur ratio |
| **Ultra** | 10+ Gbps | 128+ | 300€+ | Enterprise, ultra haute performance |

Estimation basée sur région EU (2024)

### 2.3 Configuration Site-to-Site (S2S)

#### Étapes de Configuration

```text
ÉTAPE 1: Créer la VPN Gateway Azure
    ↓
ÉTAPE 2: Créer une Local Network Gateway
        (représente le réseau local/distant)
    ↓
ÉTAPE 3: Créer une Connexion VPN
    ↓
ÉTAPE 4: Télécharger la configuration VPN
        (pour configurer l'équipement distant)
    ↓
ÉTAPE 5: Tester la connexion
```

#### Schéma Complet S2S

```text
┌────────────────────────────────────────────────────────────────┐
│                      LOCAL NETWORK                             │
│                   (ex: DataCenter)                             │
│                  10.50.0.0/16                                  │
│                                                                │
│  ┌──────────────────┐                                          │
│  │ Firewall/Router  │                                          │
│  │ IP: 203.0.113.10 │  (IP Publique)                           │
│  └────────┬─────────┘                                          │
└───────────┼────────────────────────────────────────────────────┘
            │
    IPSec Tunnel (chiffré)
   Port UDP 500 (IKE)
   Port UDP 4500 (IPSec)
            │
┌───────────┼────────────────────────────────────────────────────┐
│           v                                                    │
│  ┌────────────────────┐                                        │
│  │  VPN Gateway       │                                        │
│  │  IP: 203.0.113.45  │  (IP Publique Azure)                   │
│  │  Mode: Route-Based │                                        │
│  └────────┬───────────┘                                        │
│           │                                                    │
│           v                                                    │
│  ┌─────────────────────────────────┐                           │
│  │      AZURE VNET                 │                           │
│  │    10.0.0.0/16                  │                           │
│  │                                 │                           │
│  │  ┌──────────────────┐           │                           │
│  │  │ App Subnet       │           │                           │
│  │  │ 10.0.1.0/24      │           │                           │
│  │  │ (2 VMs)          │           │                           │
│  │  └──────────────────┘           │                           │
│  │                                 │                           │
│  │  ┌──────────────────┐           │                           │
│  │  │ DB Subnet        │           │                           │
│  │  │ 10.0.2.0/24      │           │                           │
│  │  │ (SQL Server)     │           │                           │
│  │  └──────────────────┘           │                           │
│  └─────────────────────────────────┘                           │
│                                                                │
│        AZURE                                                   │
└────────────────────────────────────────────────────────────────┘
```

### 2.4 Configuration Point-to-Site (P2S)

Point-to-Site connecte des **clients individuels** (télétravail, etc.) à un VNet Azure.

#### Architecture P2S

```text
┌─────────────┐         Internet        ┌──────────────────────┐
│             │                         │                      │
│ Client 1    │──────────────┐          │  VPN Gateway         │
│ (VPN Conn)  │              │          │  (P2S)               │
│             │              │          │  Public IP:          │
└─────────────┘              │          │  203.0.113.45        │
                             │          │                      │
┌─────────────┐              ├──────────│  Protocole:          │
│             │              │          │  • SSTP (L2TP/IPSec) │
│ Client 2    │──────────────┤          │  • OpenVPN           │
│ (Télétravaill)             │          │  • IKEv2             │
│             │              │          │                      │
└─────────────┘              │          └─────────┬────────────┘
                             │                    │
┌─────────────┐              │                    │
│             │              │          (Tunnel chiffré)
│ Mobile App  │──────────────┘                    │
│ (iPad)      │                                   v
│             │              ┌──────────────────────────────┐
└─────────────┘              │  AZURE VNET                  │
                             │  10.0.0.0/16                 │
                             │                              │
                             │  Clients reçoivent IP de:    │
                             │  172.16.0.0/24 (exemple)     │
                             │                              │
                             └──────────────────────────────┘

FLUX DE CONNEXION:
1. Client demande connexion P2S
2. VPN Gateway genère certificat
3. Établit tunnel SSTP/IKEv2
4. Client reçoit IP privée du VNet
5. Client accède aux ressources Azure comme s'il était local
```

### 2.5 Configuration VNet-to-VNet

Connecte deux VNets Azure (même région ou régions différentes).

```text
Region: West Europe            Region: East Europe
┌──────────────────┐          ┌──────────────────┐
│  VNet 1          │          │  VNet 2          │
│  10.0.0.0/16     │          │  10.10.0.0/16    │
│                  │          │                  │
│ ┌──────────────┐ │          │ ┌──────────────┐ │
│ │ App Tier     │ │          │ │ Data Tier    │ │
│ │ 10.0.1.0/24  │ │          │ │ 10.10.1.0/24 │ │
│ └────────┬─────┘ │          │ └────────┬─────┘ │
│          │       │          │          │       │
│ ┌────────v─────┐ │          │ ┌────────v─────┐ │
│ │VPN Gateway   │ │          │ │VPN Gateway   │ │
│ │203.0.113.45  │ │          │ │203.0.113.80  │ │
│ └────────┬─────┘ │          │ └────────┬─────┘ │
└──────────┼───────┘          └──────────┼───────┘
           │                             │
           └────────── Tunnel IPSec ─────┘
              (Chiffré, Port UDP 500/4500)

✅ AVANTAGES:
• Connexion rapide (pas d'Internet public)
• Débit élevé
• Redondance possible
```

### 2.6 Protocoles VPN & Authentification

#### Protocoles Supportés

```text
┌─────────────────────────────────────────────────────┐
│           PROTOCOLES VPN AZURE                      │
├─────────────────────────────────────────────────────┤
│ S2S (Site-to-Site):                                 │
│  • IPSec (standard industriel)                      │
│  • IKEv2 (plus moderne, meilleur handshake)         │
│                                                     │
│ P2S (Point-to-Site):                                │
│  • SSTP (SSL/TLS, port 443 — traverse proxies)      │
│  • OpenVPN (protocole open-source)                  │
│  • IKEv2 (performance)                              │
│                                                     │
│ CHIFFREMENT:                                        │
│  • AES-128, AES-192, AES-256 (options)              │
│  • SHA-1, SHA-256, SHA-384, SHA-512                 │
│                                                     │
│ PHASE 1 (IKE):                                      │
│  • Établit une connexion de contrôle (chiffré)      │
│                                                     │
│ PHASE 2 (IPSec):                                    │
│  • Établit le tunnel de données (chiffré)           │
└─────────────────────────────────────────────────────┘
```

#### Authentification S2S

```text
┌──────────────────────────────────────────────┐
│    AUTHENTIFICATION S2S OPTIONS              │
├──────────────────────────────────────────────┤
│ 1. PRE-SHARED KEY (PSK)                      │
│    • Clé partagée (ex: MySecretKey123!)      │
│    • Simple, moins sécurisé                  │
│    • ❌ Ne pas utiliser en production       │
│                                              │
│ 2. CERTIFICATS (Recommandé)                  │
│    • Certificat Root CA                      │
│    • Certificat de client/serveur            │
│    • ✅ Plus sécurisé en production          │
│    • Géré par Azure ou votre PKI             │
└──────────────────────────────────────────────┘
```

---

## 3. 🧱 Azure Firewall — Guide Complet {#3-azure-firewall-guide-complet}

### 3.1 Qu'est-ce qu'Azure Firewall ?

**Azure Firewall** est un service cloud **stateful**, **fully managed**, qui protège les ressources VNet contre les menaces entrantes/sortantes en inspectant le trafic aux couches 3-7 (réseau et application).

#### Schéma: Azure Firewall dans une Architecture

```text
Internet
    |
    v
┌─────────────────────────────────────────────────┐
│   Azure Firewall (Subnets: AzureFirewallSubnet) │
│   • Stateful                                    │
│   • Inspect réseau (L3-L4)                      │
│   • Inspect application (L7)                    │
│   • Logs centralisés                            │
└─────────────────────────────────────────────────┘
    |
    | Trafic filtré
    v
┌─────────────────────────────────────┐
│  VNet (10.0.0.0/16)                 │
│                                     │
│  ┌──────────────────┐               │
│  │ App Subnet       │               │
│  │ 10.0.1.0/24      │               │
│  └──────────────────┘               │
│                                     │
│  ┌──────────────────┐               │
│  │ DB Subnet        │               │
│  │ 10.0.2.0/24      │               │
│  └──────────────────┘               │
│                                     │
│  ┌─────────────────────┐            │
│  │ AzureFirewallSubnet │            │
│  │ 10.0.3.0/24         │            │
│  └─────────────────────┘            │
└─────────────────────────────────────┘
```

### 3.2 SKU Azure Firewall

| SKU | Débit | Price | Use Case |
| --- | --- | --- | --- |
| **Standard** | ~2.5 Gbps | ~1.5€/h (~1000€/mois) | Production générale |
| **Premium** | ~30 Gbps | ~3€/h (~2000€/mois) | Mission-critique, inspection avancée |
| **Basic** | 100 Mbps | ~0.5€/h (~300€/mois) | Petite charge, dev/test |

### 3.3 Types de Règles Firewall

#### Règles Réseau (Network Rules) — Couche 3-4

```text
┌──────────────────────────────────────┐
│  RÈGLES RÉSEAU (Network Rules)       │
├──────────────────────────────────────┤
│ Appliquées AVANT règles application  │
│ Filtrent sur: IP, Port, Protocole    │
│                                      │
│ Exemple:                             │
│ ┌──────────────────────────────────┐ │
│ │ Nom: AllowSQL                    │ │
│ │ Priorité: 100                    │ │
│ │ Action: Allow                    │ │
│ │ Protocole: TCP                   │ │
│ │ Source: 10.0.1.0/24              │ │
│ │ Port Source: *                   │ │
│ │ Destination: 10.0.2.0/24         │ │
│ │ Port Destination: 1433           │ │
│ └──────────────────────────────────┘ │
│                                      │
│ Traduction: Autoriser les VMs en     │
│ 10.0.1.0/24 à se connecter à SQL     │
│ (port 1433) en 10.0.2.0/24           │
└──────────────────────────────────────┘
```

#### Règles Application (Application Rules) — Couche 7

```text
┌──────────────────────────────────────┐
│  RÈGLES APPLICATION (App Rules)      │
├──────────────────────────────────────┤
│ Inspectent le contenu HTTP/HTTPS     │
│ Filtrent sur: Domaine, URL, Host     │
│                                      │
│ Exemple:                             │
│ ┌──────────────────────────────────┐ │
│ │ Nom: AllowWindowsUpdate          │ │
│ │ Priorité: 200                    │ │
│ │ Action: Allow                    │ │
│ │ Protocoles: HTTP, HTTPS          │ │
│ │ Source: 10.0.1.0/24              │ │
│ │ Target FQDNs: *.update.microsoft │ │
│ │              .com                │ │
│ │              *.windowsupdate.com │ │
│ └──────────────────────────────────┘ │
│                                      │
│ Traduction: Autoriser les VMs à      │
│ télécharger les mises à jour Windows │
└──────────────────────────────────────┘
```

#### Règles NAT — Redirection Port

```text
┌───────────────────────────────────────┐
│  RÈGLES NAT (Destination NAT)         │
├───────────────────────────────────────┤
│ Redirigent le trafic entrant Internet │
│ Vers des ressources VNet              │
│                                       │
│ Exemple:                              │
│ ┌──────────────────────────────────┐  │
│ │ Nom: RDP-To-VM                   │  │
│ │ Priorité: 100                    │  │
│ │ Protocole: TCP                   │  │
│ │ Port Destination (firewall IP):  │  │
│ │   3389                           │  │
│ │ Adresse traduite (VM interne):   │  │
│ │   10.0.1.10:3389                 │  │
│ └──────────────────────────────────┘  │
│                                       │
│ Traduction:                           │
│ Trafic -> FW:3389 → VM 10.0.1.10:3389 │
└───────────────────────────────────────┘
```

### 3.4 Collections de Règles

**Les règles sont organisées en collections** avec une **priorité** :

```text
FLUX DE TRAITEMENT:
1. Règles NAT (priorité 100-200)
   ↓ (si pas match, continue)
2. Règles Réseau (priorité 100-65535)
   ↓ (si pas match, continue)
3. Règles Application (priorité 100-65535)
   ↓ (si pas match, continue)
4. Action par défaut: DENY (DROP)

RÉSULTAT FINAL:
┌─────────────────────┐
│ ALLOW / DENY / DROP │
└─────────────────────┘
```

### 3.5 Threat Intelligence (OSINT)

Azure Firewall peut bloquer les adresses IP/domaines **connus pour être malveillants** :

```text
┌───────────────────────────────────────┐
│   THREAT INTELLIGENCE MODES           │
├───────────────────────────────────────┤
│ • OFF: Aucun filtrage threat intel    │
│                                       │
│ • ALERT: Log les connexions vers IP   │
│   malveillantes, mais autorise        │
│   (mode warning)                      │
│                                       │
│ • DENY: Bloque les connexions vers IP │
│   malveillantes (mode strict)         │
│   ✅ Recommandé en production         │
│                                       │
│ Source: Microsoft Threat Intelligence │
│         Feed (mis à jour en continu)  │
└───────────────────────────────────────┘
```

---

## 4. 📊 Comparaison AWS vs Azure {#4-comparaison-aws-vs-azure}

### 4.1 VPN Gateway Comparison

| Feature | 🟠 AWS | 🔵 Azure |
| --- | --- | --- |
| **Service** | Virtual Private Gateway (VGW) | VPN Gateway |
| **Type S2S** | IPSec | IPSec + IKEv2 |
| **Type P2S** | Client VPN Endpoint | VPN Gateway P2S |
| **VNet-to-VNet** | VPC Peering (préféré) ou TGW | VNet Peering ou VPN Gateway |
| **Haute Dispo** | Redondance automatique (2 tunnels) | Redondance configurable |
| **Débit Max** | 1.25 Gbps (Customer Gateway) | 10 Gbps (HighPerformance) |
| **Chiffrement** | AES-128/192/256 | AES-128/192/256 |
| **Modèle Tarif** | Paiement à l'heure + données | Paiement à l'heure + données |
| **Failover** | Manuel ou via Route53 | Auto avec redondance multi-AZ |

### 4.2 Firewall Comparison

| Feature | 🟠 AWS | 🔵 Azure |
| --- | --- | --- |
| **Firewall Réseau (L3-L4)** | Network Firewall (nouveau) | Network Security Group (NSG) |
| **Firewall Application (L7)** | WAF (Web Application Firewall) | Azure Firewall + WAF |
| **Inspection Profonde** | AWS Network Firewall | Azure Firewall (Standard/Premium) |
| **Stateful** | ✅ | ✅ |
| **Gestion Centralisée** | AWS Firewall Manager | Azure Firewall Manager |
| **Prix** | ~$1.94/h | ~$1.5/h (Standard) |
| **Haute Disponibilité** | Multi-AZ automatique | Zones de disponibilité |
| **Rules Format** | JSON/Terraform | Portal/CLI/Terraform |
| **Threat Intel** | ✅ (AWS Threat Intel) | ✅ (Microsoft Threat Intel) |

---

## 5. 🏗️ Architectures Intégrées {#5-architectures-integrees}

### 5.1 Architecture Sécurisée: VPN + Firewall

```text
┌──────────────────────────────────────────────────────────────────┐
│                      DATACENTER ON-PREMISE                       │
│                       10.50.0.0/16                                │
│                                                                   │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ Firewall Local & Router (Ex: Cisco, Fortinet, Palo Alto)   │ │
│  │ IP Publique: 203.0.113.10                                  │ │
│  └────────────────┬───────────────────────────────────────────┘ │
└───────────────────┼──────────────────────────────────────────────┘
                    │
        ┌───────────┼──────────┐
        │           │          │
        │    IPSec Tunnel      │
        │   (Chiffré)          │
        │           │          │
┌───────┴───────────┼──────────┴────────────────────────────────────┐
│                   │                                               │
│        ┌──────────v────────┐                                      │
│        │  VPN Gateway      │                                      │
│        │  203.0.113.45     │                                      │
│        │  (1-3 AZ)         │                                      │
│        └──────────┬────────┘                                      │
│                   │                                               │
│        ┌──────────v────────────────────┐                          │
│        │   Route Table (UDR)           │                          │
│        │   10.50.0.0/16 → VPN GW       │                          │
│        │   0.0.0.0/0 → Azure Firewall  │                          │
│        └────────┬──────────────────────┘                          │
│                 │                                                 │
│        ┌────────v──────────────────────────────────────────┐      │
│        │       AZURE FIREWALL                              │      │
│        │       (Subnet: AzureFirewallSubnet)               │      │
│        │       10.0.3.0/24                                 │      │
│        │                                                   │      │
│        │  ┌─────────────────────────────────────────────┐  │      │
│        │  │ NAT Rules:                                  │  │      │
│        │  │ • RDP: port 3389 → VM 10.0.1.5              │  │      │
│        │  └─────────────────────────────────────────────┘  │      │
│        │                                                   │      │
│        │  ┌─────────────────────────────────────────────┐  │      │
│        │  │ Network Rules:                              │  │      │
│        │  │ • Allow 10.50.0.0/16 → 10.0.1.0/24 (App)    │  │      │
│        │  │ • Allow 10.50.0.0/16 → 10.0.2.0/24 (DB)     │  │      │
│        │  └─────────────────────────────────────────────┘  │      │
│        │                                                   │      │
│        │  ┌─────────────────────────────────────────────┐  │      │
│        │  │ Application Rules:                          │  │      │
│        │  │ • Allow HTTP/HTTPS to *.microsoft.com       │  │      │
│        │  │ • Allow DNS (port 53)                       │  │      │
│        │  └─────────────────────────────────────────────┘  │      │
│        └────────┬──────────────────────────────────────────┘      │
│                 │                                                 │
│                 v (Trafic filtré)                                 │
│        ┌────────────────────┐                                     │
│        │   App Subnet       │                                     │
│        │  10.0.1.0/24       │                                     │
│        │  • 2-3 VMs         │                                     │
│        │  • NSG: app-nsg    │                                     │
│        └────────────────────┘                                     │
│                                                                   │
│        ┌────────────────────┐                                     │
│        │   DB Subnet        │                                     │
│        │  10.0.2.0/24       │                                     │
│        │  • SQL Server      │                                     │
│        │  • NSG: db-nsg     │                                     │
│        └────────────────────┘                                     │
│                                                                   │
│         AZURE VNET: 10.0.0.0/16                                   │
└───────────────────────────────────────────────────────────────────┘

✅ FLUX D'UN CLIENT DISTANT:
1. Client connecté au DC via VPN IPSec
2. Envoie trafic vers 10.0.1.0/24 (App)
3. Trafic traverse VPN Gateway (chiffré)
4. Azure Firewall inspecte (règles NAT, Network, App)
5. Trafic autorisé → VM App reçoit connexion
6. Réponse traverse le même chemin (retour)

✅ FLUX D'UN UTILISATEUR P2S:
1. Utilisateur distant se connecte via SSTP/IKEv2
2. Reçoit IP du pool P2S (ex: 172.16.0.5)
3. Peut accéder ressources VNet selon NSG
4. Firewall protège l'entrée/sortie
```

### 5.2 Architecture Hub-Spoke avec VPN + Firewall

```text
┌───────────────────────────────────────────────────────────────┐
│                    HUB VNET (10.0.0.0/16)                     │
│                                                               │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │           AZURE FIREWALL (Centralisé)                   │  │
│  │  • Protège tout le trafic entrant/sortant               │  │
│  │  • Gestion unique des règles                            │  │
│  └─────────────────────────────────────────────────────────┘  │
│                            |                                  │
│  ┌─────────────────────────┼───────────────────────────────┐  │
│  │      VPN GATEWAY (S2S & P2S)                            │  │
│  │  • Connecte DC on-premise (S2S)                         │  │
│  │  • Connecte clients distants (P2S)                      │  │
│  └─────────────────────────┼───────────────────────────────┘  │
└────────────────────────────┼──────────────────────────────────┘
                             │
                ┌────────────┼────────────┐
                │            │            │
         ┌──────v────┐  ┌────v──────┐ ┌──v──────┐
         │ SPOKE 1   │  │ SPOKE 2   │ │ SPOKE 3 │
         │ 10.1.0.0  │  │ 10.2.0.0  │ │ 10.3.0  │
         │ /16       │  │ /16       │ │ .0/16   │
         │           │  │           │ │         │
         │ • App     │  │ • DB      │ │ • Data  │
         │ • NSG     │  │ • NSG     │ │ Lake    │
         │ • VMs     │  │ • RDS     │ │ • NSG   │
         └───────────┘  └───────────┘ └─────────┘

AVANTAGES:
✅ Centralisation firewall (une place pour les règles)
✅ VPN centralisée (un tunnel au DC)
✅ Routage simplifié
✅ Scaling facile (ajouter spokes)
✅ Isolation entre spokes possible
```

### 5.3 Architecture Multi-Région avec VPN Redondante

```text
┌────────────────────────────────────────┬────────────────────────────┐
│   REGION: WEST EUROPE                  │   REGION: EAST EUROPE      │
│                                        │                            │
│  ┌──────────────────────────────────┐  │  ┌──────────────────────┐  │
│  │  VPN GW 1 (Primary)              │  │  │  VPN GW 2 (Secondary)│  │
│  │  203.0.113.45                    │  │  │  203.0.113.80        │  │
│  │  Mode: Active-Active             │  │  │  Mode: Active-Active │  │
│  └────────┬─────────────────────────┘  │  └────────┬─────────────┘  │
│           │                            │           │                │
│  ┌────────v──────────────────────────┐ │ ┌─────────v─────────────┐  │
│  │  AZURE FIREWALL (West EU)         │ │ │ AZURE FIREWALL (East) │  │
│  │  10.0.3.0/24                      │ │ │ 10.10.3.0/24          │  │
│  │                                    │ │ │                      │  │
│  │  Règles centralisées (synchro)    │ │ │ (Réplicage geo)       │  │
│  └────────┬──────────────────────────┘ │ └────────┬──────────────┘  │
│           │                            │          │                 │
│  ┌────────v──────────────────────────┐ │ ┌────────v──────────────┐  │
│  │  VNET: 10.0.0.0/16                │ │ │ VNET: 10.10.0.0/16    │  │
│  │  • App Subnet: 10.0.1.0/24        │ │ │ • App Subnet: 10.10.1 │  │
│  │  • DB Subnet: 10.0.2.0/24         │ │ │   .0/24               │  │
│  │  • FW Subnet: 10.0.3.0/24         │ │ │ • DB Subnet: 10.10.2  │  │
│  │                                   │ │ │   .0/24               │  │
│  │  • 3 VMs App                      │ │ │ • FW Subnet: 10.10.3  │  │
│  │  • SQL DB                         │ │ │   .0/24               │  │
│  └───────────────────────────────────┘ │ │ • 3 VMs App           │  │
│                                        │ │ • SQL DB              │  │
│                                        │ └───────────────────────┘  │
└────────────────────────────────────────┴────────────────────────────┘
                  │                                │
                  │  VNet Peering Global           │
                  │  (Tous subnets connectés)      │
                  └────────────────────────────────┘

DC ON-PREMISE (10.50.0.0/16)
         │
         │ ┌─────────────────────────────────────┐
         │ │   DUAL TUNNEL (Redondance)          │
         │ ├─────────────────────────────────────┤
         │ │ Tunnel 1: DC → VPN GW 1 (West EU)   │
         │ │ Tunnel 2: DC → VPN GW 2 (East EU)   │
         │ └─────────────────────────────────────┘
         │
    ┌────v──────┐
    │  Firewall │
    │   DC      │
    └───────────┘

✅ HA GÉOGRAPHIQUE:
• Tunnel 1 down → Trafic bascule auto à Tunnel 2
• Firewall synchro → Règles identiques 2 régions
• App failover -> Traffic de West → East
```

---

## 6. 💼 Cas d'Usage Réels {#6-cas-dusage-reels}

### 6.1 Cas 1: Migration Cloud Hybride (DC + Azure)

**Problème:** Une entreprise a un DC on-premise avec 500 utilisateurs, souhaite migrer certaines apps à Azure tout en gardant certaines locales.

**Solution:**

```text
┌────────────────────────────────────────────────────────────────┐
│ ARCHITECTURE                                                   │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  1. S2S VPN: DC ↔ Azure VNet (chiffré)                         │
│  2. Azure Firewall: Filtrer trafic hybride                     │
│  3. NSG + NACLs: Défense en profondeur                         │
│                                                                │
│  DC RESOURCES:                   AZURE RESOURCES:              │
│  • ERP SAP (local)               • Web App (migré)             │
│  • File Server (local)            • DB migré (SQL Azure)       │
│  • AD DC (local)                  • Storage (Blobs)            │
│                                                                │
│  ✅ Apps locales et Azure communiquent via VPN                │
│  ✅ Authentification centralisée (AD Hybrid)                  │
│  ✅ Chiffrement end-to-end                                    │
└────────────────────────────────────────────────────────────────┘

MISE EN PLACE (Étapes):
1. Créer VPN Gateway & Local Network Gateway (DC)
2. Établir tunnel S2S VPN
3. Configurer Azure Firewall rules
4. Migrer app par app (progressif)
5. Tester failover
```

### 6.2 Cas 2: Télétravail Sécurisé (P2S VPN + Firewall)

**Problème:** 200 employés en télétravail doivent accéder à des ressources internes Azure de manière sécurisée.

**Solution:**

```text
┌────────────────────────────────────────────────────────────────┐
│ ARCHITECTURE                                                   │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  1. P2S VPN Gateway: Chaque employé se connecte via SSTP/IKEv2 │
│  2. MFA (Azure AD): Double authentification                    │
│  3. Azure Firewall: Inspecter trafic employés                  │
│  4. Conditional Access: Accès basé sur device compliance       │
│                                                                │
│  EMPLOYEE DEVICE                                               │
│  • Windows 10/11 + Azure VPN Client                            │
│  • Mac/Linux + OpenVPN                                         │
│  • Mobile (iOS/Android) + Cert Auth                            │
│                                                                │
│  CONNEXION:                                                    │
│  1. Employee se connecte VPN P2S                               │
│  2. Auth avec Azure AD + MFA                                   │
│  3. Reçoit IP du pool VPN (ex: 172.16.0.5)                     │
│  4. Accès ressources selon règles firewall/NSG                 │
│  5. Internet sort via Firewall (proxy + DLP)                   │
│                                                                │
│  ✅ Chiffrement bout-à-bout                                    │
│  ✅ Authentication forte (MFA)                                 │
│  ✅ Audit complet (logs Azure Firewall)                        │
│  ✅ Révocation rapide (AD group)                               │
└────────────────────────────────────────────────────────────────┘

COÛTS:
• VPN Gateway P2S: ~$50/mois
• Azure Firewall: ~$1500/mois
• Storage logs: ~$50/mois
= ~$1600/mois pour 200 employés = ~$8/emp/mois (très rentable)
```

### 6.3 Cas 3: Sécurisation Trafic Internet Sortant (Egress Filtering)

**Problème:** Des VMs Azure téléchargent des malwares depuis Internet, besoin de filtrer l'accès sortant.

**Solution:**

```text
┌────────────────────────────────────────────────────────────────┐
│ ARCHITECTURE (Egress Filtering)                                │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  VM (App Subnet 10.0.1.0/24)                                   │
│        │                                                       │
│        │ Trafic sortant (default route: 0.0.0.0/0)             │
│        v                                                       │
│  ┌──────────────────┐                                          │
│  │ Firewall Subnet  │                                          │
│  │ 10.0.3.0/24      │                                          │
│  │                  │                                          │
│  │ RULES:           │                                          │
│  │ ✅ Allow HTTP/HTTPS to *.microsoft.com                      │
│  │ ✅ Allow NTP to time.nist.gov                               │
│  │ ✅ Allow DNS to 8.8.8.8                                     │
│  │ ❌ Deny ALL other (Default)                                 │
│  │                  │                                          │
│  │ Threat Intel:    │                                          │
│  │ • Block IPs malveillants                                    │
│  │ • Log tentatives                                            │
│  └────────┬─────────┘                                          │
│           │                                                    │
│           v (Autorisés uniquement)                             │
│        Internet                                                │
│                                                                │
│ RÉSULTAT:                                                      │
│ • VM ne peut télécharger que depuis Microsoft                  │
│ • Tentative accès malveillant? → Blocked + Logged              │
│ • Admin reçoit alerte Azure Monitor                            │
└────────────────────────────────────────────────────────────────┘

RÈGLES APPLICATION:
┌────────────────────────────────────────────┐
│ AllowWindowsUpdate                         │
│  Protocole: HTTP, HTTPS                    │
│  Source: 10.0.1.0/24, 10.0.2.0/24          │
│  Target FQDNs: *.update.microsoft.com      │
│                *.windowsupdate.com         │
│                *.microsoft.com             │
└────────────────────────────────────────────┘

┌────────────────────────────────────────────┐
│ AllowDNS                                   │
│  Protocole: TCP, UDP port 53               │
│  Source: 10.0.0.0/16                       │
│  Destination: 8.8.8.8, 8.8.4.4             │
└────────────────────────────────────────────┘
```

---

## 7. 🛠️ Configuration Pas à Pas {#7-configuration-pas-a-pas}

### 7.1 Configuration VPN Gateway S2S (Étape par Étape)

**PRÉREQUIS:**

- Subscription Azure active
- VNet créé (ex: 10.0.0.0/16)
- Subnet pour Gateway créé (ex: 10.0.0.0/27, minimum requis)
- IP publique statique DC on-premise

#### ÉTAPE 1: Créer la VPN Gateway

```azure-cli
# Créer une IP publique pour le gateway
az network public-ip create \
  --name MyVPNGW-PubIP \
  --resource-group MyRG \
  --allocation-method Static \
  --sku Standard

# Créer la VPN Gateway
az network vnet-gateway create \
  --name MyVPNGateway \
  --resource-group MyRG \
  --public-ip-address MyVPNGW-PubIP \
  --vnet MyVNet \
  --gateway-type Vpn \
  --vpn-type RouteBased \
  --sku Standard \
  --no-wait

# Attendre création (5-10 minutes)
az network vnet-gateway wait --created \
  --name MyVPNGateway \
  --resource-group MyRG
```

#### ÉTAPE 2: Créer Local Network Gateway (représente DC on-premise)

```azure-cli
az network local-gateway create \
  --name MyDCLocalGateway \
  --resource-group MyRG \
  --gateway-ip-address 203.0.113.10 \
  --address-prefixes 10.50.0.0/16 10.50.1.0/24

# 203.0.113.10 = IP publique du DC
# 10.50.0.0/16 = Réseau du DC on-premise
```

#### ÉTAPE 3: Créer la Connexion VPN

```azure-cli
# Créer avec Pre-Shared Key (démo, pas production!)
az network vpn-connection create \
  --name MyDCtoAzureVPN \
  --resource-group MyRG \
  --vnet-gateway1 MyVPNGateway \
  --shared-key MySecretKey123! \
  --local-gateway2 MyDCLocalGateway \
  --connection-type IPSec

# ⚠️ En production: utiliser certificats, pas PSK!
```

#### ÉTAPE 4: Télécharger Config VPN (pour l'équipement DC)

```azure-cli
# Ceci donne un ZIP avec config pour Cisco/Palo Alto/Fortigate/etc
az network vpn-connection download \
  --name MyDCtoAzureVPN \
  --resource-group MyRG \
  --output table

# Ouvrir le ZIP et appliquer config sur le device DC
```

#### ÉTAPE 5: Vérifier l'État de la Connexion

```azure-cli
az network vpn-connection show \
  --name MyDCtoAzureVPN \
  --resource-group MyRG

# Output attendu:
# "connectionStatus": "Connected"
# "connectionProtocol": "IKEv2"
# "ingressBytesTransferred": 1234567
# "egressBytesTransferred": 7654321
```

#### ÉTAPE 6: Tester la Connexion

```bash
# Sur une VM Azure (10.0.1.10), tenter ping vers DC
ping 10.50.0.1

# Si répond → ✅ VPN fonctionne!
# Si timeout → ❌ Vérifier routing tables et règles firewall
```

### 7.2 Configuration Point-to-Site P2S VPN

#### ÉTAPE 1: Configurer l'authentification du client (Certificats)

```powershell
# Sur machine locale (Windows PowerShell Admin):

# Créer Root Certificate
$cert = New-SelfSignedCertificate -Type Custom `
  -KeySpec Signature `
  -Subject "CN=MyRootCert" `
  -KeyExportPolicy Exportable `
  -HashAlgorithm sha256 `
  -KeyLength 2048 `
  -CertStoreLocation "Cert:\CurrentUser\My" `
  -NotAfter (Get-Date).AddYears(5)

# Créer Client Certificate (signé par Root)
$params = @{
  Type              = 'Custom'
  KeySpec           = 'Signature'
  Subject           = 'CN=MyClientCert'
  DnsName           = 'MyClientCert'
  Issuer            = $cert
  KeyExportPolicy   = 'Exportable'
  HashAlgorithm     = 'sha256'
  KeyLength         = 2048
  CertStoreLocation = 'Cert:\CurrentUser\My'
  NotAfter          = (Get-Date).AddYears(3)
}
$clientCert = New-SelfSignedCertificate @params

# Exporter les certificats
Export-PfxCertificate -Cert $clientCert -FilePath C:\mycert.pfx -Password (ConvertTo-SecureString -String "password" -AsPlainText -Force)
Export-Certificate -Cert $cert -FilePath C:\myroot.cer -Type CERT
```

#### ÉTAPE 2: Ajouter Root Certificate à la VPN Gateway

```azure-cli
az network vnet-gateway root-cert create \
  --gateway-name MyVPNGateway \
  --resource-group MyRG \
  --name MyRootCert \
  --public-cert-data @C:\myroot.cer
```

#### ÉTAPE 3: Configurer la Configuration P2S

```azure-cli
# Configurer les paramètres P2S
az network vnet-gateway update \
  --name MyVPNGateway \
  --resource-group MyRG \
  --vpn-client-protocol SSTP IKEv2 OpenVPN \
  --vpn-client-root-certificates MyRootCert \
  --address-pool 172.16.0.0/24

# SSTP = Port 443 (traverse proxies)
# IKEv2 = Meilleure performance
# OpenVPN = Cross-platform
# Pool 172.16.0.0/24 = IP assignées aux clients P2S
```

#### ÉTAPE 4: Télécharger le Profil VPN Client

```azure-cli
# Générer le package VPN pour les clients
az network vnet-gateway vpn-client generate \
  --name MyVPNGateway \
  --resource-group MyRG

# Output: URL pour télécharger profil (ZIP)
# Exemple: https://mystorageaccount.blob.core.windows.net/vpn/VpnClientConfiguration.zip
```

#### ÉTAPE 5: Client se Connecte au VPN P2S

```text
Sur Windows 10/11:
1. Télécharger VpnClientConfiguration.zip
2. Extraire et exécuter VpnClientSetup.exe (64-bit)
3. Windows ajoute la connexion VPN
4. Ouvrir Settings → Network → VPN
5. Cliquer "Connect" sur la connexion VPN
6. Authentifier avec certificat client (mycert.pfx)
7. Recevoir IP du pool (ex: 172.16.0.5)
8. Ping VM Azure: ping 10.0.1.10 ✅

Sur macOS/Linux (OpenVPN):
1. Installer OpenVPN client
2. Télécharger OpenVPN config depuis le ZIP
3. openvpn --config vpnconfig.ovpn
4. Authentifier
5. ifconfig → voir IP 172.16.0.x
6. ping 10.0.1.10 ✅
```

### 7.3 Configuration Azure Firewall

#### ÉTAPE 1: Créer un Subnet pour Azure Firewall

```azure-cli
# Le subnet DOIT s'appeler "AzureFirewallSubnet"
az network vnet subnet create \
  --resource-group MyRG \
  --vnet-name MyVNet \
  --name AzureFirewallSubnet \
  --address-prefix 10.0.3.0/24

# Minimum /26 requis, recommandé /24 pour expansion future
```

#### ÉTAPE 2: Créer IP Publique pour Firewall

```azure-cli
az network public-ip create \
  --name MyFirewall-PubIP \
  --resource-group MyRG \
  --sku Standard \
  --allocation-method Static
```

#### ÉTAPE 3: Créer Azure Firewall

```azure-cli
az network firewall create \
  --name MyAzureFirewall \
  --resource-group MyRG \
  --location eastus \
  --public-ip MyFirewall-PubIP \
  --virtual-network MyVNet \
  --sku Standard \
  --threat-intel-mode Deny

# SKU Standard = ~$1.5/h
# threat-intel-mode Deny = Bloquer IPs malveillantes
```

#### ÉTAPE 4: Ajouter Règles Réseau (Network Rules)

```azure-cli
# Créer une collection de règles réseau
az network firewall network-rule create \
  --firewall-name MyAzureFirewall \
  --resource-group MyRG \
  --collection-name AllowSQL \
  --name AllowSQL_DC_to_Azure \
  --action Allow \
  --priority 100 \
  --source-addresses 10.50.0.0/16 \
  --destination-addresses 10.0.2.0/24 \
  --destination-ports 1433 \
  --protocols TCP

# Traduction: Autoriser les clients en 10.50.0.0/16
# à accéder au port 1433 (SQL) sur 10.0.2.0/24 (DB subnet)
```

#### ÉTAPE 5: Ajouter Règles Application (App Rules)

```azure-cli
# Créer règle pour permettre Windows Update
az network firewall application-rule create \
  --firewall-name MyAzureFirewall \
  --resource-group MyRG \
  --collection-name AllowWindowsUpdate \
  --name AllowUpdate \
  --action Allow \
  --priority 200 \
  --source-addresses 10.0.0.0/16 \
  --protocols Http=80 Https=443 \
  --target-fqdns \
    "*.update.microsoft.com" \
    "*.windowsupdate.com" \
    "*.microsoft.com"

# Traduction: Les VMs du VNet peut télécharger mises à jour
```

#### ÉTAPE 6: Configurer les Route Tables pour utiliser le Firewall

```azure-cli
# Créer une route table pour le subnet App
az network route-table create \
  --name AppSubnetRouteTable \
  --resource-group MyRG

# Ajouter une route par défaut via le Firewall
az network route-table route create \
  --route-table-name AppSubnetRouteTable \
  --resource-group MyRG \
  --name DefaultRoute \
  --address-prefix 0.0.0.0/0 \
  --next-hop-type VirtualAppliance \
  --next-hop-ip-address 10.0.3.4  # IP privée du Firewall

# Associer la route table au subnet App
az network vnet subnet update \
  --vnet-name MyVNet \
  --name AppSubnet \
  --resource-group MyRG \
  --route-table AppSubnetRouteTable
```

#### ÉTAPE 7: Vérifier l'État du Firewall

```azure-cli
az network firewall show \
  --name MyAzureFirewall \
  --resource-group MyRG \
  --query provisioningState

# Expected output: "Succeeded"
```

---

## 8. 📝 Infrastructure as Code {#8-infrastructure-as-code}

### 8.1 Terraform — Architecture Complète VPN + Firewall

```hcl
# main.tf

terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

# Variables
variable "location" {
  default = "eastus"
}

variable "vnet_cidr" {
  default = "10.0.0.0/16"
}

variable "on_premise_cidr" {
  default = "10.50.0.0/16"
}

variable "on_premise_vpn_gateway_ip" {
  default = "203.0.113.10"
}

# Resource Group
resource "azurerm_resource_group" "main" {
  name     = "MyResourceGroup"
  location = var.location
}

# VNet
resource "azurerm_virtual_network" "main" {
  name                = "MyVNet"
  address_space       = [var.vnet_cidr]
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
}

# Subnets
resource "azurerm_subnet" "app" {
  name                 = "AppSubnet"
  resource_group_name  = azurerm_resource_group.main.name
  virtual_network_name = azurerm_virtual_network.main.name
  address_prefixes     = ["10.0.1.0/24"]
}

resource "azurerm_subnet" "db" {
  name                 = "DBSubnet"
  resource_group_name  = azurerm_resource_group.main.name
  virtual_network_name = azurerm_virtual_network.main.name
  address_prefixes     = ["10.0.2.0/24"]
}

resource "azurerm_subnet" "firewall" {
  name                 = "AzureFirewallSubnet"
  resource_group_name  = azurerm_resource_group.main.name
  virtual_network_name = azurerm_virtual_network.main.name
  address_prefixes     = ["10.0.3.0/24"]
}

resource "azurerm_subnet" "gateway" {
  name                 = "GatewaySubnet"
  resource_group_name  = azurerm_resource_group.main.name
  virtual_network_name = azurerm_virtual_network.main.name
  address_prefixes     = ["10.0.0.0/27"]
}

# VPN Gateway — Public IP
resource "azurerm_public_ip" "vpn_gw" {
  name                = "VPNGateway-PublicIP"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  allocation_method   = "Static"
  sku                 = "Standard"
}

# VPN Gateway
resource "azurerm_vpn_gateway" "main" {
  name                = "MyVPNGateway"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  type                = "Vpn"
  vpn_type            = "RouteBased"
  sku                 = "Standard"

  ip_configuration {
    name                 = "vnetGatewayConfig"
    public_ip_address_id = azurerm_public_ip.vpn_gw.id
    private_ip_address_allocation = "Dynamic"
    subnet_id            = azurerm_subnet.gateway.id
  }
}

# Local Network Gateway (représente le DC on-premise)
resource "azurerm_local_network_gateway" "on_premise" {
  name                = "OnPremiseNetworkGateway"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  gateway_address     = var.on_premise_vpn_gateway_ip
  address_space       = [var.on_premise_cidr]
}

# VPN Connection (S2S)
resource "azurerm_vpn_connection" "s2s" {
  name                = "OnPremiseToAzureVPN"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  type                = "IPSec"
  virtual_network_gateway_id = azurerm_vpn_gateway.main.id
  local_network_gateway_id   = azurerm_local_network_gateway.on_premise.id
  shared_key                  = "MySecretKey123!"  # ⚠️ À remplacer par certificat
}

# Azure Firewall — Public IP
resource "azurerm_public_ip" "firewall" {
  name                = "AzureFirewall-PublicIP"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  allocation_method   = "Static"
  sku                 = "Standard"
}

# Azure Firewall
resource "azurerm_firewall" "main" {
  name                = "MyAzureFirewall"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  sku_name            = "AZFW_VNet"
  sku_tier            = "Standard"
  threat_intel_mode   = "Deny"

  ip_configuration {
    name                 = "configuration"
    subnet_id            = azurerm_subnet.firewall.id
    public_ip_address_id = azurerm_public_ip.firewall.id
  }
}

# Firewall Network Rule Collection
resource "azurerm_firewall_network_rule_collection" "allow_sql" {
  name                = "AllowSQL"
  azure_firewall_name = azurerm_firewall.main.name
  resource_group_name = azurerm_resource_group.main.name
  priority            = 100
  action              = "Allow"

  rule {
    name                  = "AllowSQL_DC_to_Azure"
    source_addresses      = [var.on_premise_cidr]
    destination_addresses = [azurerm_subnet.db.address_prefix[0]]
    destination_ports     = ["1433"]
    protocols             = ["TCP"]
  }
}

# Firewall Application Rule Collection
resource "azurerm_firewall_application_rule_collection" "allow_windows_update" {
  name                = "AllowWindowsUpdate"
  azure_firewall_name = azurerm_firewall.main.name
  resource_group_name = azurerm_resource_group.main.name
  priority            = 200
  action              = "Allow"

  rule {
    name             = "AllowUpdate"
    source_addresses = ["10.0.0.0/16"]
    target_fqdns     = [
      "*.update.microsoft.com",
      "*.windowsupdate.com",
      "*.microsoft.com"
    ]
    protocols {
      port = "80"
      type = "Http"
    }
    protocols {
      port = "443"
      type = "Https"
    }
  }
}

# Route Table for App Subnet
resource "azurerm_route_table" "app" {
  name                = "AppSubnetRouteTable"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name

  route {
    name                   = "DefaultRoute"
    address_prefix         = "0.0.0.0/0"
    next_hop_type          = "VirtualAppliance"
    next_hop_in_ip_address = azurerm_firewall.main.ip_configuration[0].private_ip_address
  }
}

# Associate Route Table to App Subnet
resource "azurerm_subnet_route_table_association" "app" {
  subnet_id      = azurerm_subnet.app.id
  route_table_id = azurerm_route_table.app.id
}

# Outputs
output "vpn_gateway_public_ip" {
  value = azurerm_public_ip.vpn_gw.ip_address
}

output "firewall_public_ip" {
  value = azurerm_public_ip.firewall.ip_address
}

output "firewall_private_ip" {
  value = azurerm_firewall.main.ip_configuration[0].private_ip_address
}
```

**Utilisation:**

```bash
# Initialiser Terraform
terraform init

# Planifier les ressources
terraform plan -out=tfplan

# Appliquer la configuration
terraform apply tfplan

# Obtenir les outputs
terraform output
```

### 8.2 Bicep — Architecture Complète VPN + Firewall

```bicep
// main.bicep

param location string = 'eastus'
param vnetCidr string = '10.0.0.0/16'
param onPremiseCidr string = '10.50.0.0/16'
param onPremiseVpnGatewayIp string = '203.0.113.10'

var vnetName = 'MyVNet'
var vpnGwName = 'MyVPNGateway'
var firewallName = 'MyAzureFirewall'
var resourceGroupName = resourceGroup().name

// VNet + Subnets
resource vnet 'Microsoft.Network/virtualNetworks@2023-05-01' = {
  name: vnetName
  location: location
  properties: {
    addressSpace: {
      addressPrefixes: [
        vnetCidr
      ]
    }
    subnets: [
      {
        name: 'AppSubnet'
        properties: {
          addressPrefix: '10.0.1.0/24'
        }
      }
      {
        name: 'DBSubnet'
        properties: {
          addressPrefix: '10.0.2.0/24'
        }
      }
      {
        name: 'AzureFirewallSubnet'
        properties: {
          addressPrefix: '10.0.3.0/24'
        }
      }
      {
        name: 'GatewaySubnet'
        properties: {
          addressPrefix: '10.0.0.0/27'
        }
      }
    ]
  }
}

// VPN Gateway Public IP
resource vpnGwPublicIp 'Microsoft.Network/publicIPAddresses@2023-05-01' = {
  name: '${vpnGwName}-PublicIP'
  location: location
  sku: {
    name: 'Standard'
  }
  properties: {
    publicIPAllocationMethod: 'Static'
  }
}

// VPN Gateway
resource vpnGateway 'Microsoft.Network/virtualNetworkGateways@2023-05-01' = {
  name: vpnGwName
  location: location
  properties: {
    gatewayType: 'Vpn'
    vpnType: 'RouteBased'
    sku: {
      name: 'Standard'
      tier: 'Standard'
    }
    ipConfigurations: [
      {
        name: 'vnetGatewayConfig'
        properties: {
          privateIPAllocationMethod: 'Dynamic'
          publicIPAddress: {
            id: vpnGwPublicIp.id
          }
          subnet: {
            id: '${vnet.id}/subnets/GatewaySubnet'
          }
        }
      }
    ]
  }
}

// Local Network Gateway
resource localNetworkGateway 'Microsoft.Network/localNetworkGateways@2023-05-01' = {
  name: 'OnPremiseNetworkGateway'
  location: location
  properties: {
    gatewayIpAddress: onPremiseVpnGatewayIp
    localNetworkAddressSpace: {
      addressPrefixes: [
        onPremiseCidr
      ]
    }
  }
}

// VPN Connection
resource vpnConnection 'Microsoft.Network/connections@2023-05-01' = {
  name: 'OnPremiseToAzureVPN'
  location: location
  properties: {
    virtualNetworkGateway1: {
      id: vpnGateway.id
    }
    localNetworkGateway2: {
      id: localNetworkGateway.id
    }
    connectionType: 'IPSec'
    sharedKey: 'MySecretKey123!'  // ⚠️ À remplacer par certificat
  }
}

// Azure Firewall Public IP
resource firewallPublicIp 'Microsoft.Network/publicIPAddresses@2023-05-01' = {
  name: '${firewallName}-PublicIP'
  location: location
  sku: {
    name: 'Standard'
  }
  properties: {
    publicIPAllocationMethod: 'Static'
  }
}

// Azure Firewall
resource firewall 'Microsoft.Network/azureFirewalls@2023-05-01' = {
  name: firewallName
  location: location
  properties: {
    sku: {
      name: 'AZFW_VNet'
      tier: 'Standard'
    }
    threatIntelMode: 'Deny'
    ipConfigurations: [
      {
        name: 'configuration'
        properties: {
          subnet: {
            id: '${vnet.id}/subnets/AzureFirewallSubnet'
          }
          publicIPAddress: {
            id: firewallPublicIp.id
          }
        }
      }
    ]
    networkRuleCollections: [
      {
        name: 'AllowSQL'
        priority: 100
        action: {
          type: 'Allow'
        }
        rules: [
          {
            name: 'AllowSQL_DC_to_Azure'
            sourceAddresses: [
              onPremiseCidr
            ]
            destinationAddresses: [
              '10.0.2.0/24'
            ]
            destinationPorts: [
              '1433'
            ]
            protocols: [
              'TCP'
            ]
          }
        ]
      }
    ]
    applicationRuleCollections: [
      {
        name: 'AllowWindowsUpdate'
        priority: 200
        action: {
          type: 'Allow'
        }
        rules: [
          {
            name: 'AllowUpdate'
            sourceAddresses: [
              '10.0.0.0/16'
            ]
            protocols: [
              {
                protocolType: 'Http'
                port: 80
              }
              {
                protocolType: 'Https'
                port: 443
              }
            ]
            targetFqdns: [
              '*.update.microsoft.com'
              '*.windowsupdate.com'
              '*.microsoft.com'
            ]
          }
        ]
      }
    ]
  }
}

// Route Table
resource routeTable 'Microsoft.Network/routeTables@2023-05-01' = {
  name: 'AppSubnetRouteTable'
  location: location
  properties: {
    routes: [
      {
        name: 'DefaultRoute'
        properties: {
          addressPrefix: '0.0.0.0/0'
          nextHopType: 'VirtualAppliance'
          nextHopIpAddress: firewall.properties.ipConfigurations[0].properties.privateIPAddress
        }
      }
    ]
  }
}

// Outputs
output vpnGatewayPublicIp string = vpnGwPublicIp.properties.ipAddress
output firewallPublicIp string = firewallPublicIp.properties.ipAddress
output firewallPrivateIp string = firewall.properties.ipConfigurations[0].properties.privateIPAddress
```

**Utilisation:**

```bash
# Valider le template
az bicep validate --file main.bicep

# Déployer
az deployment group create \
  --resource-group MyResourceGroup \
  --template-file main.bicep

# Voir les outputs
az deployment group show \
  --resource-group MyResourceGroup \
  --name main \
  --query 'properties.outputs'
```

---

## 9. 🔒 Sécurité & Bonnes Pratiques {#9-securite-bonnes-pratiques}

### 9.1 Authentification VPN

| Méthode | Sécurité | Complexité | Recommandation |
| --- | --- | --- | --- |
| **Pre-Shared Key (PSK)** | ❌ Faible | ✅ Simple | ❌ Non en production |
| **Certificats Self-Signed** | ⚠️ Moyen | ⚠️ Moyen | ⚠️ Petites orgs |
| **Certificats PKI** | ✅ Fort | ❌ Complexe | ✅ Enterprise |
| **Azure AD + MFA** | ✅✅ Très Fort | ❌ Très Complexe | ✅ Recommandé |

### 9.2 Chiffrement Firewall

```text
┌─────────────────────────────────────────┐
│  CHIFFREMENT APPLIQUÉ PAR FIREWALL      │
├─────────────────────────────────────────┤
│                                         │
│ Règles Réseau (L3-L4):                  │
│  → Pas d'inspection du contenu          │
│  → IP, Port uniquement                  │
│  → Pas de chiffrement ajouté            │
│                                         │
│ Règles Application (L7):                │
│  → Inspection HTTPS (SSL/TLS)           │
│  → Nécessite certificats Firewall       │
│  → Déchiffre/Inspecte/Rechiffre         │
│  → Peut aussi filtrer sur contenu URL   │
│                                         │
│ NOTE: Firewall ne crée PAS encryption   │
│       Il inspecte le traffic existant   │
└─────────────────────────────────────────┘
```

### 9.3 Checklist Sécurité VPN + Firewall

```text
✅ VPN SECURITY:
  □ Utiliser certificats, pas PSK
  □ Certificats avec expiration limitée
  □ Authentification multi-facteurs (MFA)
  □ IKEv2 au lieu de IKEv1
  □ PFS (Perfect Forward Secrecy) activé
  □ Logguer toutes connexions VPN
  □ Tester failover régulièrement
  □ Documenter les changements de topologie

✅ FIREWALL SECURITY:
  □ Threat Intelligence mode = DENY
  □ Défaut-deny policy (blquer tout, autoriser explicitement)
  □ Auditer règles mensuellement
  □ Logging activé → Log Analytics / SIEM
  □ Alertes sur tentatives de blocage
  □ Segmenter réseau (0-trust)
  □ Utiliser workspaces de logs
  □ Chiffrer les logs

✅ NETWORK SECURITY:
  □ NSG (Network Security Groups) en place
  □ NACLs (Network ACLs) sur subnets sensibles
  □ Private Endpoints pour services Azure
  □ Service Endpoints pour Storage/SQL
  □ Bastion Host pour accès administrateur
  □ Monitoring Network Watcher
  □ DDoS Protection Standard
  □ Audit trails via Azure Activity Log

✅ COMPLIANCE & GOVERNANCE:
  □ Respecter compliance requirements (ISO27001, etc.)
  □ Backup/DR plan en place
  □ Disaster recovery testée annuellement
  □ Rotation des certificats automatisée
  □ Access reviews trimestrielles
  □ Principle of least privilege
```

### 9.4 Segmentation Réseau (Zero Trust)

```text
AVANT (Perimeter Security):
┌──────────────────────────────────────┐
│  FIREWALL PERIMETER                  │
│                                      │
│  ┌────────────────────────────────┐  │
│  │ Tout en interne = Confiance ✅ │  │
│  │ • VMs                          │  │
│  │ • Databases                    │  │
│  │ • File servers                 │  │
│  └────────────────────────────────┘  │
└──────────────────────────────────────┘
         Internet (❌ = Danger)

PROBLÈME: Compromis d'une VM → Accès à tout!

APRÈS (Zero Trust Architecture):
┌──────────────────────────────────────┐
│  VNET avec SEGMENTATION              │
│                                      │
│  ┌──────────────────────────────┐    │
│  │ App Tier (NSG: app-nsg)      │    │
│  │ • Peut accéder DB seulement  │    │
│  │ • Authentification requise   │    │
│  │ • Audit logs chaque accès    │    │
│  └──────────────────────────────┘    │
│           ↓                          │
│  ┌────────────────────────────────┐  │
│  │ Data Tier (NSG: db-nsg)        │  │
│  │ • Reçoit connexions App seul   │  │
│  │ • Port 1433 (SQL)              │  │
│  │ • Authentification obligatoire │  │
│  └────────────────────────────────┘  │
│           ↓                          │
│  ┌──────────────────────────────┐    │
│  │ Admin Access                 │    │
│  │ • Bastion Host seulement     │    │
│  │ • MFA + Conditional Access   │    │
│  │ • Just-in-time (JIT) access  │    │
│  └──────────────────────────────┘    │
└──────────────────────────────────────┘

RÉSULTAT: Compromis d'une VM → Accès limité
```

---

## 10. 🔍 Diagnostic & Dépannage {#10-diagnostic-depannage}

### 10.1 Outils Azure Natifs

#### Network Watcher

```azure-cli
# Vérifier routage entre deux VMs
az network watcher show-next-hop \
  --resource-group MyRG \
  --vm MyVM \
  --dest-ip 10.0.2.10 \
  --nic MyVM-NIC

# Output:
# {
#   "nextHopIpAddress": "10.0.3.4",  <- IP du Firewall
#   "nextHopType": "VirtualAppliance",
#   "routeTableId": "/subscriptions/.../routeTables/AppSubnetRouteTable"
# }
```

#### Packet Capture

```azure-cli
# Capturer le trafic d'une VM
az network watcher packet-capture create \
  --resource-group MyRG \
  --vm MyVM \
  --name MyCapture \
  --storage-account mystorageaccount

# Exporter et analyser avec Wireshark
az network watcher packet-capture show-status \
  --resource-group MyRG \
  --name MyCapture
```

#### Connectivity Check

```azure-cli
# Tester si VM1 peut atteindre VM2:port
az network watcher test-connectivity \
  --resource-group MyRG \
  --source-resource MyVM1-NIC \
  --dest-resource-id /subscriptions/.../MyVM2-NIC \
  --dest-port 1433

# Output:
# {
#   "connectionStatus": "Reachable"  ou "Unreachable"
# }
```

### 10.2 Workflow de Dépannage VPN

```text
PROBLÈME: VPN Connection status = "Disconnected"

ÉTAPE 1: Vérifier les événements VPN Gateway
┌────────────────────────────────────────┐
│ az network vnet-gateway show \         │
│   --name MyVPNGateway \                │
│   --resource-group MyRG \              │
│   --query provisioningState            │
│                                        │
│ Expected: "Succeeded"                  │
│ If: "Failed" → Recréer le gateway      │
└────────────────────────────────────────┘

ÉTAPE 2: Vérifier la connexion VPN
┌────────────────────────────────────────┐
│ az network vpn-connection show \       │
│   --name MyDCtoAzureVPN \              │
│   --resource-group MyRG                │
│                                        │
│ Check:                                 │
│ • connectionStatus = Connected?        │
│ • sharedKey = correct?                 │
│ • tunnel stats (bytes transferred)?    │
└────────────────────────────────────────┘

ÉTAPE 3: Vérifier le device DC on-premise
┌────────────────────────────────────────┐
│ SSH into DC firewall/router            │
│ Check:                                 │
│ • IPSec status (online/down?)          │
│ • Log: connection attempts             │
│ • Config: Azure endpoint = correct IP? │
│ • Firewall rules: Allow port 500/4500? │
└────────────────────────────────────────┘

ÉTAPE 4: Vérifier les routes
┌────────────────────────────────────────┐
│ az network route-table route list \    │
│   --route-table-name AppRouteTable \   │
│   --resource-group MyRG                │
│                                        │
│ Check:                                 │
│ • 10.50.0.0/16 route exist?            │
│ • nextHopType = VpnGateway?            │
│ • Not overridden by other routes?      │
└────────────────────────────────────────┘

ÉTAPE 5: Test ping à travers VPN
┌────────────────────────────────────────┐
│ VM Azure (10.0.1.10) → ping DC (10.50) │
│                                        │
│ ✅ Success: VPN working                │
│ ❌ Timeout:                            │
│    • Check NSG rules                   │
│    • Check DC firewall rules           │
│    • Check ICMP allowed?               │
│    • Recreate VPN connection           │
└────────────────────────────────────────┘
```

### 10.3 Workflow de Dépannage Firewall

```text
PROBLÈME: VM ne peut pas atteindre Internet

ÉTAPE 1: Vérifier la route table
┌────────────────────────────────────────┐
│ az network vnet subnet show \          │
│   --vnet-name MyVNet \                 │
│   --name AppSubnet \                   │
│   --resource-group MyRG                │
│                                        │
│ Check: routeTable associée?            │
│ Si oui → next hop type = VirtualApp?   │
│ Si non → Ajouter route table           │
└────────────────────────────────────────┘

ÉTAPE 2: Vérifier l'état du Firewall
┌────────────────────────────────────────┐
│ az network firewall show \             │
│   --name MyAzureFirewall \             │
│   --resource-group MyRG                │
│                                        │
│ Check:                                 │
│ • provisioningState = "Succeeded"?     │
│ • threatIntelMode = "Deny"?            │
│ • IP configurations (public + private)?│
└────────────────────────────────────────┘

ÉTAPE 3: Vérifier les règles firewall
┌────────────────────────────────────────┐
│ az network firewall application-rule \ │
│   collection list \                    │
│   --firewall-name MyAzureFirewall \    │
│   --resource-group MyRG                │
│                                        │
│ Check:                                 │
│ • Règles appliquées à la source?       │
│ • Priorités (plus bas = plus tôt)?     │
│ • Action = Allow?                      │
│ • Target FQDNs incluent *.microsoft?   │
└────────────────────────────────────────┘

ÉTAPE 4: Vérifier les logs firewall
┌────────────────────────────────────────────┐
│ az monitor log-analytics query \           │
│   --workspace MyWorkspace \                │
│   --analytics-query "                      │
│   AzureDiagnostics                         │
│   | where ResourceType == 'AZUREFIREWALLS' │
│   | where msg_s contains 'Deny'            │
│   | project TimeGenerated, msg_s, ... "    │
│                                            │
│ Cela affiche tous les packets bloqués      │
│ Chercher pattern...                        │
└────────────────────────────────────────────┘

ÉTAPE 5: Ajouter une règle permet
┌────────────────────────────────────────┐
│ az network firewall application-rule \ │
│   create \                             │
│   --firewall-name MyAzureFirewall \    │
│   --collection-name AllowInternet \    │
│   --rule-name AllowHTTPS \             │
│   --source-addresses 10.0.1.0/24 \     │
│   --target-fqdns "*" \                 │
│   --protocols Https=443                │
│                                        │
│ ⚠️ Prudence: Trop permissif peut être  │
│    une faille de sécurité              │
└────────────────────────────────────────┘

ÉTAPE 6: Test final
┌────────────────────────────────────────┐
│ VM Azure:                              │
│ $ curl https://www.example.com         │
│                                        │
│ ✅ Success: Firewall autorisant        │
│ ❌ Still blocked: Revoir règles        │
└────────────────────────────────────────┘
```

---

## 11. 💪 Exercices Pratiques {#11-exercices-pratiques}

### EXERCICE 1: Configurer une VPN S2S Simple

**Objectif:** Connecter un VNet Azure à un réseau local simulé.

**Étapes:**

1. Créer un VNet (10.0.0.0/16) avec Gateway Subnet (10.0.0.0/27)
2. Créer une VPN Gateway (SKU: Standard)
3. Créer un Local Network Gateway (simule DC on-premise)
4. Établir une connexion S2S VPN
5. Configurer la route table
6. Tester avec ping (VM Azure vers réseau local)

**Durée estimée:** 20-30 minutes

---

### EXERCICE 2: Sécuriser le Trafic avec Azure Firewall

**Objectif:** Permettre à une VM Azure d'accéder à Windows Update uniquement via Firewall.

**Étapes:**

1. Créer un subnet AzureFirewallSubnet
2. Déployer Azure Firewall (SKU: Standard)
3. Créer une règle Application pour autoriser *.microsoft.com uniquement
4. Route table → direction par défaut vers Firewall
5. VM teste: `curl https://www.google.com` (blocké) ❌
6. VM teste: `curl https://www.microsoft.com` (autorisé) ✅

**Durée estimée:** 30-40 minutes

---

### EXERCICE 3: Configuration Multi-Région avec Firewall Centralisé

**Objectif:** Deux VNets en régions différentes, protégés par un Firewall central.

**Étapes:**

1. VNet 1 (West EU): 10.0.0.0/16 + Firewall
2. VNet 2 (East EU): 10.10.0.0/16 + Firewall
3. VNet Peering entre les deux VNets
4. Route tables chaque région → Firewall central
5. Règles Firewall synchro entre les deux instances
6. Tester: VM VNet1 → VM VNet2 (traverse Firewall)

**Durée estimée:** 45-60 minutes

---

### EXERCICE 4: Configurer P2S VPN pour Télétravail

**Objectif:** Créer une connexion P2S pour qu'un client distant accède au VNet.

**Étapes:**

1. Générer Root CA et Client certificats (PowerShell)
2. Configurer VPN Gateway P2S (SSTP + IKEv2)
3. Charger Root CA dans le gateway
4. Exporter VPN client config
5. Client télécharge et installe le profil VPN
6. Client se connecte et reçoit IP 172.16.0.x
7. Client ping une VM Azure (10.0.1.10) ✅

**Durée estimée:** 25-35 minutes

---

### EXERCICE 5: Déployer Infra Complète via Infrastructure as Code

**Objectif:** Utiliser Terraform ou Bicep pour déployer l'entière architecture VPN + Firewall en une commande.

**Étapes:**

1. Télécharger le template Terraform ou Bicep fourni
2. Modifier les variables (location, CIDR, etc.)
3. `terraform plan` ou `bicep build` + `az deployment group create`
4. Attendre le déploiement (~10-15 min)
5. Vérifier outputs: IPs publiques, infos gateway
6. Tester la connectivité entre composants

**Durée estimée:** 20-30 minutes

---

## 12. 📚 Ressources & Références {#12-ressources-references}

### Documentation Officielle Azure

- **Azure VPN Gateway Documentation:**
[https://docs.microsoft.com/en-us/azure/vpn-gateway/](https://docs.microsoft.com/en-us/azure/vpn-gateway/)

- **Azure Firewall Documentation:**
 [https://docs.microsoft.com/en-us/azure/firewall/](https://docs.microsoft.com/en-us/azure/firewall/)
- **Network Security Groups:**
[https://docs.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview](https://docs.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)
- **Azure Network Watcher:**
[https://docs.microsoft.com/en-us/azure/network-watcher/](https://docs.microsoft.com/en-us/azure/network-watcher/)

### Certification & Learning Paths

- **AZ-104 (Azure Administrator):** Couvre VPN + Firewall
- **AZ-500 (Azure Security Engineer):** Approfondit la sécurité réseau
- **AZ-700 (Azure Network Engineer Associate):** Spécialisation réseaux

### Outils Pratiques

| Tool | Usage |
| --- | --- |
| **Azure Portal** | Configuration GUI |
| **Azure CLI** | Scripting et automation |
| **Terraform** | IaC pour multi-cloud |
| **Bicep** | IaC spécifique Azure |
| **Azure Monitor + Log Analytics** | Logs et monitoring |
| **Network Watcher** | Diagnostic réseau |
| **Wireshark** | Packet analysis |
| **CloudTrail (AWS) / Activity Log (Azure)** | Audit trail |

### Comparaisons & Case Studies

- **AWS vs Azure Networking:**
 [https://docs.microsoft.com/en-us/azure/architecture/aws-professional/](https://docs.microsoft.com/en-us/azure/architecture/aws-professional/)
- **Azure Architecture Center:**
[https://docs.microsoft.com/en-us/azure/architecture/](https://docs.microsoft.com/en-us/azure/architecture/)
- **Microsoft Learn Modules:**
[https://learn.microsoft.com/en-us/training/](https://learn.microsoft.com/en-us/training/)

---

## 🎓 Conclusion

Vous avez maintenant une **compréhension complète d'Azure VPN Gateway et Azure Firewall**, du débutant à l'expert :

✅ **Concepts fondamentaux:** VPN types, Firewall layers, chiffrement
✅ **Architectures pratiques:** Hybride cloud, télétravail, egress filtering
✅ **Configuration hands-on:** S2S, P2S, règles Firewall
✅ **Infrastructure as Code:** Terraform + Bicep
✅ **Sécurité & compliance:** Bonnes pratiques, zero-trust
✅ **Diagnostic:** Outils et workflows de dépannage
✅ **Exercices pratiques:** 5 labs pour consolider les apprentissages

### Prochaines Étapes

1. **Pratiquez** les 5 exercices dans un laboratoire Azure (Free Trial possible)
2. **Déployez** votre propre architecture hybride
3. **Passez** une certification Azure (AZ-104 ou AZ-500)
4. **Explorez** des solutions avancées: ExpressRoute, Azure Firewall Manager, Sentinel
5. **Contribuez** à la communauté: blogs, forums, open-source
