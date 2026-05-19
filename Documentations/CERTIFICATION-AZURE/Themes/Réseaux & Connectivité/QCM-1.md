# QCM + corrections détaillées pour l'AZ-104 - Connectivité réseau

***

## QCM (10 questions) - Domaine : Réseaux et connectivité

1. **Quel est le rôle principal d'une Virtual Network (VNet) dans Azure ?**  
   a) Stocker des données de manière temporaire  
   b) Créer un réseau logique isolé dans Azure où les ressources peuvent communiquer  
   c) Authentifier les utilisateurs uniquement  
   d) Gérer la facturation des ressources  

2. **Vous devez créer un sous-réseau pour les serveurs de bases de données. Quel est l'avantage d'utiliser des subnets séparés ?**  
   a) Aucun avantage, tous les subnets sont identiques  
   b) Segmentation de sécurité, gestion du trafic et appliance de Network Security Groups (NSG)  
   c) Augmenter la performance du réseau  
   d) Réduire le coût du stockage  

3. **Quel service Azure vous permet de filtrer le trafic réseau au niveau des ressources (entrée/sortie) ?**  
   a) Application Gateway  
   b) Network Security Group (NSG)  
   c) Virtual Network Peering  
   d) Azure VPN Gateway  

4. **Vous disposez de deux VNets dans Azure. Comment établir une communication sécurisée et directe entre elles ?**  
   a) Utiliser Internet public  
   b) Ajouter un appareil physique externe  
   c) Configurer Virtual Network Peering ou VPN  
   d) C'est impossible dans Azure  

5. **Quel composant Azure vous permet de connecter votre réseau on-premises à Azure via une connexion privée et chiffrée ?**  
   a) Virtual Network Peering  
   b) Azure Public IP  
   c) Azure VPN Gateway ou ExpressRoute  
   d) Network Security Group  

6. **Quelle est la différence entre une adresse IP statique et une adresse IP dynamique dans Azure ?**  
   a) L'IP dynamique est plus rapide  
   b) L'IP statique reste la même après redémarrage, l'IP dynamique peut changer  
   c) Il n'y a pas de différence  
   d) L'IP statique n'existe pas dans Azure  

7. **Quel service Azure vous permet de distribuer le trafic réseau entre plusieurs machines virtuelles (Load Balancing) ?**  
   a) Network Security Group  
   b) Virtual Network Peering  
   c) Azure Load Balancer ou Application Gateway  
   d) Azure Storage  

8. **Vous avez une application multi-couche (Web, App, Database). Quelle est la meilleure pratique pour l'organisation réseau ?**  
   a) Tout dans un seul subnet  
   b) Utiliser des subnets séparés par couche avec NSG pour contrôler la communication  
   c) Héberger chaque couche dans une région différente  
   d) N'utiliser que des adresses IP publiques  

9. **Quel est l'avantage d'Azure ExpressRoute par rapport à une connexion VPN site-à-site ?**  
   a) ExpressRoute est gratuit  
   b) ExpressRoute offre une connexion privée dédiée avec plus de bande passante et moins de latence  
   c) Le VPN est toujours plus performant  
   d) Aucune différence  

10. **Vous devez implémenter une solution de contrôle d'accès réseau au niveau de l'application (par port, protocole, adresse IP source). Quel est le meilleur outil ?**  
    a) Virtual Network uniquement  
    b) Network Security Group (NSG) pour couche 3-4  
    c) Application Gateway avec Web Application Firewall (WAF) pour couche 7  
    d) Azure Load Balancer uniquement  

***

## Corrections détaillées

1. **b) Créer un réseau logique isolé dans Azure où les ressources peuvent communiquer**  
   - Une **VNet** est l'équivalent d'un réseau privé dans Azure. Elle permet aux ressources (VMs, App Services, etc.) de communiquer de façon sécurisée. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/introduction-to-azure-virtual-networks/)

2. **b) Segmentation de sécurité, gestion du trafic et appliance de Network Security Groups (NSG)**  
   - Les **subnets** permettent de diviser le réseau, d'appliquer des NSGs différents par étage (ex: DMZ, application, database), et de gérer les plages IP logiquement. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/introduction-to-azure-virtual-networks/)

3. **b) Network Security Group (NSG)**  
   - Un **NSG** est un pare-feu logiciel qui filtre le trafic réseau (règles entrante/sortante) par protocole, port, adresse IP source/destination. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/introduction-to-azure-virtual-networks/)

4. **c) Configurer Virtual Network Peering ou VPN**  
   - **VNet Peering** connecte deux VNets de façon directe et rapide dans Azure (même région ou inter-régions). **VPN** convient pour une sécurité renforcée ou inter-cloud. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/introduction-to-azure-virtual-networks/)

5. **c) Azure VPN Gateway ou ExpressRoute**  
   - **VPN Gateway** crée une tunneling VPN chiffrée entre on-premises et Azure. **ExpressRoute** offre une connexion privée dédiée (pas via Internet). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/introduction-to-azure-virtual-networks/)

