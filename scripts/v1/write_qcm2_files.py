from pathlib import Path
files = {
    'Documentations/CERTIFICATION-AZURE/Themes/Machines virtuelles & Calcul/QCM-2.md': """# QCM + corrections détaillées pour l'AZ-104 - Machines virtuelles et Calcul

***

## QCM (10 questions) - Domaine : Machines virtuelles avancées

1. **Quel type de disque Azure est recommandé pour des performances cohérentes et un faible latence sur une base de données critique ?**  
   a) Standard HDD  
   b) Standard SSD  
   c) Premium SSD  
   d) Archive  

2. **Quel service permet d’obtenir une VM temporaire et peu coûteuse pour exécuter un batch qui peut être interrompu ?**  
   a) VM classique  
   b) Azure Spot VMs  
   c) App Service  
   d) Azure SQL Database  

3. **Quelle option de disque OS Azure peut accélérer les performances de lecture/écriture tout en étant reconstruite à chaque redémarrage ?**  
   a) Disque Premium SSD  
   b) Disque Ultra  
   c) Ephemeral OS Disk  
   d) Disque Standard HDD  

4. **Quel composant Azure est le meilleur choix pour accéder à une VM via le portail sans exposer de port RDP/SSH public ?**  
   a) Public IP  
   b) VPN Gateway  
   c) Azure Bastion  
   d) Load Balancer  

5. **Quel type d’extension Azure VM permet d’exécuter un script de configuration après le déploiement ?**  
   a) Managed Identity  
   b) Custom Script Extension  
   c) Virtual Network Gateway  
   d) Application Insights  

6. **Quelle propriété d’une machine virtuelle permet de déployer automatiquement la configuration via ARM/Bicep ?**  
   a) Resource Group  
   b) VM size  
   c) Template d’Azure Resource Manager  
   d) Azure Policy  

7. **Dans Azure, que signifie le terme \"Availability Zone\" pour une VM ?**  
   a) Une zone réseau interne  
   b) Une garantie de sauvegarde  
   c) Un datacenter physique séparé dans la même région  
   d) Une machine virtuelle temporaire  

8. **Quel composant Azure permet d’optimiser la distribution des requêtes vers plusieurs VMs de la même application ?**  
   a) Azure Firewall  
   b) Virtual Network Peering  
   c) Azure Load Balancer  
   d) Application Gateway uniquement  

9. **Quel outil Azure est utile pour capturer les diagnostics de démarrage d’une VM lorsque celle-ci ne démarre pas correctement ?**  
   a) Boot diagnostics  
   b) Log Analytics  
   c) Azure Policy  
   d) Application Insights  

10. **Quel modèle présente une limitation en cas d’éviction de la VM par Azure pour libérer des ressources ?**  
    a) Reserved Instances  
    b) Pay-as-you-go  
    c) Azure Spot VMs  
    d) Dedicated Hosts  

***

## Corrections détaillées

1. **c) Premium SSD**  
   - Le **Premium SSD** offre des performances cohérentes et une faible latence adaptées aux bases de données critiques. [learn.microsoft](https://learn.microsoft.com/en-us/azure/virtual-machines/disks-types)

2. **b) Azure Spot VMs**  
   - Les **Spot VMs** sont économiques mais peuvent être arrêtées si Azure a besoin de capacité. Parfait pour les charges batch et tolérantes à l’interruption. [learn.microsoft](https://learn.microsoft.com/en-us/azure/virtual-machines/spot-vms)

3. **c) Ephemeral OS Disk**  
   - L’**Ephemeral OS Disk** est stocké sur le cache local de la VM et améliore les performances, mais les données sont perdues lors d’un redémarrage. [learn.microsoft](https://learn.microsoft.com/en-us/azure/virtual-machines/ephemeral-os-disks)

4. **c) Azure Bastion**  
   - **Azure Bastion** permet d’accéder à une VM via le portail en RDP/SSH sans exposer de port public. [learn.microsoft](https://learn.microsoft.com/en-us/azure/bastion/bastion-overview)

5. **b) Custom Script Extension**  
   - L’**extension Custom Script** exécute des scripts sur une VM après le déploiement, utile pour la configuration et l’installation initiale. [learn.microsoft](https://learn.microsoft.com/en-us/azure/virtual-machines/extensions/custom-script-windows)

6. **c) Template d’Azure Resource Manager**  
   - Un **ARM template** ou Bicep permet de définir et déployer la configuration déclarative d’une VM. [learn.microsoft](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/overview)

7. **c) Un datacenter physique séparé dans la même région**  
   - Les **Availability Zones** sont des emplacements physiques distincts dans la même région pour améliorer la résilience. [learn.microsoft](https://learn.microsoft.com/en-us/azure/availability-zones/az-overview)

8. **c) Azure Load Balancer**  
   - **Azure Load Balancer** répartit le trafic réseau entre plusieurs instances de VM. [learn.microsoft](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-overview)

9. **a) Boot diagnostics**  
   - **Boot diagnostics** capture les captures d’écran et journaux de console du démarrage de la VM pour diagnostiquer les problèmes. [learn.microsoft](https://learn.microsoft.com/en-us/azure/virtual-machines/boot-diagnostics)

10. **c) Azure Spot VMs**  
    - Les **Spot VMs** peuvent être évincées lorsque Azure a besoin de ressources, contrairement aux VMs pay-as-you-go ou Reserved. [learn.microsoft](https://learn.microsoft.com/en-us/azure/virtual-machines/spot-vms)

***

## Fiches de révision synthétiques

- **Spot VMs** : coût très faible, interruptions possibles.
- **Premium SSD** : disque performant pour production.
- **Ephemeral OS Disk** : très rapide, volatile.
- **Azure Bastion** : accès sécurisé sans port public.
- **ARM/Bicep** : déploiement déclaratif.
- **Availability Zone** : résilience physique.
- **Load Balancer** : répartiteur de trafic.
- **Boot diagnostics** : diagnostic de démarrage.
""",
    'Documentations/CERTIFICATION-AZURE/Themes/RBAC & Contrôle d'accès/QCM-2.md': """# QCM + corrections détaillées pour l'AZ-104 - RBAC & Contrôle d'accès

***

## QCM (10 questions) - Domaine : Contrôle d'accès approfondi

1. **Quel rôle RBAC est adapté si un utilisateur doit seulement démarrer et arrêter des VMs sans modifier les ressources réseau ?**  
   a) Owner  
   b) Contributor  
   c) Virtual Machine Contributor  
   d) Reader  

