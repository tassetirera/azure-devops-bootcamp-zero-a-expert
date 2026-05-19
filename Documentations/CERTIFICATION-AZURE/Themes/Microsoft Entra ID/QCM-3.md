# QCM + corrections détaillées pour l'AZ-104 - Entra ID et les applications cloud

***

## QCM (10 questions) - Domaine : Applications et SSO

1. **Quel composant Entra ID est utilisé pour représenter une application cloud ?**  
   a) App registration  
   b) Resource Group  
   c) Storage Account  
   d) Virtual Network  

2. **Quel mécanisme permet à une application de s'authentifier via Entra ID ?**  
   a) App registration  
   b) NSG  
   c) Log Analytics  
   d) Load Balancer  

3. **Quel protocole est recommandé pour l'authentification d'une application web moderne ?**  
   a) SMTP  
   b) OpenID Connect  
   c) FTP  
   d) SMB  

4. **Quel type d'application Entra ID peut gérer en mode SaaS pré-intégré ?**  
   a) Une application locale non cloud  
   b) Une application tierce telle que Slack ou Salesforce  
   c) Un disque managé  
   d) Un réseau virtuel  

5. **Que permet le Single Sign-On pour les utilisateurs d'applications SaaS ?**  
   a) Un accès sans mot de passe obligé  
   b) Une seule authentification pour plusieurs applications  
   c) Un accès uniquement aux applications Microsoft  
   d) Un chiffrement des données  

6. **Quel type d'application Entra ID stocke les informations d'identification et les permissions de l'application ?**  
   a) App Service  
   b) App registration  
   c) Managed Disk  
   d) Azure Function  

7. **Quel protocole est principalement utilisé pour l'autorisation des ressources d'une API ?**  
   a) OAuth 2.0  
   b) RDP  
   c) ICMP  
   d) DNS  

8. **Quel composant Entra ID permet de gérer les permissions des applications sur les API ?**  
   a) Roles RBAC  
   b) App registration et API permissions  
   c) Network Security Group  
   d) Storage Account  

9. **Quelle confusion faut-il éviter entre Entra ID et AD DS pour les applications ?**  
   a) Croire qu'Entra ID gère les GPO comme AD DS  
   b) Croire qu'Entra ID ne gère pas l'authentification  
   c) Croire qu'Entra ID ne peut pas être utilisé avec les applications mobiles  
   d) Croire qu'Entra ID remplace les disques managés  

10. **Quel service permet de publier des applications internes vers internet de façon sécurisée ?**  
    a) Azure Application Proxy  
    b) Azure Backup  
    c) Azure Monitor  
    d) Azure Storage  

***

## Corrections détaillées

1. **a) App registration**  
   - Une **App registration** représente une application dans Entra ID et permet de configurer son identité et ses permissions.

2. **a) App registration**  
   - L'enregistrement d'application permet à une application de s'authentifier auprès d'Entra ID.

3. **b) OpenID Connect**  
   - OpenID Connect est un protocole recommandé pour l'authentification des applications web modernes.

4. **b) Une application tierce telle que Slack ou Salesforce**  
   - Entra ID supporte des applications pré-intégrées en mode SaaS via la galerie d'applications.

5. **b) Une seule authentification pour plusieurs applications**  
   - Le SSO permet aux utilisateurs de se connecter une fois et d'accéder à plusieurs applications.

6. **b) App registration**  
   - L'enregistrement d'application stocke les informations d'identification et les permissions nécessaires.

7. **a) OAuth 2.0**  
   - OAuth 2.0 est le protocole d'autorisation standard utilisé pour les API modernes.

8. **b) App registration et API permissions**  
   - Entra ID utilise les enregistrements d'applications et les permissions d'API pour contrôler l'accès des apps aux ressources.

9. **a) Croire qu'Entra ID gère les GPO comme AD DS**  
   - Entra ID n'utilise pas de GPO ; c'est une différence clé avec AD DS.

10. **a) Azure Application Proxy**  
    - Le Proxy d'application permet de publier des applications internes de manière sécurisée sans VPN ou DMZ.
