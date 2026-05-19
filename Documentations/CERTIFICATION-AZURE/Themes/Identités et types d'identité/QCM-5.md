# QCM + corrections détaillées pour l'AZ-104 - Gestion d’identité et sécurité

***

## QCM (10 questions) - Domaine : Gestion d’identité et sécurité

1. **Quel mécanisme améliore la sécurité des identités en exigeant plusieurs facteurs ?**  
   a) MFA
   b) NSG
   c) VNet Peering
   d) Azure Policy

2. **Quel type d’identité est idéal pour un service Azure Function ?**  
   a) Identité d’utilisateur
   b) Principal de service
   c) Identité managée
   d) Identité d’appareil

3. **Quel service fournit un accès conditionnel basé sur l’emplacement ou l’état du périphérique ?**  
   a) Conditional Access
   b) Azure Backup
   c) Azure Policy
   d) Application Gateway

4. **Quel type d’identité peut être réutilisé sur plusieurs ressources Azure ?**  
   a) Managed identity affectée par le système
   b) Managed identity affectée par l’utilisateur
   c) Identité d’appareil
   d) Identité utilisateur

5. **Quel composant Entra permet l’audit des connexions et des modifications ?**  
   a) Azure Activity Log
   b) Azure AD Audit Logs
   c) Azure Monitor
   d) Azure DNS

6. **Quel rôle Azure AD est nécessaire pour gérer les applications enregistrées ?**  
   a) Application Administrator
   b) Storage Blob Data Contributor
   c) Reader
   d) Backup Contributor

7. **Quel type d’identité assure un accès sans secret pour une VM ?**  
   a) Principal de service
   b) User-assigned managed identity
   c) Identité B2C
   d) Identité d’appareil

8. **Quel service permet de fédérer l’authentification avec un fournisseur tiers ?**  
   a) Azure AD B2C
   b) Azure Firewall
   c) Azure Policy
   d) Virtual WAN

9. **Pour un scénario de collaboration interentreprise, quel modèle utiliser ?**  
   a) Azure AD B2B
   b) Azure AD B2C
   c) Azure Site Recovery
   d) Azure ExpressRoute

10. **Quel mécanisme permet d’empêcher l’accès aux comptes compromis ?**  
   a) Identity Protection
   b) Network Security Group
   c) Managed Disk
   d) Azure DNS

***

## Corrections détaillées

1. **a) MFA**  
   - MFA ajoute un facteur d’authentification supplémentaire.

2. **c) Identité managée**  
   - Les identités managées sont adaptées aux fonctions serverless.

3. **a) Conditional Access**  
   - Conditional Access permet de restreindre l’accès selon le contexte.

4. **b) Managed identity affectée par l’utilisateur**  
   - User-assigned managed identities peuvent être attachées à plusieurs ressources.

5. **b) Azure AD Audit Logs**  
   - Azure AD Audit Logs trace l’activité d’identité et de connexion.

6. **a) Application Administrator**  
   - Application Administrator peut gérer les applications enregistrées.

7. **b) User-assigned managed identity**  
   - User-assigned managed identities peuvent être partagées entre ressources.

8. **a) Azure AD B2C**  
   - Azure AD B2C supporte l’authentification via fournisseurs externes.

9. **a) Azure AD B2B**  
   - Azure AD B2B est conçu pour la collaboration partenaire.

10. **a) Identity Protection**  
   - Identity Protection détecte et bloque les comptes compromis.