2. **Quel type de compte est utilisé pour attribuer un rôle RBAC à une application Azure ou un service ?**  
   a) Compte local Windows  
   b) Service principal  
   c) Identité d’appareil  
   d) Compte Microsoft personnel  

3. **Quel mécanisme permet de limiter une attribution de rôle RBAC à une période précise ?**  
   a) Access review  
   b) Privileged Identity Management (PIM)  
   c) Azure Policy  
   d) Azure Firewall  

4. **Quel rôle RBAC ne permet pas de modifier les accès RBAC existants ?**  
   a) Owner  
   b) User Access Administrator  
   c) Contributor  
   d) Security Admin  

5. **Quel élément Azure est recommandé pour centraliser l’attribution de rôles à plusieurs souscriptions ?**  
   a) Resource Group  
   b) Management Group  
   c) Virtual Network  
   d) Storage Account  

6. **Quel est l’avantage principal d’utiliser des groupes AAD pour l’attribution RBAC ?**  
   a) Les groupes sont gratuits  
   b) Une attribution unique s’applique à tous les membres du groupe  
   c) Les groupes augmentent les performances réseau  
   d) Les groupes remplacent les Resource Groups  

7. **Quel outil permet d’afficher l’historique des attributions RBAC et de vérifier qui a fait quoi ?**  
   a) Activity Log  
   b) Azure Monitor Metrics  
   c) Azure CLI  
   d) Azure Resource Graph  

