# 📚 Cours complet — Microsoft Entra ID B2B vs B2C

## 🌐 Introduction
Dans l’écosystème Microsoft, l’ancien nom **Azure Active Directory (Azure AD)** est devenu :  
🔐 **Microsoft Entra ID**

Microsoft Entra ID permet de gérer :  
🔐 l’authentification,  
👨‍💼 les identités,  
🔒 les permissions,  
🚪 l’accès aux applications,  
🛡️ la sécurité des utilisateurs.

Deux concepts très importants existent pour les utilisateurs externes :  

| Technologie | Objectif |
|------------|----------|
| **B2B 🤝 (Business-to-Business)** | Collaborer avec des partenaires externes |
| **B2C 🛒 (Business-to-Consumer)** | Authentifier des clients/consommateurs |

***

## 1️⃣ Comprendre Microsoft Entra ID

### 🎯 Rôle principal
Microsoft Entra ID sert à :  
✅ authenticated les utilisateurs,  
🎫 délivrer des tokens JWT,  
📜 appliquer des politiques de sécurité,  
🔑 gérer les accès aux applications.

### 🧩 Exemples d’applications protégées
- 📞 Teams  
- 🗂️ SharePoint  
- 🖥️ API ASP.NET Core  
- 🌐 Applications web  
- 📱 Applications mobiles  
- ☁️ Azure Portal  
- 📊 CRM  
- 🧮 ERP  

***

## 2️⃣ Architecture globale

### 👥 Types d’utilisateurs

| Type      | Description |
|-----------|-------------|
| **Member 👨‍💼** | Utilisateur interne de l’entreprise |
| **Guest 👥** | Utilisateur externe invité (B2B) |
| **Consumer 🛍️** | Client grand public (B2C) |

***

## 3️⃣ Microsoft Entra ID B2B 🤝

### 📌 Définition
Le **B2B** permet à une entreprise d’inviter des utilisateurs externes afin qu’ils accèdent à certaines ressources internes.

### 🧩 Cas typiques
- 👨‍🔧 consultant externe  
- 🏭 fournisseur  
- 🧩 sous‑traitant  
- 🤝 partenaire commercial  
- 🏢 client entreprise  

***

## 4️⃣ Fonctionnement du B2B 🔄

### 📥 Processus complet

1️⃣ **Invitation**  
L’administrateur invite un utilisateur :  
📧 `user@gmail.com`  
ou  
📧 `consultant@partner-company.com`

2️⃣ **Création automatique du Guest User** 🞋  
Microsoft Entra ID crée automatiquement :  
`UserType = Guest`  

Exemple :  
`user_gmail.com#EXT#@contoso.onmicrosoft.com`

**Important ⚠️** :  
🚫 Le compte n’est **PAS** créé manuellement,  
Azure crée uniquement un **objet invité**.

3️⃣ **Email d’invitation 📨**  
Azure envoie un email :  
📩 *"Vous êtes invité à rejoindre l’organisation Contoso"*

4️⃣ **Acceptation ✅**  
L’utilisateur clique sur :  
⏯️ **Accept invitation**  

Puis il se connecte avec :  
- 🏢 son Azure AD d’entreprise,  
- 🟦 son compte Microsoft,  
- 📬 parfois un OTP email.

5️⃣ **Accès aux ressources 🚪**  
L’utilisateur peut maintenant accéder à :  
- 📞 Teams  
- 🗂️ SharePoint  
- 🖥️ une API  
- 🌐 une application web  
- 🖥️ un portail interne  

***

## 5️⃣ Où est stocké le mot de passe ? 🔐

### ⚠️ Point extrêmement important
En **B2B** :  
❌ Ton tenant **NE stocke PAS** le mot de passe.  

Le mot de passe reste :  

| Fournisseur | Exemple |
|-------------|---------|
| Azure AD externe 🏢 | Entreprise partenaire |
| Microsoft Account 🟦 | Outlook/Hotmail |
| OTP Email 📬 | Code temporaire |

Ton tenant stocke seulement :  
- 🧩 l’objet invité  
- 🔐 les permissions  
- 👥 les groupes  
- 🎖️ les rôles  

***

## 6️⃣ Types d’identités acceptées en B2B ✅

### Acceptés

| Type | Supporté |
|------|---------|
| Azure AD entreprise 🏢 | ✅ |
| Outlook/Hotmail 🟦 | ✅ |
| Gmail via Microsoft Account 🟩 | ✅ |
| One-Time Passcode Email 📬 | ✅ |

### Non supportés directement

| Fournisseur social | B2B |
|--------------------|-----|
| Facebook 🟦 | ❌ |
| LinkedIn 🟦 | ❌ |
| Twitter/X □ | ❌ |

👉 Ces fournisseurs sont principalement destinés au **B2C**.

***

## 7️⃣ One-Time Passcode (OTP) 📬

### 🔧 Fonctionnement
Si l’utilisateur n’a pas de compte Microsoft :  
- Azure envoie un code par email 📬,  
- l’utilisateur saisit le code 🔢,  
- il est authentifié ✅.

Exemple :  
📧 Email → 💬 code 123456 → 🚪 accès

