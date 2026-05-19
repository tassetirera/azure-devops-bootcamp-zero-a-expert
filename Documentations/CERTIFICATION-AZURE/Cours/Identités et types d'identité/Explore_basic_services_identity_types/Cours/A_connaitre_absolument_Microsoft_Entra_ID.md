
# À connaître absolument – Microsoft Entra ID

> **Fiche ultra-complète pour maîtriser Microsoft Entra ID (ex-Azure AD)**

Cette fiche synthétise tous les concepts, définitions, exemples, astuces et liens utiles pour comprendre et réussir l’examen sur Microsoft Entra ID.

---


## Glossaire : Terminologies de base

| Terme             | Définition                                                                 |
|-------------------|----------------------------------------------------------------------------|
| Locataire (Tenant)| Instance dédiée et isolée d’Entra ID pour une organisation                 |
| Annuaire          | Base de données des identités (utilisateurs, groupes, applis, appareils)   |
| Multilocataire    | Application ou ressource accessible par plusieurs tenants                   |
| Monolocataire     | Application ou ressource accessible par un seul tenant                     |

**Astuce** :
> Un locataire = une entreprise, un annuaire = la liste de toutes ses identités.

---

## Qui utilise Microsoft Entra ID ?

- Employés internes (membres)
- Partenaires externes (invités)
- Applications cloud (SaaS, internes, API)
- Appareils (PC, mobiles, IoT)
- Agents IA, bots, workflows automatisés

**Exemples** :
- Un salarié accède à Teams ou SharePoint
- Un partenaire externe accède à un portail B2B
- Un bot Teams ou un agent Copilot s’authentifie

---

### Microsoft Entra ID
Service cloud de gestion des identités et des accès (IAM) de Microsoft. Il authentifie les utilisateurs, contrôle les accès aux ressources et permet l’intégration avec Azure, Microsoft 365 et des applications SaaS.

**Exemple** :
> Quand tu te connectes à Teams, Outlook, ou au portail Azure, c’est Entra ID qui vérifie ton identité.

### IAM (Identity and Access Management)
Gestion centralisée des identités et des accès : qui peut se connecter, à quoi, et comment les autorisations sont accordées ou révoquées.

### Tenant
Instance isolée de Microsoft Entra ID associée à une organisation. Chaque tenant a son propre annuaire d’identités et de rôles.

**Schéma** :
```
Entreprise A = Tenant A (contoso.onmicrosoft.com)
Entreprise B = Tenant B (fabrikam.onmicrosoft.com)
```

### Subscription (abonnement)
Conteneur de facturation Azure qui appartient à un tenant. Une subscription peut être liée à un seul tenant.

### Domaine personnalisé
Nom de domaine ajouté à Entra ID, ex : `contoso.com`, pour remplacer le domaine par défaut `*.onmicrosoft.com`.

### Azure Portal
Interface web où l’on configure Entra ID, les applications, les stratégies et les rôles.

**Astuce** :
> Retenir que tout ce qui touche à l’identité dans Azure passe par Entra ID.

