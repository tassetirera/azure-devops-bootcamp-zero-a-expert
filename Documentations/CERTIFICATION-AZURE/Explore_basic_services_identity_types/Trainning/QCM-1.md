# QCM + corrections détaillées pour t’entraîner sur le module *“Explore basic services: identity types”* (Microsoft Learn)

***

## QCM (10 questions)

1. **Quelle est la fonction principale de Microsoft Entra ID ?**  
   a) Héberger des applications web dans le cloud  
   b) Gérer les identités et les accès aux applications, services et données  
   c) Gérer uniquement le stockage Azure  
   d) Remplacer complètement Active Directory local  

2. **Quel type d’identité est associé à un employé qui se connecte à une application SaaS ?**  
   a) Identité de service (principal de service)  
   b) Identité d’appareil  
   c) Identité utilisateur  
   d) Identité d’agent IA  

3. **Quelle identité est utilisée pour une application Azure qui appelle une API ?**  
   a) Identité utilisateur  
   b) Identité d’appareil  
   c) Principal de service / identité de service  
   d) Identité B2C  

4. **Que permet une identité managée affectée par le système ?**  
   a) Être partagée sur plusieurs ressources Azure  
   b) Être créée séparément de toute ressource  
   c) Être liée à une ressource spécifique et supprimée si la ressource est détruite  
   d) Être utilisée uniquement pour les utilisateurs externes  

5. **Dans un scénario hybride, où sont créés les comptes utilisateurs par défaut ?**  
   a) Directement dans Microsoft Entra ID  
   b) Dans Active Directory DS local  
   c) Dans Azure AD B2C  
   d) Dans Azure AD B2B  

6. **Quel service permet d’inviter un partenaire externe dans Microsoft Entra ID ?**  
   a) Azure AD Connect  
   b) Microsoft Entra External ID (Azure AD B2B)  
   c) Microsoft Entra Agent ID  
   d) Azure Key Vault  

7. **Quelle identité gère les appareils (PC, mobiles) enregistrés dans l’environnement ?**  
   a) Identité utilisateur  
   b) Identité d’appareil  
   c) Identité de service  
   d) Identité d’agent IA  

8. **Quel type d’identité est utilisé pour un agent IA (bot, workflow automatisé) dans Microsoft Entra ID ?**  
   a) Identité utilisateur  
   b) Identité d’appareil  
   c) Identité d’agent IA (Microsoft Entra Agent ID)  
   d) Identité managée  

9. **Quel outil est utilisé pour synchroniser Active Directory DS local avec Microsoft Entra ID ?**  
   a) Azure AD B2B  
   b) Azure AD B2C  
   c) Azure AD Connect  
   d) Microsoft Intune  

10. **Quand parle‑t‑on d’identité “hybride” dans Microsoft Entra ID ?**  
    a) Quand tout est uniquement dans le cloud  
    b) Quand les comptes sont créés dans AD local et synchronisés vers Microsoft Entra ID  
    c) Quand on utilise uniquement des identités externes  
    d) Quand on utilise uniquement des identités d’agent IA  

***

## Corrections détaillées

1. **b) Gérer les identités et les accès aux applications, services et données**  
   - Microsoft Entra ID est le service d’identité et d’accès centralisé de Microsoft (authentification, autorisation, gestion des utilisateurs, appareils, invités). [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/)

2. **c) Identité utilisateur**  
   - Un employé qui se connecte représente une **identité utilisateur** ; elle est utilisée pour l’authentification interactive. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/explore-basic-services-identity-types/)

3. **c) Principal de service / identité de service**  
   - Une application Azure qui appelle une API utilise un **principal de service** ou une **identité managée** (service identity) pour s’authentifier auprès de la ressource. [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/3-describe-identity-types)

4. **c) Être liée à une ressource spécifique et supprimée si la ressource est détruite**  
   - L’identité managée **affectée par le système** est liée à une seule ressource Azure et est supprimée automatiquement si la ressource est détruite. [varonis](https://www.varonis.com/fr/blog/azure-managed-identities)

5. **b) Dans Active Directory DS local**  
   - Dans un scénario hybride, les comptes sont créés dans **Active Directory Domain Services (AD DS)** local, puis synchronisés vers Microsoft Entra ID via Azure AD Connect. [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/7-summary-resources)

6. **b) Microsoft Entra External ID (Azure AD B2B)**  
   - Microsoft Entra External ID permet d’inviter des utilisateurs externes (partenaires, clients) via **Azure AD B2B**. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/explore-basic-services-identity-types/)

7. **b) Identité d’appareil**  
   - Chaque PC ou mobile inscrit ou rejoint Entra (via Intune, AAD Join, Hybrid AD Join) obtient une **identité d’appareil**. [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/3-describe-identity-types)

8. **c) Identité d’agent IA (Microsoft Entra Agent ID)**  
   - Microsoft Entra Agent ID gère les identités des agents IA (bots, workflows, assistants IA) pour sécuriser et auditer leurs actions. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/explore-basic-services-identity-types/)

9. **c) Azure AD Connect**  
   - **Azure AD Connect** est l’outil utilisé pour synchroniser les comptes AD local avec Microsoft Entra ID. [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/7-summary-resources)

10. **b) Quand les comptes sont créés dans AD local et synchronisés vers Microsoft Entra ID**

- On parle d’**identité hybride** lorsque les utilisateurs sont gérés dans AD local et synchronisés vers Entra ID, tout en gardant les deux environnements. [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/3-describe-identity-types)

***

Si tu veux, je peux te préparer :  

- une **deuxième série de QCM** (plus orientée “scénarios”)  
- ou des **fiches de révision plus synthétiques** (type résumé de 1 page) pour le module.
