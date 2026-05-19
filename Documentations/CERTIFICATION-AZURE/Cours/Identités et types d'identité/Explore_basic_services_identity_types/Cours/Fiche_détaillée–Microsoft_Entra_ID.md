# Fiche détaillée – Microsoft Entra ID (Azure AD) pour AZ-104

Source du module :
[Microsoft Learn – Describe Azure Active Directory](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/2-describe-azure-active-directory?utm_source=chatgpt.com)

---

# 1. Microsoft Entra ID (ancien Azure AD)

## Définition

Microsoft Entra ID est un service cloud de gestion des identités et des accès (*Identity and Access Management – IAM*).

Il permet :

* d’authentifier les utilisateurs
* de contrôler les accès
* de sécuriser les ressources Azure
* de connecter les utilisateurs aux applications Microsoft 365 et SaaS

C’est le “centre d’identité” du cloud Microsoft.

---

## Exemple concret

Quand un employé se connecte :

* à Azure Portal
* Teams
* Outlook
* SharePoint

➡ c’est Microsoft Entra ID qui vérifie son identité.

---

## Ce qu’il gère

### Identités

* utilisateurs
* groupes
* applications
* appareils

### Accès

* permissions Azure
* accès applications
* stratégies de sécurité

---

## Concepts clés

| Fonction       | Description                       |
| -------------- | --------------------------------- |
| Authentication | Vérifie qui tu es                 |
| Authorization  | Vérifie ce que tu peux faire      |
| SSO            | Une connexion pour plusieurs apps |
| MFA            | Vérification supplémentaire       |
| RBAC           | Gestion des permissions           |

---

# 2. Différence entre AD DS et Microsoft Entra ID

---

# A. Active Directory Domain Services (AD DS)

## Définition

Service d’identité traditionnel installé sur des serveurs Windows locaux.

Souvent utilisé dans :

* entreprises classiques
* infrastructures on-premise

---

## Fonctionnement

Les utilisateurs se connectent à un domaine Windows :

```text
entreprise.local
```

Le serveur contrôleur de domaine :

* authentifie
* applique des politiques
* gère les ordinateurs

---

## Protocoles utilisés

| Protocole | Utilité               |
| --------- | --------------------- |
| LDAP      | annuaire              |
| Kerberos  | authentification      |
| NTLM      | ancien protocole auth |

---

## Exemple

Quand un PC Windows rejoint un domaine :

```text
PC → Domain Controller → validation utilisateur
```

---

# B. Microsoft Entra ID

## Définition

Version cloud moderne de gestion d’identité.

Ne nécessite pas :

* de Domain Controller
* d’infrastructure locale

---

## Fonctionnement

L’utilisateur s’authentifie directement via Internet.

Exemple :

```text
Utilisateur → Azure Portal → Entra ID
```

---

## Protocoles modernes

| Protocole      | Utilité                  |
| -------------- | ------------------------ |
| OAuth 2.0      | accès API                |
| OpenID Connect | authentification moderne |
| SAML           | SSO applications         |

---

# Différence importante pour l’examen

| AD DS       | Entra ID      |
| ----------- | ------------- |
| Local       | Cloud         |
| Kerberos    | OAuth         |
| GPO         | Intune        |
| Domain Join | Azure AD Join |
| LDAP        | REST/API      |

---

# 3. Tenant Microsoft Entra

## Définition

Un tenant est une instance dédiée et isolée de Microsoft Entra ID.

On peut le voir comme :

```text
Une entreprise = un tenant
```

---

## Contenu d’un tenant

* utilisateurs
* groupes
* applications
* rôles
* abonnements Azure

---

## Exemple

Entreprise :

```text
contoso.onmicrosoft.com
```

➡ représente le tenant Azure.

---

## Important AZ-104

Un tenant peut contenir :

* plusieurs subscriptions Azure

Mais :

* une subscription appartient à un seul tenant.

---

# 4. Les identités dans Entra ID

---

# A. Utilisateurs (Users)

## Définition

Compte représentant une personne.

---

## Types

| Type   | Description         |
| ------ | ------------------- |
| Member | employé interne     |
| Guest  | utilisateur externe |

---

## Exemple

```text
alice@contoso.com
```

Utilisateur standard Azure.

---

## Cas d’usage

* connexion Azure
* Microsoft 365
* accès applications

---

# B. Groupes (Groups)

## Définition

Conteneur logique regroupant plusieurs utilisateurs.

---

## Pourquoi utiliser des groupes ?

Au lieu :

```text
Donner accès à 100 utilisateurs
```

On fait :

```text
Créer groupe → attribuer accès au groupe
```

---

## Exemple

```text
Groupe : IT-Admins
```

Tous les membres héritent des permissions.

---

## Types

| Groupe              | Utilité       |
| ------------------- | ------------- |
| Security Group      | permissions   |
| Microsoft 365 Group | collaboration |

---

# C. Service Principal

## Définition

Identité utilisée par une application ou un service.

Equivalent :

```text
Compte utilisateur pour application
```

---

## Exemple concret

Terraform doit créer des VM Azure.

Terraform utilise :

* un Service Principal
* avec permissions spécifiques

---

## Important

Le Service Principal :

* possède un ID
* possède un secret/certificat
* reçoit des rôles RBAC

---

# D. Managed Identity

## Définition

Identité automatique créée et gérée par Azure pour une ressource.

---

## Objectif

Éviter :

* mots de passe
* secrets codés en dur

---

## Exemple classique

VM Azure → accès Key Vault.

Sans Managed Identity :

```text
Stockage mot de passe dans le code
```

Avec Managed Identity :

```text
Azure fournit automatiquement un token
```

---

# Types de Managed Identity

## System-assigned

Attachée à UNE ressource.

Suppression ressource :
➡ identité supprimée.