Très utilisé pour :  
- 👨‍🔧 consultants  
- 🏭 fournisseurs  
- 🕐 accès temporaires  

***

## 8️⃣ Architecture technique B2B 🏗️

### 🔄 Flux simplifié
`User 👥 → Microsoft Entra ID 🔐 → External Identity Provider 🌍`

### 📜 Protocoles utilisés

| Protocole | Usage |
|-----------|-------|
| OAuth 2.0 🔐 | Autorisation |
| OpenID Connect 🌐 | Authentification |
| SAML 🧩 | Fédération |
| JWT 🎫 | Tokens |

***

## 9️⃣ Claims importantes dans le token 🎫

### Exemple JWT
```json
{
  "name": "John Doe",
  "email": "john@gmail.com",
  "tid": "tenant-id",
  "userType": "Guest"
}
```

***

## 1️⃣0️⃣ Sécurité B2B 🔐

### 🔒 Conditional Access
Tu peux imposer :  
- 🦾 MFA  
- 🖥️ device compliant  
- 📍 localisation  
- ⚠️ niveau de risque  
- 🚫 restrictions IP  

**Exemple 🎯** :  
🔐 *"Les invités DOIVENT utiliser MFA"*

***

## 1️⃣1️⃣ Gouvernance B2B 📊

### ⚠️ Risque principal
Les **invités oubliés** 👥❌.

### 🛠️ Solutions
- **Access Reviews 🔄**  
  Revue périodique :  
  *"Cet invité a-t-il encore besoin d’accès ?"*  
- **Expiration automatique ⏳**  
  Exemple :  
  🗑️ *Supprimer les invités après 90 jours*

***

## 1️⃣2️⃣ Microsoft Graph API pour B2B 📡

### 📤 Invitation automatisée
Exemple :  
`POST /invitations`

**Payload** :
```json
{
  "invitedUserEmailAddress": "user@gmail.com",
  "inviteRedirectUrl": "https://app.contoso.com",
  "sendInvitationMessage": true
}
```

***

## 1️⃣3️⃣ Cas d’usage B2B 🧩

| Cas | B2B |
|-----|-----|
| Teams externe 📞 | ✅ |
| Partage SharePoint 🗂️ | ✅ |
| API partenaire 🖥️ | ✅ |
| Portail fournisseur 🏭 | ✅ |
| Accès consultant 👨‍🔧 | ✅ |

***

## 1️⃣4️⃣ Microsoft Entra ID B2C 🛒

### 🌐 Définition
Le **B2C** est destiné aux applications grand public 🌍.

### 📋 Exemples
- 🛍️ e‑commerce  
- 📱 application mobile  
- ☁️ SaaS public  
- 🏛️ portail citoyen  
- 🧑‍🤝‍🧑 plateforme client  

***

## 1️⃣5️⃣ Philosophie B2C 🧠

### 🆚 Différence fondamentale

| Contexte | Philosophie |
|----------|-------------|
| **B2B 🤝** | Entreprise invite l’utilisateur |
| **B2C 🛒** | Utilisateur s’inscrit lui‑même |

***

## 1️⃣6️⃣ Fonctionnement du B2C 🔁

1️⃣ **Accès au site 🌐**  
`https://www.monapp.com`

2️⃣ **Inscription ✍️**  
L’utilisateur choisit :  
- 📧 email/mot de passe  
- 🟩 Google  
- 🟦 Facebook  
- 🟩 Apple  
- 🟦 Microsoft  

3️⃣ **Création du compte 🧩**  
Le compte est créé dans :  
**Tenant B2C séparé 🏢**

4️⃣ **Authentification 🔐**  
B2C délivre un **JWT** à l’application 🎫.

***

## 1️⃣7️⃣ Fournisseurs d’identité B2C 🌍

| Provider | Support |
|----------|--------|
| Google 🟩 | ✅ |
| Facebook 🟦 | ✅ |
| Apple 🍏 | ✅ |
| LinkedIn 🟦 | ✅ |
| Azure AD 🏢 | ✅ |
| Compte local 🧑 | ✅ |

***

## 1️⃣8️⃣ UI personnalisable en B2C 🎨

### 🎯 Très important
B2C permet :  
- 🎨 branding  
- 🎨 CSS  
- 🎨 HTML  
- 💼 parcours personnalisés  
- 🖼️ pages customisées  

***

## 1️⃣9️⃣ User Flows B2C 🌀

| Flow | Usage |
|------|-------|
| **SignUpSignIn** | Inscription + login |
| **PasswordReset** | Reset password |
| **ProfileEdit** | Modifier profil |

***

## 2️⃣0️⃣ Custom Policies 🧩

### 🔧 Niveau avancé
B2C permet des politiques XML complexes :  
- 🦾 MFA conditionnel  
- 📡 appels API REST  
- 🔍 validation custom  
- 💼 workflows métier  

***

## 2️⃣1️⃣ Architecture B2C 🏗️

```text
Client 👥 → B2C Tenant 🏢 → Identity Provider 🌍 → JWT 🎫 → Application 🖥️
```

***

## 2️⃣2️⃣ Comparaison complète B2B vs B2C 🆚

