# QCM + corrections détaillées pour l'AZ-104 - Scénarios hybrides avec Entra ID

***

## QCM (10 questions) - Domaine : Scénarios hybrides et synchronisation

1. **Quel outil permet de synchroniser les objets AD DS vers Entra ID ?**  
   a) Azure Backup  
   b) Azure AD Connect  
   c) Azure Firewall  
   d) Azure Policy  

2. **Quel type de synchronisation est utilisé entre AD DS et Entra ID ?**  
   a) Bidirectionnelle  
   b) Unidirectionnelle  
   c) Aucune synchronisation  
   d) Aléatoire  

3. **Quelle identité peut être synchronisée depuis un AD local vers Entra ID ?**  
   a) Utilisateur  
   b) Disque  
   c) VNet  
   d) Storage Account  

4. **Un environnement hybride avec Entra ID implique généralement :**  
   a) Un tenant cloud et un AD local  
   b) Un réseau privé seulement  
   c) Aucun service cloud  
   d) Une seule machine virtuelle  

5. **Quel type d'accès est possible pour un utilisateur synchronisé en hybride ?**  
   a) Accès uniquement local  
   b) Accès aux ressources cloud et locales selon la configuration  
   c) Accès uniquement aux disques  
   d) Aucun accès  

6. **Quel protocole est directement lié à la synchronisation d'annuaire sur site ?**  
   a) Kerberos  
   b) LDAP  
   c) FTP  
   d) SNMP  

7. **Quel service permet aux appareils Windows de s'authentifier avec Entra ID ?**  
   a) Azure DNS  
   b) Enregistrement d'appareil  
   c) Azure Backup  
   d) Azure Monitor  

8. **Quel bénéfice majeur apporte la synchronisation Entra Connect ?**  
   a) Réduction des coûts de stockage  
   b) Cohérence des identités entre local et cloud  
   c) Meilleure performance du réseau  
   d) Création automatique de VMs  

9. **Quel composant Entra ID permet de sécuriser les accès en fonction du contexte ?**  
   a) Azure Storage  
   b) Accès conditionnel  
   c) VNet Peering  
   d) Availability Zone  

10. **Quelle affirmation décrit le mieux un scénario hybride ?**  
    a) Tous les comptes sont uniquement dans le cloud  
    b) Les comptes sont gérés à la fois sur site et dans Entra ID  
    c) Aucune synchronisation entre local et cloud  
    d) Les identités sont uniquement gérées par Azure Monitor  

***

## Corrections détaillées

1. **b) Azure AD Connect**  
   - Azure AD Connect synchronise les objets AD DS vers Entra ID pour un scénario hybride.

2. **b) Unidirectionnelle**  
   - La synchronisation d'AD DS vers Entra ID est unidirectionnelle par défaut.

3. **a) Utilisateur**  
   - Les comptes utilisateurs et groupes peuvent être synchronisés depuis AD local.

4. **a) Un tenant cloud et un AD local**  
   - Un environnement hybride combine un tenant Entra ID avec une infrastructure AD locale.

5. **b) Accès aux ressources cloud et locales selon la configuration**  
   - Les utilisateurs synchronisés peuvent accéder aux ressources dans les deux environnements quand cela est configuré.

6. **b) LDAP**  
   - AD DS utilise LDAP pour l'annuaire, tandis qu'Entra ID utilise des protocoles modernes.

7. **b) Enregistrement d'appareil**  
   - L'enregistrement d'appareil permet aux appareils de s'authentifier et d'être gérés par Entra ID.

8. **b) Cohérence des identités entre local et cloud**  
   - Entra Connect assure que les identités locales et cloud restent cohérentes.

9. **b) Accès conditionnel**  
   - L'accès conditionnel applique des règles de sécurité en fonction du contexte de connexion.

10. **b) Les comptes sont gérés à la fois sur site et dans Entra ID**  
    - C'est la définition d'un environnement hybride.
