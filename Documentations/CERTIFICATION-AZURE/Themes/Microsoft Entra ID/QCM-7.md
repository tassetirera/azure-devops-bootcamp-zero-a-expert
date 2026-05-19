# QCM + corrections détaillées pour l'AZ-104 - Microsoft Entra Domain Services

***

## QCM (10 questions) - Domaine : Entra Domain Services

1. **Quel service fournit des fonctionnalités LDAP et Kerberos dans Azure sans gérer de contrôleurs de domaine ?**  
   a) Azure AD Connect  
   b) Entra Domain Services  
   c) Azure Active Directory  
   d) Azure DNS  

2. **Entra Domain Services offre-t-il des forêts et des trusts complexes ?**  
   a) Oui  
   b) Non  
   c) Seulement dans P2  
   d) Seulement avec AD Connect  

3. **Quel protocole n'est PAS pris en charge par Entra Domain Services ?**  
   a) LDAP  
   b) Kerberos  
   c) NTLM  
   d) SMB  

4. **Entra Domain Services synchronise les identités depuis :**  
   a) Azure Storage  
   b) Entra ID  
   c) Azure Monitor  
   d) Azure Firewall  

5. **Quel type d'application profite le plus d'Entra Domain Services ?**  
   a) Applications cloud natives  
   b) Applications héritées utilisant LDAP/Kerberos  
   c) Applications purement mobiles  
   d) Services Azure Functions  

6. **Qui gère l'infrastructure d'Entra Domain Services ?**  
   a) L'entreprise cliente  
   b) Microsoft  
   c) Un fournisseur tiers  
   d) Les utilisateurs  

7. **Quelle fonctionnalité Entra Domain Services propose-t-il pour les applications héritées ?**  
   a) Service managé de domaine compatible AD  
   b) Gestion de conteneurs  
   c) Monitoring temps réel  
   d) Déploiement de VMs  

8. **Quel élément n'est pas possible avec Entra Domain Services ?**  
   a) Jointure de domaine  
   b) LDAP  
   c) Extendre le schéma  
   d) Utiliser Kerberos  

9. **Entra Domain Services peut aider à remplacer :**  
   a) Les applications SaaS  
   b) L'infrastructure AD locale  
   c) Le stockage de blobs  
   d) Le gestionnaire de mots de passe  

10. **Quel est un cas d'usage typique pour Entra Domain Services ?**  
    a) Migrer des applications héritées vers Azure  
    b) Créer des API REST  
    c) Gérer des réseaux virtuels  
    d) Sauvegarder des bases de données  

***

## Corrections détaillées

1. **b) Entra Domain Services**  
   - Entra Domain Services propose LDAP, Kerberos et NTLM en tant que service managé.

2. **b) Non**  
   - Entra Domain Services ne supporte pas les forêts complexes ou les trusts avancés.

3. **d) SMB**  
   - SMB n'est pas le protocole principal d'authentification géré par Entra Domain Services.

4. **b) Entra ID**  
   - Le service synchronise unidirectionnellement les identités depuis Entra ID.

5. **b) Applications héritées utilisant LDAP/Kerberos**  
   - Ces applications peuvent migrer sur Entra Domain Services sans changer leur authentification.

6. **b) Microsoft**  
   - L'infrastructure est entièrement gérée par Microsoft.

7. **a) Service managé de domaine compatible AD**  
   - Le service fournit une compatibilité AD sans nécessiter de contrôleurs de domaine.

8. **c) Extendre le schéma**  
   - L'extension de schéma n'est pas prise en charge par Entra Domain Services.

9. **b) L'infrastructure AD locale**  
   - Il aide à réduire la dépendance aux contrôleurs de domaine on-premises.

10. **a) Migrer des applications héritées vers Azure**  
    - C'est un cas d'usage typique pour Entra Domain Services.