---

## User-assigned

Identité indépendante réutilisable.

Exemple :

```text
1 identité → plusieurs VM
```

---

# 5. Authentification vs Autorisation

---

# A. Authentication

## Définition

Vérifie l’identité.

Question :

```text
Qui es-tu ?
```

---

## Exemple

Login :

```text
user + password + MFA
```

---

# B. Authorization

## Définition

Détermine les permissions.

Question :

```text
Que peux-tu faire ?
```

---

## Exemple

Utilisateur :

* peut lire Storage
* ne peut pas supprimer VM

---

# Résumé essentiel

| Concept        | Question            |
| -------------- | ------------------- |
| Authentication | Qui es-tu ?         |
| Authorization  | Que peux-tu faire ? |

---

# 6. Single Sign-On (SSO)

## Définition

Une seule authentification pour plusieurs applications.

---

## Exemple

Connexion une fois :

* Outlook
* Teams
* Azure Portal

Sans ressaisir le mot de passe.

---

## Avantages

* moins de mots de passe
* meilleure sécurité
* meilleure expérience utilisateur

---

# 7. Multi-Factor Authentication (MFA)

## Définition

Ajoute une vérification supplémentaire.

---

## Facteurs possibles

| Facteur            | Exemple      |
| ------------------ | ------------ |
| Ce que tu sais     | mot de passe |
| Ce que tu possèdes | téléphone    |
| Ce que tu es       | empreinte    |

---

## Exemple

```text
Password + Microsoft Authenticator
```

---

## Pourquoi important ?

Même si mot de passe volé :
➡ accès bloqué sans second facteur.

---

# 8. Conditional Access

## Définition

Politiques intelligentes d’accès.

Fonctionne comme :

```text
IF condition → THEN action
```

---

# Exemples

## Exemple 1

SI :

* utilisateur hors France

ALORS :

* MFA obligatoire

---

## Exemple 2

SI :

* appareil non conforme

ALORS :

* accès refusé

---

## Conditions possibles

* localisation
* appareil
* utilisateur
* risque
* application

---

## Actions possibles

* autoriser
* bloquer
* forcer MFA

---

# 9. RBAC (Role-Based Access Control)

## Définition

Système de gestion des permissions Azure.

---

# Structure RBAC

## A. Security Principal

Qui reçoit les droits :

* utilisateur
* groupe
* application

---

## B. Role Definition

Quelles permissions ?

---

## C. Scope

Sur quelle ressource ?

---

# Scopes Azure

Du plus large au plus précis :

```text
Management Group
→ Subscription
→ Resource Group
→ Resource
```

---

# Exemple pratique

```text
Alice = Contributor
Sur RG-Production
```

Alice :

* peut créer VM
* peut modifier Storage

Mais :

* ne peut pas gérer IAM

---

# Rôles importants

| Rôle                      | Description        |
| ------------------------- | ------------------ |
| Owner                     | contrôle total     |
| Contributor               | gestion ressources |
| Reader                    | lecture seule      |
| User Access Administrator | gère accès         |

---

# 10. Azure AD Join

## Définition

Ordinateur connecté directement à Entra ID.

---

## Utilisé pour

* cloud-first
* télétravail
* entreprises modernes

---

## Exemple

Laptop connecté :

```text
PC → Entra ID
```

Sans domaine local.

---

# 11. Hybrid Azure AD Join

## Définition

Machine :

* join domaine local
* enregistrée aussi dans Entra ID

---

## Pourquoi ?

Transition :

```text
On-premise → Cloud
```

---

## Très fréquent en entreprise

Permet :

* compatibilité legacy
* intégration cloud

---

# 12. Microsoft Entra Domain Services

## Définition

Service managé fournissant :

* LDAP
* Kerberos
* NTLM

Sans gérer de Domain Controllers.

---

## Utilité

Applications anciennes nécessitant :

* LDAP
* domaine Windows

---

## Exemple

Application legacy sur VM Azure.

---

# 13. Self-Service Password Reset (SSPR)

## Définition

Les utilisateurs réinitialisent eux-mêmes leur mot de passe.

---

## Exemple

Utilisateur oublié mot de passe :

* email
* SMS
* MFA

➡ reset automatique.

---

## Avantages

* moins de tickets support
* gain de temps

---

# 14. Editions Microsoft Entra ID

| Edition | Fonctionnalités           |
| ------- | ------------------------- |
| Free    | utilisateurs/groupes      |
| P1      | Conditional Access        |
| P2      | PIM + Identity Protection |

---

# 15. Points CRITIQUES pour AZ-104

## À connaître parfaitement

### Identity

* Users
* Groups
* Managed Identity
* Service Principal

---

### Security

* MFA
* Conditional Access
* RBAC

---

### Hybrid

* AD DS vs Entra ID
* Hybrid Join

---

### Azure Permissions

* Scope RBAC
* rôles intégrés

---

# Questions typiques examen

---

## Question

Une VM doit accéder à Key Vault sans mot de passe.

✅ Réponse :
Managed Identity

---

## Question

Quel rôle permet de créer des VM sans gérer les permissions ?

✅ Contributor

---

## Question

Quelle fonctionnalité impose MFA selon la localisation ?

✅ Conditional Access

---

# Résumé final ultra rapide

| Concept            | Résumé                  |
| ------------------ | ----------------------- |
| Entra ID           | IAM cloud Microsoft     |
| Tenant             | instance Entra ID       |
| Authentication     | vérifier identité       |
| Authorization      | vérifier permissions    |
| RBAC               | contrôle accès Azure    |
| MFA                | sécurité supplémentaire |
| Conditional Access | règles intelligentes    |
| Managed Identity   | identité automatique    |
| Service Principal  | identité application    |
| Hybrid Join        | local + cloud           |
