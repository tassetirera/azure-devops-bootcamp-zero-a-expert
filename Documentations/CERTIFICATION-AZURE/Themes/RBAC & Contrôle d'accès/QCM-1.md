# QCM + corrections détaillées pour l'AZ-104 - Contrôle d'accès et sécurité

***

## QCM (10 questions) - Domaine : Authentification, autorisation et RBAC

1. **Quel est le rôle principal du Role-Based Access Control (RBAC) dans Azure ?**  
   a) Chiffrer les données au repos  
   b) Définir qui peut faire quoi sur quelles ressources  
   c) Gérer les noms de domaine uniquement  
   d) Sauvegarde les données  

2. **Quels sont les trois éléments clés d'une attribution RBAC (role assignment) ?**  
   a) Identité, action, région  
   b) Sécurité principal (identité) + rôle + scope  
   c) Compte + mot de passe + date  
   d) VM + disque + réseau  

3. **Quel rôle RBAC donne tous les droits et ne doit être attribué qu'à des administrateurs approuvés ?**  
   a) Contributor  
   b) Reader  
   c) Owner  
   d) Custom Role  

4. **Vous avez besoin qu'un développeur puisse créer et gérer des ressources dans un Resource Group sans accès aux souscriptions. Quel rôle attribuer ?**  
   a) Owner au niveau subscription  
   b) Contributor au niveau Resource Group  
   c) Reader uniquement  
   d) Aucun accès ne devrait être donné  

5. **Quelle différence entre "Owner" et "Contributor" dans RBAC ?**  
   a) Aucune différence  
   b) Contributor peut tout faire sauf gérer les accès (permissions). Owner peut aussi gérer RBAC.  
   c) Owner ne peut pas supprimer les ressources  
   d) Contributor est plus puissant  

6. **Quel est le principe de sécurité RBAC à appliquer pour limiter les risques ?**  
   a) Donner les droits maximaux à tout le monde  
   b) Accorder uniquement les permissions minimales nécessaires (Least Privilege)  
   c) Les rôles ne sont pas importants  
   d) Tout le monde doit être Owner  

7. **Quel service Azure vous permet de gérer les accès aux ressources via une interface graphique et auditer les changements d'accès ?**  
   a) Azure Storage uniquement  
   b) Azure Access Control (IAM) dans le portail  
   c) Application Insights  
   d) Azure Backup  

8. **Vous avez besoin d'un rôle personnalisé qui combine des permissions spécifiques. Comment le créer ?**  
   a) Les rôles prédéfinis ne peuvent pas être modifiés  
   b) Créer un Custom Role en JSON avec les actions spécifiques (permissions) autorisées  
   c) C'est impossible  
   d) Utiliser uniquement les rôles prédéfinis  

9. **Quel est le scope maximum pour une attribution RBAC dans Azure ?**  
   a) Resource Group  
   b) VM  
   c) Management Group (peut s'appliquer à plusieurs souscriptions)  
   d) Région  

10. **Quel rôle permet seulement de lire les ressources sans pouvoir les modifier ?**  
    a) Contributor  
    b) Owner  
    c) Reader  
    d) Custom Role toujours  

***

## Corrections détaillées

1. **b) Définir qui peut faire quoi sur quelles ressources**  
   - **RBAC (Role-Based Access Control)** contrôle l'accès basé sur les rôles assignés aux utilisateurs/services à un niveau de scope (Resource Group, souscription, Management Group). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)

2. **b) Sécurité principal (identité) + rôle + scope**  
   - Une **role assignment** comprend : **Security Principal** (user, group, service principal) + **Role** (définit les permissions) + **Scope** (Resource, Resource Group, subscription, Management Group). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)

3. **c) Owner**  
   - Le rôle **Owner** a accès complet, incluant la gestion des accès (RBAC). À réserver aux administrateurs approuvés uniquement. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)

4. **b) Contributor au niveau Resource Group**  
   - **Contributor** permet de créer/modifier/supprimer les ressources MAIS pas de gérer les accès. C'est l'attribution appropriée pour un développeur. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)

