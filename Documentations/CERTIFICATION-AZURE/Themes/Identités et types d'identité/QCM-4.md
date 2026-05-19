# QCM + corrections détaillées pour l'AZ-104 - Principaux services d’identité

***

## QCM (10 questions) - Domaine : Principaux services d’identité

1. **Quel service fournit un annuaire cloud pour les utilisateurs et applications ?**  
   a) Microsoft Entra ID
   b) Azure Storage
   c) Azure DNS
   d) Azure Firewall

2. **Quel type d’identité doit être utilisé pour une application qui définit des règles automatisées ?**  
   a) Identité utilisateur
   b) Principal de service
   c) Identité d’appareil
   d) Identité hybride

3. **Quel outil identifie les utilisateurs locaux et synchronise les mots de passe vers Entra ID ?**  
   a) Azure AD Connect
   b) Azure Policy
   c) Azure Backup
   d) Azure Monitor

4. **Quel type d’identité est le plus adapté pour des services Azure qui accèdent à Key Vault ?**  
   a) Principal de service
   b) Identité managée
   c) Identité d’utilisateur
   d) Identité externe

5. **Quel service peut gérer des utilisateurs invités et partenaires ?**  
   a) Azure AD B2B
   b) Azure AD B2C
   c) Azure DevOps
   d) Azure App Configuration

6. **Quelle identité permet de séparer le contrôle d’accès des ressources d’un utilisateur humain ?**  
   a) Identité d’appareil
   b) Identité managée
   c) Identité d’agent IA
   d) Identité hybride

7. **Quel type d’identité est utilisé pour une application de service interne Azure ?**  
   a) Identité B2C
   b) Identité utilisateur
   c) Principal de service
   d) Identité d’appareil

8. **Quelle fonction Entra permet de protéger l’accès par mot de passe faible ou risqué ?**  
   a) MFA et Conditional Access
   b) NSG
   c) Azure Policy
   d) Azure Load Balancer

9. **Que signifie un environnement d’identité “cloud only” ?**  
   a) Comptes uniquement dans Entra ID
   b) Comptes uniquement dans AD local
   c) Comptes uniquement invités
   d) Comptes uniquement B2C

10. **Quel service est destiné aux clients, pas aux partenaires internes ?**  
   a) Azure AD B2C
   b) Azure AD B2B
   c) Azure AD Connect
   d) Azure AD Domain Services

***

## Corrections détaillées

1. **a) Microsoft Entra ID**  
   - Microsoft Entra ID est l’annuaire cloud de Microsoft.

2. **b) Principal de service**  
   - Les applications automatisées utilisent généralement un principal de service.

3. **a) Azure AD Connect**  
   - Azure AD Connect synchronise les mots de passe AD local.

4. **b) Identité managée**  
   - Les identités managées simplifient l’accès aux services Azure.

5. **a) Azure AD B2B**  
   - Azure AD B2B gère les partenaires externes.

6. **b) Identité managée**  
   - Les identités managées séparent l’accès des utilisateurs humains.

7. **c) Principal de service**  
   - Les applications internes utilisent des principals de service.

8. **a) MFA et Conditional Access**  
   - MFA et Conditional Access protègent les accès risqués.

9. **a) Comptes uniquement dans Entra ID**  
   - Un modèle cloud only signifie des comptes créés directement dans Entra ID.

10. **a) Azure AD B2C**  
   - Azure AD B2C est destiné aux clients grand public.
