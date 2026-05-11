# À connaître absolument – Microsoft Entra ID

Cette fiche présente les termes clés de Microsoft Entra ID, leurs définitions et des suggestions pour bien comprendre le service.

---

## 1. Concepts fondamentaux

### Microsoft Entra ID
Service cloud de gestion des identités et des accès (IAM) de Microsoft. Il authentifie les utilisateurs, contrôle les accès aux ressources et permet l’intégration avec Azure, Microsoft 365 et des applications SaaS.

### IAM (Identity and Access Management)
Ensemble de fonctions pour gérer qui peut se connecter, à quoi ils ont accès, et comment les autorisations sont accordées ou révoquées.

### Tenant
Instance isolée de Microsoft Entra ID associée à une organisation. Chaque tenant a son propre annuaire d’identités et de rôles.

### Subscription (abonnement)
Conteneur de facturation Azure qui appartient à un tenant. Une subscription peut être liée à un seul tenant.

### Domaine personnalisé
Nom de domaine que l’organisation ajoute à Entra ID, par exemple `contoso.com`, pour remplacer le domaine par défaut `*.onmicrosoft.com`.

### Azure Portal
Interface web où l’on configure Microsoft Entra ID, les applications, les stratégies et les rôles.

---

## 2. Types d’identités

### Utilisateur (User)

Compte représentant une personne. Il peut être de type :

- `Member` : employé interne ou compte géré par l’organisation.

    - `Membre interne` : ces utilisateurs sont souvent considérés comme des employés de votre organisation. L’utilisateur s’authentifie en interne via l’instance Microsoft Entra ID de son organisation et l’objet utilisateur créé dans le répertoire Microsoft Entra de la ressource a un UserType de Membre.
    - `Membre externe` : Ce scénario est courant dans les organisations avec plusieurs locataires. Par exemple, si les locataires Contoso et Fabrikam Microsoft Entra se trouvent dans une grande organisation, les utilisateurs de Contoso peuvent être configurés dans l’annuaire Fabrikam Microsoft Entra pour s’authentifier auprès de leur compte Contoso (externe à Fabrikam), mais disposent d’un UserType de membre, ce qui permet l’accès au niveau du membre aux ressources de Fabrikam.

    
- `Guest` : invité externe invité à collaborer via Azure B2B.
    - `Invité externe` : les utilisateurs ou invités externes (notamment des consultants, des fournisseurs et des partenaires) appartiennent généralement à cette catégorie. L’utilisateur s’authentifie à l’aide d’un compte Microsoft Entra externe ou d’un fournisseur d’identité externe (par exemple, une identité sociale) et son objet utilisateur a un UserType d’invité.

    
    - `Invité interne` : ce scénario existe lorsque les organisations configurent des comptes Microsoft Entra internes pour des utilisateurs externes tels que des distributeurs ou des fournisseurs, mais les désignent en tant qu’invités en définissant l’objet utilisateur UserType sur Invité. Il s’agit d’un scénario hérité, car il est désormais plus courant d’utiliser B2B Collaboration, où les utilisateurs peuvent utiliser leurs propres informations d’identification.
### Groupe
Conteneur logique qui regroupe des utilisateurs, des appareils ou des applications. Utilisé pour attribuer des rôles ou appliquer des stratégies à plusieurs identités en même temps.

### Application
Enregistrement d’application dans Entra ID. Permet de gérer l’accès et l’authentification des applications cloud ou internes.

### Principal de service (Service Principal)
Identité créée dans le tenant pour représenter une application ou un service dans l’authentification et l’autorisation.

### Identité managée (Managed Identity)
Identité gérée automatiquement par Azure pour une ressource. Elle simplifie l’accès aux services Azure sans stocker de secrets.
- `System-assigned` : créée pour une seule ressource et supprimée avec elle.
- `User-assigned` : créée séparément et peut être partagée entre plusieurs ressources.

