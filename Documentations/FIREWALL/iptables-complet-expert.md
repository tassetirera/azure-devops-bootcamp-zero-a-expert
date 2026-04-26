# 🔥 iptables — Cours Complet: Du Débutant à l'Expert

**Objectif du cours :** Maîtriser complètement iptables, le pare-feu Linux par défaut, pour configurer, administrer et sécuriser vos systèmes Linux avec une précision chirurgicale. De la théorie aux cas d'usage production.

---

## 📋 Sommaire

1. [Concepts Fondamentaux](#1-concepts-fondamentaux)
2. [Architecture d'iptables](#2-architecture-diptables)
3. [Tables](#3-tables)
4. [Chains (Chaînes)](#4-chains-chaînes)
5. [Rules (Règles)](#5-rules-règles)
6. [Syntaxe Complète d'iptables](#6-syntaxe-complète-diptables)
7. [Filtre (Filter Table) — Le Cœur](#7-filtre-filter-table--le-cœur)
8. [NAT (Network Address Translation)](#8-nat-network-address-translation)
9. [Mangle (Modification de Paquets)](#9-mangle-modification-de-paquets)
10. [Raw & Security](#10-raw--security)
11. [Stateful vs Stateless](#11-stateful-vs-stateless)
12. [Cas d'Usage Réels](#12-cas-dusage-réels)
13. [Configuration Persistante](#13-configuration-persistante)
14. [Debugging & Logs](#14-debugging--logs)
15. [Firewalld (Modern Wrapper)](#15-firewalld-modern-wrapper)
16. [Migration vers nftables](#16-migration-vers-nftables)
17. [Performance & Optimisation](#17-performance--optimisation)
18. [Bonnes Pratiques & Sécurité](#18-bonnes-pratiques--sécurité)
19. [Exercices Pratiques](#19-exercices-pratiques)
20. [Ressources & Références](#20-ressources--références)

---

## 1. 🎓 Concepts Fondamentaux {#1-concepts-fondamentaux}

### 1.1 Qu'est-ce qu'iptables?

**iptables** est un utilitaire Linux (user-space) qui permet de configurer les règles de filtrage des paquets réseau via le module kernel **netfilter**.

#### Le Modèle Client-Serveur

```text
┌─────────────────────────────────────────┐
│  User Space (iptables command)          │
│  • Commandes administrateur             │
│  • Interface de configuration           │
└────────────────┬────────────────────────┘
                 │ (ioctls / sockets)
                 ↓
┌─────────────────────────────────────────┐
│  Kernel (netfilter)                     │
│  • Traitement réel des paquets          │
│  • Inspection & Filtrage                │
│  • Stateful Inspection                  │
│  • NAT & Mangling                       │
└─────────────────────────────────────────┘
                 ↓
         Paquets réseau
```

### 1.2 Flux d'un Paquet à Travers iptables

```text
┌─────────────────────────────────────────┐
│         PAQUET ENTRANT (INPUT)          │
│         Depuis Internet                 │
└────────────┬────────────────────────────┘
             ↓
     ┌───────────────────┐
     │ Interface réseau  │
     │ (eth0, wlan0)     │
     └────────┬──────────┘
              ↓
     ┌───────────────────────────────────────┐
     │  NETFILTER HOOK: NF_IP_PRE_ROUTING    │
     │  • mangle table                       │
     │  • nat table (DNAT)                   │
     └──────────┬────────────────────────────┘
                ↓
     ┌──────────────────────────────────────────┐
     │  Routing Decision                        │
     │  Cible locale? → INPUT                   │
     │  Cible distante? → FORWARD               │
      └──────────┬───────────────────────────────┘
                ↓
    ╔═════════════════════════════════════╗
    ║  LOCAL DESTINATION?                 ║
    ║  ↙                    ↘             ║
    ║ OUI                   NON           ║
    ╚═════════════════════════════════════╝
     ↓                        ↓
┌────────────────┐    ┌──────────────────┐
│ INPUT CHAIN    │    │ FORWARD CHAIN    │
│                │    │                  │
│ mangle table   │    │ mangle table     │
│ filter table   │    │ filter table     │
│ security table │    │ security table   │
└────────┬───────┘    └────────┬─────────┘
         ↓                      ↓
    ┌────────────┐        ┌──────────────┐
    │ Application│        │ Post Routing │
    │ (port 80)  │        │ (SNAT)       │
    └─────┬──────┘        └─────┬────────┘
          ↓                      ↓
     OUTPUT CHAIN         ┌────────────┐
     • mangle table       │ Interface  │
     • nat table (SNAT)   │ de sortie  │
     • filter table       └────────────┘
     • security table
```

### 1.3 Les 5 Concepts Clés

```text
┌────────────────────────────────────────────────┐
│          5 CONCEPTS CLÉS D'IPTABLES            │
├────────────────────────────────────────────────┤
│                                                │
│ 1. TABLES (Tableaux)                           │
│    • filter: Filtrage (allow/drop)             │
│    • nat: Network Address Translation          │
│    • mangle: Modification de paquets           │
│    • raw: Bypass conntrack                     │
│    • security: Étiquetage SELinux              │
│                                                │
│ 2. CHAINS (Chaînes)                            │
│    • INPUT: Paquets entrants                   │
│    • OUTPUT: Paquets sortants                  │
│    • FORWARD: Paquets routés                   │
│    • PREROUTING: Avant routing decision        │
│    • POSTROUTING: Après routing decision       │
│                                                │
│ 3. RULES (Règles)                              │
│    • Condition (IP source, port, proto, etc.)  │
│    • Action (ACCEPT, DROP, REJECT, etc.)       │
│    • Priority (ordre d'exécution)              │
│                                                │
│ 4. POLICY (Politique par défaut)               │
│    • Qu'advient-il si aucune règle ne match?   │
│    • ACCEPT (autoriser par défaut)             │
│    • DROP (bloquer par défaut)                 │
│    • REJECT (rejeter avec notification)        │
│                                                │
│ 5. CONNECTION TRACKING (Tracking d'état)       │
│    • Suivre l'état des connexions              │
│    • NEW, ESTABLISHED, RELATED, INVALID        │
│    • Permet "stateful filtering"               │
│                                                │
└────────────────────────────────────────────────┘
```

---

## 2. 🏗️ Architecture d'iptables {#2-architecture-diptables}

### 2.1 Modèle OSI & iptables

```text
┌───────────────────────────────────────────────────────────┐
│                   MODÈLE OSI                              │
├───────────────────────────────────────────────────────────┤
│                                                           │
│ L7 Application    (HTTP, FTP, DNS)  ← iptables (limité)   │
│ L6 Présentation                                           │
│ L5 Session        (TCP sessions)                          │
│ L4 Transport      (TCP, UDP)        ← iptables (oui)      │
│ L3 Réseau         (IP, ICMP)        ← iptables (oui)      │
│ L2 Lien de données (MAC, Ethernet)  ← iptables (non)      │
│ L1 Physique       (Fils, radios)                          │
│                                                           │
│ NOTE: iptables = L3-L4 (pas L7)                           │
│       Pour L7 = nDPI, nfstream, DPI firewalls             │
│                                                           │
└───────────────────────────────────────────────────────────┘
```

### 2.2 Structure Hiérarchique

```text
TABLE (5 types)
  ├─ CHAIN (5 points d'entrée)
  │   ├─ RULE 1 (priorité 100)
  │   │   ├─ Condition
  │   │   └─ Action
  │   ├─ RULE 2 (priorité 200)
  │   │   ├─ Condition
  │   │   └─ Action
  │   └─ RULE 3 (priorité 300)
  │       ├─ Condition
  │       └─ Action
  │
  ├─ DEFAULT POLICY (ACCEPT/DROP/REJECT)
  │   └─ Utilisé si aucune règle ne match
  │
  └─ USER-DEFINED CHAINS (chaînes perso)
      └─ Peuvent être appelées depuis d'autres chaînes
```

### 2.3 Flux de Décision

```text
PAQUET ARRIVE
       ↓
┌──────────────────────┐
│ Match Rule 1?        │
│ ├─ Condition OK?     │
│ └─ Action: DROP      │
└──────────────────────┘
       │
       ├─ OUI: STOP. Paquet supprimé.
       │
       ├─ NON: Continuer...
       ↓
┌──────────────────────┐
│ Match Rule 2?        │
│ ├─ Condition OK?     │
│ └─ Action: ACCEPT    │
└──────────────────────┘
       │
       ├─ OUI: STOP. Paquet accepté.
       │
       ├─ NON: Continuer...
       ↓
       ... (Autres règles)
       ↓
┌──────────────────────┐
│ Aucune règle match?  │
│ Appliquer POLICY     │
│ par défaut           │
└──────────────────────┘
       ↓
   ACCEPT/DROP/REJECT
```

---

## 3. 📦 Tables {#3-tables}

### 3.1 Les 5 Tables

#### 1. FILTER Table (Principale)

```text
┌───────────────────────────────────────────────────────────┐
│              FILTER TABLE (Défaut)                        │
├───────────────────────────────────────────────────────────┤
│                                                           │
│ Objectif: Filtrage standard allow/drop                    │
│                                                           │
│ Chains:                                                   │
│ • INPUT: Trafic entrant vers la machine                   │
│ • OUTPUT: Trafic sortant de la machine                    │
│ • FORWARD: Trafic routé via la machine                    │
│                                                           │
│ Cas d'usage: 90% des règles sont ici                      │
│                                                           │
│ Exemple:                                                  │
│   iptables -t filter -A INPUT -p tcp --dport 22 -j ACCEPT │
│   (Autoriser SSH entrant)                                 │
│                                                           │
└───────────────────────────────────────────────────────────┘
```

#### 2. NAT Table (Network Address Translation)

```text
┌────────────────────────────────────────────────────────┐
│              NAT TABLE                                 │
├────────────────────────────────────────────────────────┤
│                                                        │
│ Objectif: Traduire adresses IP (masquerade)            │
│                                                        │
│ Chains:                                                │
│ • PREROUTING: Avant routing (DNAT)                     │
│   └─ Changer IP destination d'un paquet                │
│                                                        │
│ • POSTROUTING: Après routing (SNAT)                    │
│   └─ Changer IP source d'un paquet                     │
│                                                        │
│ • OUTPUT: Paquets générés localement                   │
│                                                        │
│ Cas d'usage:                                           │
│ • Port Forwarding (external:80 → internal:8080)        │
│ • Masquerade (LAN privé → Internet public)             │
│ • Load Balancing basique                               │
│                                                        │
│ Exemple:                                               │
│   iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE │
│   (Masquerade: LAN → Internet via eth0)                │
│                                                        │
└────────────────────────────────────────────────────────┘
```

#### 3. MANGLE Table (Modification)

```text
┌─────────────────────────────────────────────────────────┐
│              MANGLE TABLE                               │
├─────────────────────────────────────────────────────────┤
│                                                         │
│ Objectif: Modifier les paquets (champs header)          │
│                                                         │
│ Chains: PREROUTING, INPUT, OUTPUT, POSTROUTING          │
│                                                         │
│ Cas d'usage:                                            │
│ • TTL manipulation (Time To Live)                       │
│ • TOS/DSCP marking (Qualité de Service)                 │
│ • MSS clamping (Maximum Segment Size)                   │
│ • Mark packets (firewall marking)                       │
│                                                         │
│ Exemple:                                                │
│   iptables -t mangle -A POSTROUTING -p tcp --dport 80 \ │
│     -j MARK --set-mark 1                                │
│   (Marquer les paquets HTTP)                            │
│                                                         │
│ ⚠️ Avancé! Utilisé rarement en production               │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

#### 4. RAW Table (Bypass)

```text
┌─────────────────────────────────────────────────────┐
│              RAW TABLE                              │
├─────────────────────────────────────────────────────┤
│                                                     │
│ Objectif: Bypass le connection tracking             │
│                                                     │
│ Chains: PREROUTING, OUTPUT                          │
│                                                     │
│ Cas d'usage:                                        │
│ • Désactiver tracking pour certains paquets         │
│ • Améliorer performance (skip conntrack overhead)   │
│ • Ignorer les connexions invalides                  │
│                                                     │
│ Exemple:                                            │
│   iptables -t raw -A PREROUTING -p tcp --dport 25 \ │
│     -j NOTRACK                                      │
│   (Ne pas tracker SMTP)                             │
│                                                     │
│ ⚠️ Très avancé! Rarement utilisé                    │
│                                                     │
└─────────────────────────────────────────────────────┘
```

#### 5. SECURITY Table (SELinux)

```text
┌────────────────────────────────────────────────┐
│              SECURITY TABLE                    │
├────────────────────────────────────────────────┤
│                                                │
│ Objectif: Étiquetage pour SELinux              │
│                                                │
│ Chains: INPUT, OUTPUT, FORWARD                 │
│                                                │
│ Cas d'usage:                                   │
│ • Intégration avec SELinux                     │
│ • Étiquetage de contexte de sécurité           │
│                                                │
│ ⚠️ Spécialisé! Rarement utilisé hors SELinux  │
│                                                │
└────────────────────────────────────────────────┘
```

### 3.2 Ordre de Traitement des Tables

```text
INCOMING PACKET
       ↓
   ┌───────────────┐
   │ RAW Table     │ ← Point d'arrêt (NOTRACK)
   │ PREROUTING    │
   └───────┬───────┘
           ↓
   ┌───────────────┐
   │ MANGLE Table  │ ← Modification de champs
   │ PREROUTING    │
   └───────┬───────┘
           ↓
   ┌───────────────┐
   │ NAT Table     │ ← DNAT (destination change)
   │ PREROUTING    │
   └───────┬───────┘
           ↓
   [ROUTING DECISION]
   ↙              ↘
LOCAL            FORWARD
   ↓              ↓
┌──────────────────────────────────────────┐
│ INPUT CHAIN                              │
│ • Mangle INPUT                           │
│ • Filter INPUT                           │
│ • Security INPUT                         │
└──────────────────────────────────────────┘
   ↓
[LOCAL APPLICATION]
   ↓
┌──────────────────────────────────────────┐
│ OUTPUT CHAIN                             │
│ • RAW OUTPUT (NOTRACK)                   │
│ • Mangle OUTPUT                          │
│ • NAT OUTPUT                             │
│ • Filter OUTPUT                          │
│ • Security OUTPUT                        │
└──────────────────────────────────────────┘
   ↓
   ... (FORWARD chain if routing)
   ↓
   [OUTGOING]
```

### 3.3 Ordre des Tables pour PREROUTING

```text
PREROUTING (inbound):
1. RAW table (NOTRACK)
2. MANGLE table
3. NAT table (DNAT)

POSTROUTING (outbound):
1. MANGLE table
2. NAT table (SNAT)
```

---

## 4. ⛓️ Chains (Chaînes) {#4-chains-chaînes}

### 4.1 Les 5 Built-in Chains

#### INPUT Chain

```text
┌──────────────────────────────────────────┐
│        INPUT CHAIN                       │
├──────────────────────────────────────────┤
│                                          │
│ Traite: Paquets destinés à la machine   │
│                                          │
│ ↓ Paquet arrive ↓                        │
│ IP destination = Local?                  │
│ └─ OUI → INPUT CHAIN                     │
│                                          │
│ Tables utilisables:                      │
│ • Mangle (modification)                  │
│ • Filter (allow/deny)                    │
│ • Security (SELinux)                     │
│                                          │
│ Exemple:                                 │
│ Quelqu'un envoie SSH au serveur          │
│ → 22.tcp.inbound → INPUT CHAIN           │
│                                          │
│ Cas d'usage:                             │
│ • Autoriser/bloquer services locaux      │
│ • Filtrer accès SSH, HTTP, etc.          │
│ • Défense contre attaques réseaux        │
│                                          │
└──────────────────────────────────────────┘
```

#### OUTPUT Chain

```text
┌──────────────────────────────────────────┐
│        OUTPUT CHAIN                      │
├──────────────────────────────────────────┤
│                                          │
│ Traite: Paquets générés localement      │
│                                          │
│ ↓ Application crée paquet ↓              │
│ Avant envoi → OUTPUT CHAIN               │
│                                          │
│ Tables utilisables:                      │
│ • Raw (bypass tracking)                  │
│ • Mangle (modification)                  │
│ • NAT (SNAT - changer IP source)        │
│ • Filter (allow/deny)                    │
│ • Security (SELinux)                     │
│                                          │
│ Exemple:                                 │
│ Serveur envoie réponse HTTP              │
│ → Paquet TCP:port80 → OUTPUT CHAIN       │
│                                          │
│ Cas d'usage:                             │
│ • Limiter trafic sortant (DLP)           │
│ • Bloquer malwares qui se connectent     │
│ • NAT pour multilingue                   │
│                                          │
└──────────────────────────────────────────┘
```

#### FORWARD Chain

```text
┌──────────────────────────────────────────┐
│        FORWARD CHAIN                     │
├──────────────────────────────────────────┤
│                                          │
│ Traite: Paquets routés via la machine  │
│                                          │
│ ↓ Paquet arrive ↓                        │
│ IP destination ≠ Local?                  │
│ Forwarder vers autre interface?          │
│ └─ OUI → FORWARD CHAIN                   │
│                                          │
│ Tables utilisables:                      │
│ • Mangle (modification)                  │
│ • Filter (allow/deny)                    │
│ • Security (SELinux)                     │
│                                          │
│ Prérequis:                               │
│ • ip_forward=1 dans kernel               │
│ • Machine agit comme routeur             │
│                                          │
│ Exemple:                                 │
│ LAN 192.168.1.0/24 → Internet via router │
│ → FORWARD CHAIN (paquet transité)        │
│                                          │
│ Cas d'usage:                             │
│ • Routeur pare-feu                       │
│ • Firewall appliance                     │
│ • Contrôle LAN→Internet                  │
│ • Load balancer                          │
│                                          │
└──────────────────────────────────────────┘
```

#### PREROUTING Chain

```text
┌──────────────────────────────────────────┐
│        PREROUTING CHAIN                  │
├──────────────────────────────────────────┤
│                                          │
│ Traite: Tous les paquets (avant routing) │
│                                          │
│ ↓ Paquet arrive du réseau ↓              │
│ Avant décision de routage                │
│ → PREROUTING CHAIN                       │
│                                          │
│ Tables utilisables:                      │
│ • Raw (bypass tracking)                  │
│ • Mangle (modification)                  │
│ • NAT (DNAT - changer IP destination)   │
│                                          │
│ Ordre d'exécution:                       │
│ 1. RAW table                             │
│ 2. MANGLE table                          │
│ 3. NAT table                             │
│                                          │
│ Exemple (Port Forwarding):               │
│ ext:8080 → int:80                        │
│ DNAT in PREROUTING                       │
│                                          │
│ Cas d'usage:                             │
│ • DNAT (port forwarding)                 │
│ • Redirection de ports                   │
│ • Load balancing inbound                 │
│ • Service discovery                      │
│                                          │
└──────────────────────────────────────────┘
```

#### POSTROUTING Chain

```text
┌──────────────────────────────────────────┐
│        POSTROUTING CHAIN                 │
├──────────────────────────────────────────┤
│                                          │
│ Traite: Tous les paquets sortants       │
│                                          │
│ ↓ Paquet prêt à partir ↓                 │
│ Après routage, avant envoi               │
│ → POSTROUTING CHAIN                      │
│                                          │
│ Tables utilisables:                      │
│ • Mangle (modification)                  │
│ • NAT (SNAT - changer IP source)        │
│                                          │
│ Exemple (Masquerade):                    │
│ LAN 192.168.1.x → Internet               │
│ Source: 192.168.1.100 → Firewall IP     │
│ SNAT in POSTROUTING                      │
│                                          │
│ Cas d'usage:                             │
│ • Masquerade (NAT sortant)               │
│ • Partage Internet                       │
│ • Anonymiser sources internes            │
│ • Load balancing outbound                │
│                                          │
└──────────────────────────────────────────┘
```

### 4.2 Custom (User-Defined) Chains

```text
Vous pouvez créer vos propres chaînes:

iptables -N my_custom_chain
  └─ Crée une chaîne personnalisée

Puis les appeler depuis une chaîne existante:

iptables -A INPUT -p tcp --dport 80 -j my_custom_chain
  └─ Si port 80, envoyer à ma chaîne perso

AVANTAGE: Organisation modulaire
  • Grouper des règles logiquement
  • Réutilisabilité
  • Maintenance simplifiée
  • Performance (branchement)

EXEMPLE: Chaîne pour "Acceptable IPs"

iptables -N Acceptable_IPs
iptables -A Acceptable_IPs -s 192.168.1.0/24 -j ACCEPT
iptables -A Acceptable_IPs -s 10.0.0.0/8 -j ACCEPT
iptables -A Acceptable_IPs -j DROP

iptables -A INPUT -p tcp --dport 22 -j Acceptable_IPs
  └─ SSH seulement desde IPs acceptables
```

### 4.3 Policy vs Rules

```text
┌────────────────────────────────────────────┐
│  POLICY vs RULES                           │
├────────────────────────────────────────────┤
│                                            │
│ POLICY (Politique par défaut):             │
│ iptables -P INPUT DROP                     │
│   └─ Si AUCUNE règle ne match → DROP       │
│                                            │
│ RULES (Règles spécifiques):                │
│ iptables -A INPUT -p tcp --dport 22        │
│   -j ACCEPT                                │
│   └─ Si port 22 TCP → ACCEPT               │
│                                            │
│ ORDRE D'EXÉCUTION:                         │
│ 1. Vérifier TOUTES les règles              │
│ 2. Si aucune ne correspond → Policy        │
│                                            │
│ STRATÉGIE RECOMMEND:                       │
│ Policy: DROP (Deny-All par défaut)         │
│ Rules: Autoriser explicitement             │
│ = "Whitelist" approach (plus sûr)         │
│                                            │
│ ALTERNATIVE UNSAFE:                        │
│ Policy: ACCEPT (Allow-All par défaut)      │
│ Rules: Bloquer les mauvaises choses        │
│ = "Blacklist" approach (moins sûr)        │
│                                            │
└────────────────────────────────────────────┘
```

---

## 5. 📝 Rules (Règles) {#5-rules-règles}

### 5.1 Anatomy d'une Règle

```text
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
 │       │ │   │  │  │   │     │  │ │
 │       │ │   │  │  │   │     │  │ └─ ACTION (ACCEPT, DROP, REJECT)
 │       │ │   │  │  │   │     │  └─ TARGET (-j)
 │       │ │   │  │  │   │     └─ PORT DESTINATION (80 = HTTP)
 │       │ │   │  │  │   └─ FLAG DE PORT (--dport)
 │       │ │   │  │  └─ PROTOCOLE (tcp, udp, icmp)
 │       │ │   │  └─ FLAG PROTOCOLE (-p)
 │       │ │   └─ CONDITION
 │       │ └─ CHAÎNE (INPUT, OUTPUT, FORWARD)
 │       └─ OPÉRATION (A=append, I=insert, D=delete)
 └─ UTILITAIRE

RÉSULTAT: Autoriser TCP port 80 entrant
```

### 5.2 Conditions (Matches)

```text
┌────────────────────────────────────────────────────────┐
│           CONDITIONS (Critères de Filtrage)           │
├────────────────────────────────────────────────────────┤
│                                                        │
│ -p, --protocol <proto>                                 │
│   tcp, udp, icmp, all                                  │
│   iptables -A INPUT -p tcp                             │
│                                                        │
│ -s, --source <addr>                                    │
│   Single: 192.168.1.1                                  │
│   CIDR: 192.168.1.0/24                                 │
│   Range: 192.168.1.0-192.168.1.255                     │
│   iptables -A INPUT -s 192.168.1.0/24                  │
│                                                        │
│ -d, --destination <addr>                               │
│   Même syntax que -s                                   │
│   iptables -A INPUT -d 10.0.0.5                        │
│                                                        │
│ -i, --in-interface <iface>                             │
│   Interface entrante (INPUT, FORWARD, PREROUTING)     │
│   eth0, wlan0, ppp0                                    │
│   ! eth0 (négation = tout sauf eth0)                   │
│   iptables -A INPUT -i eth0                            │
│                                                        │
│ -o, --out-interface <iface>                            │
│   Interface sortante (OUTPUT, FORWARD, POSTROUTING)   │
│   Même syntax que -i                                   │
│   iptables -A OUTPUT -o eth1                           │
│                                                        │
│ --sport <port>                                         │
│   Port source (TCP/UDP)                                │
│   Single: --sport 22                                   │
│   Range: --sport 1024:65535                            │
│   List: --sport 22,80,443 (pas de space!)             │
│   iptables -A INPUT -p tcp --sport 1024:65535          │
│                                                        │
│ --dport <port>                                         │
│   Port destination (TCP/UDP)                           │
│   Même syntax que --sport                             │
│   iptables -A INPUT -p tcp --dport 80                  │
│                                                        │
│ --syn                                                   │
│   TCP SYN flag (initiation de connexion)               │
│   iptables -A INPUT -p tcp --syn -j DROP               │
│   (Bloquer SYN floods)                                 │
│                                                        │
│ -m state --state <state>                               │
│   NEW: Nouvelle connexion                              │
│   ESTABLISHED: Connexion existante                     │
│   RELATED: Connexion liée (ex: FTP)                    │
│   INVALID: Paquet invalide                             │
│   iptables -A INPUT -m state --state ESTABLISHED -j ACCEPT
│                                                        │
│ -m conntrack --ctstate <state>                         │
│   Moderne alias de state                               │
│   Même états que state                                 │
│   iptables -A INPUT -m conntrack --ctstate ESTABLISHED │
│                                                        │
└────────────────────────────────────────────────────────┘
```

### 5.3 Actions (Targets)

```text
┌────────────────────────────────────────────────────────┐
│            ACTIONS (Targets)                           │
├────────────────────────────────────────────────────────┤
│                                                        │
│ ACCEPT                                                 │
│   Autoriser le paquet                                 │
│   Continu normalement le traitement                   │
│   iptables -A INPUT -p tcp --dport 22 -j ACCEPT       │
│                                                        │
│ DROP                                                   │
│   Supprimer silencieusement le paquet                 │
│   Pas de notification à l'expéditeur                  │
│   Sortir de la chaîne                                 │
│   iptables -A INPUT -p tcp --dport 25 -j DROP         │
│                                                        │
│ REJECT                                                 │
│   Refuser + envoyer notification (ICMP)               │
│   L'expéditeur sait que c'est bloqué                  │
│   Types: ICMP host-unreachable (défaut)              │
│   iptables -A INPUT -j REJECT --reject-with icmp-host-unreachable
│                                                        │
│ RETURN                                                 │
│   Revenir à la chaîne parentale                       │
│   Utilisé dans les custom chains                      │
│   iptables -A mychain -p tcp --dport 666 -j RETURN    │
│                                                        │
│ <chainname>                                            │
│   Sauter à une autre chaîne                           │
│   iptables -A INPUT -p tcp --dport 22 -j SSH_Rules    │
│                                                        │
│ MARK                                                   │
│   Marquer le paquet (mangle table)                    │
│   Pour routage ultérieur/classification               │
│   iptables -t mangle -A INPUT -j MARK --set-mark 10   │
│                                                        │
│ LOG                                                    │
│   Logger le paquet (puis continuer!)                 │
│   Très utile pour debug                               │
│   iptables -A INPUT -p tcp --dport 666 -j LOG \       │
│     --log-prefix "BLOCKED_SSH_SCAN: "                 │
│                                                        │
│ SNAT / MASQUERADE (NAT table)                          │
│   Source NAT - changer IP source                      │
│   MASQUERADE = SNAT auto (interface IP change)        │
│   iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
│                                                        │
│ DNAT (NAT table)                                       │
│   Destination NAT - changer IP destination            │
│   Port forwarding!                                    │
│   iptables -t nat -A PREROUTING -d 203.0.113.10 \    │
│     -p tcp --dport 8080 \                             │
│     -j DNAT --to-destination 192.168.1.100:80         │
│                                                        │
│ NOTRACK (RAW table)                                    │
│   Bypass connection tracking                          │
│   Pour performance                                    │
│   iptables -t raw -A PREROUTING -p tcp --dport 25 \  │
│     -j NOTRACK                                        │
│                                                        │
└────────────────────────────────────────────────────────┘
```

### 5.4 Négation (!)

```text
! (NOT operator)

-i ! eth0
  └─ Tout SAUF eth0

! -s 192.168.1.0/24
  └─ Toutes sources SAUF 192.168.1.0/24

-p ! tcp
  └─ Tous protocoles SAUF TCP

--dport ! 22
  └─ Tous ports SAUF 22

EXEMPLE COMPLET:
iptables -A INPUT -i ! lo -p tcp --dport 22 \
  -s ! 192.168.1.0/24 -j DROP

Traduction:
"Bloquer SSH entrant sur toutes interfaces
sauf loopback, depuis toutes les IPs
sauf 192.168.1.0/24"
```

---

## 6. 💻 Syntaxe Complète d'iptables {#6-syntaxe-complète-diptables}

### 6.1 Opérations Principales

```text
┌────────────────────────────────────────────────────────┐
│         OPÉRATIONS DE GESTION                         │
├────────────────────────────────────────────────────────┤
│                                                        │
│ CRÉER / MANIPULER RÈGLES:                             │
│                                                        │
│ iptables -A <chain> <condition> -j <target>           │
│   Append (ajouter à la fin)                           │
│   iptables -A INPUT -p tcp --dport 80 -j ACCEPT       │
│                                                        │
│ iptables -I <chain> [num] <condition> -j <target>     │
│   Insert (insérer à la position, défaut=1)            │
│   iptables -I INPUT 1 -p tcp --dport 22 -j ACCEPT     │
│   (Ajoute en position 1 = priorité!)                 │
│                                                        │
│ iptables -D <chain> <num|condition>                    │
│   Delete (supprimer)                                  │
│   Par numéro: iptables -D INPUT 1                    │
│   Par condition: iptables -D INPUT -p tcp --dport 80 -j ACCEPT
│                                                        │
│ iptables -R <chain> <num> <condition> -j <target>     │
│   Replace (remplacer)                                │
│   iptables -R INPUT 1 -p tcp --dport 443 -j ACCEPT    │
│                                                        │
│ iptables -F [chain]                                   │
│   Flush (vider toutes les règles)                     │
│   iptables -F INPUT (vider INPUT)                     │
│   iptables -F (vider TOUTES les chaînes)              │
│                                                        │
│ iptables -L [chain] [-n] [-v]                         │
│   List (afficher les règles)                          │
│   -n: Afficher IP (pas hostname)                      │
│   -v: Verbeux (détails supplémentaires)               │
│   iptables -L INPUT -n -v                             │
│                                                        │
│ iptables -L [chain] --line-numbers                    │
│   List avec numéros de ligne                          │
│   Utile pour savoir quoi supprimer                    │
│   iptables -L INPUT --line-numbers                    │
│                                                        │
│ iptables -P <chain> <policy>                          │
│   Set policy (politique par défaut)                   │
│   iptables -P INPUT DROP                              │
│   (Bloquer tout par défaut)                           │
│                                                        │
│ iptables -N <chain>                                   │
│   New chain (créer chaîne perso)                      │
│   iptables -N my_rules                                │
│                                                        │
│ iptables -X [chain]                                   │
│   Delete chain (supprimer chaîne perso)               │
│   iptables -X my_rules                                │
│                                                        │
│ iptables -E <old> <new>                               │
│   Rename chain (renommer)                             │
│   iptables -E old_name new_name                       │
│                                                        │
│ iptables -Z [chain]                                   │
│   Zero statistics (réinitialiser compteurs)           │
│   iptables -Z INPUT                                   │
│   (Réinitialiser nombre de paquets/bytes)             │
│                                                        │
│ iptables -t <table>                                   │
│   Spécifier la table (filter, nat, mangle)            │
│   Défaut: filter                                      │
│   iptables -t nat -L                                  │
│   iptables -t mangle -A POSTROUTING ...              │
│                                                        │
└────────────────────────────────────────────────────────┘
```

### 6.2 Options Avancées

```text
┌────────────────────────────────────────────────────────┐
│         OPTIONS AVANCÉES                              │
├────────────────────────────────────────────────────────┤
│                                                        │
│ AFFICHAGE:                                             │
│                                                        │
│ iptables -L -n -v                                      │
│   -L: List                                             │
│   -n: Numeric (pas de DNS lookup)                      │
│   -v: Verbose (détails)                               │
│                                                        │
│ iptables -L -n -v -x                                   │
│   -x: Exact numbers (pas d'abréviation K/M)           │
│                                                        │
│ iptables -L INPUT --line-numbers                      │
│   Avec numéros de ligne (pour supprimer)              │
│                                                        │
│ iptables -L FORWARD -t nat                            │
│   Afficher chaîne NAT FORWARD                         │
│                                                        │
│ iptables -S [chain]                                   │
│   Afficher sous forme de commandes                    │
│   Facile à copier/coller                              │
│   iptables -S INPUT                                   │
│                                                        │
│ iptables -S INPUT | grep -- "-A INPUT"                │
│   Afficher seulement les appends (pas policies)       │
│                                                        │
│ ÉDITION:                                               │
│                                                        │
│ iptables -I INPUT 1 ...                               │
│   Insert position 1 (haute priorité)                  │
│                                                        │
│ iptables --insert INPUT 3 ...                         │
│   Insert position 3                                   │
│                                                        │
│ iptables -R INPUT 5 ...                               │
│   Replace rule 5                                      │
│                                                        │
│ SUPPRESSION:                                           │
│                                                        │
│ iptables -D INPUT 1                                   │
│   Delete rule 1                                       │
│                                                        │
│ iptables -D INPUT -p tcp --dport 22 -j ACCEPT         │
│   Delete by specification                             │
│                                                        │
│ iptables -F                                           │
│   Flush ALL rules                                     │
│                                                        │
│ iptables -F INPUT                                     │
│   Flush INPUT chain only                              │
│                                                        │
│ POLITIQUES:                                            │
│                                                        │
│ iptables -P INPUT DROP                                │
│   Set INPUT policy to DROP                            │
│                                                        │
│ iptables -P INPUT ACCEPT                              │
│   Set INPUT policy to ACCEPT                          │
│                                                        │
│ iptables -P FORWARD DROP                              │
│   Set FORWARD policy to DROP                          │
│                                                        │
│ STATISTIQUES:                                          │
│                                                        │
│ iptables -L -n -v                                      │
│   Affiche PKts et Bytes pour chaque règle             │
│                                                        │
│ iptables -Z                                           │
│   Reset statistics (Pkts/Bytes = 0)                   │
│                                                        │
│ iptables -Z INPUT                                     │
│   Reset INPUT chain stats                             │
│                                                        │
└────────────────────────────────────────────────────────┘
```

### 6.3 Short vs Long Options

```text
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
│ │     │ │   │ │  │     │ │ │
│ │     │ │   │ │  │     │ │ └─ ACCEPT = action
│ │     │ │   │ │  │     │ └─ -j = jump target
│ │     │ │   │ │  │     └─ 80 = HTTP port
│ │     │ │   │ │  └─ --dport = destination port (long)
│ │     │ │   │ └─ tcp = TCP protocol
│ │     │ │   └─ -p = protocol (short)
│ │     │ └─ INPUT = input chain
│ │     └─ -A = append
│ └─ iptables command
└─ root privileges needed

LONG vs SHORT:

-A (--append)       | iptables -A INPUT ...
-D (--delete)       | iptables -D INPUT 1
-I (--insert)       | iptables -I INPUT 1
-R (--replace)      | iptables -R INPUT 1
-L (--list)         | iptables -L
-F (--flush)        | iptables -F
-N (--new-chain)    | iptables -N my_chain
-X (--delete-chain) | iptables -X my_chain
-P (--policy)       | iptables -P INPUT DROP
-E (--rename-chain) | iptables -E old new
-Z (--zero)         | iptables -Z
-n (--numeric)      | iptables -L -n
-v (--verbose)      | iptables -L -v
-x (--exact)        | iptables -L -x
-t (--table)        | iptables -t nat
-j (--jump)         | -j ACCEPT
-p (--protocol)     | -p tcp
-s (--source)       | -s 192.168.1.0/24
-d (--destination)  | -d 10.0.0.1
-i (--in-interface) | -i eth0
-o (--out-interface)| -o eth1
```

---

## 7. 🎯 Filtre (Filter Table) — Le Cœur {#7-filtre-filter-table--le-cœur}

### 7.1 Architecture Filter Table

```text
FILTER TABLE (90% de vos règles seront ici)
│
├─ INPUT CHAIN
│  ├─ Rule 1: Allow established connections
│  ├─ Rule 2: Allow SSH (port 22)
│  ├─ Rule 3: Allow HTTP (port 80)
│  ├─ Rule 4: Allow HTTPS (port 443)
│  └─ Policy: DROP (par défaut = bloquer tout)
│
├─ OUTPUT CHAIN
│  ├─ Rule 1: Allow DNS (port 53)
│  ├─ Rule 2: Allow HTTP (port 80)
│  ├─ Rule 3: Allow HTTPS (port 443)
│  └─ Policy: ACCEPT (par défaut = autoriser tout sortant)
│
└─ FORWARD CHAIN
   ├─ Rule 1: Allow established
   ├─ Rule 2: Allow LAN to Internet
   └─ Policy: DROP (par défaut = bloquer tout)
```

### 7.2 Firewall Simple (Stateless)

```bash
# RESET ALL
sudo iptables -F
sudo iptables -X
sudo iptables -P INPUT ACCEPT
sudo iptables -P OUTPUT ACCEPT
sudo iptables -P FORWARD ACCEPT

# BASIC FIREWALL (Stateless):

# INPUT: Default DENY
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP

# Allow ESTABLISHED connections (crucial!)
sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Allow loopback (important pour applications)
sudo iptables -A INPUT -i lo -j ACCEPT

# Allow SSH
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Allow HTTP/HTTPS
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Allow ICMP (ping)
sudo iptables -A INPUT -p icmp -j ACCEPT

# OUTPUT: Default ALLOW
sudo iptables -P OUTPUT ACCEPT

# Vérifier
sudo iptables -L -n -v
```

### 7.3 Firewall Stateful (Recommandé)

```bash
# RESET
sudo iptables -F
sudo iptables -P INPUT ACCEPT
sudo iptables -P OUTPUT ACCEPT
sudo iptables -P FORWARD ACCEPT

# ==== STATEFUL FIREWALL ====

# 1. Default policies: Deny-All
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
sudo iptables -P OUTPUT DROP  # Strict egress filtering

# 2. LOOPBACK (important!)
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -A OUTPUT -o lo -j ACCEPT

# 3. CONNECTION TRACKING (le cœur du stateful)
# Accept established/related
sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A OUTPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A FORWARD -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# 4. INBOUND RULES (Autoriser services)
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT     # SSH
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT     # HTTP
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT    # HTTPS
sudo iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT  # Ping

# 5. OUTBOUND RULES (Client-side)
sudo iptables -A OUTPUT -p tcp --dport 80 -j ACCEPT    # HTTP client
sudo iptables -A OUTPUT -p tcp --dport 443 -j ACCEPT   # HTTPS client
sudo iptables -A OUTPUT -p udp --dport 53 -j ACCEPT    # DNS
sudo iptables -A OUTPUT -p tcp --dport 22 -j ACCEPT    # SSH client
sudo iptables -A OUTPUT -p tcp --dport 25 -j ACCEPT    # SMTP
sudo iptables -A OUTPUT -p udp --dport 123 -j ACCEPT   # NTP
sudo iptables -A OUTPUT -p icmp --icmp-type echo-request -j ACCEPT  # Ping

# 6. FORWARD RULES (Router/Firewall)
# Allow LAN to Internet
sudo iptables -A FORWARD -i eth1 -o eth0 -j ACCEPT     # LAN → Internet
sudo iptables -A FORWARD -i eth0 -o eth1 -j ACCEPT     # Internet → LAN

# 7. LOGGING (pour debug)
sudo iptables -A INPUT -j LOG --log-prefix "INPUT_BLOCK: " --log-level 4
sudo iptables -A FORWARD -j LOG --log-prefix "FORWARD_BLOCK: " --log-level 4

# Vérifier
sudo iptables -L INPUT -n -v
```

---

## 8. 🔄 NAT (Network Address Translation) {#8-nat-network-address-translation}

### 8.1 Concepts NAT

```text
┌────────────────────────────────────────────────────────┐
│           NAT (Network Address Translation)            │
├────────────────────────────────────────────────────────┤
│                                                        │
│ SOURCE NAT (SNAT) - Changer IP source                 │
│ ├─ Paquet: src=192.168.1.100 dst=8.8.8.8            │
│ ├─ SNAT appliqué: src=203.0.113.10 dst=8.8.8.8       │
│ ├─ Réponse: src=8.8.8.8 dst=203.0.113.10             │
│ ├─ REVERSE SNAT: src=8.8.8.8 dst=192.168.1.100       │
│ └─ Location: POSTROUTING                              │
│                                                        │
│ DESTINATION NAT (DNAT) - Changer IP destination       │
│ ├─ Paquet: src=8.8.8.8 dst=203.0.113.10:8080         │
│ ├─ DNAT appliqué: src=8.8.8.8 dst=192.168.1.100:80   │
│ ├─ Réponse: src=192.168.1.100:80 dst=8.8.8.8         │
│ ├─ REVERSE DNAT: src=203.0.113.10:8080 dst=8.8.8.8   │
│ └─ Location: PREROUTING                               │
│                                                        │
└────────────────────────────────────────────────────────┘
```

### 8.2 SNAT (Source NAT) - Masquerade

```bash
# SCENARIO: LAN 192.168.1.0/24 accède Internet via eth0

# METHOD 1: MASQUERADE (simple)
# Utilise l'IP de l'interface (dynamic)
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

# METHOD 2: Static SNAT
# Utilise une IP fixe
sudo iptables -t nat -A POSTROUTING -o eth0 \
  -j SNAT --to-source 203.0.113.10

# METHOD 3: Port SNAT (Advanced)
sudo iptables -t nat -A POSTROUTING -o eth0 -p tcp \
  -j SNAT --to-source 203.0.113.10:10000-20000

# VÉRIFIER:
sudo iptables -t nat -L POSTROUTING -n -v

# RÉSULTAT:
# 192.168.1.100 → Google (8.8.8.8)
# devient
# 203.0.113.10 → Google (8.8.8.8)
# 
# Réponse:
# 8.8.8.8 → 203.0.113.10
# devient
# 8.8.8.8 → 192.168.1.100 (automatic REVERSE NAT)
```

### 8.3 DNAT (Destination NAT) - Port Forwarding

```bash
# SCENARIO: Port 8080 public → Port 80 interne

# FORWARDING SETUP (prerequisite):
sudo sysctl -w net.ipv4.ip_forward=1

# DNAT RULE: redirect external traffic
sudo iptables -t nat -A PREROUTING -d 203.0.113.10 \
  -p tcp --dport 8080 \
  -j DNAT --to-destination 192.168.1.100:80

# SNAT RULE: allow reply traffic
sudo iptables -t nat -A POSTROUTING -d 192.168.1.100 \
  -p tcp --dport 80 \
  -j SNAT --to-source 203.0.113.10

# OR SIMPLER with MASQUERADE:
sudo iptables -t nat -A POSTROUTING -d 192.168.1.100 \
  -p tcp --dport 80 \
  -j MASQUERADE

# VÉRIFIER:
sudo iptables -t nat -L PREROUTING -n -v

# RÉSULTAT:
# External: curl http://203.0.113.10:8080
# Forwarded to: 192.168.1.100:80 (internal web server)
```

### 8.4 Cas Pratique: Partage Internet (Router)

```bash
# Setup:
# eth0 = Internet (203.0.113.10/24)
# eth1 = LAN (192.168.1.1/24)
# 5 machines LAN need internet access

# 1. Enable forwarding
sudo sysctl -w net.ipv4.ip_forward=1
echo "net.ipv4.ip_forward=1" | sudo tee -a /etc/sysctl.conf

# 2. Configure INPUT (firewall)
sudo iptables -P INPUT DROP
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -A INPUT -i eth0 -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A INPUT -i eth1 -j ACCEPT  # Trust LAN
sudo iptables -A INPUT -p icmp -j ACCEPT

# 3. Configure FORWARD
sudo iptables -P FORWARD DROP
sudo iptables -A FORWARD -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A FORWARD -i eth1 -o eth0 -j ACCEPT  # LAN → Internet
sudo iptables -A FORWARD -i eth0 -o eth1 -j ACCEPT  # Internet → LAN (reply)

# 4. Configure OUTPUT
sudo iptables -P OUTPUT ACCEPT

# 5. NAT: Masquerade LAN traffic
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

# 6. Verify
sudo iptables -L -n -v
sudo iptables -t nat -L -n -v
```

---

## 9. 🔨 Mangle (Modification de Paquets) {#9-mangle-modification-de-paquets}

### 9.1 MANGLE use cases

```text
┌────────────────────────────────────────────────────────┐
│           MANGLE TABLE (Avancé)                       │
├────────────────────────────────────────────────────────┤
│                                                        │
│ TTL MANIPULATION:                                      │
│                                                        │
│ # Décrémenter TTL (empêcher bypass de firewall)       │
│ iptables -t mangle -A FORWARD -j TTL --ttl-dec 1      │
│                                                        │
│ # Fixer TTL à une valeur                              │
│ iptables -t mangle -A POSTROUTING -j TTL --ttl-set 64 │
│                                                        │
│ ─────────────────────────────────────────────────────  │
│                                                        │
│ PACKET MARKING (Pour routage):                        │
│                                                        │
│ # Marquer paquets HTTP                                │
│ iptables -t mangle -A OUTPUT -p tcp --dport 80 \      │
│   -j MARK --set-mark 1                                │
│                                                        │
│ # Marquer paquets SSH                                 │
│ iptables -t mangle -A OUTPUT -p tcp --dport 22 \      │
│   -j MARK --set-mark 2                                │
│                                                        │
│ # Utiliser les marks pour routing (ip rule)           │
│ # ip rule add fwmark 1 table 100                       │
│ # ip route add default via 10.0.0.1 table 100         │
│                                                        │
│ ─────────────────────────────────────────────────────  │
│                                                        │
│ MSS CLAMPING (TCP):                                    │
│                                                        │
│ # Fixer MSS à 1472 pour PPPoE (1500 - 28 = 1472)      │
│ iptables -t mangle -A FORWARD -p tcp --tcp-flags SYN,RST SYN \
│   -j TCPMSS --clamp-mss-to-pmtu                       │
│                                                        │
│ ─────────────────────────────────────────────────────  │
│                                                        │
│ DSCP / TOS MARKING (QoS):                              │
│                                                        │
│ # Marquer paquets VoIP avec DSCP EF (46)              │
│ iptables -t mangle -A OUTPUT -p udp --dport 5060 \    │
│   -j DSCP --set-dscp-class EF                         │
│                                                        │
│ # Marquer HTTP avec AF13 (Best-effort)                │
│ iptables -t mangle -A OUTPUT -p tcp --dport 80 \      │
│   -j DSCP --set-dscp-class AF13                       │
│                                                        │
│ ─────────────────────────────────────────────────────  │
│                                                        │
│ STATE RESET (Advanced):                               │
│                                                        │
│ # Conntrack timeout adjustment                        │
│ # Fait dans conntrack, pas iptables...               │
│                                                        │
└────────────────────────────────────────────────────────┘
```

---

## 10. 🚀 Raw & Security Tables {#10-raw--security}

### 10.1 RAW Table

```bash
# RAW table: Bypass connection tracking

# Notrack specific traffic (performance):
sudo iptables -t raw -A PREROUTING -p tcp --dport 25 -j NOTRACK
sudo iptables -t raw -A OUTPUT -p tcp --dport 25 -j NOTRACK

# Why?
# • Reduce kernel memory usage (conntrack state)
# • Performance for stateless traffic (DNS, DNS-over-HTTPS)
# • Save conntrack table space

# Use case: High-traffic SMTP server
iptables -t raw -A PREROUTING -i eth0 -p tcp --dport 25 -j NOTRACK
```

### 10.2 SECURITY Table

```bash
# SECURITY table: SELinux integration

# Mark packets for SELinux policy:
sudo iptables -t security -A OUTPUT -p tcp --dport 3306 \
  -j SECMARK --selctx system_u:object_r:mysql_port_t:s0

# Requires SELinux enabled and configured
# Most deployments: not needed
```

---

## 11. 🔄 Stateful vs Stateless {#11-stateful-vs-stateless}

### 11.1 Stateless Filtering

```bash
# STATELESS: Examine chaque paquet indépendamment

# Bloquer tout port > 1024 (malware)
sudo iptables -A INPUT -p tcp --dport 1024:65535 -j DROP

# Problème: Vous n'avez pas les réponses des services!
# Si vous lancez DNS query, vous recevez réponse sur port high
# La règle ci-dessus bloque la réponse!

# Résultat: DNS fonctionne pas, HTTP ne fonctionne pas, etc.
```

### 11.2 Stateful Filtering (RECOMMENDED)

```bash
# STATEFUL: Suivi de l'état de la connexion

# Permettre toutes les réponses de services externes
sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Connection states:
# • NEW: Nouveau paquet (initiateur)
# • ESTABLISHED: Réponse à une connexion existante
# • RELATED: Connexion liée (ex: FTP passive mode)
# • INVALID: Paquet invalide/corrompu

# EXEMPLE STATEFUL:
sudo iptables -P INPUT DROP  # Default: deny
sudo iptables -A INPUT -i lo -j ACCEPT  # Loopback
sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT  # Replies!
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT  # SSH inbound
# Les réponses de services lancés localement passeront via ESTABLISHED
```

### 11.3 Connection Tracking Details

```text
┌────────────────────────────────────────────────────────┐
│        CONNECTION TRACKING (conntrack)                │
├────────────────────────────────────────────────────────┤
│                                                        │
│ STATE MACHINE:                                         │
│                                                        │
│ 1. TCP Connection:                                     │
│                                                        │
│    CLIENT                                SERVER        │
│    SYN ──────────────────────────→ (NEW)              │
│    ←─── SYN-ACK (ESTABLISHED)  ←─── (ESTABLISHED)     │
│    ACK ──────────────────────────→ (ESTABLISHED)      │
│    DATA ──────────────────────────→ (ESTABLISHED)      │
│    ←─── DATA (ESTABLISHED)  ←─── (ESTABLISHED)         │
│    FIN ──────────────────────────→ (ESTABLISHED)      │
│    ←─── FIN-ACK (ESTABLISHED) ←─── (ESTABLISHED)       │
│    [Connection closed after timeout]                  │
│                                                        │
│ 2. UDP (Connectionless):                              │
│                                                        │
│    CLIENT ────→ SERVER                                │
│    (NEW)        (NEW paquet)                          │
│    CLIENT ←──── SERVER                                │
│    (ESTABLISHED) (Réponse - matched)                  │
│                                                        │
│ 3. RELATED:                                            │
│                                                        │
│    Primary: FTP control (port 21)                     │
│    Related: FTP data (port 20)                        │
│    conntrack recognizes this relationship             │
│                                                        │
│ Checking state:                                        │
│                                                        │
│ sudo cat /proc/net/nf_conntrack                        │
│ Shows active connections being tracked                │
│                                                        │
│ Tuning:                                                │
│                                                        │
│ # Max connections                                      │
│ echo 262144 > /proc/sys/net/nf_conntrack_max          │
│                                                        │
│ # Timeout (seconds)                                    │
│ echo 300 > /proc/sys/net/netfilter/nf_conntrack_tcp_timeout_established
│                                                        │
└────────────────────────────────────────────────────────┘
```

---

## 12. 💼 Cas d'Usage Réels {#12-cas-dusage-réels}

### 12.1 Web Server Protection

```bash
#!/bin/bash
# Protect a web server from common attacks

# Clear rules
iptables -F
iptables -X
iptables -P INPUT ACCEPT
iptables -P OUTPUT ACCEPT
iptables -P FORWARD ACCEPT

# Set default policies
iptables -P INPUT DROP
iptables -P OUTPUT DROP
iptables -P FORWARD DROP

# 1. LOOPBACK
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT

# 2. ESTABLISHED CONNECTIONS
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
iptables -A OUTPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# 3. INBOUND RULES
iptables -A INPUT -p tcp --dport 22 -s 10.0.0.0/8 -j ACCEPT  # SSH from admin only
iptables -A INPUT -p tcp --dport 80 -j ACCEPT   # HTTP
iptables -A INPUT -p tcp --dport 443 -j ACCEPT  # HTTPS
iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT  # Ping

# 4. OUTBOUND RULES
iptables -A OUTPUT -p tcp --dport 80 -j ACCEPT      # HTTP
iptables -A OUTPUT -p tcp --dport 443 -j ACCEPT     # HTTPS
iptables -A OUTPUT -p udp --dport 53 -j ACCEPT      # DNS
iptables -A OUTPUT -p tcp --dport 25 -j ACCEPT      # SMTP (email)
iptables -A OUTPUT -p icmp --icmp-type echo-request -j ACCEPT  # Ping

# 5. RATE LIMITING (DDoS protection)
iptables -N RATE_LIMIT
iptables -A RATE_LIMIT -p tcp --dport 80 -m limit --limit 25/minute --limit-burst 100 -j ACCEPT
iptables -A RATE_LIMIT -p tcp --dport 80 -j DROP
iptables -A INPUT -j RATE_LIMIT

# 6. LOG DROPPED PACKETS
iptables -A INPUT -j LOG --log-prefix "DROPPED_IN: "
iptables -A OUTPUT -j LOG --log-prefix "DROPPED_OUT: "

# 7. SYN FLOOD PROTECTION
iptables -N SYN_FLOOD
iptables -A SYN_FLOOD -p tcp --syn -m limit --limit 1/second --limit-burst 3 -j ACCEPT
iptables -A SYN_FLOOD -p tcp --syn -j DROP
iptables -A INPUT -p tcp --dport 80 -j SYN_FLOOD
iptables -A INPUT -p tcp --dport 443 -j SYN_FLOOD

# Save rules
sudo iptables-save > /etc/iptables/rules.v4
```

### 12.2 Router/Gateway Setup

```bash
#!/bin/bash
# Configure router (eth0=WAN, eth1=LAN)

# Enable forwarding
sysctl -w net.ipv4.ip_forward=1

# Clear
iptables -F
iptables -P INPUT ACCEPT
iptables -P OUTPUT ACCEPT
iptables -P FORWARD ACCEPT

# Input policies
iptables -P INPUT DROP
iptables -P FORWARD DROP

# Loopback
iptables -A INPUT -i lo -j ACCEPT
iptables -A FORWARD -i lo -j ACCEPT

# Established
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
iptables -A FORWARD -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Allow from LAN
iptables -A INPUT -i eth1 -j ACCEPT
iptables -A FORWARD -i eth1 -o eth0 -j ACCEPT  # LAN → Internet
iptables -A FORWARD -i eth0 -o eth1 -j ACCEPT  # Internet → LAN (reply)

# NAT
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

# Save
iptables-save > /etc/iptables/rules.v4
```

### 12.3 DDoS Protection

```bash
#!/bin/bash
# Protection against common DDoS attacks

# SYN flood protection
iptables -A INPUT -p tcp --syn -m limit --limit 1/s --limit-burst 3 -j ACCEPT
iptables -A INPUT -p tcp --syn -j DROP

# UDP flood protection
iptables -A INPUT -p udp -m limit --limit 1/s --limit-burst 3 -j ACCEPT
iptables -A INPUT -p udp -j DROP

# ICMP flood protection
iptables -A INPUT -p icmp -m limit --limit 1/s --limit-burst 1 -j ACCEPT
iptables -A INPUT -p icmp -j DROP

# Connection limit per IP
iptables -A INPUT -p tcp --dport 80 -m connlimit --connlimit-above 20 -j REJECT

# Portscanning detection
iptables -N port_scanning
iptables -A port_scanning -p tcp --tcp-flags SYN,ACK,FIN,RST RST -m limit --limit 1/s --limit-burst 2 -j RETURN
iptables -A port_scanning -p tcp --tcp-flags SYN,ACK,FIN,RST RST -j DROP
iptables -A INPUT -p tcp -j port_scanning
```

---

## 13. 💾 Configuration Persistante {#13-configuration-persistante}

### 13.1 iptables-save / iptables-restore

```bash
# SAVE current rules to file
sudo iptables-save > /tmp/iptables-backup.rules
sudo cat /tmp/iptables-backup.rules

# Example output:
# *filter
# :INPUT DROP [0:0]
# :FORWARD DROP [0:0]
# :OUTPUT ACCEPT [0:0]
# -A INPUT -i lo -j ACCEPT
# -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
# -A INPUT -p tcp --dport 22 -j ACCEPT
# COMMIT
# *nat
# :PREROUTING ACCEPT [0:0]
# ...

# RESTORE from file
sudo iptables-restore < /tmp/iptables-backup.rules

# Verify
sudo iptables -L -n -v
```

### 13.2 Persistent Across Reboot (Ubuntu/Debian)

```bash
# Install iptables-persistent package
sudo apt-get install iptables-persistent

# Automatically save when you create a rule:
# The package provides services that auto-save

# Manual save to persistence:
sudo iptables-save | sudo tee /etc/iptables/rules.v4

# Enable persistence service
sudo systemctl enable iptables.service
sudo systemctl enable netfilter-persistent.service

# On reboot, rules are automatically restored

# Check service:
sudo systemctl status netfilter-persistent
```

### 13.3 Create Script for Reapply

```bash
#!/bin/bash
# /usr/local/bin/firewall.sh
# Make executable: chmod +x /usr/local/bin/firewall.sh

case "$1" in
    start)
        echo "Starting firewall..."
        iptables-restore < /etc/iptables/rules.v4
        echo "Firewall started"
        ;;
    stop)
        echo "Stopping firewall..."
        iptables -P INPUT ACCEPT
        iptables -P OUTPUT ACCEPT
        iptables -P FORWARD ACCEPT
        iptables -F
        iptables -X
        echo "Firewall stopped (all rules flushed)"
        ;;
    restart)
        $0 stop
        sleep 1
        $0 start
        ;;
    status)
        iptables -L -n -v
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|status}"
        exit 1
        ;;
esac
exit 0

# Add to /etc/rc.local or systemd:
# SystemD: Create /etc/systemd/system/firewall.service:
# [Unit]
# Description=Custom Firewall Rules
# After=network-online.target
#
# [Service]
# Type=oneshot
# RemainAfterExit=yes
# ExecStart=/usr/local/bin/firewall.sh start
# ExecStop=/usr/local/bin/firewall.sh stop
#
# [Install]
# WantedBy=multi-user.target

sudo systemctl enable firewall.service
sudo systemctl start firewall.service
```

---

## 14. 🔍 Debugging & Logs {#14-debugging--logs}

### 14.1 Logging Dropped Packets

```bash
# LOG TARGET (examine, don't drop)
iptables -A INPUT -p tcp --dport 666 -j LOG --log-prefix "SUSPICIOUS_PORT: "

# Then packets matching will appear in:
sudo tail -f /var/log/kern.log
# Output: [12345.123456] SUSPICIOUS_PORT: IN=eth0 OUT= MAC=... SRC=192.168.1.100 DST=10.0.0.1 PROTO=TCP SPT=52341 DPT=666

# All log-options:
# --log-prefix "TEXT": prefix for easier grep
# --log-level: emergency(0), alert(1), critical(2), error(3), warning(4), notice(5), info(6), debug(7)
# --log-tcp-sequence: log TCP sequence numbers (for debugging)
# --log-tcp-options: log TCP options
# --log-ip-options: log IP options
# --log-uid: log UID of process (needs kernel support)

# Performance: Use LIMIT with LOG
iptables -A INPUT -j LOG --log-prefix "INPUT_DROP: " -m limit --limit 1/minute

# Check logs:
grep "INPUT_DROP:" /var/log/kern.log | tail -20
```

### 14.2 Connection Tracking Debug

```bash
# View active connections being tracked
sudo cat /proc/net/nf_conntrack | head -20

# Example output:
# ipv4     2 tcp      6 300 ESTABLISHED src=192.168.1.100 dst=8.8.8.8 sport=52341 dport=53 src=8.8.8.8 dst=203.0.113.10 sport=53 dport=52341 [ASSURED] mark=0 use=2

# Count total connections
sudo wc -l /proc/net/nf_conntrack

# Conntrack stats:
sudo cat /proc/net/nf_conntrack_stat

# Real-time monitoring:
watch -n 1 'wc -l /proc/net/nf_conntrack'

# Flush conntrack table (careful!):
sudo conntrack -F

# List connections with conntrack tool:
sudo conntrack -L
sudo conntrack -L -p tcp  # TCP only
sudo conntrack -L -s 192.168.1.100  # From specific IP
```

### 14.3 Test Rules

```bash
# Generate test traffic
nc -l -p 5555  # Server listening on port 5555
nc -zv localhost 5555  # Client connecting

# Generate TCP SYN
hping3 -S -p 22 localhost

# Generate UDP
echo "test" | nc -u localhost 5555

# Check if rule matched:
iptables -L INPUT -n -v -x | grep "22"
# Shows packet count

# Test with tcpdump:
sudo tcpdump -i eth0 -n port 22
```

---

## 15. 🔧 Firewalld (Modern Wrapper) {#15-firewalld-modern-wrapper}

### 15.1 Firewalld vs iptables

```text
┌────────────────────────────────────────────────────────┐
│     FIREWALLD vs RAW iptables                         │
├────────────────────────────────────────────────────────┤
│                                                        │
│ FIREWALLD:                                             │
│ • High-level wrapper around iptables/nftables         │
│ • Dynamic rule management (no restart needed)         │
│ • Zone-based concept (public, private, trusted)       │
│ • YAML configuration                                  │
│ • systemctl restart firewalld → rules preserved       │
│ • Easier for most users                               │
│ • RedHat/CentOS standard                              │
│                                                        │
│ RAW iptables:                                          │
│ • Direct kernel interface                             │
│ • Lower level, more control                           │
│ • Rules lost on restart (need persistence)            │
│ • Steeper learning curve                              │
│ • Sometimes faster (no daemon overhead)               │
│ • Can coexist with firewalld (careful!)               │
│                                                        │
└────────────────────────────────────────────────────────┘
```

### 15.2 Firewalld Basics

```bash
# Check status
sudo firewall-cmd --state

# Start/Enable
sudo systemctl start firewalld
sudo systemctl enable firewalld

# List zones
sudo firewall-cmd --get-zones
# Output: block dmz drop external home internal public trusted work

# Get active zones
sudo firewall-cmd --get-active-zones

# Get default zone
sudo firewall-cmd --get-default-zone

# Set default zone
sudo firewall-cmd --set-default-zone=public

# List rules in zone
sudo firewall-cmd --zone=public --list-all

# Add service (permanent)
sudo firewall-cmd --permanent --zone=public --add-service=http
sudo firewall-cmd --reload  # apply

# Add port (temporary)
sudo firewall-cmd --zone=public --add-port=8080/tcp

# Add port (permanent)
sudo firewall-cmd --permanent --zone=public --add-port=8080/tcp
sudo firewall-cmd --reload

# Remove rule
sudo firewall-cmd --permanent --zone=public --remove-service=http
sudo firewall-cmd --reload

# Rich rules (advanced):
sudo firewall-cmd --permanent --zone=public \
  --add-rich-rule='rule family="ipv4" source address="192.168.1.0/24" service name="ssh" accept'
sudo firewall-cmd --reload
```

### 15.3 Zones in Firewalld

```text
Public (default):
  • For public networks (Internet)
  • SSH open, everything else denied
  • Untrusted

Internal:
  • For internal networks
  • More services open than public
  • Somewhat trusted

Home:
  • For home networks
  • More permissive
  • Trusted

Trusted:
  • Complete trust
  • All traffic accepted

Drop:
  • Deny-all
  • Drops incoming packets silently

Block:
  • Reject all incoming
  • Sends ICMP reject

DMZ:
  • Demilitarized zone
  • Limited services exposed
```

---

## 16. 🚀 Migration vers nftables {#16-migration-vers-nftables}

### 16.1 Why nftables?

```text
nftables is the modern replacement for iptables/ip6tables/arptables

ADVANTAGES:
✅ Unified syntax (one tool, all protocols)
✅ Faster packet processing
✅ Lower memory usage
✅ Better rule composition
✅ Cleaner configuration
✅ Atomic operations

DISADVANTAGES:
❌ Newer (requires recent kernel 3.13+)
❌ Fewer tools/documentation
❌ Less adoption (as of 2024)
❌ Breaking changes from iptables

RECOMMENDED TIMELINE:
• 2024: iptables still widely used
• 2025-2026: Gradual migration to nftables
• 2027+: nftables becomes standard

For now: Learn iptables (essential knowledge)
```

### 16.2 nftables Basics

```bash
# Install nftables
sudo apt-get install nftables

# View current rules
sudo nft list ruleset

# Basic example (replaces iptables -A INPUT -p tcp --dport 22 -j ACCEPT):
sudo nft add rule filter input tcp dport 22 accept

# List tables
sudo nft list tables

# List a table
sudo nft list table filter

# Create table
sudo nft add table filter

# Create chain
sudo nft add chain filter input { type filter hook input priority 0 \; policy drop \; }

# Add rule
sudo nft add rule filter input ct state established,related accept

# Load config
sudo nft -f /etc/nftables.conf

# Save config
sudo nft list ruleset > /etc/nftables.conf

# Start service
sudo systemctl enable nftables
sudo systemctl start nftables
```

---

## 17. ⚡ Performance & Optimisation {#17-performance--optimisation}

### 17.1 Connection Tracking Tuning

```bash
# Check current settings
sysctl -a | grep nf_conntrack

# Max connections
echo 262144 > /proc/sys/net/nf_conntrack_max

# Or persistent:
echo "net.nf_conntrack_max=262144" >> /etc/sysctl.conf
sysctl -p

# Timeouts:
# TCP established (default 432000 = 5 days)
echo 86400 > /proc/sys/net/netfilter/nf_conntrack_tcp_timeout_established

# TCP time-wait (default 120)
echo 60 > /proc/sys/net/netfilter/nf_conntrack_tcp_timeout_time_wait

# UDP (default 180)
echo 120 > /proc/sys/net/netfilter/nf_conntrack_udp_timeout

# Persistent:
cat >> /etc/sysctl.conf << EOF
net.netfilter.nf_conntrack_tcp_timeout_established=86400
net.netfilter.nf_conntrack_tcp_timeout_time_wait=60
net.netfilter.nf_conntrack_udp_timeout=120
EOF
sysctl -p
```

### 17.2 Rule Optimization

```bash
# 1. ORDER RULES BY FREQUENCY
# Most frequent rules first (less matching)
iptables -I INPUT 1 -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
# (established is majority of traffic)

# 2. Use STATEFUL instead of STATELESS
✅  GOOD:  -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
❌ BAD:  -p tcp --dport 1:65535 (matches everything)

# 3. Be specific with ranges
✅  GOOD:  --dport 30000:40000
❌ BAD:  --dport 1:65535

# 4. Use builtin chains (INPUT, OUTPUT) instead of custom when possible
# Custom chains have overhead

# 5. Limit LOG rules (use --limit)
✅  GOOD:  -j LOG -m limit --limit 1/minute
❌ BAD:  -j LOG (logs every packet!)

# 6. Use nfqueue carefully
# nfqueue sends packets to userspace (very slow)
```

### 17.3 Monitor Performance

```bash
# Check rule hit count
iptables -L INPUT -n -v
# "pkts" column shows how many packets matched

# Reset counters
iptables -Z

# Monitor in real-time
watch -n 1 'iptables -L INPUT -n -v'

# Check conntrack usage
cat /proc/net/nf_conntrack_stat

# Example output:
# entries  searched found new invalid ignore delete delete_list insert insert_failed drop early_drop icmp_error expect_new expect_create expect_delete search_restart
# 12345    98765    54321 2100 150    300   50    0           100    5            450  12       0           4             3            25

# Total connections
wc -l /proc/net/nf_conntrack
```

---

## 18. 🔒 Bonnes Pratiques & Sécurité {#18-bonnes-pratiques--sécurité}

### 18.1 Security Best Practices

```text
✅ DO:

1. DEFAULT DENY (Whitelist approach)
   iptables -P INPUT DROP
   iptables -P FORWARD DROP
   iptables -P OUTPUT DROP  # if strict
   
   Then explicitly ACCEPT what you need

2. USE STATEFUL INSPECTION
   -m conntrack --ctstate ESTABLISHED,RELATED
   Prevents orphaned packets

3. LOG SUSPICIOUS TRAFFIC
   -j LOG --log-prefix "SUSPICIOUS: "
   Helps detect attacks

4. LIMIT CONNECTIONS
   -m connlimit --connlimit-above 20
   Prevents resource exhaustion

5. RATE LIMIT
   -m limit --limit 25/minute --limit-burst 100
   Prevents DDoS

6. SEPARATE RULES BY PURPOSE
   Use custom chains for organization
   -N SSH_RULES
   -N WEB_RULES

7. DOCUMENT YOUR RULES
   Add comments (need custom script)
   Echo "# Allow SSH from admin subnet" before rule

8. TEST BEFORE APPLYING
   Load in separate table
   Or test with firewalld zones

9. BACKUP BEFORE CHANGES
   iptables-save > backup.rules
   Before major changes

10. MONITOR & AUDIT
    Check logs regularly
    Review rules quarterly
```

```text
❌ DON'T:

1. DON'T USE DEFAULT POLICY ACCEPT with blacklist rules
   iptables -P INPUT ACCEPT  # BAD!
   Then trying to block bad things
   Malware you don't know about will get through

2. DON'T LEAVE RULES PERSISTENT WITHOUT TESTING
   Changes disappear on reboot without testing

3. DON'T LOCK YOURSELF OUT
   Test SSH before applying strict rules
   Keep at least one access method open!

4. DON'T MIX FIREWALLD + RAW IPTABLES
   Both will fight over rules
   Use one or the other

5. DON'T IGNORE CONNECTION TRACKING
   Stateless filtering = broken applications

6. DON'T LOG EVERYTHING
   Fills disk quickly
   CPU impact

7. DON'T FORGET ICMP
   Ping is useful for debugging
   Block selectively, not completely

8. DON'T HARDCODE IPs (if possible)
   Use variables/scripts
   Makes changes easier

9. DON'T SKIP TESTING RULES
   Test rules in non-prod first
   Apply during maintenance window

10. DON'T FORGET IPv6
    ip6tables is separate!
    Need to configure both
```

### 18.2 Security Rules Checklist

```text
Before deploying firewall:

☐ Test SSH access (don't lock yourself out!)
☐ Allow loopback interface
☐ Enable connection tracking
☐ Set default policies to DROP
☐ Allow ESTABLISHED connections
☐ Have rescue console/serial access
☐ Test from different networks
☐ Check logs for unexpected blocks
☐ Document all rules
☐ Save backup (iptables-save)
☐ Test restart doesn't break access
☐ Verify persistence mechanism works
☐ Set up monitoring/alerting
☐ Have change rollback plan
☐ Test with DDoS simulation tools
☐ Review with security team
```

---

## 19. 🎓 Exercices Pratiques {#19-exercices-pratiques}

### Exercice 1: Basic Firewall (15 min)

**Objectif:** Créer un firewall stateful basique

```bash
# TODO: Écrivez un script qui:
# 1. Set default policies to DROP
# 2. Allow loopback
# 3. Allow SSH (port 22)
# 4. Allow established connections
# 5. Verify rules

# Hints:
# - Use iptables -P for policies
# - Use iptables -A for rules
# - Use iptables -L to verify
```

**Solution:**

```bash
#!/bin/bash
# Basic firewall setup

sudo iptables -P INPUT DROP
sudo iptables -P OUTPUT DROP
sudo iptables -P FORWARD DROP

# Loopback
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -A OUTPUT -o lo -j ACCEPT

# Established
sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A OUTPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# SSH
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
sudo iptables -A OUTPUT -p tcp --sport 22 -j ACCEPT

# DNS (for resolving)
sudo iptables -A OUTPUT -p udp --dport 53 -j ACCEPT
sudo iptables -A OUTPUT -p tcp --dport 53 -j ACCEPT

# Verify
sudo iptables -L -n -v
```

### Exercice 2: Port Forwarding (20 min)

**Objectif:** Setup port forwarding (8080 → 80)

```bash
# TODO:
# 1. Enable IP forwarding
# 2. Create DNAT rule (8080 → 80)
# 3. Create SNAT rule for replies
# 4. Test with curl
```

**Solution:**

```bash
# 1. Enable forwarding
sudo sysctl -w net.ipv4.ip_forward=1

# 2. DNAT
sudo iptables -t nat -A PREROUTING -d 203.0.113.10 \
  -p tcp --dport 8080 \
  -j DNAT --to-destination 192.168.1.100:80

# 3. SNAT
sudo iptables -t nat -A POSTROUTING -d 192.168.1.100 \
  -p tcp --dport 80 \
  -j SNAT --to-source 203.0.113.10

# 4. Test
curl http://203.0.113.10:8080
```

### Exercice 3: DDoS Protection (25 min)

**Objectif:** Implement rate limiting

```bash
# TODO: Create rules to protect against:
# 1. SYN floods
# 2. UDP floods
# 3. Connection exhaustion
```

**Solution:**

```bash
# SYN Flood protection
sudo iptables -N SYN_FLOOD
sudo iptables -A SYN_FLOOD -p tcp --syn -m limit --limit 1/s --limit-burst 3 -j ACCEPT
sudo iptables -A SYN_FLOOD -p tcp --syn -j DROP
sudo iptables -A INPUT -p tcp --dport 80 -j SYN_FLOOD

# UDP Flood
sudo iptables -A INPUT -p udp -m limit --limit 1/s --limit-burst 3 -j ACCEPT
sudo iptables -A INPUT -p udp -j DROP

# Connection limit
sudo iptables -A INPUT -p tcp --dport 80 \
  -m connlimit --connlimit-above 20 -j REJECT
```

---

## 20. 📚 Ressources & Références {#20-ressources--références}

### Documentation Officielle

- Linux Networking HOWTO: [https://tldp.org/HOWTO/Networking-Overview-HOWTO.html](https://tldp.org/HOWTO/Networking-Overview-HOWTO.html)
- iptables Tutorial: [https://www.frozentux.net/iptables-tutorial/](https://www.frozentux.net/iptables-tutorial/)
- NetFilter Documentation: [https://www.netfilter.org/documentation/](https://www.netfilter.org/documentation/)

### Man Pages

```bash
man iptables
man iptables-extensions
man conntrack
man firewall-cmd
man nft
```

### Tools & Commands

```bash
# Monitoring
iptables -L -n -v
conntrack -L
nf_conntrack
tcpdump

# Testing
nc (netcat)
nmap
hping3
curl

# Configuration
iptables-save
iptables-restore
firewall-cmd
nftables
```

### Learning Resources

- [iptables Explained](https://www.digitalocean.com/community/tutorials/iptables-essentials-common-firewall-rules-and-commands)
- Netfilter Project
- Firewalld Documentation
- Linux Foundation courses

---

## 🎓 Conclusion

Vous avez maintenant une compréhension complète d'iptables:

✅ **Fondamentaux:** Tables, Chains, Rules, Targets
✅ **Configuration:** Syntaxe complète, opérations
✅ **Cas d'usage:** Web servers, routers, DDoS protection
✅ **Optimisation:** Performance tuning, connection tracking
✅ **Alternatives:** Firewalld, nftables
✅ **Bonnes Pratiques:** Security checklist, debugging

**Prochaines étapes:**
1. Pratiquer les exercices
2. Déployer un firewall simple
3. Progresser vers des architectures complexes
4. Explorer nftables pour l'avenir

**Bon apprentissage et bienvenue dans le monde du filtrage réseau Linux! 🚀**
