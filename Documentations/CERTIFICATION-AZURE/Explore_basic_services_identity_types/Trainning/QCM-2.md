Très bon choix : une **2e série de QCM orientée “scénarios” + un résumé ultra‑synthétique d’une page** pour le module *Microsoft Learn: Explore basic services – identity types*.  

***

## Série 2 – QCM orienté scénarios (10 questions)

1. Une entreprise a un AD local et utilise Microsoft Entra ID pour ses utilisateurs cloud. Les comptes sont créés dans AD DS, puis automatiquement synchronisés dans Entra ID. Comment appelle‑t‑on ce type d’identité ?  
   a) Identité cloud uniquement  
   b) Identité hybride  
   c) Identité externe  
   d) Identité d’agent IA  

2. Un développeur déploie une application Azure Function qui doit lire des secrets dans Azure Key Vault sans mot de passe ni secret. Quelle solution d’identité est la plus appropriée ?  
   a) Compte utilisateur spécifique  
   b) Principal de service avec secret  
   c) Identité managée (managed identity)  
   d) Identité d’appareil  

3. Une entreprise veut permettre à ses clients grand public de s’inscrire et de se connecter à une application web (gestion de compte client). Quel type d’identité / service doit‑elle utiliser ?  
   a) Identité hybride  
   b) Azure AD B2B  
   c) Azure AD B2C  
   d) Identité d’appareil  

4. Une équipe de développement crée un “bot” IA qui automatise des workflows dans Microsoft 365. Comment doit‑elle modéliser l’identité de ce bot dans Microsoft Entra ID ?  
   a) Comme un utilisateur classique  
   b) Comme un appareil  
   c) Comme une identité d’agent IA (Microsoft Entra Agent ID)  
   d) Comme un principal de service  

5. Une entreprise utilise Intune et Azure AD. Ses salariés s’authentifient sur leurs PC Windows, qui sont gérés dans Entra ID. Quel type d’identité est principalement utilisé pour ces PC ?  
   a) Identité utilisateur  
   b) Identité d’appareil  
   c) Identité de service  
   d) Identité externe  

6. Un partenaire de l’entreprise doit accéder ponctuellement à un portail SharePoint. L’IT ne veut pas lui créer un compte employé permanent. Comment doit‑il être géré dans Entra ID ?  
   a) Identité hybride  
   b) Identité locale  
   c) Identité d’invité (Azure AD B2B)  
   d) Identité d’agent IA  

7. Une application web Azure utilise une identité managée affectée par le système pour accéder à une base de données. Que se passe‑t‑il si la ressource Azure est supprimée ?  
   a) L’identité managée reste active et peut être réutilisée  
   b) L’identité managée est aussi supprimée  
   c) L’identité devient une identité d’utilisateur  
   d) L’identité devient une identité hybride  

8. Une PME ne dispose que d’un AD local et souhaite intégrer Office 365. Les comptes sont synchronisés dans Microsoft Entra ID via un outil installé en local. De quel outil s’agit‑il ?  
   a) Azure AD B2B  
   b) Azure AD B2C  
   c) Azure AD Connect  
   d) Microsoft Entra External ID  

9. Vous configurez une API hébergée dans Azure qui doit être appelée uniquement par une application interne. L’application doit s’authentifier auprès de l’API sans mot de passe. Quelle approche est la plus recommandée ?  
   a) Compte utilisateur partagé  
   b) Principal de service / identité de service  
   c) Identité d’appareil  
   d) Identité hybride  

10. Vous concevez une solution IAM pour un environnement cloud‑centric où tous les comptes sont créés directement dans Microsoft Entra ID, sans AD local. Comment qualifiez‑vous ce modèle d’identité ?  
    a) Modèle hybride  
    b) Modèle cloud‑seul  
    c) Modèle B2B  
    d) Modèle d’identité d’agent  

***

## Corrections rapides (sans tout détailler, tu peux demander les explications si besoin)

1. **b) Identité hybride** [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/3-describe-identity-types)
2. **c) Identité managée (managed identity)** [varonis](https://www.varonis.com/fr/blog/azure-managed-identities)
3. **c) Azure AD B2C** [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/7-summary-resources)
4. **c) Identité d’agent IA (Microsoft Entra Agent ID)** [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/explore-basic-services-identity-types/)
5. **b) Identité d’appareil** [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/3-describe-identity-types)
6. **c) Identité d’invité (Azure AD B2B)** [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/7-summary-resources)
7. **b) L’identité managée est aussi supprimée** (system‑assigned) [varonis](https://www.varonis.com/fr/blog/azure-managed-identities)
8. **c) Azure AD Connect** [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/3-describe-identity-types)
9. **b) Principal de service / identité de service** [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/3-describe-identity-types)
10. **b) Modèle cloud‑seul** [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/)

Si tu veux, je peux détailler les explications pour chaque question.

***

## Fiches de révision synthétiques – 1 page

Voici un **résumé ultra‑condensé** destiné à tenir sur une “page” de révision (tu peux le copier‑coller dans un OneNote ou un PDF).

### 1. Fonction de Microsoft Entra ID
- Service d’identité et d’accès cloud pour Azure, M365, SaaS, etc. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/explore-basic-services-identity-types/)
- Gestion centralisée : authentification, autorisation, rôles, politiques d’accès. [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/)

### 2. Types d’identité clés
- **Utilisateur** : employé, collaborateur (interactive sign‑in). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/explore-basic-services-identity-types/)
- **Service / principal de service** : application, démon, API. [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/3-describe-identity-types)
- **Identité managée** :  
  - Affectée par le système : liée à une ressource, supprimée avec elle. [varonis](https://www.varonis.com/fr/blog/azure-managed-identities)
  - Affectée par l’utilisateur : réutilisable sur plusieurs ressources. [varonis](https://www.varonis.com/fr/blog/azure-managed-identities)
- **Appareil** : PC, mobile, IoT enregistré dans Entra (via Intune, AAD Join…). [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/3-describe-identity-types)
- **Hybride** : comptes créés dans AD DS local, synchronisés vers Entra ID via **Azure AD Connect**. [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/7-summary-resources)
- **Externe** : invités via **Azure AD B2B** ; clients via **Azure AD B2C** (Microsoft Entra External ID). [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/7-summary-resources)
- **Agent IA** : **Microsoft Entra Agent ID**, pour bots / workflows automatisés. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/explore-basic-services-identity-types/)

### 3. Scoops “scénarios” à retenir
- **AD local + Azure / M365** → identité hybride + Azure AD Connect. [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/7-summary-resources)
- **Partenaire qui accède ponctuellement** → Azure AD B2B (invité). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/explore-basic-services-identity-types/)
- **Clients grand public (inscriptions)** → Azure AD B2C. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/explore-basic-services-identity-types/)
- **Application qui appelle une API sans secret** → identité managée ou principal de service. [varonis](https://www.varonis.com/fr/blog/azure-managed-identities)
- **Bot / IA automatisée** → identité d’agent IA (Microsoft Entra Agent ID). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/explore-basic-services-identity-types/)

***

Si tu veux, je peux aussi te générer une **version “fiche A4”** (format texte prêt à imprimer) ou une **version PDF** structurée (en texte Markdown/CSS, que tu peux copier dans un outil de conversion).