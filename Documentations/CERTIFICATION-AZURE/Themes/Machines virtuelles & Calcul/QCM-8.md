# QCM + corrections détaillées pour l'AZ-104 - Tarification et dimensionnement des VMs (Révision 8)

***

## QCM (10 questions) - Domaine : Tarification et dimensionnement des VMs (Révision 8)

1. **Quel est le modèle de tarification le moins cher pour charge non-critique ?**  
   a) Pay-as-you-go
   b) Reserved Instances
   c) Spot VMs
   d) Hybrid Benefit

2. **Quel type de VM peut être évincé pour économiser ?**  
   a) Pay-as-you-go
   b) Spot VMs
   c) Reserved Instances
   d) Dedicated hosts

3. **Quel service permet de déployer plusieurs VMs identiques avec autoscale ?**  
   a) VM Scale Sets
   b) Availability Set
   c) Load Balancer
   d) Application Gateway

4. **Quel mécanisme assure la haute disponibilité dans une Availability Set ?**  
   a) Replication
   b) Domaines de défaillance
   c) Backup
   d) Snapshot

5. **Quel type de disque est recommandé pour une VM de production ?**  
   a) Standard HDD
   b) Standard SSD
   c) Premium SSD
   d) Ultra Disk

6. **Quel service permet l'autoscale basé sur métriques CPU ?**  
   a) Auto Shutdown
   b) Autoscale (VMSS)
   c) Availability Set
   d) Load Balancer

7. **Quel alternative serverless est idéale pour exécution courte ?**  
   a) Azure Functions
   b) App Service
   c) Container Instances
   d) VMSS

8. **Quel outil configure une VM après déploiement ?**  
   a) ARM Template
   b) Custom Script Extension
   c) Load Balancer
   d) NSG

9. **Quel service sauvegarde les VMs avec point de restauration ?**  
   a) Site Recovery
   b) Azure Backup
   c) Snapshots
   d) Storage Account

10. **Quel avantage offre Hybrid Benefit ?**  
   a) Réduction pour licences SQL/Windows
   b) Augmentation de CPU
   c) Disques gratuits
   d) Réseau gratuit

***

## Corrections détaillées

1. **c) Spot VMs**  
   - Spot VMs offrent réduction jusqu'à 90%.

2. **b) Spot VMs**  
   - Les Spot VMs peuvent être évincées si Azure a besoin de capacité.

3. **a) VM Scale Sets**  
   - VMSS gère le déploiement et l'autoscale d'un groupe de VMs.

4. **b) Domaines de défaillance**  
   - Les domaines de défaillance répartissent les VMs sur du hardware différent.

5. **c) Premium SSD**  
   - Premium SSD offre performance optimale pour production.

6. **b) Autoscale (VMSS)**  
   - Autoscale VMSS ajoute/retire les VMs selon la demande.

7. **a) Azure Functions**  
   - Azure Functions est serverless et facturé à la milliseconde.

8. **b) Custom Script Extension**  
   - Custom Script Extension exécute des scripts post-déploiement.

9. **b) Azure Backup**  
   - Azure Backup fournit sauvegarde managée et restauration.

10. **a) Réduction pour licences SQL/Windows**  
   - Hybrid Benefit réduit les coûts pour licences existantes.
