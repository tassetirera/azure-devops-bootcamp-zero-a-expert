# QCM + corrections détaillées pour l'AZ-104 - Scénarios et synthèse Microsoft Entra ID

***

## QCM (10 questions) - Domaine : Scénarios et synthèse

1. **Dans quel cas Entra ID est-il le plus approprié ?**  
   a) Pour sécuriser les applications cloud et hybrides  
   b) Pour gérer uniquement des applications on-premises  
   c) Pour stocker des fichiers  
   d) Pour gérer un DNS public  

2. **Quel service Entra ID complète pour offrir des fonctionnalités d'annuaire cloud ?**  
   a) Azure Monitor  
   b) Microsoft Entra Domain Services  
   c) Azure Storage  
   d) Azure DevOps  

3. **Quel composant d'Entra ID permet de gérer les utilisateurs invités externes ?**  
   a) Azure AD B2B  
   b) Azure AD Connect  
   c) Entra Domain Services  
   d) Azure Backup  

4. **Quel concept décrit une organisation de type cloud dans Entra ID ?**  
   a) Tenant  
   b) Forêt  
   c) Domaine local  
   d) Unité d'organisation  

5. **Quel service Entra ID ne remplace pas ?**  
   a) Azure AD Connect  
   b) Azure Application Proxy  
   c) Contrôleurs de domaine AD DS  
   d) Azure AD B2C  

6. **Quel est l’avantage de la gestion des identités dans Entra ID par rapport aux annuaires locaux ?**  
   a) SLA plus faible  
   b) Aucune authentification possible  
   c) Pas de gestion d'infrastructure de contrôleurs de domaine  
   d) Pas de gestion d'applications  

7. **Quel service est utilisé pour faire migrer des applications héritées vers Azure sans GPO ni contrôleur de domaine local ?**  
   a) Entra ID Gratuit  
   b) Entra Domain Services  
   c) Azure AD Connect  
   d) Azure Functions  

8. **Quel est le meilleur argument pour utiliser Entra ID P1 plutôt que l'édition gratuite ?**  
   a) Plus de capacité de stockage  
   b) Accès conditionnel et SSO illimité  
   c) Des VMs plus performantes  
   d) Un réseau plus sécurisé  

9. **Quel élément est essentiel pour comprendre la sécurité Entra ID ?**  
   a) La facturation  
   b) Les protocoles d'authentification moderne  
   c) Les VM sizes  
   d) Les comptes de stockage  

10. **Quel terme décrit une solution de sécurité des droits d'administrateurs dans Entra ID ?**  
    a) Azure Firewall  
    b) Privileged Identity Management  
    c) Azure AD Connect  
    d) VNet Peering  

***

## Corrections détaillées

1. **a) Pour sécuriser les applications cloud et hybrides**  
   - Entra ID est principalement conçu pour la gestion des identités dans les scénarios cloud et hybrides.

2. **b) Microsoft Entra Domain Services**  
   - Entra Domain Services complète Entra ID en fournissant des services hérités de type AD sans contrôleurs de domaine.

3. **a) Azure AD B2B**  
   - La collaboration B2B permet d'inviter des utilisateurs externes dans Entra ID.

4. **a) Tenant**  
   - Un tenant Entra ID est l'organisation cloud qui contient les identités.

5. **c) Contrôleurs de domaine AD DS**  
   - Entra ID ne remplace pas les contrôleurs de domaine AD DS ; il les complète ou les remplace dans certains scénarios avec Entra Domain Services.

6. **c) Pas de gestion d'infrastructure de contrôleurs de domaine**  
   - Entra ID est un service cloud managé, sans nécessité de gérer des contrôleurs de domaine physiques.

7. **b) Entra Domain Services**  
   - Entra Domain Services permet de migrer des applications héritées basées sur LDAP/Kerberos.

8. **b) Accès conditionnel et SSO illimité**  
   - P1 apporte des fonctionnalités avancées comme l'accès conditionnel et un SSO sans limite.

9. **b) Les protocoles d'authentification moderne**  
   - Comprendre OAuth, OIDC et SAML est essentiel pour la sécurité Entra ID.

10. **b) Privileged Identity Management**  
    - PIM est la solution de gestion des droits d'administrateurs dans Entra ID.
