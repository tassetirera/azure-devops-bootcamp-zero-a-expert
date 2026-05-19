# QCM + corrections détaillées pour l'AZ-104 - Azure Key Vault et secrets (Révision 10)

***

## QCM (10 questions) - Domaine : Azure Key Vault et secrets (Révision 10)

1. **Quel service protège les secrets, clés et certificats ?**  
   a) Azure Storage
   b) Azure Key Vault
   c) Application Insights
   d) Azure DNS

2. **Quel type de donnée peut être stocké dans Key Vault ?**  
   a) Secrets uniquement
   b) Clés uniquement
   c) Secrets, clés, certificats
   d) Données binaires

3. **Quel service permet à une VM d'accéder à Key Vault sans secret ?**  
   a) Principal de service
   b) Managed Identity
   c) User Identity
   d) API Key

4. **Quel protocole chiffre les données en transit ?**  
   a) HTTP
   b) FTP
   c) HTTPS/TLS
   d) SMTP

5. **Quel type de chiffrement s'applique aux données au repos ?**  
   a) AES-256
   b) RSA-2048
   c) MD5
   d) Base64

6. **Quel chiffrement s'applique au niveau de l'application ?**  
   a) Platform-managed
   b) Customer-managed
   c) Application-level
   d) Network-level

7. **Quel service gère les certificats SSL/TLS ?**  
   a) Azure DNS
   b) Key Vault
   c) Application Gateway
   d) Load Balancer

8. **Quel type de clé est utilisé pour signature numérique ?**  
   a) Clé symétrique
   b) Clé asymétrique (RSA/EC)
   c) Clé de session
   d) Clé partagée

9. **Quel audit trace l'accès à Key Vault ?**  
   a) Application Insights
   b) Audit Logs Key Vault
   c) NSG logs
   d) Activity Log

10. **Quel niveau de tarification supporte les HSM (Hardware Security Module) ?**  
   a) Free
   b) Standard
   c) Premium
   d) Enterprise

***

## Corrections détaillées

1. **b) Azure Key Vault**  
   - Key Vault est le service de gestion des secrets Azure.

2. **c) Secrets, clés, certificats**  
   - Key Vault supporte les trois types de données critiques.

3. **b) Managed Identity**  
   - Managed Identity authentifie sans secret.

4. **c) HTTPS/TLS**  
   - HTTPS/TLS chiffre les données en chemin.

5. **a) AES-256**  
   - AES-256 est l'algorithme symétrique standard pour chiffrement at-rest.

6. **c) Application-level**  
   - Application-level encryption chiffre avant envoi au serveur.

7. **b) Key Vault**  
   - Key Vault gère le cycle de vie des certificats.

8. **b) Clé asymétrique (RSA/EC)**  
   - Les clés asymétriques signent et chiffrent (RSA/EC).

9. **b) Audit Logs Key Vault**  
   - Audit Logs Key Vault trace tous les accès.

10. **c) Premium**  
   - Premium HSM offre isolation physique des clés.