8. **Que signifie le principe de least privilege dans RBAC ?**  
   a) Donner un rôle Owner à tout le monde  
   b) Donner uniquement les permissions nécessaires pour accomplir la tâche  
   c) Ne pas utiliser de rôles  
   d) Utiliser uniquement le rôle Reader  

9. **Quel rôle RBAC donne uniquement le droit de lire les ressources et les métadonnées de la souscription ?**  
   a) Contributor  
   b) Reader  
   c) Owner  
   d) Security Reader  

10. **Pour quel besoin créer un rôle personnalisé (Custom Role) ?**  
    a) Quand les rôles existants donnent trop ou trop peu de permissions  
    b) Pour avoir un rôle plus rapide  
    c) Parce qu’on ne peut pas utiliser les rôles prédéfinis  
    d) Pour un usage local uniquement  

***

## Corrections détaillées

1. **c) Virtual Machine Contributor**  
   - Le rôle **Virtual Machine Contributor** permet de gérer des actions VM sans toucher à la configuration RBAC ou réseau. [learn.microsoft](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles)

2. **b) Service principal**  
   - Un **service principal** est l’identité d’une application ou d’un service qui peut recevoir des rôles RBAC. [learn.microsoft](https://learn.microsoft.com/en-us/azure/active-directory/develop/app-objects-and-service-principals)

3. **b) Privileged Identity Management (PIM)**  
   - **PIM** permet d’assigner des rôles éligibles et de limiter l’élévation de privilèges dans le temps. [learn.microsoft](https://learn.microsoft.com/en-us/azure/active-directory/privileged-identity-management/pim-configure)

4. **c) Contributor**  
   - Le rôle **Contributor** peut gérer les ressources mais pas les attributions RBAC. [learn.microsoft](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments)

5. **b) Management Group**  
   - Un **Management Group** permet d’appliquer des rôles et politiques sur plusieurs souscriptions. [learn.microsoft](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview)

6. **b) Une attribution unique s’applique à tous les membres du groupe**  
   - Utiliser des **groupes AAD** facilite la gestion et réduit les assignations individuelles. [learn.microsoft](https://learn.microsoft.com/en-us/azure/role-based-access-control/group-assignments)

7. **a) Activity Log**  
   - L’**Activity Log** trace les opérations de gestion, y compris les changements de rôle et d’accès. [learn.microsoft](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/activity-log)

8. **b) Donner uniquement les permissions nécessaires pour accomplir la tâche**  
   - Le **principe de least privilege** limite l’exposition et réduit les risques de sécurité. [learn.microsoft](https://learn.microsoft.com/en-us/security/benchmark/azure/concepts/least-privilege)

9. **b) Reader**  
   - Le rôle **Reader** donne un accès en lecture seule aux ressources et métadonnées. [learn.microsoft](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles)

10. **a) Quand les rôles existants donnent trop ou trop peu de permissions**  
    - Un **Custom Role** est utile pour créer des permissions adaptées à un besoin métier précis. [learn.microsoft](https://learn.microsoft.com/en-us/azure/role-based-access-control/custom-roles)

***

## Fiches de révision synthétiques

- **RBAC** : Identity + Role + Scope.
- **Service principal** : identité d’application.
- **PIM** : rôles éligibles dans le temps.
- **Management Groups** : gouvernance multi-souscription.
- **Least Privilege** : permissions minimales.
- **Custom Role** : personnalisation fine.
""",
    'Documentations/CERTIFICATION-AZURE/Themes/Ressources & Stockage/QCM-2.md': """# QCM + corrections détaillées pour l'AZ-104 - Ressources & Stockage

***

## QCM (10 questions) - Domaine : Stockage avancé

1. **Quel type de compte de stockage Azure permet de stocker des tables NoSQL, des blobs et des files ?**  
   a) Storage Account General-purpose v2  
   b) Blob Storage uniquement  
   c) File Storage uniquement  
   d) Table Storage uniquement  

2. **Quel niveau de redondance stocke une copie des données dans une région secondaire distante ?**  
   a) LRS  
   b) ZRS  
   c) GRS  
   d) S1  

