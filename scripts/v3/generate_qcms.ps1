$base = "c:\Users\mouss\source\repos\azure-devops-bootcamp-zero-a-expert\Documentations\CERTIFICATION-AZURE\Themes"

function Write-QcmFile {
    param(
        [string]$Path,
        [string]$Title,
        [array]$Questions
    )
    $lines = @()
    $lines += "# QCM + corrections détaillées pour l'AZ-104 - $Title"
    $lines += ""
    $lines += "***"
    $lines += ""
    $lines += "## QCM (10 questions) - Domaine : $Title"
    $lines += ""
    for ($i = 0; $i -lt 10; $i++) {
        $q = $Questions[$i]
        $lines += "$(($i + 1)). **$($q.question)**  "
        foreach ($opt in $q.options) { $lines += "   $opt" }
        $lines += ""
    }
    $lines += "***"
    $lines += ""
    $lines += "## Corrections détaillées"
    $lines += ""
    for ($i = 0; $i -lt 10; $i++) {
        $q = $Questions[$i]
        $lines += "$(($i + 1)). **$($q.answer)**  "
        $lines += "   - $($q.explanation)"
        $lines += ""
    }
    $lines | Out-File -FilePath $Path -Encoding utf8
}

function Create-QcmSeries {
    param(
        [string]$Folder,
        [string]$TitlePrefix,
        [array]$QuestionBank,
        [int]$StartIndex,
        [int]$EndIndex
    )
    New-Item -ItemType Directory -Path $Folder -Force | Out-Null
    for ($n = $StartIndex; $n -le $EndIndex; $n++) {
        $path = Join-Path $Folder "QCM-$n.md"
        if (Test-Path $path) { continue }
        $offset = (($n - $StartIndex) * 2) % $QuestionBank.Count
        $questions = @()
        for ($j = 0; $j -lt 10; $j++) {
            $questions += $QuestionBank[($offset + $j) % $QuestionBank.Count]
        }
        Write-QcmFile -Path $path -Title "$TitlePrefix - Série $n" -Questions $questions
    }
}

$identityBank = @(
    @{question="Quelle solution Azure gère les identités des applications et services ?"; options=@("a) Azure AD Connect","b) Microsoft Entra ID","c) Azure Policy","d) Azure DNS"); answer="b) Microsoft Entra ID"; explanation="Microsoft Entra ID est le service central d'identité pour Azure."},
    @{question="Quel type d'identité est utilisé pour une application Azure Function qui accède à Key Vault ?"; options=@("a) Identité managée","b) Identité utilisateur","c) Identité d'appareil","d) Identité B2C"); answer="a) Identité managée"; explanation="Les identités managées permettent l'accès aux ressources sans secret."},
    @{question="Quel service permet d'inviter un partenaire externe dans Microsoft Entra ?"; options=@("a) Azure AD B2B","b) Azure AD B2C","c) Azure AD Connect","d) Azure Firewall"); answer="a) Azure AD B2B"; explanation="Azure AD B2B invite des partenaires externes en tant qu'invités."},
    @{question="Quel type d'identité est associé à un appareil Windows joint à Entra ?"; options=@("a) Identité d'appareil","b) Identité utilisateur","c) Identité managée","d) Identité B2C"); answer="a) Identité d'appareil"; explanation="Un appareil joint a une identité d'appareil dans Entra."},
    @{question="Quel outil synchronise les utilisateurs AD local vers Entra ID ?"; options=@("a) Azure AD Connect","b) Azure AD B2C","c) Azure Site Recovery","d) Azure Policy"); answer="a) Azure AD Connect"; explanation="Azure AD Connect synchronise AD local et Entra."},
    @{question="Quel type d'identité est utilisé pour un bot IA ?"; options=@("a) Identité d'agent IA","b) Identité utilisateur","c) Identité d'appareil","d) Identité hybride"); answer="a) Identité d'agent IA"; explanation="Les bots IA utilisent des identités d'agent IA."},
    @{question="Quel service Entra est conçu pour gérer des clients grand public ?"; options=@("a) Azure AD B2C","b) Azure AD B2B","c) Azure AD Connect","d) Azure Key Vault"); answer="a) Azure AD B2C"; explanation="Azure AD B2C est destiné aux applications client grand public."},
    @{question="Quel type d'identité est créé automatiquement avec une VM Azure ?"; options=@("a) Managed identity affectée par le système","b) Identité utilisateur","c) Identité B2C","d) Identité d'appareil"); answer="a) Managed identity affectée par le système"; explanation="Les identities system-assigned sont créées avec la ressource."},
    @{question="Quel service Azure protège l'accès basé sur l'emplacement et le dispositif ?"; options=@("a) Conditional Access","b) NSG","c) Azure Policy","d) Azure Monitor"); answer="a) Conditional Access"; explanation="Conditional Access applique des contrôles en fonction du contexte."},
    @{question="Quel rôle Entra est nécessaire pour gérer les applications ?"; options=@("a) Application Administrator","b) Reader","c) Contributor","d) Owner"); answer="a) Application Administrator"; explanation="Application Administrator gère les applications enregistrées."},
    @{question="Quel concept signifie accorder le minimum de permissions nécessaires ?"; options=@("a) Least Privilege","b) Max Privilege","c) Full Access","d) No Access"); answer="a) Least Privilege"; explanation="Least Privilege réduit la surface d'attaque."},
    @{question="Quel service gère les comptes invités et partenaires ?"; options=@("a) Azure AD B2B","b) Azure AD B2C","c) Azure AD Connect","d) Azure DNS"); answer="a) Azure AD B2B"; explanation="B2B est fait pour les partenaires externes."},
    @{question="Quel fournisseur d'identité est utilisé pour l'authentification client via réseaux sociaux ?"; options=@("a) Azure AD B2C","b) Azure AD B2B","c) Azure AD Connect","d) Azure Policy"); answer="a) Azure AD B2C"; explanation="B2C supporte les identités sociales pour les clients."},
    @{question="Quel type d'identité sépare les comptes utilisateurs et applications ?"; options=@("a) Principal de service","b) Identité utilisateur","c) Identité d'appareil","d) Identité hybride"); answer="a) Principal de service"; explanation="Les principals de service sont dédiés aux applications."},
    @{question="Quel service permet l'audit des connexions Entra ?"; options=@("a) Azure AD Audit Logs","b) Azure Monitor","c) NSG","d) Azure Policy"); answer="a) Azure AD Audit Logs"; explanation="Azure AD Audit Logs trace les événements de connexion."},
    @{question="Quel service est requis pour l'accès conditionnel avancé ?"; options=@("a) Azure AD P1/P2","b) Azure AD Free","c) Azure AD B2C","d) Azure AD B2B"); answer="a) Azure AD P1/P2"; explanation="Conditional Access nécessite une licence P1 ou P2."},
    @{question="Quel composant empêche l'utilisation de mots de passe faibles ?"; options=@("a) Password Protection","b) Azure Policy","c) NSG","d) Load Balancer"); answer="a) Password Protection"; explanation="Password Protection bloque les mots de passe faibles ou compromis."},
    @{question="Quel service d'identité est utilisé pour authentifier un service Azure sans secret ?"; options=@("a) Managed Identity","b) Guest user","c) User principal","d) Device identity"); answer="a) Managed Identity"; explanation="Les managed identities permettent une authentification sans secret."},
    @{question="Quel service gère les applications d'entreprise et les intégrations ?"; options=@("a) Azure AD","b) Azure Backup","c) Azure DNS","d) Azure Storage"); answer="a) Azure AD"; explanation="Azure AD gère les applications d'entreprise et les intégrations."},
    @{question="Quel service permet de protéger les applications contre les attaques de force brute ?"; options=@("a) Azure AD Identity Protection","b) NSG","c) Azure Policy","d) Azure Monitor"); answer="a) Azure AD Identity Protection"; explanation="Identity Protection détecte et bloque les attaques de force brute."}
)

