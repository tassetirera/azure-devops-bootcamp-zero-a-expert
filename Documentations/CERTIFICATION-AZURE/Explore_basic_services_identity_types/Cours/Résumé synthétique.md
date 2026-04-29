<!DOCTYPE html>
<html>
<head>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      line-height: 1.6;
      max-width: 900px;
      margin: 40px auto;
      padding: 20px;
      color: #333;
      background: #f8f9fa;
    }
    h1, h2, h3 {
      color: #0057b7;
    }
    pre {
      background: #f0f0f0;
      padding: 12px;
      border-radius: 6px;
      overflow-x: auto;
      font-size: 0.92em;
      border: 1px solid #ccc;
    }
    .card {
      margin: 16px 0;
      padding: 12px 16px;
      border-radius: 8px;
      border: 1px solid #ddd;
      background: #fff;
      box-shadow: 0 1px 4px rgba(0,0,0,0.1);
    }
    .highlight {
      background: #e3f2fd;
      padding: 2px 6px;
      border-radius: 4px;
      font-weight: 600;
      color: #0057b7;
    }
  </style>
</head>
<body>

# Microsoft Learn – Explore basic services: identity types  
## Résumé synthétique (1 page) – Markdown/CSS

---

## 1. Fonction de Microsoft Entra ID

- Service d’identité et d’accès cloud qui gère :
  - Authentification et autorisation des utilisateurs, applications, appareils et agents IA. [web:1][web:3]  
  - Accès aux ressources Azure, Microsoft 365, SaaS, etc. [web:1][web:4]  

- Rôle principal :  
  - Centraliser la gestion des identités (credentials, MFA, SSO, conditions d’accès). [web:1][web:3]  

---

## 2. Types d’identité clés

### Identité utilisateur
- Associée à une personne (employé, collaborateur, stagiaire). [web:2][web:3]  
- Peut être créée dans le cloud ou synchronisée depuis AD DS local. [web:2][web:4]  

### Identité de service / principal de service
- Identité d’une **application** ou d’un **service** pour s’authentifier auprès d’une API ou d’une ressource Azure. [web:2]  
- Exemple : une application Azure qui appelle Microsoft Graph ou une base de données. [web:2]  

### Identité managée (managed identity)
- **Affectée par le système**  
  - Liée à une seule ressource Azure (ex : VM, Function App).  
  - Supprimée automatiquement si la ressource est détruite. [web:2][web:6]  
- **Affectée par l’utilisateur**  
  - Gérée séparément, réutilisable sur plusieurs ressources. [web:2][web:6]  
- Avantage : **pas de secret / mot de passe** à gérer dans le code. [web:2]  

### Identité d’appareil
- Identité d’un **PC, mobile, serveur ou IoT** inscrit dans Microsoft Entra ID. [web:2]  
- Scénarios :  
  - Intune / Azure AD Join / Hybrid AD Join.  
  - Accès conditionnel basé sur l’appareil (ex : “accès uniquement depuis appareil géré”). [web:2]  

### Identité hybride
- Les comptes sont créés dans **Active Directory DS local** puis synchronisés vers **Microsoft Entra ID** via **Azure AD Connect**. [web:2][web:4]  
- Objectif : garder AD local comme source d’authentité tout en activant le cloud (Azure, M365). [web:2][web:4]  

### Identité externe – Microsoft Entra External ID
- **Azure AD B2B** : inviter des partenaires/invités (collaborateurs externes). [web:3][web:4]  
- **Azure AD B2C** : gérer les identités de clients grand public (candidatures, portails clients, etc.). [web:3]  

### Identité d’agent IA – Microsoft Entra Agent ID
- Nouveau type d’identité pour les **agents IA** (bots, workflows automatisés, assistants IA). [web:3]  
- Permet de :
  - Attribuer des rôles et permissions à l’agent.  
  - Audit et traçabilité des actions effectuées automatiquement. [web:3]  

---

## 3. Scénarios clés à retenir

<style>
  table {
    border-collapse: collapse;
    width: 100%;
    margin: 16px 0;
  }
  th, td {
    border: 1px solid #ddd;
    padding: 8px 12px;
    text-align: left;
  }
  th {
    background-color: #e3f2fd;
  }
</style>

<table>
  <thead>
    <tr>
      <th>Scénario</th>
      <th>Solution / type d’identité</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AD local + Azure / M365</td>
      <td><span class="highlight">Identité hybride + Azure AD Connect</span></td>
    </tr>
    <tr>
      <td>Partenaire qui accède ponctuellement</td>
      <td><span class="highlight">Invité via Azure AD B2B (External ID)</span></td>
    </tr>
    <tr>
      <td>Application Azure qui appelle une API sans secret</td>
      <td><span class="highlight">Identité managée ou principal de service</span></td>
    </tr>
    <tr>
      <td>Agent IA / bot automatisé</td>
      <td><span class="highlight">Microsoft Entra Agent ID</span></td>
    </tr>
    <tr>
      <td>Accès client grand public (portail, inscription)</td>
      <td><span class="highlight">Azure AD B2C (External ID)</span></td>
    </tr>
    <tr>
      <td>Appareil (PC, mobile) géré et sécurisé</td>
      <td><span class="highlight">Identité d’appareil + Intune / AAD Join</span></td>
    </tr>
  </tbody>
</table>

---

## 4. À maîtriser pour l’examen

- Différencier :
  - **Identité utilisateur** vs **service** vs **appareil** vs **agent IA**. [web:2][web:3]  
- Savoir reconnaître :
  - Scénario **hybride** (AD local + Azure AD Connect). [web:2][web:4]  
  - Scénario **B2B** (invités/partenaires) et **B2C** (clients grand public). [web:3][web:4]  
- Expliquer l’intérêt des **identités managées** (pas de secret, sécurisé). [web:2][web:6]  

</body>
</html>