| Aspect | B2B 🤝 | B2C 🛒 |
|--------|--------|--------|
| Public cible | Partenaires 👥 | Clients 🛍️ |
| Type d’accès | Collaboration 🤝 | Consommation 🛒 |
| Création compte | Invitation admin 📩 | Auto‑inscription ✍️ |
| Réseaux sociaux | ❌ | ✅ |
| Tenant séparé | ❌ | ✅ |
| UI personnalisable | Faible 🎨 | Très forte 🎨 |
| Gestion utilisateurs | Entreprise 🏢 | Grand public 🌍 |
| Échelle | Milliers 👥 | Millions 👥 |
| Cas typique | Teams 📞 | E‑commerce 🛍️ |

***

## 2️⃣3️⃣ Cas d’usage DevOps / Développement 🧩

### 🤝 Quand utiliser B2B ?

**Exemple** :  
🔐 **API interne partenaire** :  
`partner-api.contoso.com`

Accès pour :  
- 🏭 fournisseurs  
- 🤝 partenaires  
- 👨‍🔧 consultants  

→ ✅ **B2B**

### 🛒 Quand utiliser B2C ?

**Exemple** :  
📱 **Application mobile publique** :  
Netflix / Uber / E‑commerce  

Connexion via :  
- 🟩 Google  
- 🟦 Facebook  
- 🟩 Apple  

→ ✅ **B2C**

***

## 2️⃣4️⃣ Authentification ASP.NET Core 🖥️

### 🎯 Exemple B2C

```csharp
builder.Services.AddAuthentication(OpenIdConnectDefaults.AuthenticationScheme)
    .AddMicrosoftIdentityWebApp(Configuration.GetSection("AzureAdB2C"));
```

### 🎯 Exemple Challenge

```csharp
return Challenge(
    new AuthenticationProperties
    {
        RedirectUri = "/"
    },
    "B2C_1_signupsignin");
```

***

## 2️⃣5️⃣ Bonnes pratiques 🧭

### 🤝 B2B
Toujours :  
- 🔐 activer MFA  
- 🔄 faire des Access Reviews  
- 🚪 limiter les permissions  
- 🎖️ utiliser PIM  
- 👀 surveiller les invités dormants  

### 🛒 B2C
Toujours :  
- 🤖 protéger contre les bots  
- 🦾 utiliser MFA adaptatif  
- 🎫 sécuriser les tokens  
- ⏳ limiter la durée des refresh tokens  

***

## 2️⃣6️⃣ Concepts importants à connaître 🧠

- **Federation 💫** → Permet à Azure de déléguer l’authentification.  
- **Tenant 🏢** → Un annuaire Microsoft Entra ID.  
- **Guest vs Member 👥**  

| Type | Description |
|------|-------------|
| **Member 👨‍💼** | Employé interne |
| **Guest 👥** | Utilisateur externe |

- **Claims 🎫** → Informations présentes dans le JWT.  
- **Consent ✅** → Autorisation donnée à une application.  

***

## 2️⃣7️⃣ Différences fondamentales à retenir 🧩

- **B2B 🤝** :  
  *"Je t’invite dans mon entreprise"*

- **B2C 🛒** :  
  *"Tu t’inscris sur mon application"*

***

## 2️⃣8️⃣ Ce qu’il faut maîtriser pour un entretien DevOps / Cloud / IAM 🧪

Savoir expliquer :  
- 📊 OAuth2  
- 🔐 OpenID Connect  
- 🎫 JWT  
- 🎫 Claims  
- 💫 Federation  
- 🔐 SSO  
- 🦾 MFA  
- 🛡️ Conditional Access  
- 👥 Guest User  
- 🌀 User Flows  
- 🧩 Custom Policies  

***

## 2️⃣9️⃣ Résumé final ultra‑simple 🧩

| | B2B 🤝 | B2C 🛒 |
|---|-------|-------|
| **Utilisateurs** | Partenaires 👥 | Clients 🛍️ |
| **Qui crée le compte ?** | Admin 🏢 | Utilisateur 👥 |
| **Réseaux sociaux** | ❌ | ✅ |
| **Tenant séparé** | ❌ | ✅ |
| **Usage** | Collaboration 🤝 | Applications publiques 🌐 |

***

## 3️⃣0️⃣ Vision architecture complète 🏗️

```text
                ┌────────────────────┐
                │ Microsoft Entra ID 🔐 │
                └─────────┬──────────┘
                          │
        ┌─────────────────┴─────────────────┐
        │                                   │
   ┌────▼────┐                        ┌─────▼─────┐
   │   B2B   🤝 │                        │    B2C    🛒 │
   └────┬────┘                        └─────┬─────┘
        │                                   │
 Partenaires externes 🤝            Clients grand public 🛍️
        │                                   │
 Azure AD / Outlook 🏢                 Google / Facebook 🌍
        │                                   │
 Teams / SharePoint 📞                 Apps mobiles / Web 🖥️
```

***

Souhaites‑tu une version prête à télécharger (PDF / Markdown) ou une présentation plus « slide » avec emojis pour un support pédagogique ? 🎯