### Identité d’appareil
Identité assignée à un appareil (PC, mobile, IoT) pour l’enregistrement ou l’authentification auprès d’Entra ID.

### Identité hybride
Identité synchronisée entre un Active Directory local (AD DS) et Entra ID. Permet aux utilisateurs et aux appareils on-premises de se connecter au cloud.

### Identité externe (External ID)
Identité de partenaire ou de client invitée via Microsoft Entra External ID, souvent utilisée pour les scénarios B2B et B2C.

### Identité d’agent (Agent ID)
Identité conçue pour les agents IA ou les workflows automatisés, permettant de sécuriser les interactions programmatiques.

---

## 3. Authentification et accès

### Authentication (authentification)
Processus de vérification de l’identité d’un utilisateur ou d’une application.

### Authorization (autorisation)
Processus de vérification des actions qu’une identité est autorisée à effectuer.

### SSO (Single Sign-On)
Fonctionnalité permettant à un utilisateur de s’authentifier une seule fois pour accéder à plusieurs applications.

### MFA (Multi-Factor Authentication)
Méthode de sécurité qui demande deux facteurs ou plus pour s’authentifier (mot de passe + téléphone, application, code SMS, etc.).

### Conditional Access
Stratégies qui contrôlent l’accès aux ressources en fonction de conditions comme l’emplacement, l’état de l’appareil, le groupe utilisateur, le type d’application, etc.

### Identity Protection
Service qui détecte et répond aux risques d’identité (connexions suspectes, utilisateurs compromis, attaques par force brute).

### PIM (Privileged Identity Management)
Gestion des rôles à privilèges élevés : activation temporaire, approbation, notifications et journalisation pour les rôles administratifs.

---

## 4. Protocoles et technologies

### OAuth 2.0
Protocole d’autorisation utilisé pour permettre aux applications d’accéder aux ressources au nom d’un utilisateur.

### OpenID Connect (OIDC)
Extension de OAuth 2.0 qui ajoute l’authentification. Permet à une application d’obtenir des informations sur l’utilisateur.

### SAML
Protocole d’authentification fédérée utilisé principalement pour SSO avec des applications d’entreprise.

### WS-Federation
Ancien protocole de fédération, encore utilisé dans certains scénarios legacy.

### LDAP, Kerberos, NTLM
Protocoles associés à AD DS on-premises. Entra ID utilise plutôt OAuth, OIDC et SAML pour le cloud.

---

## 5. Gestion des rôles et des accès

### RBAC (Role-Based Access Control)
Contrôle d’accès basé sur des rôles Azure. Permet d’attribuer des rôles comme `Reader`, `Contributor`, `Owner` à des utilisateurs, groupes ou identités de service.

### Rôles Entra ID vs rôles Azure
- Rôles Entra ID : administratifs pour la gestion du tenant et des identités (Global Admin, User Administrator, Security Reader...).
- Rôles Azure : contrôlent l’accès aux ressources Azure (VM, stockage, réseaux, etc.).

### Rôles privilégiés
- `Global Administrator` : administrateur principal du tenant Entra ID.
- `User Administrator` : gère les comptes utilisateurs.
- `Security Administrator` : gère les paramètres de sécurité et les stratégies.

---

## 6. Scénarios importants

### Azure AD Join
Inscription d’un appareil Windows directement dans Entra ID.

### Hybrid Azure AD Join
Appareils Windows joints à un domaine AD local et enregistrés dans Entra ID.

### Azure AD Connect
Outil de synchronisation entre AD DS local et Entra ID. Permet de synchroniser les comptes, les mots de passe et les attributs.

### Pass-through Authentication
Méthode hybride où les utilisateurs s’authentifient dans Entra ID mais la vérification des mots de passe est réalisée via l’infrastructure locale.

### Fédérations
Permet à Entra ID d’utiliser un fournisseur d’identité local (comme ADFS) pour authentifier les utilisateurs.

