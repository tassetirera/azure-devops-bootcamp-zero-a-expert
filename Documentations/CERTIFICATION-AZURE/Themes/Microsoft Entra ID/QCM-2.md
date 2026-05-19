# QCM + corrections détaillées pour l'AZ-104 - Entra ID vs Active Directory Domain Services

***

## QCM (10 questions) - Domaine : Entra ID vs AD DS

1. **Quelle différence principale existe entre AD DS et Microsoft Entra ID ?**  
   a) AD DS est un service cloud, Entra ID est local  
   b) AD DS utilise LDAP et Kerberos, Entra ID utilise OAuth/OIDC/SAML  
   c) AD DS gère les applications SaaS, Entra ID ne le fait pas  
   d) Il n'y a pas de différence  

2. **Quelle structure de gestion est présente dans AD DS mais pas dans Entra ID ?**  
   a) Unités d'organisation (OU)  
   b) Tenants  
   c) App registrations  
   d) Groupes dynamiques  

3. **Quel protocole est utilisé par Entra ID pour permetre l'authentification moderne ?**  
   a) SMB  
   b) OAuth 2.0  
   c) FTP  
   d) Telnet  

4. **Quel mécanisme Entra ID utilise-t-il pour permettre l'accès aux applications cloud ?**  
   a) GPO  
   b) OpenID Connect  
   c) NTLM  
   d) Kerberos  

5. **Quel est l'objectif principal de Microsoft Entra Connect ?**  
   a) Chiffrer les données dans Azure  
   b) Synchroniser les identités d'AD DS vers Entra ID  
   c) Gérer les certificats SSL  
   d) Déployer des machines virtuelles  

6. **Dans quel type d'environnement Entra ID est-il le plus adapté ?**  
   a) Environnements locaux seulement  
   b) Environnements cloud et hybrides  
   c) Réseaux isolés sans Internet  
   d) Environnements SAP uniquement  

7. **Quel type d'identité n'est pas géré par AD DS mais par Entra ID ?**  
   a) Utilisateur interne  
   b) Invité B2B  
   c) Compte ordinateur  
   d) Compte de service  

8. **Quel mode d'authentification des appareils est utilisé avec Entra ID ?**  
   a) Jointure de domaine classique  
   b) Enregistrement d'appareil (device registration)  
   c) NTP  
   d) DHCP  

9. **Quelle technologie AD DS supporte-t-elle mais Entra ID ne propose pas nativement ?**  
   a) OAuth 2.0  
   b) LDAP  
   c) MFA  
   d) SSO  

10. **Quel élément est une caractéristique d'Entra ID mais pas d'AD DS ?**  
    a) Structure plate basée sur un tenant  
    b) Forêts et domaines  
    c) Contrôleurs de domaine  
    d) Unités d'organisation  

***

## Corrections détaillées

1. **b) AD DS utilise LDAP et Kerberos, Entra ID utilise OAuth/OIDC/SAML**  
   - AD DS est conçu autour de protocoles hérités, tandis qu'Entra ID utilise des protocoles modernes adaptés au cloud.

2. **a) Unités d'organisation (OU)**  
   - Entra ID a une structure plate sans OUs, contrairement à AD DS qui utilise des forêts, domaines et OUs.

3. **b) OAuth 2.0**  
   - Entra ID utilise OAuth 2.0 pour l'authentification moderne, souvent avec OpenID Connect et SAML.

4. **b) OpenID Connect**  
   - OpenID Connect est un protocole moderne pour l'authentification des applications cloud.

5. **b) Synchroniser les identités d'AD DS vers Entra ID**  
   - Microsoft Entra Connect permet de synchroniser les utilisateurs et groupes d'un AD local vers Entra ID.

6. **b) Environnements cloud et hybrides**  
   - Entra ID est conçu pour les scénarios cloud et hybrides, pas uniquement pour les environnements locaux.

7. **b) Invité B2B**  
   - Entra ID prend en charge les utilisateurs invités B2B, ce que AD DS ne gère pas nativement.

8. **b) Enregistrement d'appareil (device registration)**  
   - Entra ID gère l'enregistrement d'appareils pour la gestion et l'accès conditionnel.

9. **b) LDAP**  
   - AD DS supporte LDAP, alors qu'Entra ID n'est pas un annuaire LDAP natif.

10. **a) Structure plate basée sur un tenant**  
    - Entra ID est basé sur un tenant plat, contrairement aux structures hiérarchiques d'AD DS.