3. **Quel mécanisme Azure permet de déplacer automatiquement un blob du niveau Hot vers Archive selon l’âge ?**  
   a) Azure Backup  
   b) Lifecycle Management  
   c) Azure Policy  
   d) Storage Account Firewall  

4. **Quelle option protège un compte de stockage contre la suppression accidentelle des blobs ?**  
   a) Soft Delete  
   b) Network Security Group  
   c) Azure Policy  
   d) Private Endpoint  

5. **Quel service Azure permet d’accéder à un partage de fichiers via SMB depuis plusieurs machines ?**  
   a) Azure Disks  
   b) Azure File Share  
   c) Azure Queue  
   d) Azure Blob  

6. **Quel niveau de performance storage est le plus approprié pour des données d’accès fréquent et latence faible ?**  
   a) Premium  
   b) Cool  
   c) Archive  
   d) Standard HDD  

7. **Quelle fonctionnalité Azure Storage permet de restreindre l’accès à un compte depuis certaines plages IP uniquement ?**  
   a) Azure Firewall  
   b) Storage account network rules  
   c) Azure Policy  
   d) Role assignment  

8. **Quelle solution est adaptée pour stocker des données structurées et relationnelles ?**  
   a) Azure Blob Storage  
   b) Azure SQL Database  
   c) Azure Table Storage  
   d) Azure Queue Storage  

9. **Quel service permet de restaurer des fichiers supprimés dans un partage Azure File ?**  
   a) File Sync  
   b) Soft Delete  
   c) Azure Backup  
   d) Lifecycle Management  

10. **Quel service Azure est recommandé pour des besoins massifs de stockage d’objets non structurés ?**  
    a) Azure Blob Storage  
    b) Azure SQL Database  
    c) Azure Cosmos DB  
    d) Azure Files  

***

## Corrections détaillées

1. **a) Storage Account General-purpose v2**  
   - Un **Storage Account General-purpose v2** prend en charge blobs, files, queues et tables. [learn.microsoft](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview)

2. **c) GRS**  
   - **GRS** (Geo-redundant storage) réplique les données vers une région distante pour une résilience géographique. [learn.microsoft](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)

3. **b) Lifecycle Management**  
   - La **Lifecycle Management** applique des règles de transition automatique entre niveaux de stockage selon l’âge ou l’activité. [learn.microsoft](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-lifecycle-management-concepts)

4. **a) Soft Delete**  
   - **Soft Delete** protège contre la suppression accidentelle des blobs en conservant les données supprimées pendant une période définie. [learn.microsoft](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview)

5. **b) Azure File Share**  
   - **Azure File Share** fournit un partage de fichiers SMB accessible depuis plusieurs machines. [learn.microsoft](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-introduction)

6. **a) Premium**  
   - Les niveaux **Premium** sont optimisés pour une faible latence et des performances élevées. [learn.microsoft](https://learn.microsoft.com/en-us/azure/storage/common/storage-performance-tiers)

7. **b) Storage account network rules**  
   - Les **network rules** des storage accounts permettent de restreindre l’accès IP et d’autoriser des réseaux privés. [learn.microsoft](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security)

8. **b) Azure SQL Database**  
   - **Azure SQL Database** est le service relationnel managé idéal pour des données structurées. [learn.microsoft](https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview)

9. **b) Soft Delete**  
   - Pour Azure File Share, activer **Soft Delete** permet de récupérer les fichiers supprimés. [learn.microsoft](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-soft-delete)

10. **a) Azure Blob Storage**  
    - **Azure Blob Storage** est conçu pour le stockage d’objets non structurés à grande échelle. [learn.microsoft](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction)

***

## Fiches de révision synthétiques

- **Storage Account GPv2** : supporte blobs, files, tables, queues.
- **Redondance** : LRS, ZRS, GRS, RA-GRS.
- **Lifecycle Management** : transition automatique entre Hot/Cool/Archive.
- **Soft Delete** : protection contre la suppression accidentelle.
- **Azure File Share** : partage SMB.
- **Premium** : stockage haute performance.
- **Network rules** : restreindre l’accès IP.
- **Azure SQL Database** : stockage relationnel.
- **Blob Storage** : stockage d’objets massifs.
""",
    'Documentations/CERTIFICATION-AZURE/Themes/Réseaux & Connectivité/QCM-2.md': """# QCM + corrections détaillées pour l'AZ-104 - Réseaux & Connectivité