5. **b) Contributor peut tout faire sauf gérer les accès (permissions). Owner peut aussi gérer RBAC.**  
   - **Owner** = Contributor + droit de gérer les rôles et accès. **Contributor** = créer/modifier ressources mais pas de gestion RBAC. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)

6. **b) Accorder uniquement les permissions minimales nécessaires (Least Privilege)**  
   - Le **Least Privilege Principle** minimise les risques de sécurité : donner uniquement les droits nécessaires pour accomplir la tâche, rien de plus. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)

7. **b) Azure Access Control (IAM) dans le portail**  
   - Le panneau **Access Control (IAM)** dans Azure Portal permet d'assigner des rôles, consulter les attributions actuelles et auditer les changements. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)

8. **b) Créer un Custom Role en JSON avec les actions spécifiques (permissions) autorisées**  
   - Les **Custom Roles** permettent de définir des permissions fine-grained en JSON (spécifier les actions autorisées/refusées). Utile pour des besoins spécifiques métier. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)

9. **c) Management Group (peut s'appliquer à plusieurs souscriptions)**  
   - **Management Groups** organisent les souscriptions hiérarchiquement et les rôles assignés à ce niveau s'appliquent à tous les enfants. C'est le scope maximum. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)

10. **c) Reader**  
    - Le rôle **Reader** permet uniquement de lire les ressources, pas de les modifier ni de gérer les accès. Idéal pour l'audit et la consultation. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)

***

## Fiches de révision synthétiques

### 1. Fondamentaux du RBAC
- **Role Assignment** = Security Principal + Role + Scope. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)
- **Security Principal** : utilisateur (comptes AAD), groupes (AAD groups), service principals (applications), managed identities. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)
- **Role** : ensemble de permissions prédéfinies (Owner, Contributor, Reader…) ou custom. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)
- **Scope** : Resource, Resource Group, souscription, Management Group (hiérarchique). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)

### 2. Rôles prédéfinis courants
- **Owner** : accès complet + gestion RBAC. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)
- **Contributor** : créer/modifier/supprimer ressources, sauf gestion RBAC. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)
- **Reader** : lecture seule, pas de modifications. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)
- **User Access Administrator** : gérer les rôles d'accès (sans créer ressources). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)

### 3. Rôles spécifiques par service
- **Virtual Machine Contributor** : gérer les VMs uniquement. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)
- **Storage Blob Data Contributor** : accès aux données dans Blob Storage (pas la gestion du compte). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)
- **Key Vault Administrator** : gérer les secrets/certificats. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)

### 4. Custom Roles
- Créer un rôle personnalisé en **JSON** pour permissions fine-grained. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)
- Actions possibles : `"Microsoft.Compute/virtualMachines/start/action"` (ex: démarrer une VM). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)
- Scopes de custom role : Management Group, souscription. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)

### 5. Management Groups
- **Management Groups** : conteneurs hiérarchiques pour souscriptions. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)
- Les **policies**, **RBAC**, **budgets** au niveau Management Group s'appliquent en cascade aux enfants. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)
- Permet une gouvernance multi-souscription centralisée. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)

### 6. Bonnes pratiques de sécurité
- **Least Privilege** : attribuer le minimum de permissions nécessaires. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)
- Éviter Owner au niveau subscription (privilège maximal). Préférer Owner au niveau Resource Group. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)
- Utiliser des groupes AAD au lieu d'assignations individuelles pour scalabilité. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)
- Auditer régulièrement les assignations RBAC via Access Control (IAM). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)

### 7. Intégration avec Entra ID
- **Azure RBAC** utilise **Microsoft Entra ID** comme backend pour l'authentification. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)
- Les utilisateurs/groupes AAD peuvent être assignés à des rôles Azure. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)
- **Managed Identities** (service principals) peuvent aussi recevoir des rôles RBAC pour l'authentification inter-services. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)
