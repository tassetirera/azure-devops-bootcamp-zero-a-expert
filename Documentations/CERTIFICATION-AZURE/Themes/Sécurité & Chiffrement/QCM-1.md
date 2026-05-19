# QCM + corrections détaillées pour l'AZ-104 - Sécurité des données et chiffrement

***

## QCM (10 questions) - Domaine : Sécurité des données et chiffrement

1. **Quel est le rôle principal d'Azure Key Vault ?**  
   a) Stocker les bases de données uniquement  
   b) Gérer et protéger les clés de chiffrement, secrets et certificats  
   c) Gérer uniquement le réseau  
   d) Effectuer les sauvegardes  

2. **Quel type de données peut être stocké dans Azure Key Vault ?**  
   a) Uniquement les clés de chiffrement  
   b) Clés, secrets (mots de passe, connection strings, API keys), certificats, données binaires  
   c) Uniquement les certificats  
   d) Les données compressées  

3. **Quel est le type de chiffrement "at rest" (au repos) le plus couramment utilisé pour les disques Azure ?**  
   a) ROT13  
   b) Azure Disk Encryption ou chiffrement de plateforme (Platform-managed keys)  
   c) Pas de chiffrement  
   d) MD5  

4. **Vous avez besoin de chiffrer le trafic réseau entre votre client et Azure (données en transit). Quel protocole utiliser ?**  
   a) HTTP uniquement  
   b) HTTPS (TLS/SSL)  
   c) FTP  
   d) Aucun, le trafic n'a pas besoin de protection  

5. **Quel service Azure vous permet de chiffrer les données dans une application avant qu'elles n'arrivent au serveur ?**  
   a) Azure Storage  
   b) Application-level encryption (chiffrement côté client) ou service comme Always Encrypted pour SQL  
   c) Azure SQL Database uniquement  
   d) C'est impossible  

6. **Quelle est la différence entre "Platform-managed keys" et "Customer-managed keys" pour Azure Storage ?**  
   a) Aucune différence  
   b) Platform-managed : Microsoft gère les clés. Customer-managed : vous gérez les clés via Key Vault  
   c) Customer-managed est gratuit  
   d) Platform-managed est plus sécurisé  

7. **Quel service Azure vous permet de créer et gérer des secrets de façon sécurisée pour les applications ?**  
   a) Azure Storage Accounts  
   b) Azure Key Vault  
   c) Application Insights  
   d) Virtual Networks  

8. **Vous avez besoin que votre application accède à Azure Key Vault sans stocker un mot de passe/secret hardcodé. Quelle solution utiliser ?**  
   a) Hardcoder la clé dans l'application  
   b) Utiliser une identité managée (managed identity) pour authentifier via Entra ID  
   c) Stocker le secret en clair dans un fichier config  
   d) Ne pas utiliser Key Vault  

9. **Quelle est l'utilité des certificats dans Azure Key Vault ?**  
   a) Stocker des données binaires  
   b) Gérer les certificats SSL/TLS, les renouvellements automatiques et le déploiement  
   c) Créer des sauvegardes uniquement  
   d) Aucune utilité  

10. **Quel est le principal avantage d'utiliser Azure Key Vault par rapport à stocker les secrets en clair ?**  
    a) Cela n'a pas d'avantage  
    b) Accès centralisé, audit complet, rotation des secrets, chiffrement, contrôle d'accès granulaire (RBAC)  
    c) Key Vault est plus lent  
    d) Les secrets sont toujours en clair de toute façon  

***

## Corrections détaillées

1. **b) Gérer et protéger les clés de chiffrement, secrets et certificats**  
   - **Azure Key Vault** est un service de gestion des secrets centralisé et sécurisé : clés de chiffrement, secrets (passwords, API keys…), certificats. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)

2. **b) Clés, secrets (mots de passe, connection strings, API keys), certificats, données binaires**  
   - **Key Vault** supporte : cryptographic keys, secrets (strings, connection strings), certificates (SSL/TLS), et données binaires custom. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)

3. **b) Azure Disk Encryption ou chiffrement de plateforme (Platform-managed keys)**  
   - Les disques Azure sont chiffrés par défaut avec des clés gérées par Microsoft. **Azure Disk Encryption** permet le chiffrement avec clés customer-managed. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)

4. **b) HTTPS (TLS/SSL)**  
   - **HTTPS/TLS** chiffre les données en transit (en chemin) entre client et serveur. C'est le standard pour protéger contre l'interception. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)

5. **b) Application-level encryption (chiffrement côté client) ou service comme Always Encrypted pour SQL**  
   - **Chiffrement applicatif** : la donnée est chiffrée AVANT d'être envoyée au serveur. **Always Encrypted** (SQL) chiffre les colonnes sensibles au niveau application. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)

