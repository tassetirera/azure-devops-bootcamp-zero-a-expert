# QCM + corrections détaillées pour l'AZ-104 - Gestion des ressources Azure

***

## QCM (10 questions) - Domaine : Gestion des ressources et du stockage

1. **Quel est le rôle principal d'une ressource Azure Resource Group ?**  
   a) Stocker les données de façon permanente  
   b) Gérer le cycle de vie des ressources et déployer une solution cohérente  
   c) Authentifier les utilisateurs uniquement  
   d) Gérer le trafic réseau entre ressources  

2. **Vous déployez une application multi-régions. Combien de Resource Groups devez-vous au minimum créer ?**  
   a) Un seul, peu importe la région  
   b) Un par région pour faciliter la gestion  
   c) Cela dépend de l'architecture et des politiques d'organisation  
   d) Dix, un par service Azure  

3. **Quelle est la meilleure pratique pour étiqueter les ressources Azure (Tags) ?**  
   a) Utiliser des balises sans structure définie  
   b) Utiliser un système cohérent avec les bonnes pratiques métier (environment, project, cost-center…)  
   c) Les tags ne sont pas importants  
   d) Étiqueter uniquement les ressources critiques  

4. **Quel type de stockage Azure est idéal pour les données structurées qui nécessitent des transactions ACID ?**  
   a) Azure Blob Storage  
   b) Azure Queue Storage  
   c) Azure Table Storage  
   d) Azure SQL Database  

5. **Vous disposez d'une machine virtuelle Azure qui a besoin d'un stockage haute performance pour une base de données. Quel type de disque managé recommandez-vous ?**  
   a) Standard HDD  
   b) Standard SSD  
   c) Premium SSD  
   d) Ultra Disk (pour I/O ultra-rapide)  

6. **Quel niveau de stockage Blob (Hot, Cool, Archive) est le plus économique pour les données rarement consultées ?**  
   a) Hot (accès fréquent)  
   b) Cool (accès occasionnel)  
   c) Archive (accès très rare)  
   d) Tous les niveaux coûtent pareil  

7. **Quelle est la différence clé entre un managed disk et un storage account ?**  
   a) Un managed disk est uniquement pour le stockage d'objets  
   b) Un managed disk est un volume de stockage bloc attaché à une VM, un storage account est un service polyvalent  
   c) Un storage account gère les identités  
   d) Il n'y a pas de différence  

8. **Vous avez besoin de déplacer 50 TB de données entre deux régions Azure. Quelle solution est la plus appropriée ?**  
   a) Uploader via internet (réseau)  
   b) Utiliser Azure Import/Export ou Data Box  
   c) Copier fichier par fichier manuellement  
   d) Cela n'est pas possible  

9. **Quel service Azure vous permet de gérer la capacité de calcul pour plusieurs machines virtuelles avec mise à l'échelle automatique ?**  
   a) Application Insights  
   b) Virtual Machine Scale Sets (VMSS)  
   c) Storage Accounts  
   d) Key Vault  

10. **Quelle est l'utilité d'une policy Azure ?**  
    a) Authentifier les utilisateurs  
    b) Définir des règles d'application et de conformité pour les ressources Azure  
    c) Gérer uniquement le stockage  
    d) Sauvegarde les données  

***

## Corrections détaillées

1. **b) Gérer le cycle de vie des ressources et déployer une solution cohérente**  
   - Un **Resource Group** est un conteneur logique qui permet de gérer, déployer, détruire et facturer un ensemble de ressources de façon groupée. [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/control-and-organize-with-azure-resource-manager/)

2. **c) Cela dépend de l'architecture et des politiques d'organisation**  
   - Il n'y a pas de règle fixe. Généralement, on crée un RG par région ou par environnement (dev, prod, staging) selon les besoins de gestion, facturation et conformité. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)

3. **b) Utiliser un système cohérent avec les bonnes pratiques métier (environment, project, cost-center…)**  
   - Les **tags** permettent d'organiser les ressources pour facturation, automatisation, gestion des droits d'accès. Adopter une convention commune (env:prod, project:erp, etc.) est essentiel pour l'échelle. [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/control-and-organize-with-azure-resource-manager/)

4. **d) Azure SQL Database**  
   - **Azure SQL Database** est un service de base de données relationnelle managé qui supporte les transactions ACID. Azure Blob Storage est pour les fichiers binaires, Queue pour les messages, Table pour les données sans schéma. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/explore-azure-storage-services/)