$resourcesBank = @(
    @{question="Quel composant Azure permet de regrouper plusieurs ressources pour gérer leur cycle de vie ?"; options=@("a) Resource Group","b) Storage Account","c) Virtual Network","d) Key Vault"); answer="a) Resource Group"; explanation="Les Resource Groups groupent les ressources pour la gestion."},
    @{question="Quel service permet de créer des tags pour le suivi de facturation ?"; options=@("a) Tags","b) NSG","c) Azure Policy","d) Load Balancer"); answer="a) Tags"; explanation="Les tags permettent l'organisation et le suivi des coûts."},
    @{question="Quel type de stockage Azure convient le mieux pour des fichiers blob non structurés ?"; options=@("a) Blob Storage","b) Table Storage","c) Queue Storage","d) File Share"); answer="a) Blob Storage"; explanation="Blob Storage est conçu pour les fichiers non structurés."},
    @{question="Quel niveau de stockage est le moins cher pour des données rarement consultées ?"; options=@("a) Archive","b) Cool","c) Hot","d) Premium"); answer="a) Archive"; explanation="Archive est le niveau le plus économique pour accès très rare."},
    @{question="Quel type de disque managé offre le plus haut débit IOPS ?"; options=@("a) Ultra Disk","b) Standard HDD","c) Standard SSD","d) Premium SSD"); answer="a) Ultra Disk"; explanation="Ultra Disk offre les performances les plus élevées."},
    @{question="Quel service permet de déplacer de grandes quantités de données physiquement ?"; options=@("a) Azure Data Box","b) Azure VPN","c) Azure DNS","d) Azure Policy"); answer="a) Azure Data Box"; explanation="Azure Data Box est conçu pour le transfert hors ligne de gros volumes."},
    @{question="Quel service fournit un stockage de tables NoSQL ?"; options=@("a) Table Storage","b) Blob Storage","c) Queue Storage","d) File Share"); answer="a) Table Storage"; explanation="Table Storage est un service NoSQL pour données structurées."},
    @{question="Quel service est recommandé pour un partage de fichiers SMB ?"; options=@("a) File Share","b) Blob Storage","c) Queue Storage","d) Table Storage"); answer="a) File Share"; explanation="Azure File Share fournit un partage SMB managé."},
    @{question="Quel service permet de chiffrer les données au repos par défaut ?"; options=@("a) Azure Storage Encryption","b) Azure Monitor","c) Azure Policy","d) Azure Load Balancer"); answer="a) Azure Storage Encryption"; explanation="Azure Storage chiffre les données au repos par défaut."},
    @{question="Quel service supporte les snapshots de disques pour sauvegarde rapide ?"; options=@("a) Azure Managed Disk","b) Storage Accounts","c) Azure DNS","d) Azure AD"); answer="a) Azure Managed Disk"; explanation="Les managed disks prennent en charge les snapshots pour la sauvegarde."},
    @{question="Quel élément est utilisé pour déployer des ressources déclarativement ?"; options=@("a) ARM Template","b) Load Balancer","c) NSG","d) Azure DNS"); answer="a) ARM Template"; explanation="Les templates ARM permettent le déploiement déclaratif."},
    @{question="Quel type de stockage est conçu pour la file d'attente des messages ?"; options=@("a) Queue Storage","b) Blob Storage","c) Table Storage","d) File Share"); answer="a) Queue Storage"; explanation="Queue Storage est conçu pour l'échange de messages asynchrones."},
    @{question="Quel service permet de contrôler la conformité des ressources avec des règles ?"; options=@("a) Azure Policy","b) Azure Backup","c) Azure Monitor","d) Azure DNS"); answer="a) Azure Policy"; explanation="Azure Policy applique des règles de conformité aux ressources."},
    @{question="Quel type de resource group est le plus adapté pour un environnement de production ?"; options=@("a) Resource Group dédié","b) Aucun","c) Resource Group unique pour tout","d) Resource Group temporaire"); answer="a) Resource Group dédié"; explanation="Garder les environnements séparés facilite la gestion."},
    @{question="Quel service peut organiser des subscriptions en hiérarchies ?"; options=@("a) Management Groups","b) Resource Groups","c) VNets","d) Storage Accounts"); answer="a) Management Groups"; explanation="Les management groups organisent les subscriptions hiérarchiquement."},
    @{question="Quel service permet de gérer les coûts et budgets Azure ?"; options=@("a) Cost Management","b) Azure Monitor","c) Azure Policy","d) Azure DNS"); answer="a) Cost Management"; explanation="Cost Management aide à suivre et planifier les dépenses Azure."},
    @{question="Quel type de stockage est utilisé pour des données semi-structurées avec clés/valeurs ?"; options=@("a) Table Storage","b) Blob Storage","c) File Share","d) Queue Storage"); answer="a) Table Storage"; explanation="Table Storage stocke des entités semi-structurées."},
    @{question="Quel niveau de stockage est préférable pour accès fréquent ?"; options=@("a) Hot","b) Cool","c) Archive","d) Premium"); answer="a) Hot"; explanation="Hot est optimisé pour un accès fréquent."},
    @{question="Quel service Azure permet de restaurer des ressources supprimées depuis un backup ?"; options=@("a) Azure Backup","b) Azure Monitor","c) Azure Policy","d) Azure DNS"); answer="a) Azure Backup"; explanation="Azure Backup restaure les données et ressources sauvegardées."}
)

