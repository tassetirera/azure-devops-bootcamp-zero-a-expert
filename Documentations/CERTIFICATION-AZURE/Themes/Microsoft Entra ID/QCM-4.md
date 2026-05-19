# QCM + corrections détaillées pour l'AZ-104 - Publication des applications avec Entra ID

***

## QCM (10 questions) - Domaine : Proxy d'application et intégration SaaS

1. **Quel est l'objectif principal du Proxy d'application dans Microsoft Entra ID ?**  
   a) Stocker des applications dans Azure  
   b) Publier des applications locales sur internet de façon sécurisée  
   c) Déployer des machines virtuelles  
   d) Chiffrer les données en transit  

2. **Le Proxy d'application permet de publier des applications locales sans utiliser :**  
   a) Un service cloud  
   b) Un VPN ou une DMZ  
   c) Une application mobile  
   d) Azure AD Connect  

3. **Quel type d'application peut être publié via Azure Application Proxy ?**  
   a) Une application web interne  
   b) Un disque managé  
   c) Un groupe de ressources  
   d) Un VNet  

4. **La galerie Entra ID contient plus de combien d'applications pré-intégrées ?**  
   a) 300  
   b) 3 000  
   c) 30  
   d) 300 000  

5. **Quels sont des exemples d'applications SaaS pré-intégrées ?**  
   a) Salesforce et Slack  
   b) SQL Server et Redis  
   c) VNet et Firewall  
   d) Disques Azure  

6. **Quel protocole est généralement utilisé pour sécuriser l'accès des applications dans Entra ID ?**  
   a) HTTP  
   b) OpenID Connect  
   c) FTP  
   d) Telnet  

7. **Le Proxy d'application permet aux utilisateurs d'accéder à une application locale comme à une application :**  
   a) SaaS  
   b) Desktop  
   c) Serveur DNS  
   d) Stockage  

8. **Quelle affirmation est vraie concernant le Proxy d'application ?**  
   a) Il remplace Azure AD Connect  
   b) Il publie les applications sans exposer directement le réseau local  
   c) Il remplace les contrôleurs de domaine  
   d) Il gère les utilisateurs B2B  

9. **Quel service n'est PAS directement concerné par le Proxy d'application ?**  
   a) Application web interne  
   b) Application Bureau à distance  
   c) Application SaaS pré-intégrée  
   d) Application métier locale  

10. **Pourquoi utiliser le Proxy d'application plutôt qu'un VPN pour accéder aux applications internes ?**  
    a) Parce qu'il est gratuit  
    b) Parce qu'il fournit un accès sécurisé sans exposer le réseau local  
    c) Parce qu'il augmente la bande passante  
    d) Parce qu'il crée des machines virtuelles  

***

## Corrections détaillées

1. **b) Publier des applications locales sur internet de façon sécurisée**  
   - Le Proxy d'application expose des applications internes sans nécessiter un VPN direct.

2. **b) Un VPN ou une DMZ**  
   - Le Proxy d'application fonctionne sans VPN ni DMZ, tout en assurant un accès sécurisé.

3. **a) Une application web interne**  
   - Il est conçu pour publier des applications web internes de manière sécurisée.

4. **b) 3 000**  
   - La galerie Entra ID contient plus de 3 000 applications pré-intégrées.

5. **a) Salesforce et Slack**  
   - Ces applications sont des exemples courants d'applications SaaS pré-intégrées.

6. **b) OpenID Connect**  
   - OpenID Connect est un protocole moderne utilisé pour sécuriser l'accès aux applications.

7. **a) SaaS**  
   - Le Proxy d'application permet aux applications internes d'être accessibles comme des applications SaaS.

8. **b) Il publie les applications sans exposer directement le réseau local**  
   - Le trafic est proxifié de manière sécurisée par Azure.

9. **c) Application SaaS pré-intégrée**  
   - Les applications SaaS pré-intégrées ne passent pas par le Proxy d'application ; elles sont déjà cloud.

10. **b) Parce qu'il fournit un accès sécurisé sans exposer le réseau local**  
    - Le Proxy d'application réduit le besoin d'un accès réseau direct comme un VPN.