5. **d) Ultra Disk (pour I/O ultra-rapide)**  
   - Pour une base de données nécessitant des performances maximales, **Ultra Disk** offre la latence et le débit les plus élevés (jusqu'à 160,000 IOPS). Premium SSD est bon pour la plupart des cas (20,000 IOPS). [learn.microsoft](https://learn.microsoft.com/en-us/azure/virtual-machines/disks-types)

6. **c) Archive (accès très rare)**  
   - **Archive** est le niveau le plus économique (coût de stockage très bas) mais avec latence d'accès haute. Cool est pour accès occasionnel (moyen coût). Hot est pour accès fréquent. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/explore-azure-storage-services/)

7. **b) Un managed disk est un volume de stockage bloc attaché à une VM, un storage account est un service polyvalent**  
   - Un **managed disk** est un disque bloc managé directement par Azure, attaché à une VM. Un **storage account** est un service polyvalent pour blobs, files, tables, queues. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/explore-azure-storage-services/)

8. **b) Utiliser Azure Import/Export ou Data Box**  
   - Pour de grandes quantités de données (50+ TB), **Azure Data Box** ou **Import/Export** sont plus économiques et rapides qu'un transfert réseau. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/explore-azure-storage-services/)

9. **b) Virtual Machine Scale Sets (VMSS)**  
   - **VMSS** permet de gérer plusieurs VMs identiques avec mise à l'échelle automatique basée sur métriques (CPU, mémoire, etc.). Application Insights est pour la surveillance. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/manage-virtual-machines/)

10. **b) Définir des règles d'application et de conformité pour les ressources Azure**  
    - **Azure Policies** permet d'imposer des règles (ex: les ressources doivent avoir un tag "department", les VMs doivent être en SKU approuvés…). [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/control-and-organize-with-azure-resource-manager/)

***

## Fiches de révision synthétiques

### 1. Resource Groups & Tags
- **Resource Group (RG)** : conteneur logique pour grouper et gérer les ressources (déploiement, cycle de vie, facturation). [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/control-and-organize-with-azure-resource-manager/)
- **Tags** : paires clé-valeur pour organiser (cost-center, env, project, owner…). [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/control-and-organize-with-azure-resource-manager/)

### 2. Stockage Azure - Types de service
- **Blob Storage** : fichiers non-structurés (images, documents, backups). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/explore-azure-storage-services/)
- **Queue Storage** : files d'attente pour la communication asynchrone. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/explore-azure-storage-services/)
- **Table Storage** : données NoSQL semi-structurées. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/explore-azure-storage-services/)
- **File Share** : partages de fichiers réseau (NFS, SMB). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/explore-azure-storage-services/)

### 3. Stockage Azure - Niveaux (Tiers) Blob
- **Hot** : accès fréquent, coût accès bas, coût stockage élevé. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/explore-azure-storage-services/)
- **Cool** : accès occasionnel, coût stockage moyen, coût accès plus élevé. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/explore-azure-storage-services/)
- **Archive** : accès très rare, coût stockage ultra-bas, latence haute. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/explore-azure-storage-services/)

### 4. Disques Managés - Types de performance
- **Standard HDD** : charges générales, faible performance. [learn.microsoft](https://learn.microsoft.com/en-us/azure/virtual-machines/disks-types)
- **Standard SSD** : applications avec I/O modéré. [learn.microsoft](https://learn.microsoft.com/en-us/azure/virtual-machines/disks-types)
- **Premium SSD** : applications critiques (20,000 IOPS). [learn.microsoft](https://learn.microsoft.com/en-us/azure/virtual-machines/disks-types)
- **Ultra Disk** : I/O ultra-haute (160,000 IOPS max). [learn.microsoft](https://learn.microsoft.com/en-us/azure/virtual-machines/disks-types)

### 5. Gestion de la capacité
- **Virtual Machine Scale Sets (VMSS)** : déployer & mettre à l'échelle automatiquement des VMs. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/manage-virtual-machines/)
- **Azure Load Balancer** : distribuer le trafic entre instances. [learn.microsoft](https://learn.microsoft.com/en-us/azure/load-balancer/)

### 6. Governance & Conformité
- **Azure Policies** : imposer des règles d'entreprise (tags obligatoires, SKUs approuvés, restrictions régionales…). [learn.microsoft](https://learn.microsoft.com/fr-fr/training/modules/control-and-organize-with-azure-resource-manager/)
- **Role-Based Access Control (RBAC)** : contrôler qui peut faire quoi sur les ressources. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/control-and-organize-with-azure-resource-manager/)