### Azure B2B
Collaboration externe : invitation de partenaires pour accéder aux ressources de l’organisation.

### Azure B2C
Gestion d’identité des clients finaux (consommateurs) avec des scénarios d’inscription et de connexion personnalisés.

---

## 7. Termes à connaître absolument

- `Tenant` : instance dédiée Entra ID.
- `Subscription` : unité de facturation Azure liée à un tenant.
- `User` : compte personnel ou employé.
- `Guest` : utilisateur externe invité.
- `Group` : ensemble de membres pour simplifier l’attribution de droits.
- `Service Principal` : identité d’application.
- `Managed Identity` : identité gérée par Azure pour un service.
- `SSO` : authentification unique.
- `MFA` : authentification multi-facteurs.
- `Conditional Access` : règles d’accès selon le contexte.
- `RBAC` : contrôle d’accès basé sur les rôles.
- `Azure AD Join` : inscription d’un appareil au cloud.
- `Hybrid Azure AD Join` : appareil lié à AD local + Entra ID.
- `Azure AD Connect` : synchronisation AD locale → Entra ID.
- `External ID` : identités externes B2B/B2C.
- `Agent ID` : identité pour les agents IA.
- `Identity Protection` : détection des risques d’identité.
- `PIM` : gestion des privilèges élevés.

---

## 8. Comparaison rapide

### AD DS vs Microsoft Entra ID
- AD DS : service local, Domain Controllers, LDAP/Kerberos/NTLM.
- Entra ID : service cloud, OAuth/OIDC/SAML, accès aux applications cloud.

### Identité d’utilisateur vs identité de service
- Utilisateur : personne qui se connecte.
- Service : application ou ressource qui s’authentifie sans personne.

### Service Principal vs Managed Identity
- Service Principal : identité de l’application gérée par le tenant.
- Managed Identity : identité gérée entièrement par Azure pour des ressources spécifiques.

---

## 9. Suggestions d’étude

- Comprendre le rôle de Entra ID dans Azure et Microsoft 365.
- Mémoriser les différences entre AD DS, Entra ID et les identités hybrides.
- Savoir quand utiliser `Service Principal` vs `Managed Identity`.
- Étudier les usages de `Conditional Access`, `MFA` et `PIM`.
- Pratiquer la création de : utilisateur, groupe, application, service principal, identité managée.
- Lire les définitions dans le portail Azure : tenant, domaine, subscription et rôles.
- Réviser les protocoles : OAuth 2.0, OpenID Connect, SAML.
- Comparer les rôles Entra ID et les rôles Azure RBAC.
- Retenir que “un abonnement Azure appartient à un seul tenant”.
- Se souvenir que les invités externes sont des `Guest`, pas des `Member`.

---

## 10. Conseils pratiques pour l’examen

- Si on te demande « qu’est-ce que Entra ID ? », répond : « le service cloud Microsoft d’IAM, qui authentifie, autorise et connecte les utilisateurs, appareils et applications. »
- Si on te demande « que gère un tenant ? », cite : utilisateurs, groupes, applications, rôles, stratégies et abonnements.
- Si on te demande « quelle identité utiliser pour un service Azure ? », répond : `Managed Identity` si possible, sinon `Service Principal`.
- Si on te demande « quelle différence entre Global Admin et Owner Azure ? », répond : Global Admin gère le tenant Entra ID, Owner contrôle les ressources Azure.
- Prends toujours l’option la plus sécurisée : `MFA`, `Conditional Access`, `Managed Identity`.

---

## 11. Rappels

- Microsoft Entra ID = ancien Azure Active Directory.
- Entra ID ne remplace pas immédiatement AD DS, mais il complète et modernise l’identité.
- La synchronisation hybride est fréquente dans les entreprises qui migrent progressivement vers le cloud.
- Entra ID est le cœur de l’authentification dans Azure, Microsoft 365 et bien d’autres applications SaaS.
