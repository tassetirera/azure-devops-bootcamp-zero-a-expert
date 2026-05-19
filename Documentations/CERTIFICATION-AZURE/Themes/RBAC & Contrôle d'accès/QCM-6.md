# QCM + corrections détaillées pour l'AZ-104 - Rôles et permissions Azure (Révision 6)

***

## QCM (10 questions) - Domaine : Rôles et permissions Azure (Révision 6)

1. **Quel élément définit qui peut faire quoi dans Azure ?**  
   a) NSG
   b) RBAC
   c) Azure Policy
   d) Load Balancer

2. **Quel rôle prédéfini offre l'accès complet incluant gestion RBAC ?**  
   a) Contributor
   b) Reader
   c) Owner
   d) User Access Admin

3. **Quel rôle permet de créer/modifier ressources mais pas de gérer RBAC ?**  
   a) Owner
   b) Contributor
   c) Reader
   d) Custom Role

4. **Quel rôle offre accès en lecture seule ?**  
   a) Owner
   b) Contributor
   c) Reader
   d) Operator

5. **Quel principe limite les permissions au strict nécessaire ?**  
   a) Maximum Privilege
   b) Least Privilege
   c) Full Access
   d) No Restriction

6. **Quel est le plus grand scope pour une attribution RBAC ?**  
   a) Resource
   b) Resource Group
   c) Subscription
   d) Management Group

7. **Quel service permet de créer des rôles personnalisés ?**  
   a) Azure Policy
   b) Custom Roles
   c) Azure Blueprints
   d) Azure Advisor

8. **Quel conteneur hiérarchique organise les souscriptions ?**  
   a) Resource Group
   b) Management Group
   c) Tenant
   d) Tag

9. **Quel service gère les accès périodiquement en vérifiant les utilisateurs ?**  
   a) Azure Backup
   b) Access Reviews
   c) Azure Monitor
   d) Azure Policy

10. **Quel mécanisme sépare les tâches pour réduire les risques ?**  
   a) Shared Admin
   b) Full Control
   c) Separation of Duties
   d) Single Admin

***

## Corrections détaillées

1. **b) RBAC**  
   - RBAC est le modèle de contrôle d'accès dans Azure.

2. **c) Owner**  
   - Owner a tous les droits incluant RBAC.

3. **b) Contributor**  
   - Contributor crée/modifie mais ne peut pas gérer RBAC.

4. **c) Reader**  
   - Reader ne peut que consulter les ressources.

5. **b) Least Privilege**  
   - Least Privilege minimise la surface d'attaque.

6. **d) Management Group**  
   - Management Group est le scope maximal en cascade.

7. **b) Custom Roles**  
   - Custom Roles permettent des permissions fine-grained.

8. **b) Management Group**  
   - Management Groups organisent les souscriptions hiérarchiquement.

9. **b) Access Reviews**  
   - Access Reviews valident périodiquement qui a accès à quoi.

10. **c) Separation of Duties**  
   - Separation of Duties divise les responsabilités administratives.