**Lien utile** : [Microsoft Learn – Entra ID](https://learn.microsoft.com/fr-fr/azure/active-directory/fundamentals/active-directory-whatis)

---


### Catégories de membres et invités

| Catégorie           | Définition / Origine                        |
|---------------------|---------------------------------------------|
| Membre interne      | Employé créé dans le tenant                  |
| Membre externe      | Employé d’un autre tenant, converti membre   |
| Invité externe      | Partenaire/client invité (B2B/B2C)          |
| Invité interne      | Utilisateur invité depuis un autre tenant    |

**Astuce** :
> Les invités sont toujours des `Guest` dans Entra ID, même s’ils travaillent beaucoup avec l’organisation.

---

| Type d’identité         | Définition / Usage principal                                 | Exemple concret                      |
|------------------------|-------------------------------------------------------------|--------------------------------------|
| **Utilisateur (User)** | Compte pour une personne physique                           | alice@contoso.com                    |
| **Member**             | Employé interne, géré par l’organisation                    | bob@entreprise.fr                    |
| **Guest**              | Utilisateur externe invité (B2B)                            | partenaire@gmail.com                 |
| **Groupe**             | Ensemble d’utilisateurs/appareils pour gestion collective   | Groupe « RH », « Dév », etc.         |
| **Application**        | Application enregistrée pour l’authentification             | Appli interne, SaaS, API             |
| **Service Principal**  | Identité d’une application/service pour s’authentifier      | Appli web qui accède à Azure         |
| **Managed Identity**   | Identité gérée automatiquement par Azure pour une ressource | VM Azure accédant à un stockage      |
| **Identité de charge de travail** | Identité pour une application, un service, un script, une VM, etc. | API, Logic App, VM, Function         |
| **Identité d’agent**   | Identité pour agent IA, bot, workflow automatisé            | Copilot, Bot Teams, Logic App        |
| **Appareil**           | PC, mobile, IoT enregistré dans Entra ID                    | Laptop Windows Azure AD Join         |
| **Hybride**            | Identité synchronisée AD local ↔ Entra ID                   | Employé on-premises + cloud          |
| **External ID**        | Identité partenaire/client (B2B/B2C)                        | Client B2C, partenaire B2B           |
| **Agent ID**           | Identité pour agent IA ou workflow automatisé               | Bot Teams, Logic App, Copilot        |


**Astuce** :
> Pour chaque ressource Azure, privilégier Managed Identity si possible (plus sécurisé, pas de secret à gérer).
> Les identités de charge de travail sont essentielles pour sécuriser les accès machine-to-machine.

---
## Microsoft Entra ID et l’IA

Microsoft Entra ID permet de sécuriser les agents IA, bots, workflows automatisés grâce aux identités d’agent (Agent ID). Ces identités permettent de contrôler précisément les droits des IA et de tracer leurs actions.

**Exemple** :
> Un agent Copilot ou un bot Teams utilise une identité d’agent pour accéder à des ressources Azure ou Microsoft 365.

---
## Score de sécurité d’identité

Le score de sécurité d’identité (Identity Secure Score) est un indicateur proposé dans Entra ID pour mesurer le niveau de sécurité des identités de votre tenant.

- Plus le score est élevé, plus les bonnes pratiques sont appliquées (MFA, PIM, gestion des invités, etc.).
- Permet de comparer son niveau de sécurité à celui d’autres organisations.

**Lien utile** : [Identity Secure Score – Microsoft Docs](https://learn.microsoft.com/fr-fr/azure/active-directory/fundamentals/security-operations-introduction#identity-secure-score)

**Astuce** :
> Pour l’examen, retiens que le score de sécurité d’identité est un outil d’audit et d’amélioration continue.

---

**Lien utile** : [Types d’identités – Microsoft Learn](https://learn.microsoft.com/fr-fr/training/modules/explore-basic-services-identity-types/3-describe-identity-types)

---

## 3. Authentification et accès

| Terme                  | Définition / Utilité                                                                 |
|------------------------|------------------------------------------------------------------------------------|
| **Authentication**     | Vérifie l’identité (qui es-tu ?)                                                    |
| **Authorization**      | Vérifie ce que tu peux faire (droits/actions)                                       |
| **SSO**                | Connexion unique à plusieurs applis                                                 |
| **MFA**                | Authentification à plusieurs facteurs (mot de passe + code/appareil)                |
| **Conditional Access** | Règles d’accès selon contexte (lieu, appareil, risque)                              |
| **Identity Protection**| Détection et réponse aux risques d’identité                                         |
| **PIM**                | Gestion temporaire des rôles à privilèges (activation à la demande, audit, etc.)    |

**Exemple** :
> Un administrateur doit activer PIM pour obtenir temporairement le rôle Global Admin (meilleure sécurité).

**Astuce** :
> Toujours activer MFA et Conditional Access pour sécuriser les accès.

**Lien utile** : [Sécuriser l’accès – Microsoft Learn](https://learn.microsoft.com/fr-fr/azure/active-directory/conditional-access/overview)

---

## 4. Protocoles et technologies

| Protocole         | Usage principal / Où le retrouver ?                |
|-------------------|---------------------------------------------------|
| **OAuth 2.0**     | Autorisation d’accès API/applications             |
| **OpenID Connect**| Authentification moderne (extension OAuth 2.0)    |
| **SAML**          | SSO avec applis d’entreprise (legacy, SaaS)       |
| **WS-Federation** | Ancien SSO, encore utilisé dans certains cas      |
| **LDAP/Kerberos** | Authentification AD local (on-premises)           |
| **NTLM**          | Ancien protocole Microsoft (à éviter)             |

**Schéma** :
```
Utilisateur → Application → Entra ID (OIDC/OAuth2/SAML) → Ressource
```

**Astuce** :
> Pour le cloud, retiens : OAuth 2.0 et OpenID Connect sont les standards modernes.

**Lien utile** : [Protocoles d’identité – Microsoft Docs](https://learn.microsoft.com/fr-fr/azure/active-directory/develop/authentication-scenarios)

---

## 5. Gestion des rôles et des accès

| Type de rôle         | Portée / Usage principal                                 | Exemples                       |
|----------------------|---------------------------------------------------------|--------------------------------|
| **RBAC Azure**       | Accès aux ressources Azure (VM, stockage, réseau, etc.) | Owner, Contributor, Reader     |
| **Rôles Entra ID**   | Gestion du tenant, des identités, de la sécurité        | Global Admin, User Admin, etc. |

**Exemple** :
> Un Global Admin Entra ID n’est pas Owner Azure par défaut : ce sont deux systèmes séparés.

**Astuce** :
> Toujours appliquer le principe du moindre privilège (donner le minimum de droits nécessaires).

**Lien utile** : [Rôles Entra ID – Microsoft Docs](https://learn.microsoft.com/fr-fr/azure/active-directory/roles/permissions-reference)

---

## 6. Scénarios importants

| Scénario                  | Description / Utilité principale                                 | Exemple concret                        |
|---------------------------|-----------------------------------------------------------------|----------------------------------------|
| **Azure AD Join**         | Appareil Windows inscrit directement dans Entra ID               | Laptop pro connecté au cloud           |
| **Hybrid Azure AD Join**  | Appareil joint à AD local ET enregistré dans Entra ID            | PC bureau entreprise hybride           |
| **Azure AD Connect**      | Synchronisation comptes AD local → Entra ID                      | Employé migré vers le cloud            |
| **Pass-through Auth**     | Authentification cloud, mot de passe vérifié on-premises         | Login cloud, validation locale         |
| **Fédération (ADFS)**     | Utilisation d’un fournisseur d’identité local pour Entra ID       | SSO entreprise avec ADFS               |
| **Azure B2B**             | Invitation de partenaires externes                               | Consultant externe accédant à SharePoint|
| **Azure B2C**             | Gestion d’identités clients finaux (consommateurs)               | Portail client avec inscription        |
| **Agent ID**              | Identité pour bot, workflow, Copilot, etc.                       | Bot Teams, Logic App                   |

**Schéma** :
```
PC → Azure AD Join → Entra ID
PC → AD local → Hybrid Join → Entra ID
```

**Astuce** :
> Toujours préférer Azure AD Join pour les nouveaux appareils cloud natifs.

**Lien utile** : [Scénarios d’identité – Microsoft Learn](https://learn.microsoft.com/fr-fr/azure/active-directory/fundamentals/active-directory-whatis)

---

## 7. Termes à connaître absolument

| Terme                | Définition rapide / Astuce de mémorisation                |
|----------------------|----------------------------------------------------------|
| Tenant               | Instance dédiée Entra ID (1 entreprise = 1 tenant)        |
| Subscription         | Unité de facturation Azure liée à un tenant               |
| User                 | Compte personnel ou employé                              |
| Guest                | Utilisateur externe invité (toujours B2B)                |
| Group                | Ensemble de membres pour simplifier l’attribution        |
| Service Principal    | Identité d’application                                   |
| Managed Identity     | Identité gérée par Azure pour un service                 |
| SSO                  | Authentification unique                                  |
| MFA                  | Authentification multi-facteurs                          |
| Conditional Access   | Règles d’accès selon le contexte                         |
| RBAC                 | Contrôle d’accès basé sur les rôles                      |
| Azure AD Join        | Inscription d’un appareil au cloud                       |
| Hybrid Azure AD Join | Appareil lié à AD local + Entra ID                       |
| Azure AD Connect     | Synchronisation AD locale → Entra ID                     |
| External ID          | Identités externes B2B/B2C                               |
| Agent ID             | Identité pour les agents IA                              |
| Identity Protection  | Détection des risques d’identité                          |
| PIM                  | Gestion des privilèges élevés                            |

**Astuce** :
> Pour l’examen, révise ce tableau : chaque terme peut faire l’objet d’une question directe !

---

## 8. Comparaison rapide

| Comparaison                        | AD DS (local)                        | Entra ID (cloud)                      |
|------------------------------------|--------------------------------------|---------------------------------------|
| Gestion                            | Serveurs locaux, Domain Controllers  | Service cloud, pas de serveur à gérer |
| Protocoles                         | LDAP, Kerberos, NTLM                 | OAuth2, OIDC, SAML                    |
| Appareils                          | Domain Join                          | Azure AD Join, Hybrid Join            |
| Accès                              | Réseau interne                       | Internet, cloud, SaaS                 |
| Identité d’utilisateur             | Personne physique                    | Personne physique                     |
| Identité de service                | Compte de service AD                 | Service Principal, Managed Identity   |
| Service Principal                  | N/A                                  | Identité d’application                |
| Managed Identity                   | N/A                                  | Identité gérée par Azure              |

**Astuce** :
> Retenir que Entra ID = cloud, moderne, sécurisé, sans serveur à gérer.

---

## 9. Suggestions d’étude

- Comprendre le rôle de Entra ID dans Azure et Microsoft 365 (faire des schémas !).
- Mémoriser les différences entre AD DS, Entra ID et les identités hybrides (tableaux comparatifs).
- Savoir quand utiliser `Service Principal` vs `Managed Identity` (préférer Managed Identity si possible).
- Étudier les usages de `Conditional Access`, `MFA` et `PIM` (exemples concrets dans le portail Azure).
- Pratiquer la création de : utilisateur, groupe, application, service principal, identité managée (mode labo/sandbox).
- Lire les définitions dans le portail Azure : tenant, domaine, subscription et rôles (menu Entra ID > Vue d’ensemble).
- Réviser les protocoles : OAuth 2.0, OpenID Connect, SAML (faire un schéma de flux d’authentification).
- Comparer les rôles Entra ID et les rôles Azure RBAC (tableau, cas d’usage).
- Retenir que “un abonnement Azure appartient à un seul tenant” (jamais l’inverse).
- Se souvenir que les invités externes sont des `Guest`, pas des `Member` (piège fréquent en QCM).

**Lien utile** : [Microsoft Learn – Parcours Entra ID](https://learn.microsoft.com/fr-fr/training/paths/secure-access-azure-resources/)

---

## 10. Conseils pratiques pour l’examen

	> Service cloud Microsoft d’IAM, qui authentifie, autorise et connecte utilisateurs, appareils et applications.
	> Utilisateurs, groupes, applications, rôles, stratégies, abonnements.
	> Managed Identity si possible, sinon Service Principal.
	> Global Admin = admin du tenant Entra ID, Owner = contrôle ressources Azure (RBAC).
	> MFA, Conditional Access, Managed Identity.

**Astuce** :
> Les questions d’examen sont souvent des cas pratiques : imagine le scénario réel !


## 11. Rappels et pièges fréquents


**Lien utile** : [FAQ Entra ID – Microsoft Docs](https://learn.microsoft.com/fr-fr/azure/active-directory/fundamentals/active-directory-faq)

## 12. Éditions de Microsoft Entra ID

| Édition | Fonctionnalités principales                                 |
|---------|------------------------------------------------------------|
| Free    | Gestion utilisateurs/groupes, SSO, authentification de base |
| P1      | Conditional Access, MFA, self-service password reset      |
| P2      | PIM (Privileged Identity Management), Identity Protection |

**Astuce** :
> Pour la plupart des entreprises, P1 suffit. P2 est requis pour la gestion avancée des privilèges et la détection des risques.

**Lien utile** : [Comparer les éditions Entra ID](https://learn.microsoft.com/fr-fr/azure/active-directory/fundamentals/active-directory-whatis#features-and-editions)