$networkBank = @(
    @{question="Quel composant Azure est utilisé pour créer un réseau isolé ?"; options=@("a) VNet","b) Storage Account","c) Key Vault","d) Azure DNS"); answer="a) VNet"; explanation="Une VNet crée un réseau privé isolé dans Azure."},
    @{question="Quel élément divise un VNet en segments plus petits ?"; options=@("a) Subnet","b) NSG","c) Load Balancer","d) Service Endpoint"); answer="a) Subnet"; explanation="Les subnets segmentent le VNet pour l'organisation et la sécurité."},
    @{question="Quel service filtre le trafic entrant et sortant d'un subnet ?"; options=@("a) NSG","b) Storage Account","c) Azure Policy","d) Azure AD"); answer="a) NSG"; explanation="NSG filtre le trafic réseau sur les sous-réseaux."},
    @{question="Quel service connecte deux VNets directement ?"; options=@("a) VNet Peering","b) VPN Gateway","c) Azure Firewall","d) Azure DNS"); answer="a) VNet Peering"; explanation="VNet Peering connecte deux VNets de manière directe."},
    @{question="Quel service fournit une connexion privée dédiée entre on-prem et Azure ?"; options=@("a) ExpressRoute","b) VPN Gateway","c) NSG","d) Storage Account"); answer="a) ExpressRoute"; explanation="ExpressRoute offre une liaison privée dédiée vers Azure."},
    @{question="Quel service permet d'équilibrer le trafic réseau sur plusieurs VM ?"; options=@("a) Azure Load Balancer","b) Azure DNS","c) Azure Policy","d) Azure Key Vault"); answer="a) Azure Load Balancer"; explanation="Azure Load Balancer distribue le trafic entre instances."},
    @{question="Quel service gère le trafic HTTP/HTTPS avec routage par URL ?"; options=@("a) Application Gateway","b) NSG","c) VNet Peering","d) Azure DNS"); answer="a) Application Gateway"; explanation="Application Gateway route le trafic au niveau applicatif."},
    @{question="Quel service protège une application web contre les attaques au niveau HTTP ?"; options=@("a) WAF","b) NSG","c) Azure DNS","d) Azure Policy"); answer="a) WAF"; explanation="Le Web Application Firewall protège les applications contre les attaques HTTP."},
    @{question="Quel service fournit un DNS privé pour un VNet ?"; options=@("a) Private DNS","b) Public IP","c) Azure AD","d) Azure Policy"); answer="a) Private DNS"; explanation="Azure Private DNS gère la résolution de noms privés dans un VNet."},
    @{question="Quel option permet d'attribuer une IP statique à une ressource ?"; options=@("a) IP statique","b) IP dynamique","c) IP publique uniquement","d) IP privée uniquement"); answer="a) IP statique"; explanation="Une IP statique reste la même après redémarrage."},
    @{question="Quel composant offre un point d'accès privé pour un service Azure ?"; options=@("a) Private Endpoint","b) Public IP","c) VNet Peering","d) Azure DNS"); answer="a) Private Endpoint"; explanation="Private Endpoints connectent les services Azure via des IP privées."},
    @{question="Quel service est utilisé pour surveiller la santé réseau et les latences ?"; options=@("a) Network Watcher","b) Azure Monitor","c) Azure Policy","d) Azure Backup"); answer="a) Network Watcher"; explanation="Network Watcher aide à diagnostiquer le réseau Azure."},
    @{question="Quel service VPN est utilisé pour une connexion site à site ?"; options=@("a) VPN Gateway","b) VNet Peering","c) Azure DNS","d) Azure AD"); answer="a) VPN Gateway"; explanation="VPN Gateway établit des tunnels site-à-site chiffrés."},
    @{question="Quel service permet d'équilibrer le trafic global DNS entre régions ?"; options=@("a) Traffic Manager","b) Azure DNS","c) NSG","d) Azure Policy"); answer="a) Traffic Manager"; explanation="Traffic Manager utilise le routage DNS global."},
    @{question="Quel type de pare-feu managé protège un VNet entier ?"; options=@("a) Azure Firewall","b) NSG","c) Load Balancer","d) Storage Account"); answer="a) Azure Firewall"; explanation="Azure Firewall protège le trafic network-wide."},
    @{question="Quel service aide à sécuriser l'accès aux services PaaS depuis un VNet ?"; options=@("a) Service Endpoint","b) Azure AD","c) Blob Storage","d) Azure Monitor"); answer="a) Service Endpoint"; explanation="Service Endpoints ajoutent un chemin sécurisé vers les services Azure."},
    @{question="Quel service permet d'équilibrer le trafic HTTP au niveau application et SSL ?"; options=@("a) Application Gateway","b) NSG","c) VNet Peering","d) Azure DNS"); answer="a) Application Gateway"; explanation="Application Gateway gère SSL et routage applicatif."},
    @{question="Quel coffre de réseau peut être protégé par un WAF ?"; options=@("a) App Gateway avec WAF","b) Azure Storage","c) NSG","d) Private DNS"); answer="a) App Gateway avec WAF"; explanation="Application Gateway avec WAF protège les applications web."}
)