***

## QCM (10 questions) - Domaine : Réseau avancé

1. **Quel composant Azure permet de créer des règles d’accès par IP, port et protocole pour un subnet ou une NIC ?**  
   a) Azure Firewall  
   b) Network Security Group (NSG)  
   c) Application Gateway  
   d) Route Table  

2. **Quel service permet de connecter un VNet à un service PaaS Azure via une adresse IP privée ?**  
   a) Service Endpoint  
   b) Private Endpoint  
   c) Public IP  
   d) Azure DNS  

3. **Quelle fonctionnalité est utilisée pour router le trafic entre différents sous-réseaux d’un même VNet ?**  
   a) Virtual Network Peering  
   b) Route Table (UDR)  
   c) VPN Gateway  
   d) ExpressRoute  

4. **Quel service offre une connexion privée dédiée entre votre réseau on-premises et Azure ?**  
   a) VPN Gateway  
   b) ExpressRoute  
   c) Azure Bastion  
   d) Application Gateway  

5. **Quel outil permet de résoudre les noms DNS internes entre VNets ?**  
   a) Azure DNS public  
   b) Azure Private DNS Zones  
   c) Network Watcher  
   d) Load Balancer  

6. **Quel composant Azure peut inspecter le trafic entrant et appliquera des politiques applicatives ?**  
   a) Network Security Group  
   b) Azure Firewall  
   c) Virtual Network Peering  
   d) Storage Account  

7. **Pourquoi utiliser le peering de réseaux virtuels (VNet Peering) ?**  
   a) Pour déployer une VM dans un autre abonnement  
   b) Pour permettre une communication rapide entre deux VNets sans passer par Internet  
   c) Pour sauvegarder les VNets  
   d) Pour chiffrer le trafic sur Internet  

8. **Quel composant peut appliquer des routes personnalisées dans un VNet ?**  
   a) Virtual Network Gateway  
   b) Route Table (UDR)  
   c) Application Insights  
   d) Azure Bastion  

9. **Quel service protège les applications web utilisant HTTP/HTTPS au niveau couche 7 ?**  
   a) Azure Load Balancer  
   b) Application Gateway avec WAF  
   c) VPN Gateway  
   d) Network Security Group  

10. **Quel produit Azure permet de visualiser et diagnostiquer les flux réseau dans un VNet ?**  
    a) Azure Monitor Logs  
    b) Network Watcher  
    c) Azure Policy  
    d) Azure Blueprints  

***

## Corrections détaillées

1. **b) Network Security Group (NSG)**  
   - Un **NSG** filtre le trafic entrant et sortant par IP, port et protocole au niveau du subnet ou de la NIC. [learn.microsoft](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)

2. **b) Private Endpoint**  
   - Un **Private Endpoint** attribue une adresse IP privée à une ressource PaaS, garantissant un accès privé depuis le VNet. [learn.microsoft](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)

3. **b) Route Table (UDR)**  
   - Une **User Defined Route** permet de personnaliser le routage du trafic entre sous-réseaux dans un VNet. [learn.microsoft](https://learn.microsoft.com/en-us/azure/virtual-network/udr-overview)

4. **b) ExpressRoute**  
   - **ExpressRoute** offre une connexion privée dédiée, non publique, entre on-premises et Azure. [learn.microsoft](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction)

5. **b) Azure Private DNS Zones**  
   - Les **Private DNS Zones** permettent la résolution DNS interne au sein d’un ou plusieurs VNets. [learn.microsoft](https://learn.microsoft.com/en-us/azure/dns/private-dns-overview)

6. **b) Azure Firewall**  
   - **Azure Firewall** inspecte le trafic, applique des politiques et s’intègre avec des fonctionnalités de filtrage L7. [learn.microsoft](https://learn.microsoft.com/en-us/azure/firewall/overview)

7. **b) Pour permettre une communication rapide entre deux VNets sans passer par Internet**  
   - Le **VNet Peering** offre une connectivité à faible latence entre deux VNets. [learn.microsoft](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-peering-overview)

