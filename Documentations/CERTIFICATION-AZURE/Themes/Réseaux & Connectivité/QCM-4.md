# QCM + corrections détaillées pour l'AZ-104 - VNets et segmentation réseau (Révision 4)

***

## QCM (10 questions) - Domaine : VNets et segmentation réseau (Révision 4)

1. **Quel service crée un réseau privé isolé dans Azure ?**  
   a) Virtual Network
   b) Load Balancer
   c) Application Gateway
   d) Azure Firewall

2. **Quel composant permet de diviser une VNet en sous-réseaux ?**  
   a) VNet Peering
   b) Subnets
   c) NSG
   d) Route Table

3. **Quel service filtre le trafic réseau au niveau couche 3-4 ?**  
   a) Application Gateway
   b) Load Balancer
   c) Network Security Group
   d) Traffic Manager

4. **Quel est l'avantage du VNet Peering ?**  
   a) Connecter directement deux VNets
   b) Réduire la latence
   c) Bypasser Internet
   d) Tous les avantages ci-dessus

5. **Quel service connecte un réseau on-premises à Azure via tunnel chiffré ?**  
   a) ExpressRoute
   b) VPN Gateway
   c) Virtual WAN
   d) Azure Firewall

6. **Quel service offre une connexion dédiée (non-Internet) vers Azure ?**  
   a) VPN Site-to-site
   b) ExpressRoute
   c) Private Endpoint
   d) Service Endpoint

7. **Quel service distribue le trafic au niveau couche 7 (applicatif) ?**  
   a) Load Balancer
   b) Application Gateway
   c) Traffic Manager
   d) Azure Front Door

8. **Quel composant assigne les adresses IP dans un subnet ?**  
   a) DHCP
   b) DNS
   c) NAT
   d) ACL

9. **Quel type d'IP reste inchangée après redémarrage ?**  
   a) Dynamique
   b) Statique
   c) Réservée
   d) Publique

10. **Quel service permet une requête DNS privée au sein d'une VNet ?**  
   a) Azure DNS Public
   b) Azure Private DNS
   c) DHCP
   d) Static Routes

***

## Corrections détaillées

1. **a) Virtual Network**  
   - VNet crée un espace d'adressage privé isolé.

2. **b) Subnets**  
   - Les subnets divisent le VNet logiquement.

3. **c) Network Security Group**  
   - NSG filtre le trafic aux niveaux 3-4.

4. **d) Tous les avantages ci-dessus**  
   - VNet Peering offre connectivité directe et rapide.

5. **b) VPN Gateway**  
   - VPN Gateway crée un tunnel sécurisé site-to-site.

6. **b) ExpressRoute**  
   - ExpressRoute fournit une ligne dédiée sans passer par Internet.

7. **b) Application Gateway**  
   - Application Gateway effectue du routage au niveau applicatif (HTTP/HTTPS).

8. **a) DHCP**  
   - DHCP assigne les IPs dynamiquement dans un subnet.

9. **b) Statique**  
   - Une IP statique est assignée manuellement et persiste.

10. **b) Azure Private DNS**  
   - Private DNS résout les noms en interne dans la VNet.
