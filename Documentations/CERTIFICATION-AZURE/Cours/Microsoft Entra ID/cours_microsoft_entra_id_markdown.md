# Comprendre Microsoft Entra ID

> Anciennement Azure Active Directory (Azure AD)
>
> Service cloud de gestion des identités et des accès (IAM) fourni par Microsoft.

---

## Introduction

Microsoft Entra ID est un service cloud qui permet aux organisations de gérer les identités de leurs utilisateurs et de contrôler l'accès à leurs ressources, qu'elles soient dans le cloud ou sur site.

### Ancien nom

Azure Active Directory (Azure AD) a été officiellement renommé **Microsoft Entra ID** le **1er octobre 2023**, afin de mieux refléter ses capacités multicloud et multiplateformes.

---

## Ce que Microsoft Entra ID permet

### Authentification
- Vérifier l'identité des utilisateurs

### Autorisation
- Contrôler l'accès aux ressources

### Single Sign-On (SSO)
- Une seule connexion pour accéder à plusieurs applications

---

## Ressources accessibles via Entra ID

- Microsoft 365
- Portail Azure
- Applications SaaS
- Applications internes
- Applications cloud personnalisées

---

## À retenir

Microsoft Entra ID n'est pas simplement un annuaire.

C'est une solution complète couvrant :

- La gestion des identités
- L'application de stratégies d'accès
- La sécurisation des données
- Les environnements cloud et on-premises

---

# Module 1 — Qu'est-ce que Microsoft Entra ID ?

## Définition

Microsoft Entra ID est un service cloud de gestion des identités et des accès.

Il permet :

- D'authentifier les utilisateurs
- D'autoriser l'accès aux ressources
- D'assurer le SSO
- De sécuriser les applications et les données

---

## Objectifs du cours

- Décrire Microsoft Entra ID et ses fonctionnalités clés
- Comparer Entra ID à Active Directory Domain Services (AD DS)
- Comprendre le rôle d'Entra ID comme annuaire pour les applications cloud
- Distinguer les offres Entra ID P1 et P2
- Explorer Microsoft Entra Domain Services

---

## Question de compréhension

**Quel était le nom d'Azure Active Directory avant le renommage officiel d'octobre 2023 ?**

### Réponse
Azure AD (Azure Active Directory)

---

# Module 2 — Entra ID vs Active Directory Domain Services

## Différence fondamentale

Microsoft Entra ID n'est pas une simple version cloud d'Active Directory Domain Services.

Ce sont deux produits distincts avec des architectures différentes.

---

## Comparaison AD DS vs Entra ID

| AD DS (On-premises) | Microsoft Entra ID |
|---|---|
| LDAP, Kerberos, NTLM | OAuth 2.0, OIDC, SAML |
| Jointure de domaine | Enregistrement d'appareil |
| Stratégies de groupe (GPO) | Accès conditionnel |
| Infrastructure gérée par l'entreprise | Service cloud géré par Microsoft |
| Contrôleurs de domaine sur site | Aucune infrastructure à gérer |
| Conçu pour les réseaux locaux | Conçu pour internet et le cloud |

---

## Structure des objets

### AD DS
- Forêts
- Domaines
- Unités d'organisation (OU)

### Entra ID
- Structure plate basée sur les tenants
- Pas de forêts
- Pas d'OU

---

## Types d'identités prises en charge

### AD DS
- Comptes utilisateurs
- Comptes ordinateurs

### Entra ID
- Utilisateurs internes
- Invités B2B
- Identités de charge de travail
- Applications et services
- Appareils Windows, macOS, iOS et Android

---

## Environnement hybride

Les organisations peuvent utiliser **Microsoft Entra Connect** pour synchroniser les utilisateurs et groupes d'AD DS vers Entra ID.

Cela permet de créer un environnement d'identité hybride.

---

## Question de compréhension

**Quel protocole Microsoft Entra ID utilise-t-il pour l'authentification moderne ?**

### Réponse
OAuth 2.0 / OpenID Connect

---

# Module 3 — Entra ID comme annuaire pour les applications cloud

## Rôle d'annuaire d'applications

Entra ID stocke et gère les identités d'application (App Registrations).

Cela permet aux applications de :

- S'authentifier
- Accéder à des ressources de façon sécurisée
- Utiliser des protocoles modernes

---

## Fonctionnalités principales

### Single Sign-On (SSO)
- Une seule authentification pour toutes les applications

### Intégration SaaS
- Applications pré-intégrées
- Salesforce
- Slack
- ServiceNow
- GitHub

### Applications personnalisées
- Applications web
- API
- Applications mobiles
- Intégration avec Microsoft Graph

---

## Types d'applications pris en charge

### Applications Microsoft 365
- Teams
- Outlook
- SharePoint
- OneDrive

### Applications SaaS tierces

La galerie Entra ID contient plus de 3 000 applications pré-intégrées.

### Applications métier personnalisées

