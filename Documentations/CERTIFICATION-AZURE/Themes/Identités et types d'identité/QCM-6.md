# QCM + corrections détaillées pour l'AZ-104 - Flux et bonnes pratiques d’identité

***

## QCM (10 questions) - Domaine : Flux et bonnes pratiques d’identité

1. **Quel flux d’authentification est utilisé pour les applications web via OAuth ?**  
   a) Client Credentials
   b) Authorization Code
   c) SMB
   d) FTP

2. **Quel type de compte est le plus sûr pour un service automatisé ?**  
   a) Compte utilisateur
   b) Principal de service
   c) Identité d’appareil
   d) Identité B2C

3. **Quel élément doit être appliqué pour limiter l’accès aux ressources selon l’emplacement ?**  
   a) Azure Policy
   b) NSG
   c) Conditional Access
   d) Azure DNS

4. **Quel service gère le cycle de vie de l’identité des employés externes ?**  
   a) Azure AD B2B
   b) Azure AD Domain Services
   c) Azure Key Vault
   d) Azure Monitor

5. **Quel type d’identité est le plus approprié pour une application Web SaaS consommée par des clients ?**  
   a) Azure AD B2C
   b) Azure AD B2B
   c) Azure AD Connect
   d) Azure Disk Encryption

6. **Pour une application interne, quel type d’identité offre le meilleur contrôle RBAC ?**  
   a) Identité utilisateur
   b) Principal de service
   c) Identité d’appareil
   d) Identité hybride

7. **Quel concept décrit le fait de donner le minimum de permissions nécessaire ?**  
   a) Least Privilege
   b) Maximum Privilege
   c) Full Access
   d) Owner Rights

8. **Quel service permet de tester des règles d’authentification en conditions réelles ?**  
   a) Azure AD Access Reviews
   b) Azure Backup
   c) Azure Policy
   d) Azure DNS

9. **Quel outil Azure permet de synchroniser uniquement les mots de passe et les comptes ?**  
   a) Azure AD Connect
   b) Azure Site Recovery
   c) Azure VM Scale Sets
   d) Azure Application Gateway

10. **Quel rôle Entra est nécessaire pour gérer les politiques d’accès conditionnel ?**  
   a) Security Administrator
   b) Reader
   c) Storage Blob Data Owner
   d) Network Contributor

***

## Corrections détaillées

1. **b) Authorization Code**  
   - Le flux Authorization Code est utilisé pour les applications web OAuth.

2. **b) Principal de service**  
   - Un principal de service est plus sûr pour les services automatisés.

3. **c) Conditional Access**  
   - Conditional Access limite l’accès selon le contexte et l’emplacement.

4. **a) Azure AD B2B**  
   - Azure AD B2B gère les invités et partenaires externes.

5. **a) Azure AD B2C**  
   - Azure AD B2C cible les clients grand public.

6. **b) Principal de service**  
   - Les principals de service sont bien adaptés au contrôle RBAC des applications.

7. **a) Least Privilege**  
   - Least Privilege limite les permissions au strict nécessaire.

8. **a) Azure AD Access Reviews**  
   - Access Reviews permet de vérifier les accès périodiquement.

9. **a) Azure AD Connect**  
   - Azure AD Connect synchronise comptes et mots de passe depuis AD local.

10. **a) Security Administrator**  
   - Security Administrator gère les politiques de sécurité Entra.