$vmBank = @(
    @{question="Quel modèle de tarification VM est le plus flexible pour un usage ponctuel ?"; options=@("a) Pay-as-you-go","b) Reserved Instances","c) Spot","d) Free"); answer="a) Pay-as-you-go"; explanation="Pay-as-you-go facture à l'heure sans engagement."},
    @{question="Quel type d'instance VM peut être évincé si la capacité diminue ?"; options=@("a) Spot VMs","b) Reserved Instances","c) Standard HDD","d) Premium SSD"); answer="a) Spot VMs"; explanation="Les Spot VMs bénéficient d'un coût réduit mais peuvent être évincées."},
    @{question="Quel service Azure permet de scaler automatiquement un groupe de VM ?"; options=@("a) VMSS","b) App Service","c) Azure DNS","d) Azure Monitor"); answer="a) VMSS"; explanation="Les Virtual Machine Scale Sets permettent l'autoscale."},
    @{question="Quel mécanisme répartit les VMs sur plusieurs domaines de panne ?"; options=@("a) Availability Set","b) Availability Zone","c) VNet Peering","d) NSG"); answer="a) Availability Set"; explanation="Availability Set répartit les VMs sur des domaines de défaillance."},
    @{question="Quel mécanisme utilise des datacenters séparés dans la même région ?"; options=@("a) Availability Zones","b) Availability Set","c) Load Balancer","d) Azure Policy"); answer="a) Availability Zones"; explanation="Les Availability Zones offrent une protection contre la défaillance de datacenter."},
    @{question="Quel service permet le déploiement d'images préconfigurées depuis le marketplace ?"; options=@("a) Azure Marketplace","b) Azure AD","c) Azure DNS","d) Azure Monitor"); answer="a) Azure Marketplace"; explanation="Le Marketplace propose des images de VMs prêtes à l'emploi."},
    @{question="Quel service permet d'exécuter une tâche sans provisionner une VM complète ?"; options=@("a) Azure Functions","b) Azure Backup","c) Azure AD","d) Azure DNS"); answer="a) Azure Functions"; explanation="Azure Functions exécute du code serverless sans VM dédiée."},
    @{question="Quel service Azure permet de sauvegarder des machines virtuelles ?"; options=@("a) Azure Backup","b) Azure Policy","c) Azure Monitor","d) Azure DNS"); answer="a) Azure Backup"; explanation="Azure Backup fournit une sauvegarde managée des VMs."},
    @{question="Quel extension permet d'exécuter un script sur une VM après son démarrage ?"; options=@("a) Custom Script Extension","b) VM Agent","c) NSG","d) Azure AD"); answer="a) Custom Script Extension"; explanation="Custom Script Extension exécute un script lors de l'installation de la VM."},
    @{question="Quel type de disque est recommandé pour une base de données en production ?"; options=@("a) Premium SSD","b) Standard HDD","c) Archive","d) Table Storage"); answer="a) Premium SSD"; explanation="Premium SSD offre de meilleures performances pour les bases de données."},
    @{question="Quel service permet de créer une image personnalisée d'une VM ?"; options=@("a) Image Managed","b) Storage Account","c) Azure Policy","d) Azure DNS"); answer="a) Image Managed"; explanation="Une image managée permet de répliquer une VM personnalisée."},
    @{question="Quel type de disque permet la plus faible latence pour des charges intensives ?"; options=@("a) Ultra Disk","b) Standard HDD","c) Standard SSD","d) Archive"); answer="a) Ultra Disk"; explanation="Ultra Disk offre la latence la plus faible et les meilleures IOPS."},
    @{question="Quel service permet de restaurer une VM sur une autre région en cas de sinistre ?"; options=@("a) Azure Site Recovery","b) Azure Backup","c) Azure Policy","d) Azure AD"); answer="a) Azure Site Recovery"; explanation="Azure Site Recovery réplique les VMs vers une région de secours."},
    @{question="Quel service aide à réduire le coût des licences Windows Server ou SQL ?"; options=@("a) Azure Hybrid Benefit","b) Azure Policy","c) Azure Monitor","d) Azure DNS"); answer="a) Azure Hybrid Benefit"; explanation="Le Hybrid Benefit réduit les coûts de licences existantes."},
    @{question="Quel type d'image est fourni par Microsoft pour une VM Windows ou Linux ?"; options=@("a) Marketplace image","b) Custom image","c) Storage Account","d) Azure DNS"); answer="a) Marketplace image"; explanation="Les images Marketplace sont fournies par Microsoft ou des éditeurs."},
    @{question="Quel service permet d'automatiser le déploiement des configurations de VM ?"; options=@("a) Azure Automation","b) Azure Policy","c) Azure DNS","d) Azure Monitor"); answer="a) Azure Automation"; explanation="Azure Automation orchestre des scripts et des runbooks pour les VMs."},
    @{question="Quel service permet de provisionner des conteneurs sans VM ?"; options=@("a) Azure Container Instances","b) VMSS","c) Azure DNS","d) Azure Policy"); answer="a) Azure Container Instances"; explanation="ACI exécute des conteneurs sans infrastructure VM dédiée."},
    @{question="Quel service mesure l'utilisation CPU et mémoire des VMs ?"; options=@("a) Azure Monitor","b) Azure Backup","c) Azure Policy","d) Azure DNS"); answer="a) Azure Monitor"; explanation="Azure Monitor collecte les métriques des VMs."}
)

