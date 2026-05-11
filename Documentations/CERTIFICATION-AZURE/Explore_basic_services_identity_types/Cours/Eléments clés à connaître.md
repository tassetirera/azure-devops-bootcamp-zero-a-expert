Le module Microsoft Learn **“Explore basic services: identity types”** (français: **“Décrire les types de fonction et d’identité de Microsoft Entra ID”**) couvre les bases de la gestion d’identités dans Microsoft Entra ID. [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/)

Voici **tous les éléments clés** à connaître dans ce cours.

***

### 1. Présentation de Microsoft Entra ID  

- Microsoft Entra ID est la solution cloud de gestion des identités et des accès qui connecte les utilisateurs à leurs applications, appareils et données. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/explore-basic-services-identity-types/)
- Les organisations utilisent l’ID Microsoft Entra pour permettre à leurs employés, invités, charges de travail et agents IA de se connecter et d’accéder aux ressources dont elles ont besoin, notamment :

  - Ressources internes telles que les applications situées sur votre réseau d’entreprise et intranet, ainsi que les applications cloud développées par votre propre organisation.
  - Services externes, tels que Microsoft 365, le portail Azure et toutes les applications SaaS utilisées par votre organisation.

- Microsoft Entra ID simplifie la façon dont les organisations gèrent les autorisations et les accès en fournissant un seul système d’identité pour leurs applications cloud et locales. Vous pouvez synchroniser Microsoft Entra ID avec votre instance Active Directory locale et avec d’autres services d’annuaire ou l’utiliser en tant que service autonome.

- Microsoft Entra ID permet également aux organisations d’autoriser l’utilisation d’appareils personnels, tels que des appareils mobiles et des tablettes, et d’autoriser la collaboration avec les partenaires commerciaux et les clients.

- Objectif pédagogique : comprendre la fonction globale de Microsoft Entra ID dans un environnement cloud (Azure, M365, etc.). [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/7-summary-resources)

***

### 2. Types d’identités pris en charge  
Le module détaille plusieurs catégories d’identités : [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/3-describe-identity-types)

- **Identités utilisateur** : comptes utilisateurs gérés dans Microsoft Entra ID (internes, employés, etc.).  
- **Identités de charge de travail (service principals / managed identities)** :
(une **charge de travail** est un ensemble de ressources qui travaillent ensemble pour atteindre un objectif métier commun : application, API, base de données, stockage, réseau et opérations associées.)  
  - Principaux de service : identité d’une application ou d’un service. [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/3-describe-identity-types)
  - Identités managées (managed identities) :  
    - Affectées par le système (system-assigned).  
    - Affectées par l’utilisateur (user-assigned). [varonis](https://www.varonis.com/fr/blog/azure-managed-identities)
- **Identités d’appareil** : machines, mobiles, etc., qui possèdent une identité gérée dans Entra. [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/3-describe-identity-types)
- **Identités hybrides** : sync AD DS local → Microsoft Entra ID (on‑premises + cloud). [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/7-summary-resources)
- **Identités externes** : invités / partenaires via Microsoft Entra External ID (B2B, B2C). [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/)
- **Identités d’agent (Agent ID)** : nouvelles identités pour les agents IA, utilisées pour sécuriser les interactions automatisées. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/explore-basic-services-identity-types/)

***

### 3. Identité hybride  
- Tous les comptes utilisateurs sont gérés dans AD DS local, puis synchronisés vers Microsoft Entra ID via Azure AD Connect. [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/7-summary-resources)
- Scénarios courants :  
  - Authentification hybride (pass‑through, fédération).  
  - Single‑sign‑on (SSO) entre on‑premises et cloud. [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/7-summary-resources)

***

### 4. Identités externes et Microsoft Entra External ID  
- Permet d’inviter des utilisateurs externes (partenaires, clients) dans Microsoft Entra ID. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/explore-basic-services-identity-types/)
- Cas d’usage :  
  - Accès en tant qu’invité (Azure B2B).  
  - Scénarios B2C (inscription / authentification de clients finaux). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/explore-basic-services-identity-types/)

***

### 5. Principaux concepts techniques à maîtriser  
- **Principal de service** : rôle d’application dans Microsoft Entra ID, utilisé pour l’authentification et l’autorisation. [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/3-describe-identity-types)
- **Identités managées** :  
  - Suppression automatique quand la ressource est détruite (système).  
  - Recyclables sur plusieurs ressources (user‑assigned). [varonis](https://www.varonis.com/fr/blog/azure-managed-identities)
- **Séparation des rôles** :  
  - Utilisateur vs appareil vs service.  
  - Local vs cloud vs hybride. [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/3-describe-identity-types)

***

### 6. Objectifs d’apprentissage du module  
À la fin de ce cours, tu dois pouvoir : [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/)

- Décrire la fonction de Microsoft Entra ID.  
- Lister et expliquer les types d’identités (utilisateur, service, appareil, agent IA, hybride, externe).  
- Expliquer le concept d’identité hybride.  
- Décrire le rôle d’**Microsoft Entra Agent ID** pour les agents IA.  
- Résumer les identités externes via **Microsoft Entra External ID**.  

***

Si tu veux, je peux te préparer un **résumé en fiches** (一张 par type d’identité) ou un **QCM** pour t’entraîner avant de passer l’évaluation du module.