6. **b) L'IP statique reste la même après redémarrage, l'IP dynamique peut changer**  
   - Une **IP statique** (réservée) ne change jamais. Une **IP dynamique** est assignée par le service DHCP et peut changer après redémarrage. Pour une ressource critique (base de données, serveur), utiliser une IP statique. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/introduction-to-azure-virtual-networks/)

7. **c) Azure Load Balancer ou Application Gateway**  
   - **Azure Load Balancer** fonctionne au niveau couche 4 (TCP/UDP). **Application Gateway** fonctionne au niveau couche 7 (HTTP/HTTPS) et permet du routage par URL/hostname. [learn.microsoft](https://learn.microsoft.com/en-us/azure/load-balancer/)

8. **b) Utiliser des subnets séparés par couche avec NSG pour contrôler la communication**  
   - C'est la **meilleure pratique** : isoler les couches (tier) par subnet et appliquer des NSGs restrictifs (ex: subnet App ne communique qu'avec subnet Database sur le port 1433 SQL). Cela limite la surface d'attaque. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/introduction-to-azure-virtual-networks/)

9. **b) ExpressRoute offre une connexion privée dédiée avec plus de bande passante et moins de latence**  
   - **ExpressRoute** est une connexion dédiée (non-publique) depuis on-premises vers Azure, offrant plus de débit (1 Gbps à 100 Gbps) et stabilité. Le **VPN** utilise Internet (chiffré) mais moins de garanties de bande passante. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/introduction-to-azure-virtual-networks/)

10. **c) Application Gateway avec Web Application Firewall (WAF) pour couche 7**  
    - **NSG** filtre aux niveaux 3-4 (IP, port, protocole). **Application Gateway + WAF** filtre au niveau 7 (application) : par chemin URL, hostname, contenu HTTP. Pour une sécurité applicative fine, utiliser l'Application Gateway avec WAF. [learn.microsoft](https://learn.microsoft.com/en-us/azure/web-application-firewall/)

***

## Fiches de révision synthétiques

### 1. Architecture réseau Azure
- **Virtual Network (VNet)** : réseau logique privé dans Azure. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/introduction-to-azure-virtual-networks/)
- **Subnet** : subdivision du VNet pour segmentation de sécurité et adresses IP. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/introduction-to-azure-virtual-networks/)
- **Network Interface (NIC)** : interface réseau attachée à une ressource (VM). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/introduction-to-azure-virtual-networks/)

### 2. Adressage
- **IP publique** : accès depuis Internet (statique ou dynamique). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/introduction-to-azure-virtual-networks/)
- **IP privée** : accès interne au VNet (DHCP ou statique). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/introduction-to-azure-virtual-networks/)
- **Plages recommandées** : 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 (RFC 1918). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/introduction-to-azure-virtual-networks/)

### 3. Sécurité réseau
- **Network Security Group (NSG)** : pare-feu stateless (couche 3-4). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/introduction-to-azure-virtual-networks/)
- **Application Security Group (ASG)** : grouper les ressources pour appliquer NSG de façon logique. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/introduction-to-azure-virtual-networks/)
- **Application Gateway + WAF** : pare-feu applicatif (couche 7). [learn.microsoft](https://learn.microsoft.com/en-us/azure/web-application-firewall/)
- **Azure Firewall** : pare-feu managé multi-couche (VNet ou niveau d'hub). [learn.microsoft](https://learn.microsoft.com/en-us/azure/firewall/)

### 4. Connectivité inter-ressources
- **VNet Peering** : connexion directe entre deux VNets (même région ou inter-régions). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/introduction-to-azure-virtual-networks/)
- **VPN Gateway (site-to-site)** : connexion chiffrée on-premises ↔ Azure via Internet. [learn.microsoft](https://learn.microsoft.com/en-us/azure/vpn-gateway/)
- **ExpressRoute** : connexion privée dédiée on-premises ↔ Azure (bypass Internet). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/introduction-to-azure-virtual-networks/)
- **Service Endpoints** : accès privé aux services Azure depuis un VNet (ex: Storage, SQL…). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/introduction-to-azure-virtual-networks/)
- **Private Endpoints** : interface réseau privée pour un service Azure. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/introduction-to-azure-virtual-networks/)

### 5. Load Balancing
- **Azure Load Balancer** : distribution couche 4 (TCP/UDP), haute disponibilité. [learn.microsoft](https://learn.microsoft.com/en-us/azure/load-balancer/)
- **Application Gateway** : distribution couche 7 (HTTP/HTTPS), routage URL, SSL Offloading. [learn.microsoft](https://learn.microsoft.com/en-us/azure/application-gateway/)
- **Traffic Manager** : routage DNS global pour applications multi-régions. [learn.microsoft](https://learn.microsoft.com/en-us/azure/traffic-manager/)

### 6. DNS
- **Azure DNS** : zone DNS managée pour vos domaines. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/introduction-to-azure-virtual-networks/)
- **Résolution privée** : Azure Private DNS pour noms internes au VNet. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/introduction-to-azure-virtual-networks/)