$surveillanceBank = @(
    @{question="Quel service collecte les métriques et logs des ressources Azure ?"; options=@("a) Azure Monitor","b) Azure Policy","c) Azure AD","d) Azure DNS"); answer="a) Azure Monitor"; explanation="Azure Monitor collecte métriques et logs Azure."},
    @{question="Quel espace de travail stocke les logs Azure pour l'analyse ?"; options=@("a) Log Analytics Workspace","b) Storage Account","c) Azure AD","d) Azure DNS"); answer="a) Log Analytics Workspace"; explanation="Le Workspace stocke et analyse les logs Azure."},
    @{question="Quel langage est utilisé pour interroger les logs dans Log Analytics ?"; options=@("a) KQL","b) SQL","c) JSON","d) YAML"); answer="a) KQL"; explanation="KQL est le langage de requête pour Log Analytics."},
    @{question="Quel service rapporte les exceptions et les dépendances d'une application ?"; options=@("a) Application Insights","b) Azure Backup","c) Azure Policy","d) Azure DNS"); answer="a) Application Insights"; explanation="Application Insights est pour le monitoring applicatif."},
    @{question="Quel objet déclenche une notification lorsqu'un seuil est dépassé ?"; options=@("a) Alert Rule","b) NSG","c) VNet Peering","d) Azure Policy"); answer="a) Alert Rule"; explanation="Une alerte déclenche une action lorsque le seuil est franchi."},
    @{question="Quel groupe d'actions envoie des e-mails, SMS ou webhooks pour une alerte ?"; options=@("a) Action Group","b) Resource Group","c) Management Group","d) Virtual Network"); answer="a) Action Group"; explanation="Action Groups définissent les actions d'une alerte."},
    @{question="Quel service exécute des scripts automatisés sur un horaire ?"; options=@("a) Azure Automation","b) Azure Backup","c) Azure Policy","d) Azure DNS"); answer="a) Azure Automation"; explanation="Azure Automation exécute des runbooks programmés."},
    @{question="Quel outil affiche des rapports interactifs personnalisables dans Azure ?"; options=@("a) Workbooks","b) Dashboards","c) NSG","d) Azure Policy"); answer="a) Workbooks"; explanation="Workbooks offrent des rapports interactifs et flexibles."},
    @{question="Quel service permet d'activer les diagnostics sur une ressource pour envoyer des logs vers un workspace ?"; options=@("a) Diagnostic Settings","b) NSG","c) VPN Gateway","d) Azure DNS"); answer="a) Diagnostic Settings"; explanation="Diagnostic Settings envoie les logs et métriques vers un workspace."},
    @{question="Quel service supporte l'analyse des performances des applications web ?"; options=@("a) Application Insights","b) Azure Backup","c) Azure Policy","d) Azure DNS"); answer="a) Application Insights"; explanation="Application Insights surveille les performances applicatives."},
    @{question="Quel outil permet de centraliser les journaux de plusieurs souscriptions ?"; options=@("a) Log Analytics Workspace","b) Storage Account","c) Azure AD","d) Azure Backup"); answer="a) Log Analytics Workspace"; explanation="Le workspace peut agréger les logs de plusieurs subscriptions."},
    @{question="Quel service déclenche un runbook via une alerte ?"; options=@("a) Azure Automation","b) Azure Policy","c) NSG","d) Azure DNS"); answer="a) Azure Automation"; explanation="Une alerte peut démarrer un runbook d'Azure Automation."},
    @{question="Quel service surveille les temps de réponse et la disponibilité d'une application ?"; options=@("a) Application Insights","b) Azure Backup","c) Azure Policy","d) Azure DNS"); answer="a) Application Insights"; explanation="Application Insights collecte la télémétrie d'application."},
    @{question="Quel service permet de définir des règles de conformité et remédiation ?"; options=@("a) Azure Policy","b) Azure Monitor","c) Azure Backup","d) Azure DNS"); answer="a) Azure Policy"; explanation="Azure Policy vérifie la conformité et peut corriger les écarts."},
    @{question="Quel outil affiche un tableau de bord personnalisable pour la surveillance ?"; options=@("a) Dashboards","b) NSG","c) VNet Peering","d) Azure Policy"); answer="a) Dashboards"; explanation="Les Dashboards présentent des vues personnalisées des données Azure."},
    @{question="Quel service aide à définir la fréquence de rétention des logs ?"; options=@("a) Log Analytics Workspace","b) Azure AD","c) Azure DNS","d) Azure Backup"); answer="a) Log Analytics Workspace"; explanation="La rétention des logs est configurée dans le workspace."},
    @{question="Quel service permet d'automatiser le nettoyage et la rotation des logs ?"; options=@("a) Azure Automation","b) Azure DNS","c) Azure Policy","d) Azure Backup"); answer="a) Azure Automation"; explanation="Azure Automation peut automatiser la gestion des logs."}
)