8. **b) Route Table (UDR)**  
   - Les **Route Tables** définissent des routes personnalisées pour le trafic sortant depuis un subnet. [learn.microsoft](https://learn.microsoft.com/en-us/azure/virtual-network/udr-overview)

9. **b) Application Gateway avec WAF**  
   - **Application Gateway** fournit un pare-feu applicatif (WAF) pour filtrer le trafic HTTP/HTTPS au niveau couche 7. [learn.microsoft](https://learn.microsoft.com/en-us/azure/web-application-firewall/overview)

10. **b) Network Watcher**  
    - **Network Watcher** offre des diagnostics réseau, tels que la vérification des flux et la capture de paquets. [learn.microsoft](https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-monitoring-overview)

***

## Fiches de révision synthétiques

- **NSG** : filtrage L3/L4.
- **Private Endpoint** : accès privé PaaS.
- **UDR** : routes personnalisées.
- **ExpressRoute** : connectivité privée dédiée.
- **Private DNS Zones** : résolution DNS interne.
- **Azure Firewall** : inspection et sécurité réseau.
- **VNet Peering** : communication rapide entre VNets.
- **Application Gateway WAF** : protection couche 7.
- **Network Watcher** : diagnostics réseau.
""",
    'Documentations/CERTIFICATION-AZURE/Themes/Surveillance & Gestion/QCM-2.md': """# QCM + corrections détaillées pour l'AZ-104 - Surveillance & Gestion

***

## QCM (10 questions) - Domaine : Gestion et monitoring avancés

1. **Quel service Azure stocke et analyse les logs de plusieurs ressources de manière centralisée ?**  
   a) Azure Monitor Metrics  
   b) Log Analytics Workspace  
   c) Azure Backup  
   d) Azure Policy  

2. **Quel élément permet de déclencher une action lorsque la métrique CPU dépasse un seuil donné ?**  
   a) Azure Policy  
   b) Alert Rule  
   c) Azure Advisor  
   d) Azure Blueprints  

3. **Quel composant offre une vue interactive et personnalisable des métriques et logs ?**  
   a) Azure Dashboards / Workbooks  
   b) Application Insights uniquement  
   c) Azure Storage  
   d) Azure Firewall  

4. **Quel service permet d’automatiser des tâches récurrentes comme le nettoyage de disques ou le redémarrage de VMs ?**  
   a) Azure Automation  
   b) Azure Policy  
   c) Azure Defender  
   d) Azure DNS  

5. **Quel type de données est généralement stocké dans un Log Analytics Workspace ?**  
   a) Fichiers binaires  
   b) Logs et traces  
   c) Images disque  
   d) Adresses IP publiques  

6. **Quel service est le plus adapté pour surveiller les performances d’une application web .NET en production ?**  
   a) Azure Monitor Metrics  
   b) Application Insights  
   c) Azure Backup  
   d) Azure Policy  

7. **Quel type d’alerte peut réduire le bruit en se déclenchant seulement sur une anomalie d’utilisation ?**  
   a) Metric alert  
   b) Smart detection / anomaly detection alert  
   c) Activity Log alert  
   d) Resource health alert  

8. **Quel outil permet d’exécuter un runbook déclenché par une alerte Azure Monitor ?**  
   a) Azure DevOps  
   b) Azure Automation  
   c) Azure Policy  
   d) Azure Storage  

9. **Quel rapport ou fonctionnalité d’Azure aide à analyser les coûts et à détecter les dépassements de budget ?**  
   a) Azure Cost Management + Budgets  
   b) Azure Monitor Metrics  
   c) Azure Firewall  
   d) Azure Resource Graph  