Les applications peuvent utiliser :

- OAuth 2.0
- OpenID Connect
- MFA
- Accès conditionnel

---

## Proxy d'application

Le Proxy d'application permet de publier de façon sécurisée des applications locales sur internet sans :

- VPN
- DMZ

Les utilisateurs accèdent aux applications internes comme à des applications cloud.

---

## Question de compréhension

**Qu'est-ce que le Proxy d'application dans Microsoft Entra ID ?**

### Réponse
Un outil permettant de publier des applications locales de façon sécurisée sur internet sans VPN.

---

# Module 4 — Microsoft Entra ID : Éditions et licences

## Entra ID Gratuit

### Fonctionnalités incluses

- Gestion des utilisateurs et groupes
- SSO limité
- MFA basique
- Collaboration B2B

### Limitations

- Pas d'accès conditionnel
- Pas d'Identity Protection
- Pas de PIM

---

## Entra ID P1

### Inclus dans
- Microsoft 365 E3
- EMS E3
- Business Premium

### Fonctionnalités supplémentaires

- Accès conditionnel
- SSO illimité
- Identité hybride
- Groupes dynamiques
- Réinitialisation de mot de passe self-service

---

## Entra ID P2

### Inclus dans
- Microsoft 365 E5
- EMS E5

### Fonctionnalités supplémentaires

- Identity Protection
- Privileged Identity Management (PIM)
- Access Reviews
- Détection des risques
- Gouvernance des identités

---

## Identity Protection

Identity Protection utilise l'intelligence artificielle pour détecter :

- Les connexions inhabituelles
- Les fuites de mots de passe
- Les IP suspectes
- Les appareils compromis

Il peut bloquer automatiquement les accès à risque.

---

## Privileged Identity Management (PIM)

PIM permet :

- L'attribution temporaire des rôles administrateurs
- L'administration juste-à-temps (JIT)
- La réduction des comptes administrateurs permanents
- L'audit des élévations de privilèges

---

## Question de compréhension

**Quelle fonctionnalité permet d'attribuer des droits d'administration temporaires et juste-à-temps ?**

### Réponse
Privileged Identity Management (PIM)

---

# Module 5 — Microsoft Entra Domain Services

## Objectif

Certaines applications héritées nécessitent encore :

- LDAP
- Kerberos
- NTLM
- GPO

Microsoft Entra Domain Services fournit ces fonctionnalités dans Azure sans gérer de contrôleurs de domaine.

---

## Définition

Microsoft Entra Domain Services est un service Azure managé fournissant un domaine compatible Active Directory.

Microsoft gère :

- Les contrôleurs de domaine
- Les mises à jour
- Les sauvegardes
- La réplication

---

## Protocoles pris en charge

- LDAP
- Kerberos
- NTLM
- Stratégie de groupe (GPO)
- Jointure de domaine

---

## Fonctionnalités principales

### Synchronisation
- Synchronisation unidirectionnelle depuis Entra ID

### Service managé
- Microsoft gère l'infrastructure

### Migration
- Permet de migrer des applications héritées vers Azure

---

## Cas d'usage

### Migration d'applications héritées

Les applications utilisant LDAP ou Kerberos peuvent être migrées vers Azure.

### Remplacement de l'infrastructure AD locale

Les entreprises peuvent réduire leur dépendance aux serveurs AD on-premises.

### Environnements hybrides

Les utilisateurs utilisent leurs identifiants Entra ID sur des machines jointes au domaine managé.

---

## Limites importantes

Entra Domain Services ne permet pas :

- D'étendre le schéma
- De créer des forêts complexes
- De créer des trusts complexes
- D'accéder directement aux contrôleurs de domaine

C'est un service entièrement managé.

---

# Résumé global

L'écosystème Microsoft Entra permet de couvrir tous les besoins d'identité modernes :

| Composant | Rôle |
|---|---|
| Microsoft Entra ID | Gestion des identités cloud modernes |
| Entra Connect | Synchronisation hybride |
| Entra Domain Services | Support des applications héritées |

---

# Conseils d'étude

- Comprendre le rôle de Entra ID dans Azure et Microsoft 365
- Comparer AD DS et Entra ID
- Étudier les protocoles modernes (OAuth 2.0, OIDC, SAML)
- Comprendre les différences entre P1 et P2
- Étudier les usages de Conditional Access, MFA et PIM
- Comprendre les scénarios hybrides

---

# Glossaire

| Terme | Définition |
|---|---|
| IAM | Identity and Access Management |
| MFA | Multi-Factor Authentication |
| SSO | Single Sign-On |
| OIDC | OpenID Connect |
| OAuth 2.0 | Protocole d'autorisation moderne |
| LDAP | Lightweight Directory Access Protocol |
| Kerberos | Protocole d'authentification réseau |
| PIM | Privileged Identity Management |
| GPO | Group Policy Object |
| SaaS | Software as a Service |

---

# Fin du cours