$securityBank = @(
    @{question="Quel service centralise la gestion des secrets et clés ?"; options=@("a) Azure Key Vault","b) Azure Monitor","c) Azure Policy","d) Azure DNS"); answer="a) Azure Key Vault"; explanation="Key Vault sécurise les secrets et clés."},
    @{question="Quel type d'objet stocke un mot de passe ou une chaîne de connexion ?"; options=@("a) Secret","b) Key","c) Certificate","d) NSG"); answer="a) Secret"; explanation="Les secrets stockent des mots de passe et connexions."},
    @{question="Quel type d'objet est utilisé pour des certificats SSL/TLS ?"; options=@("a) Certificate","b) Secret","c) Key","d) Storage Account"); answer="a) Certificate"; explanation="Les certificates stockent des clés et certificats SSL/TLS."},
    @{question="Quel type de clé est géré par Microsoft sans configuration supplémentaire ?"; options=@("a) Platform-managed key","b) Customer-managed key","c) Secret","d) Certificate"); answer="a) Platform-managed key"; explanation="Les clés gérées par la plateforme sont gérées par Microsoft."},
    @{question="Quel type de clé donne plus de contrôle au client via Key Vault ?"; options=@("a) Customer-managed key","b) Platform-managed key","c) Secret","d) Certificate"); answer="a) Customer-managed key"; explanation="Les CMK donnent au client le contrôle sur les clés."},
    @{question="Quel service chiffre le trafic entre un client et Azure ?"; options=@("a) HTTPS/TLS","b) HTTP","c) FTP","d) SMTP"); answer="a) HTTPS/TLS"; explanation="HTTPS chiffre les données en transit."},
    @{question="Quel service Azure fournit un point d'accès privé pour un coffre de clés ?"; options=@("a) Private Endpoint","b) Public IP","c) VNet Peering","d) Azure DNS"); answer="a) Private Endpoint"; explanation="Private Endpoint connecte Key Vault via une IP privée."},
    @{question="Quel service assure le chiffrement des disques Azure au repos ?"; options=@("a) Azure Disk Encryption","b) Azure Monitor","c) Azure Policy","d) Azure DNS"); answer="a) Azure Disk Encryption"; explanation="Azure Disk Encryption chiffre les disques au repos."},
    @{question="Quel service protège l'accès aux applications web au niveau HTTP ?"; options=@("a) WAF","b) NSG","c) VNet Peering","d) Azure DNS"); answer="a) WAF"; explanation="Le WAF protège contre les attaques de couche applicative."},
    @{question="Quel service permet la rotation automatique des certificats ?"; options=@("a) Azure Key Vault","b) Azure Monitor","c) Azure Backup","d) Azure Policy"); answer="a) Azure Key Vault"; explanation="Key Vault peut automatiser le renouvellement des certificats."},
    @{question="Quel rôle RBAC est recommandé pour la gestion des secrets dans Key Vault ?"; options=@("a) Key Vault Secrets Officer","b) Reader","c) Contributor","d) Owner"); answer="a) Key Vault Secrets Officer"; explanation="Ce rôle permet la gestion des secrets sans droits d'administration complète."},
    @{question="Quel option d'accès réduit l'exposition d'un service Key Vault sur Internet ?"; options=@("a) Private Endpoint","b) Public IP","c) Service Endpoint","d) VNet Peering"); answer="a) Private Endpoint"; explanation="Private Endpoint limite l'accès aux réseaux privés."},
    @{question="Quel service Azure permet de vérifier la conformité des ressources de sécurité ?"; options=@("a) Azure Policy","b) Azure Monitor","c) Azure Backup","d) Azure DNS"); answer="a) Azure Policy"; explanation="Azure Policy vérifie les configurations de sécurité."},
    @{question="Quel mécanisme de chiffrement permet de garder les données chiffrées avant qu'elles arrivent au serveur ?"; options=@("a) Client-side encryption","b) Server-side encryption","c) HTTP","d) FTP"); answer="a) Client-side encryption"; explanation="Le chiffrement côté client protège les données avant envoi."},
    @{question="Quel service Active Directory gère les identités des ressources des applications ?"; options=@("a) Managed Identities","b) Guest User","c) Private Endpoint","d) Azure DNS"); answer="a) Managed Identities"; explanation="Les managed identities assurent l'identité des ressources Azure."},
    @{question="Quel mécanisme bloque le trafic non autorisé en fonction des ports et IP ?"; options=@("a) NSG","b) WAF","c) Azure Policy","d) Azure Monitor"); answer="a) NSG"; explanation="Les NSG filtrent le trafic au niveau réseau."},
    @{question="Quel service Azure permet de sécuriser les clés avec du matériel HSM ?"; options=@("a) Key Vault Premium","b) Azure Monitor","c) Azure Policy","d) Azure DNS"); answer="a) Key Vault Premium"; explanation="Key Vault Premium supporte les HSM pour les clés."}
)

$rbacBank = @(
    @{question="Quel élément définit qui peut faire quoi sur quelles ressources dans Azure ?"; options=@("a) RBAC","b) NSG","c) Azure Policy","d) Load Balancer"); answer="a) RBAC"; explanation="RBAC contrôle les permissions sur les ressources Azure."},
    @{question="Quels sont les trois éléments d'une attribution de rôle ?"; options=@("a) Principal, rôle, scope","b) User, password, region","c) VM, disk, network","d) Tag, policy, group"); answer="a) Principal, rôle, scope"; explanation="Une role assignment inclut l'utilisateur, le rôle et le scope."},
    @{question="Quel rôle peut gérer les accès et les ressources ?"; options=@("a) Owner","b) Contributor","c) Reader","d) User"); answer="a) Owner"; explanation="Owner a tous les droits, y compris la gestion des accès."},
    @{question="Quel rôle ne peut que lire les ressources sans les modifier ?"; options=@("a) Reader","b) Contributor","c) Owner","d) User"); answer="a) Reader"; explanation="Reader est lecture seule."},
    @{question="Quel type de rôle peut être défini par le client avec des permissions personnalisées ?"; options=@("a) Custom Role","b) Owner","c) Reader","d) Contributor"); answer="a) Custom Role"; explanation="Les Custom Roles offrent des permissions sur mesure."},
    @{question="Quel scope est le plus large pour une attribution RBAC ?"; options=@("a) Management Group","b) Resource Group","c) Resource","d) Subscription"); answer="a) Management Group"; explanation="Les management groups s'appliquent à plusieurs subscriptions."},
    @{question="Quel principe limite l'accès aux permissions minimales nécessaires ?"; options=@("a) Least Privilege","b) Maximum Privilege","c) Full Control","d) No Access"); answer="a) Least Privilege"; explanation="Least Privilege réduit les risques de compromission."},
    @{question="Quel service permet de structurer les subscriptions en hiérarchie ?"; options=@("a) Management Groups","b) Resource Groups","c) VNets","d) Storage Accounts"); answer="a) Management Groups"; explanation="Management Groups organisent les subscriptions hiérarchiquement."},
    @{question="Quel rôle est principalement utilisé pour gérer les accès utilisateurs ?"; options=@("a) User Access Administrator","b) Reader","c) Contributor","d) Owner"); answer="a) User Access Administrator"; explanation="Ce rôle gère les attributions RBAC."},
    @{question="Quel service applique des règles de configuration mais pas forcément des droits d'accès ?"; options=@("a) Azure Policy","b) RBAC","c) NSG","d) Azure DNS"); answer="a) Azure Policy"; explanation="Azure Policy contrôle la conformité des configurations."},
    @{question="Quel type de principal RBAC peut être une application ?"; options=@("a) Service principal","b) Guest user","c) Device identity","d) B2C user"); answer="a) Service principal"; explanation="Les principals de service représentent des applications."},
    @{question="Quel rôle est utilisé pour donner uniquement des droits de lecture sur les clés Key Vault ?"; options=@("a) Key Vault Secrets User","b) Contributor","c) Owner","d) Reader"); answer="a) Key Vault Secrets User"; explanation="Ce rôle donne accès aux secrets sans droits d'administration générale."},
    @{question="Quel type de rôle est conseillé lorsque les permissions doivent être très précises ?"; options=@("a) Custom Role","b) Owner","c) Reader","d) Contributor"); answer="a) Custom Role"; explanation="Les Custom Roles autorisent des permissions spécifiques."},
    @{question="Quel mécanisme permet de révoquer rapidement l'accès d'un utilisateur ?"; options=@("a) Retirer l'attribution de rôle","b) Modifier un NSG","c) Changer une IP","d) Redémarrer une VM"); answer="a) Retirer l'attribution de rôle"; explanation="Retirer le rôle révoque l'accès immédiatement."},
    @{question="Quel service Azure contient des continuités de l'identité pour les groupes ?"; options=@("a) Azure AD Groups","b) NSG","c) Azure Storage","d) VMSS"); answer="a) Azure AD Groups"; explanation="Les groupes facilitent la gestion des attributions RBAC."},
    @{question="Quel rôle convient à un administrateur de sécurité qui ne doit pas modifier les ressources ?"; options=@("a) Security Reader","b) Owner","c) Contributor","d) Reader"); answer="a) Security Reader"; explanation="Security Reader peut voir la sécurité sans modifications."}
)