10. **Quel service offre un aperçu de l’état des ressources et des problèmes de maintenance planifiée ou imprévue ?**  
    a) Azure Resource Health  
    b) Azure Advisor  
    c) Azure Policy  
    d) Azure Security Center  

***

## Corrections détaillées

1. **b) Log Analytics Workspace**  
   - Un **Log Analytics Workspace** centralise les logs de ressources pour l’analyse et les requêtes KQL. [learn.microsoft](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-overview)

2. **b) Alert Rule**  
   - Une **Alert Rule** déclenche une action basée sur une condition de métrique ou de log. [learn.microsoft](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview)

3. **a) Azure Dashboards / Workbooks**  
   - **Dashboards** et **Workbooks** permettent la visualisation interactive et personnalisée des données de monitoring. [learn.microsoft](https://learn.microsoft.com/en-us/azure/azure-monitor/visualize/workbooks-overview)

4. **a) Azure Automation**  
   - **Azure Automation** exécute des runbooks planifiés ou déclenchés pour automatiser les opérations. [learn.microsoft](https://learn.microsoft.com/en-us/azure/automation/automation-intro)

5. **b) Logs et traces**  
   - Le **Log Analytics Workspace** stocke les logs, traces, événements et autres données de télémétrie. [learn.microsoft](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-overview)

6. **b) Application Insights**  
   - **Application Insights** fournit un monitoring applicatif pour les performances, requêtes, dépendances et exceptions. [learn.microsoft](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)

7. **b) Smart detection / anomaly detection alert**  
   - Les alertes d’**anomalie** détectent les écarts significatifs et réduisent le bruit. [learn.microsoft](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-anomaly-detection)

8. **b) Azure Automation**  
   - Un **runbook** d’Azure Automation peut être déclenché par une alerte pour exécuter une action automatique. [learn.microsoft](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-action-groups)

9. **a) Azure Cost Management + Budgets**  
   - **Azure Cost Management** offre le suivi des coûts et la création de budgets avec alertes. [learn.microsoft](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/overview)

10. **a) Azure Resource Health**  
    - **Azure Resource Health** fournit l’état opérationnel des ressources et les incidents de santé. [learn.microsoft](https://learn.microsoft.com/en-us/azure/service-health/resource-health-overview)

***

## Fiches de révision synthétiques

- **Log Analytics** : stockage et analyse des logs.
- **Alert Rules** : surveillance active.
- **Dashboards / Workbooks** : visualisation personnalisée.
- **Azure Automation** : exécution de runbooks.
- **Application Insights** : monitoring appli.
- **Anomaly detection** : réduire le bruit.
- **Cost Management** : budgets et suivi.
- **Resource Health** : état des ressources.
""",
    'Documentations/CERTIFICATION-AZURE/Themes/Sécurité & Chiffrement/QCM-2.md': """# QCM + corrections détaillées pour l'AZ-104 - Sécurité & Chiffrement

***

## QCM (10 questions) - Domaine : Sécurité des données avancée

1. **Quel composant Azure permet d’isoler l’accès à un Key Vault via un réseau privé ?**  
   a) Public IP  
   b) Private Endpoint  
   c) Service Endpoint  
   d) CDN  

2. **Quel type de clé Azure Key Vault utilise pour un chiffrement HSM-savvy et conforme ?**  
   a) AES  
   b) RSA  
   c) HSM-protected key  
   d) MD5  

3. **Quel service permet de chiffrer automatiquement les données Azure SQL sans modifier l’application ?**  
   a) Transparent Data Encryption (TDE)  
   b) Azure Policy  
   c) Azure Monitor  
   d) Azure Storage Encryption  

4. **Quel mécanisme garantit qu’une clé Key Vault ne peut pas être supprimée immédiatement ?**  
   a) Soft Delete et Purge Protection  
   b) RBAC  
   c) Network Security Group  
   d) Private Endpoint  

5. **Quel service Azure aide à détecter les menaces sur les ressources et recommande des actions de sécurisation ?**  
   a) Azure Security Center / Microsoft Defender for Cloud  
   b) Azure Monitor  
   c) Azure Backup  
   d) Azure Policy  