6. **b) Platform-managed : Microsoft gère les clés. Customer-managed : vous gérez les clés via Key Vault**  
   - **Platform-managed keys** : Microsoft gère la rotation et la sécurité (simple, recommandé pour la plupart). **Customer-managed** : vous avez le contrôle total mais plus de responsabilité. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)

7. **b) Azure Key Vault**  
   - **Key Vault** est le service spécialisé pour gérer les secrets de façon sécurisée : accès contrôlé, audit, chiffrement. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)

8. **b) Utiliser une identité managée (managed identity) pour authentifier via Entra ID**  
   - Les **identités managées** permettent à une application Azure d'accéder à Key Vault sans credentials hardcodés. Azure gère l'authentification. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)

9. **b) Gérer les certificats SSL/TLS, les renouvellements automatiques et le déploiement**  
   - **Key Vault** gère le cycle de vie des certificats : stockage, renouvellement automatique, déploiement sur App Services / Application Gateways. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)

10. **b) Accès centralisé, audit complet, rotation des secrets, chiffrement, contrôle d'accès granulaire (RBAC)**  
    - **Key Vault** offre : centralisation, audit complet (qui a accès à quoi), rotation automatique des secrets, chiffrement fort, RBAC. Bien mieux que stocker les secrets en clair. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)

***

## Fiches de révision synthétiques

### 1. Azure Key Vault – Vue d'ensemble
- **Objectif** : gestion centralisée et sécurisée des secrets critiques. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)
- **Types de contenu** : Keys (cryptographic), Secrets (passwords, API keys…), Certificates (SSL/TLS). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)
- **Niveaux de tarification** : Standard (développement/test), Premium (HSM pour compliance). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)

### 2. Keys dans Key Vault
- **RSA** : asymétrique, chiffrement/signature. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)
- **EC (Elliptic Curve)** : asymétrique, performance élevée. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)
- **Operations** : encrypt, decrypt, sign, verify, wrap key, unwrap key. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)

### 3. Secrets dans Key Vault
- **Connection Strings** : chaînes de connexion base de données. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)
- **API Keys** : clés d'accès aux services externes. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)
- **Passwords** : mots de passe critiques. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)
- **Rotation** : politique de rotation automatique possible. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)

### 4. Certificats dans Key Vault
- **SSL/TLS** : certificats pour HTTPS. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)
- **Issuance** : intégration avec autorités de certification (DigiCert, GlobalSign…). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)
- **Auto-renewal** : renouvellement automatique avant expiration. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)
- **Deployment** : déploiement automatique sur Application Gateway, App Service. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)

### 5. Contrôle d'accès
- **RBAC** : rôles (Key Vault Administrator, Key Vault Secrets Officer…). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)
- **Access Policies** : permissions granulaires par objet (clé, secret, certificat). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)
- **Managed Identities** : applications Azure authentifiées sans credentials. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)
- **Network** : Private Endpoints pour accès privé, Firewalls. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)

### 6. Audit et sécurité
- **Audit Logging** : tous les accès/modifications enregistrés. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)
- **Soft Delete & Purge Protection** : protection contre suppression accidentelle. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)
- **HSM (Hardware Security Module)** : niveau Premium pour conformité stricte. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)

### 7. Chiffrement des données

#### **At Rest (au repos)**
- **Azure Storage Encryption** : par défaut avec platform-managed keys, optionnellement customer-managed. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)
- **Azure Disk Encryption** : chiffrement du système d'exploitation et des données sur disques VM. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)
- **SQL Database TDE (Transparent Data Encryption)** : chiffrement automatique des données SQL. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)

#### **In Transit (en chemin)**
- **HTTPS/TLS** : chiffrement client ↔ serveur. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)
- **VPN / ExpressRoute** : chiffrement pour connexions on-premises ↔ Azure. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)

#### **Application Level (au niveau application)**
- **Client-side encryption** : chiffrer avant envoi au serveur. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)
- **Always Encrypted (SQL)** : colonnes sensibles chiffrées au niveau application. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)

### 8. Intégration des applications
- **SDK (Python, .NET, Node.js…)** : accéder Key Vault directement. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)
- **Managed Identities** : applications authentifiées sans secrets. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)
- **Azure App Configuration** : stocker références à Key Vault pour secrets. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)
- **GitHub Secrets** : intégration CI/CD via GitHub Actions. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)

### 9. Conformité et gouvernance
- **Audit Logging + Log Analytics** : traçabilité complète. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)
- **Azure Policies** : imposer les meilleures pratiques (ex: soft delete enabled). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)
- **Compliance Standards** : aide avec HIPAA, PCI-DSS, SOC 2… [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/configure-azure-key-vault/)