$securityBank = @(
    @{question="Quel service centralise la gestion des secrets et clés ?"; options=@("a) Azure Key Vault","b) Azure Monitor","c) Azure Policy","d) Azure DNS"); answer="a) Azure Key Vault"; explanation="Key Vault sécurise les secrets et clés."},
    @{question="Quel type d'objet stocke un mot de passe ou une chaîne de connexion ?"; options=@("a) Secret","b) Key","c) Certificate","d) NSG"); answer="a) Secret"; explanation="Les secrets stockent des mots de passe et chaînes de connexion."},
    @{question="Quel type d'objet sert à stocker des certificats SSL/TLS ?"; options=@("a) Certificate","b) Secret","c) Key","d) Storage Account"); answer="a) Certificate"; explanation="Certificates gèrent les certificats SSL/TLS."},
    @{question="Quel service chiffre les disques VM au repos ?"; options=@("a) Azure Disk Encryption","b) Azure Monitor","c) Azure Policy","d) Azure DNS"); answer="a) Azure Disk Encryption"; explanation="Azure Disk Encryption chiffre les disques VM."},
    @{question="Quel niveau de stockage est le plus économique pour des données archivées ?"; options=@("a) Archive","b) Cool","c) Hot","d) Premium"); answer="a) Archive"; explanation="Archive est le niveau le moins cher pour données rarement accédées."},
    @{question="Quel type de clé permet à l'utilisateur de gérer lui-même les clés ?"; options=@("a) Customer-managed key","b) Platform-managed key","c) Secret","d) Certificate"); answer="a) Customer-managed key"; explanation="CMK donne le contrôle des clés au client."},
    @{question="Quel service Azure permet de limiter l'accès à Key Vault au sein d'un réseau privé ?"; options=@("a) Private Endpoint","b) Public IP","c) VNet Peering","d) Azure DNS"); answer="a) Private Endpoint"; explanation="Private Endpoint connecte Key Vault via un réseau privé."},
    @{question="Quel composant réseau filtre le trafic entrant et sortant par port ?"; options=@("a) NSG","b) WAF","c) Azure Policy","d) Azure Monitor"); answer="a) NSG"; explanation="NSG filtre le trafic réseau au niveau couche 3-4."},
    @{question="Quel service protège les applications web contre les attaques HTTP ?"; options=@("a) WAF","b) NSG","c) Azure DNS","d) Load Balancer"); answer="a) WAF"; explanation="Un WAF protège contre les attaques de couche applicative."},
    @{question="Quel service chiffre les données en transit côté client ?"; options=@("a) TLS/HTTPS","b) HTTP","c) FTP","d) SMTP"); answer="a) TLS/HTTPS"; explanation="TLS chiffre le trafic entre le client et Azure."},
    @{question="Quel service gère la rotation des secrets et des certificats ?"; options=@("a) Azure Key Vault","b) Azure Monitor","c) Azure Policy","d) Azure DNS"); answer="a) Azure Key Vault"; explanation="Key Vault peut automatiser la rotation des secrets et certificats."},
    @{question="Quel rôle RBAC est adapté pour les administrateurs de secrets ?"; options=@("a) Key Vault Secrets Officer","b) Reader","c) Contributor","d) Owner"); answer="a) Key Vault Secrets Officer"; explanation="Ce rôle gère les secrets sans privilèges d'administration complète."},
    @{question="Quel type de chiffrement est appliqué par défaut aux comptes de stockage ?"; options=@("a) Storage Service Encryption","b) NSG","c) Azure Policy","d) Azure Monitor"); answer="a) Storage Service Encryption"; explanation="Azure chiffre les données de stockage par défaut."},
    @{question="Quel service rend les accès aux ressources plus sûrs en utilisant l'identité de la ressource ?"; options=@("a) Managed Identity","b) Guest User","c) VNet Peering","d) Azure DNS"); answer="a) Managed Identity"; explanation="Managed Identities éliminent les secrets codés en dur."},
    @{question="Quel service permet de stocker et gérer des clés cryptographiques dans Azure ?"; options=@("a) Azure Key Vault","b) Azure Monitor","c) Azure Policy","d) Azure DNS"); answer="a) Azure Key Vault"; explanation="Key Vault stocke des clés cryptographiques et des secrets."},
    @{question="Quel service permet l'accès privé à un service Azure via un réseau interne ?"; options=@("a) Private Endpoint","b) Public IP","c) VNet Peering","d) NSG"); answer="a) Private Endpoint"; explanation="Private Endpoint permet l'accès privé à un service Azure."}
)

