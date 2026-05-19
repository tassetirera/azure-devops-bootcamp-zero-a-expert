# QCM + corrections détaillées pour l'AZ-104 - Machines virtuelles et Calcul

***

## QCM (10 questions) - Domaine : Machines virtuelles et ressources de calcul

1. **Quels sont les deux modèles de tarification principaux pour les machines virtuelles Azure ?**  
   a) Spot et Reserved  
   b) Pay-as-you-go et Reserved Instances  
   c) Gratuit et Premium  
   d) Standard et Enterprise  

2. **Vous devez déployer une charge de travail non-critique. Comment économiser jusqu'à 90 % sur le coût des VMs ?**  
   a) Réduire la RAM  
   b) Utiliser des instances Spot (Azure Spot VMs)  
   c) Désactiver la sauvegarde  
   d) Utiliser des disques Standard HDD uniquement  

3. **Quelle est la différence entre une image de VM "managed" et "unmanaged" dans Azure ?**  
   a) Les images managées sont stockées dans le cloud, les non-managées localement  
   b) Les images managées sont gérées par Azure, les non-managées nécessitent gestion manuelle des disques  
   c) Il n'y a aucune différence  
   d) Les non-managées ne sont plus supportées  

4. **Quel service Azure permet de déployer et mettre à l'échelle automatiquement un groupe de machines virtuelles identiques ?**  
   a) Virtual Machines  
   b) Container Instances  
   c) Virtual Machine Scale Sets (VMSS)  
   d) App Service  

5. **Vous avez besoin d'exécuter une tâche critère courte (quelques secondes) sans provisionner une VM complète. Quel service Azure recommandez-vous ?**  
   a) Machine virtuelle classique  
   b) Azure Functions ou Azure Container Instances  
   c) App Service  
   d) Logic Apps uniquement  

6. **Quel type d'image de VM Azure est pré-configuré et optimisé pour des rôles spécifiques ?**  
   a) Image custom uniquement  
   b) Image Marketplace (ex: SQL Server, WordPress…)  
   c) Image générique Windows Server  
   d) Les images ne peuvent pas être pré-configurées  

7. **Vous devez assurer la haute disponibilité d'une VM critique. Quel est le mécanisme recommandé ?**  
   a) Faire tourner une seule VM  
   b) Utiliser une Availability Set (grouper 2+ VMs sur domaines de défaillance différents)  
   c) Utiliser une zone de disponibilité unique  
   d) Cela n'est pas possible dans Azure  

8. **Quelle est la différence entre une Availability Set et une Availability Zone dans Azure ?**  
   a) Aucune différence  
   b) Availability Set = logique (même datacenter), Availability Zone = physique (datacenters séparés)  
   c) Availability Zone est obsolète  
   d) Les deux offrent la même protection  

9. **Vous devez créer une sauvegarde d'une VM Azure et la restaurer rapidement en cas de sinistre. Quel service utiliser ?**  
   a) Storage Account uniquement  
   b) Azure Backup  
   c) Azure Site Recovery pour réplication inter-régions  
   d) Copier les fichiers manuellement  

10. **Quel service Azure vous permet de configurer et gérer des paramètres de VM après déploiement sans arrêter la machine ?**  
    a) Resource Manager uniquement  
    b) Azure Desired State Configuration (DSC) ou Custom Script Extension  
    c) Restart toujours la VM  
    d) C'est impossible  

***

## Corrections détaillées

1. **b) Pay-as-you-go et Reserved Instances**  
   - **Pay-as-you-go** : paiement à l'heure (flexible). **Reserved Instances (RI)** : engagement 1 ou 3 ans pour réduction (25-72%). **Spot VMs** est un 3e modèle (jusqu'à 90% moins cher). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/manage-virtual-machines/)

2. **b) Utiliser des instances Spot (Azure Spot VMs)**  
   - Les **Spot VMs** utilisent la capacité excédentaire d'Azure avec jusqu'à 90 % de réduction, mais peuvent être évincées. Idéal pour charges non-critiques, batch, calcul scientifique. [learn.microsoft](https://learn.microsoft.com/en-us/azure/virtual-machines/spot-vms)

3. **b) Les images managées sont gérées par Azure, les non-managées nécessitent gestion manuelle des disques**  
   - **Managed disks** : Azure gère entièrement le cycle de vie du disque (recommandé). **Unmanaged** : vous devez gérer les storage accounts (obsolète). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/manage-virtual-machines/)

4. **c) Virtual Machine Scale Sets (VMSS)**  
   - **VMSS** permet de déployer et mettre à l'échelle un groupe de VMs identiques de 0 à 1000 instances selon les règles d'autoscale (CPU, mémoire, métriques custom). [learn.microsoft](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/)