6. **Quel composant Azure permet de stocker des secrets comme des connexions ou des clés API ?**  
   a) Azure Key Vault  
   b) Azure Blob Storage  
   c) Azure App Service  
   d) Azure Functions  

7. **Comment s’appelle le chiffrement des données pendant leur transit entre le client et Azure ?**  
   a) At rest  
   b) In transit  
   c) Application-level  
   d) In memory  

8. **Quel service est utilisé pour gérer les certificats SSL/TLS dans Azure et renouveler automatiquement les certificats ?**  
   a) Azure DNS  
   b) Azure Key Vault  
   c) Azure Monitor  
   d) Azure Storage  

9. **Quel rôle permet à une VM Azure d’accéder à Key Vault sans secret stocké dans son code ?**  
   a) User Assigned Managed Identity  
   b) Contributor  
   c) Reader  
   d) Storage Blob Data Reader  

10. **Quel contrôle protège une base de données ou un compte de stockage en bloquant l’accès depuis Internet public ?**  
    a) Private Endpoint  
    b) Azure Policy  
    c) Reader role  
    d) Application Gateway  

***

## Corrections détaillées

1. **b) Private Endpoint**  
   - Un **Private Endpoint** permet d’accéder à un Key Vault via une adresse IP privée au sein d’un VNet. [learn.microsoft](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)

2. **c) HSM-protected key**  
   - Les clés **HSM-protected** dans Key Vault offrent une protection matérielle conforme aux standards. [learn.microsoft](https://learn.microsoft.com/en-us/azure/key-vault/keys/about-keys)

3. **a) Transparent Data Encryption (TDE)**  
   - **TDE** chiffre automatiquement les données SQL au repos sans modification applicative. [learn.microsoft](https://learn.microsoft.com/en-us/azure/azure-sql/database/transparent-data-encryption-azure-sql)

4. **a) Soft Delete et Purge Protection**  
   - Ces fonctionnalités empêchent la suppression immédiate d’un secret ou d’une clé. [learn.microsoft](https://learn.microsoft.com/en-us/azure/key-vault/general/soft-delete-overview)

5. **a) Azure Security Center / Microsoft Defender for Cloud**  
   - **Microsoft Defender for Cloud** détecte les menaces et fournit des recommandations de sécurité. [learn.microsoft](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction)

6. **a) Azure Key Vault**  
   - **Key Vault** est conçu pour stocker des secrets de manière sécurisée. [learn.microsoft](https://learn.microsoft.com/en-us/azure/key-vault/general/overview)

7. **b) In transit**  
   - Les données **in transit** sont chiffrées pendant leur transport sur le réseau. [learn.microsoft](https://learn.microsoft.com/en-us/security/zero-trust/deploy/in-transit)

8. **b) Azure Key Vault**  
   - **Key Vault** gère le cycle de vie des certificats et peut les renouveler automatiquement. [learn.microsoft](https://learn.microsoft.com/en-us/azure/key-vault/certificates/about-certificates)

9. **a) User Assigned Managed Identity**  
   - Une **User Assigned Managed Identity** permet à une VM ou un service d’accéder à Key Vault sans stockage de secret. [learn.microsoft](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview)

10. **a) Private Endpoint**  
    - Un **Private Endpoint** protège l’accès en bloquant l’exposition aux adresses IP publiques. [learn.microsoft](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)

***

## Fiches de révision synthétiques

- **Key Vault** : stockage de clés, secrets, certificats.
- **Private Endpoint** : accès privé Azure.
- **HSM-protected keys** : sécurité matérielle.
- **TDE** : chiffrement SQL transparent.
- **Soft Delete / Purge Protection** : protection contre suppression.
- **Microsoft Defender for Cloud** : détection de menaces.
- **In transit** : chiffrement du trafic.
- **Managed Identity** : authentification sans secret.
- **Private Endpoint** : réduction de la surface d’attaque.
"""
}
for rel_path, content in files.items():
    p = Path(rel_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding='utf-8')
print('done')
"@