$surveillanceBank = @(
    @{question="Quel service centralise la collecte de métriques et de logs dans Azure ?"; options=@("a) Azure Monitor","b) Azure Policy","c) Azure AD","d) Azure DNS"); answer="a) Azure Monitor"; explanation="Azure Monitor collecte les métriques et logs."},
    @{question="Quel espace de travail permet d'interroger les logs Azure ?"; options=@("a) Log Analytics Workspace","b) Storage Account","c) Azure AD","d) Azure DNS"); answer="a) Log Analytics Workspace"; explanation="Le workspace stocke et analyse les logs."},
    @{question="Quel langage est utilisé pour les requêtes sur les logs Azure ?"; options=@("a) KQL","b) SQL","c) JSON","d) YAML"); answer="a) KQL"; explanation="KQL est utilisé dans Log Analytics."},
    @{question="Quel service permet d'analyser les performances applicatives ?"; options=@("a) Application Insights","b) Azure Backup","c) Azure Policy","d) Azure DNS"); answer="a) Application Insights"; explanation="Application Insights analyse les applications."},
    @{question="Quel objet déclenche une alerte lorsque les seuils sont dépassés ?"; options=@("a) Alert Rule","b) NSG","c) VNet Peering","d) Azure Policy"); answer="a) Alert Rule"; explanation="Une alerte est déclenchée par une règle d'alarme."},
    @{question="Quel groupe d'action associe des notifications à une alerte ?"; options=@("a) Action Group","b) Resource Group","c) Management Group","d) Virtual Network"); answer="a) Action Group"; explanation="Action Groups définissent comment réagir aux alertes."},
    @{question="Quel service exécute des scripts automatisés planifiés ?"; options=@("a) Azure Automation","b) Azure Backup","c) Azure Policy","d) Azure DNS"); answer="a) Azure Automation"; explanation="Azure Automation exécute des runbooks planifiés."},
    @{question="Quel outil offre des rapports visuels interactifs ?"; options=@("a) Workbooks","b) NSG","c) VNet Peering","d) Azure Policy"); answer="a) Workbooks"; explanation="Workbooks sont des rapports interactifs dans Azure."},
    @{question="Quel paramètre configure l'envoi de diagnostics vers un workspace ?"; options=@("a) Diagnostic Settings","b) NSG","c) Azure Policy","d) Azure Backup"); answer="a) Diagnostic Settings"; explanation="Diagnostic Settings envoie les logs vers un workspace."},
    @{question="Quel service est utilisé pour visualiser des métriques temps réel sur un tableau de bord ?"; options=@("a) Dashboards","b) Azure Policy","c) Azure AD","d) Azure DNS"); answer="a) Dashboards"; explanation="Les dashboards affichent des métriques en temps réel."},
    @{question="Quel service permet d'agréger des logs de plusieurs subscriptions ?"; options=@("a) Log Analytics Workspace","b) Azure Policy","c) Azure AD","d) Azure Backup"); answer="a) Log Analytics Workspace"; explanation="Un workspace peut agréger des logs multi-subscriptions."},
    @{question="Quel service analyse les exceptions côté applicatif ?"; options=@("a) Application Insights","b) Azure Monitor","c) Azure Policy","d) Azure DNS"); answer="a) Application Insights"; explanation="Application Insights capture les exceptions applicatives."},
    @{question="Quel objet est utilisé pour surveiller la conformité des ressources ?"; options=@("a) Azure Policy","b) NSG","c) VNet Peering","d) Azure Backup"); answer="a) Azure Policy"; explanation="Azure Policy vérifie la conformité des ressources."},
    @{question="Quel service permet d'automatiser le nettoyage de métriques anciennes ?"; options=@("a) Azure Automation","b) Azure Backup","c) Azure Policy","d) Azure DNS"); answer="a) Azure Automation"; explanation="Azure Automation peut nettoyer les métriques et données historiques."},
    @{question="Quel service collecte le télémétrie des dépendances d'une application ?"; options=@("a) Application Insights","b) Azure Policy","c) Azure AD","d) Azure DNS"); answer="a) Application Insights"; explanation="Application Insights suit les dépendances externes."},
    @{question="Quel service permet de consulter les logs d'activité Azure ?"; options=@("a) Activity Log","b) Storage Account","c) Azure DNS","d) Azure Policy"); answer="a) Activity Log"; explanation="Activity Log trace les opérations de gestion Azure."}
)

$themeDefinitions = @(
    @{ folder = "Identités et types d'identité"; title = "Identités et types d'identité"; bank = $identityBank; start = 3; end = 9 },
    @{ folder = "Machines virtuelles & Calcul"; title = "Machines virtuelles & Calcul"; bank = $vmBank; start = 2; end = 9 },
    @{ folder = "RBAC & Contrôle d'accès"; title = "RBAC & Contrôle d'accès"; bank = $rbacBank; start = 2; end = 9 },
    @{ folder = "Réseaux & Connectivité"; title = "Réseaux & Connectivité"; bank = $networkBank; start = 2; end = 9 },
    @{ folder = "Ressources & Stockage"; title = "Ressources & Stockage"; bank = $resourcesBank; start = 2; end = 9 },
    @{ folder = "Surveillance & Gestion"; title = "Surveillance & Gestion"; bank = $surveillanceBank; start = 2; end = 9 },
    @{ folder = "Sécurité & Chiffrement"; title = "Sécurité & Chiffrement"; bank = $securityBank; start = 2; end = 9 },
)

foreach ($theme in $themeDefinitions) {
    $folderPath = Join-Path $base $theme.folder
    Create-QcmSeries -Folder $folderPath -TitlePrefix $theme.title -QuestionBank $theme.bank -StartIndex $theme.start -EndIndex $theme.end
}

Write-Host "QCM files created or skipped if already present."