5. **b) Azure Functions ou Azure Container Instances**  
   - Pour des tâches courtes et sporadiques : **Azure Functions** (facturé à la milliseconde). **Container Instances** pour des exécutions ponctuelles. Pas besoin de provisionner une VM complète. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/manage-virtual-machines/)

6. **b) Image Marketplace (ex: SQL Server, WordPress…)**  
   - Le **Azure Marketplace** propose des images pré-configurées et optimisées par éditeurs (Microsoft, Canonical, Red Hat…) pour des solutions clés en main. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/manage-virtual-machines/)

7. **b) Utiliser une Availability Set (grouper 2+ VMs sur domaines de défaillance différents)**  
   - Une **Availability Set** répartit les VMs sur des domaines de défaillance (hardware) et des domaines de mise à jour séparés (maintenance), garantissant la disponibilité. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/manage-virtual-machines/)

8. **b) Availability Set = logique (même datacenter), Availability Zone = physique (datacenters séparés)**  
   - **Availability Set** = protection contre pannes hardware / mises à jour (même datacenter). **Availability Zones** = protection contre défaillance datacenter entier (3 zones physiques séparées par région). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/manage-virtual-machines/)

9. **b) Azure Backup**  
   - **Azure Backup** fournit une sauvegarde managée des VMs avec restauration rapide, sauvegarde incrémentale, et rétention longue. **Site Recovery** pour réplication inter-régions en temps réel. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/manage-virtual-machines/)

10. **b) Azure Desired State Configuration (DSC) ou Custom Script Extension**  
    - **Azure DSC** (ou Desired State Configuration) permet de configurer l'état d'une VM (applications, paramètres) après déploiement. **Custom Script Extension** pour exécuter des scripts PowerShell/Bash. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/manage-virtual-machines/)

***

## Fiches de révision synthétiques

### 1. Modèles de tarification VM
- **Pay-as-you-go** : flexible, paiement à l'heure. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/manage-virtual-machines/)
- **Reserved Instances (RI)** : engagement 1 ou 3 ans, réduction 25-72%. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/manage-virtual-machines/)
- **Spot VMs** : capacité excédentaire, réduction jusqu'à 90%, risque d'éviction. [learn.microsoft](https://learn.microsoft.com/en-us/azure/virtual-machines/spot-vms)
- **Hybrid Benefit** : réduction sur licence SQL Server ou Windows Server avec Software Assurance. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/manage-virtual-machines/)

### 2. Génération & Déploiement de VMs
- **Images** : source pour créer une VM (Windows Server, Ubuntu, Marketplace…). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/manage-virtual-machines/)
- **Managed Disks** : recommandé, Azure gère le stockage. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/manage-virtual-machines/)
- **Resource Manager** : déploiement déclaratif (JSON templates, Bicep…). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/manage-virtual-machines/)
- **Cloud-Init / Custom Script Extension** : configurer la VM après déploiement. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/manage-virtual-machines/)

### 3. Haute disponibilité
- **Availability Set** : répartir les VMs sur domaines de défaillance et mise à jour. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/manage-virtual-machines/)
- **Availability Zones** : déployer sur 3 zones physiques distinctes (même région). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/manage-virtual-machines/)
- **Load Balancer / Application Gateway** : distribuer le trafic, détecter et contourner les défaillances. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/manage-virtual-machines/)

### 4. Mise à l'échelle
- **Virtual Machine Scale Sets (VMSS)** : autoscale automatique (0 à 1000 VMs). [learn.microsoft](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/)
- **Autoscale basée sur métriques** : CPU, mémoire, métriques custom (Application Insights). [learn.microsoft](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/)
- **Horaires d'autoscale** : scale up aux heures de pointe, scale down la nuit. [learn.microsoft](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/)

### 5. Alternatives légères au VM complet
- **Azure Functions** : code serverless, facturation à la milliseconde. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/manage-virtual-machines/)
- **Azure Container Instances (ACI)** : conteneur éphémère, déploiement rapide. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/manage-virtual-machines/)
- **App Service** : applications web managées (PaaS). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/manage-virtual-machines/)

### 6. Protection & Récupération
- **Azure Backup** : sauvegarde managée avec restauration rapide. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/manage-virtual-machines/)
- **Azure Site Recovery** : réplication inter-régions pour DR (disaster recovery). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/manage-virtual-machines/)
- **Snapshots & Images** : copier l'état complet d'une VM. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/manage-virtual-machines/)

### 7. Configuration post-déploiement
- **Azure DSC** : gérer l'état de configuration (registry, fichiers, services…). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/manage-virtual-machines/)
- **Custom Script Extension** : exécuter PowerShell ou Bash après déploiement. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/manage-virtual-machines/)
- **Azure Automation** : orchestrer et automatiser les tâches de gestion VM. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/manage-virtual-machines/)
