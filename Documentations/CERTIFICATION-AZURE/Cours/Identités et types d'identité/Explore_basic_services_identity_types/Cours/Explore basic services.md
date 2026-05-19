Parfait, je vais te préparer :
- **Un résumé en fiches** (une par type d’identité) inspiré du module *“Explore basic services: identity types”* de Microsoft Learn.  
- **Un QCM d’entraînement** (10 questions) pour réviser.  

***

## Résumé en fiches (1 par type d’identité)

### Fiche 1 : Microsoft Entra ID (fonction globale)  
- Serveur d’identité cloud qui gère l’accès aux applications, services et données (Azure, M365, SaaS, etc.). [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/)
- Permet de centraliser l’authentification, l’autorisation et la gestion des identités (employés, applications, appareils, invités). [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/7-summary-resources)

***

### Fiche 2 : Identités utilisateur  
- Identités associées à des personnes (employés, stagiaires, etc.) dans Microsoft Entra ID. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/explore-basic-services-identity-types/)
- Peuvent être créées directement dans le cloud ou synchronisées depuis un AD local (AD DS + Azure AD Connect). [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/3-describe-identity-types)

***

### Fiche 3 : Identités de charge de travail (service principals / managed identities)  
- **Principal de service** : identité d’une application ou d’un service pour s’authentifier auprès d’API ou de ressources Azure. [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/3-describe-identity-types)
- **Identités managées** :  
  - Affectées par le système : liées à une ressource Azure, supprimées si la ressource est détruite. [varonis](https://www.varonis.com/fr/blog/azure-managed-identities)
  - Affectées par l’utilisateur : gérées séparément, réutilisables sur plusieurs ressources. [varonis](https://www.varonis.com/fr/blog/azure-managed-identities)

***

### Fiche 4 : Identités d’appareil  
- Chaque appareil (PC, serveur, mobile) peut avoir une identité Entra gérée via Intune, Azure AD Join, Hybrid AD Join, etc. [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/3-describe-identity-types)
- Permet d’appliquer des stratégies d’accès basées sur l’appareil (ex : impossible d’accéder à certains services depuis un appareil non géré). [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/7-summary-resources)

***

### Fiche 5 : Identités hybrides  
- Comptes créés dans Active Directory DS local, puis synchronisés vers Microsoft Entra ID via **Azure AD Connect**. [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/7-summary-resources)
- Permet d’avoir un modèle unique pour les utilisateurs tout en gardant l’AD on‑premises comme source d’autorité. [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/7-summary-resources)

***

### Fiche 6 : Identités externes (Microsoft Entra External ID)  
- Gère les accès des **invités** (partenaires, clients) via **Azure AD B2B**. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/explore-basic-services-identity-types/)
- Permet aussi des scénarios **B2C** (clients finaux qui s’inscrivent et se connectent à des applications publiques). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/explore-basic-services-identity-types/)

***

### Fiche 7 : Identités d’agent IA (Microsoft Entra Agent ID)  
- Nouveau type d’identité pour les **agents IA** (workflows automatisés, bots, assistants IA). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/explore-basic-services-identity-types/)
- Permet de sécuriser et tracer les actions exécutées par les agents (permissions, audit, etc.). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/explore-basic-services-identity-types/)

***

### Fiche 8 : Points clés à retenir pour l’examen  
- Différence entre **identité utilisateur**, **identité de service**, **identité d’appareil** et **identité d’agent**. [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/3-describe-identity-types)
- Comprendre le rôle de **Microsoft Entra ID** dans Azure, M365 et la gestion des identités hybrides/externes. [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/)
- Savoir reconnaître les usages d’**Azure AD Connect** (sync on‑premises → cloud) et d’**Azure AD B2B/B2C**. [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/7-summary-resources)

***

## QCM d’entraînement (module *“Explore basic services: identity types”*)

Voici un **QCM de 10 questions** (choix multiples) pour t’entraîner. Réponds dans ta tête, puis je te donnerai les corrections et explications.

1. Quelle est la fonction principale de Microsoft Entra ID ?  
2. Quel type d’identité est associé à un employé qui se connecte à une application SaaS ?  
3. Quelle identité est utilisée pour une application Azure qui appelle une API ?  
4. Que permet une identité managée affectée par le système ?  
5. Dans un scénario hybride, où sont créés les comptes utilisateurs par défaut ?  
6. Quel service permet d’inviter un partenaire externe dans Microsoft Entra ID ?  
7. Quelle identité gère les appareils (PC, mobiles) enregistrés dans l’environnement ?  
8. Quel type d’identité est utilisé pour un agent IA (bot, workflow automatisé) dans Microsoft Entra ID ?  
9. Quel outil est utilisé pour synchroniser Active Directory DS local avec Microsoft Entra ID ?  
10. Quand parle‑t‑on d’identité “hybride” dans Microsoft Entra ID ?

***

Souhaites‑tu que je :  
- **Propose les réponses (QCM + corrections détaillées)** maintenant, **ou**  
- D’abord que tu essaies de répondre toi‑même, puis je t’envoie les corrections et une deuxième série de QCM ?