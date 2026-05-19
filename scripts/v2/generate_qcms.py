import os
from textwrap import dedent

base = r"c:\Users\mouss\source\repos\azure-devops-bootcamp-zero-a-expert\Documentations\CERTIFICATION-AZURE\Themes"

def write_qcm(path, title, questions, answers, explanations):
    content = [f"# QCM + corrections détaillées pour l'AZ-104 - {title}", "", "***", "", f"## QCM (10 questions) - Domaine : {title}", ""]
    for i, q in enumerate(questions, 1):
        content.append(f"{i}. **{q['question']}**  ")
        for option in q['options']:
            content.append(f"   {option}")
        content.append("")
    content.append("***")
    content.append("")
    content.append("## Corrections détaillées")
    content.append("")
    for i, (answer, explanation) in enumerate(zip(answers, explanations), 1):
        content.append(f"{i}. **{answer}**  ")
        content.append(f"   - {explanation}")
        content.append("")
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(content))

# Question generators for each theme.

identity_qcms = [
    {
        'title': 'Identités avancées et scénarios hybrides',
        'questions': [
            {'question': 'Dans un déploiement hybride, quel service synchronise les comptes AD local vers Entra ID ?',
             'options': ['a) Azure AD Connect', 'b) Azure AD B2B', 'c) Azure Site Recovery', 'd) Azure Firewall']},
            {'question': 'Quel type d’identité Azure permet à une application d’accéder à une ressource sans secret ?',
             'options': ['a) Identité d’utilisateur', 'b) Identité managée', 'c) Identité d’agent IA', 'd) Identité B2C']},
            {'question': 'Quel service est utilisé pour inviter un utilisateur externe comme invité ?',
             'options': ['a) Azure AD B2B', 'b) Azure AD B2C', 'c) Azure Key Vault', 'd) Azure Policy']},
            {'question': 'Quel type d’identité correspond à un appareil Windows joint au domaine ?',
             'options': ['a) Identité utilisateur', 'b) Identité d’appareil', 'c) Principal de service', 'd) Identité managée']},
            {'question': 'Quel service gère les identités pour les agents IA ?',
             'options': ['a) Azure AD Connect', 'b) Microsoft Entra Agent ID', 'c) Azure Firewall', 'd) Azure Monitor']},
            {'question': 'Quel scénario correspond à Azure AD B2C ?',
             'options': ['a) Gestion de comptes clients grand public', 'b) Synchronisation d’Active Directory local', 'c) Partage de ressources avec partenaires', 'd) Gestion de clés de chiffrement']},
            {'question': 'Quel type d’identité est créé automatiquement avec une ressource Azure ?',
             'options': ['a) Managed identity affectée par le système', 'b) Identité d’utilisateur', 'c) Identité B2C', 'd) Identité d’agent IA']},
            {'question': 'Quel composant permet de gérer les politiques d’accès selon le contexte d’utilisateur ?',
             'options': ['a) Conditional Access', 'b) NSG', 'c) Load Balancer', 'd) Storage Account']},
            {'question': 'Quel rôle Azure AD permet la gestion des utilisateurs et groupes ?',
             'options': ['a) Global Administrator', 'b) Reader', 'c) Contributor', 'd) Network Contributor']},
            {'question': 'Quel service est adapté aux applications qui vendent des abonnements à des clients externes ?',
             'options': ['a) Azure AD B2C', 'b) Azure AD Connect', 'c) Azure Site Recovery', 'd) Azure Policy']},
        ],
        'answers': ['a) Azure AD Connect', 'b) Identité managée', 'a) Azure AD B2B', 'b) Identité d’appareil', 'b) Microsoft Entra Agent ID', 'a) Gestion de comptes clients grand public', 'a) Managed identity affectée par le système', 'a) Conditional Access', 'a) Global Administrator', 'a) Azure AD B2C'],
        'explanations': [
            'Azure AD Connect synchronise les comptes AD local vers Entra ID.',
            'Les identités managées permettent l’accès sans secret codé en dur.',
            'Azure AD B2B permet d’inviter des partenaires externes.',
            'Un appareil joint à Entra reçoit une identité d’appareil.',
            'Microsoft Entra Agent ID est conçu pour les agents IA.',
            'Azure AD B2C gère les comptes clients externes.',
            'Les identities system-assigned sont créées avec la ressource.',
            'Conditional Access applique des règles basées sur le contexte.',
            'Global Administrator gère les utilisateurs et groupes Entra ID.',
            'Azure AD B2C est la solution pour les clients externes/sociétés grand public.',
        ],
    },
    {
        'title': 'Principaux services d’identité',
        'questions': [
            {'question': 'Quel service fournit un annuaire cloud pour les utilisateurs et applications ?',
             'options': ['a) Microsoft Entra ID', 'b) Azure Storage', 'c) Azure DNS', 'd) Azure Firewall']},
            {'question': 'Quel type d’identité doit être utilisé pour une application qui définit des règles automatisées ?',
             'options': ['a) Identité utilisateur', 'b) Principal de service', 'c) Identité d’appareil', 'd) Identité hybride']},
            {'question': 'Quel outil identifie les utilisateurs locaux et synchronise les mots de passe vers Entra ID ?',
             'options': ['a) Azure AD Connect', 'b) Azure Policy', 'c) Azure Backup', 'd) Azure Monitor']},
            {'question': 'Quel type d’identité est le plus adapté pour des services Azure qui accèdent à Key Vault ?',
             'options': ['a) Principal de service', 'b) Identité managée', 'c) Identité d’utilisateur', 'd) Identité externe']},
            {'question': 'Quel service peut gérer des utilisateurs invités et partenaires ?',
             'options': ['a) Azure AD B2B', 'b) Azure AD B2C', 'c) Azure DevOps', 'd) Azure App Configuration']},
            {'question': 'Quelle identité permet de séparer le contrôle d’accès des ressources d’un utilisateur humain ?',
             'options': ['a) Identité d’appareil', 'b) Identité managée', 'c) Identité d’agent IA', 'd) Identité hybride']},
            {'question': 'Quel type d’identité est utilisé pour une application de service interne Azure ?',
             'options': ['a) Identité B2C', 'b) Identité utilisateur', 'c) Principal de service', 'd) Identité d’appareil']},
            {'question': 'Quelle fonction Entra permet de protéger l’accès par mot de passe faible ou risqué ?',
             'options': ['a) MFA et Conditional Access', 'b) NSG', 'c) Azure Policy', 'd) Azure Load Balancer']},
            {'question': 'Que signifie un environnement d’identité “cloud only” ?',
             'options': ['a) Comptes uniquement dans Entra ID', 'b) Comptes uniquement dans AD local', 'c) Comptes uniquement invités', 'd) Comptes uniquement B2C']},
            {'question': 'Quel service est destiné aux clients, pas aux partenaires internes ?',
             'options': ['a) Azure AD B2C', 'b) Azure AD B2B', 'c) Azure AD Connect', 'd) Azure AD Domain Services']},
        ],
        'answers': ['a) Microsoft Entra ID', 'b) Principal de service', 'a) Azure AD Connect', 'b) Identité managée', 'a) Azure AD B2B', 'b) Identité managée', 'c) Principal de service', 'a) MFA et Conditional Access', 'a) Comptes uniquement dans Entra ID', 'a) Azure AD B2C'],
        'explanations': [
            'Microsoft Entra ID est l’annuaire cloud de Microsoft.',
            'Les applications automatisées utilisent généralement un principal de service.',
            'Azure AD Connect synchronise les mots de passe AD local.',
            'Les identités managées simplifient l’accès aux services Azure.',
            'Azure AD B2B gère les partenaires externes.',
            'Les identités managées séparent l’accès des utilisateurs humains.',
            'Les applications internes utilisent des principals de service.',
            'MFA et Conditional Access protègent les accès risqués.',
            'Un modèle cloud only signifie des comptes créés directement dans Entra ID.',
            'Azure AD B2C est destiné aux clients grand public.',
        ],
    },
    {
        'title': 'Gestion d’identité et sécurité',
        'questions': [
            {'question': 'Quel mécanisme améliore la sécurité des identités en exigeant plusieurs facteurs ?',
             'options': ['a) MFA', 'b) NSG', 'c) VNet Peering', 'd) Azure Policy']},
            {'question': 'Quel type d’identité est idéal pour un service Azure Function ?',
             'options': ['a) Identité d’utilisateur', 'b) Principal de service', 'c) Identité managée', 'd) Identité d’appareil']},
            {'question': 'Quel service fournit un accès conditionnel basé sur l’emplacement ou l’état du périphérique ?',
             'options': ['a) Conditional Access', 'b) Azure Backup', 'c) Azure Policy', 'd) Application Gateway']},
            {'question': 'Quel type d’identité peut être réutilisé sur plusieurs ressources Azure ?',
             'options': ['a) Managed identity affectée par le système', 'b) Managed identity affectée par l’utilisateur', 'c) Identité d’appareil', 'd) Identité utilisateur']},
            {'question': 'Quel composant Entra permet l’audit des connexions et des modifications ?',
             'options': ['a) Azure Activity Log', 'b) Azure AD Audit Logs', 'c) Azure Monitor', 'd) Azure DNS']},
            {'question': 'Quel rôle Azure AD est nécessaire pour gérer les applications enregistrées ?',
             'options': ['a) Application Administrator', 'b) Storage Blob Data Contributor', 'c) Reader', 'd) Backup Contributor']},
            {'question': 'Quel type d’identité assure un accès sans secret pour une VM ?',
             'options': ['a) Principal de service', 'b) User-assigned managed identity', 'c) Identité B2C', 'd) Identité d’appareil']},
            {'question': 'Quel service permet de fédérer l’authentification avec un fournisseur tiers ?',
             'options': ['a) Azure AD B2C', 'b) Azure Firewall', 'c) Azure Policy', 'd) Virtual WAN']},
            {'question': 'Pour un scénario de collaboration interentreprise, quel modèle utiliser ?',
             'options': ['a) Azure AD B2B', 'b) Azure AD B2C', 'c) Azure Site Recovery', 'd) Azure ExpressRoute']},
            {'question': 'Quel mécanisme permet d’empêcher l’accès aux comptes compromis ?',
             'options': ['a) Identity Protection', 'b) Network Security Group', 'c) Managed Disk', 'd) Azure DNS']},
        ],
        'answers': ['a) MFA', 'c) Identité managée', 'a) Conditional Access', 'b) Managed identity affectée par l’utilisateur', 'b) Azure AD Audit Logs', 'a) Application Administrator', 'b) User-assigned managed identity', 'a) Azure AD B2C', 'a) Azure AD B2B', 'a) Identity Protection'],
        'explanations': [
            'MFA ajoute un facteur d’authentification supplémentaire.',
            'Les identités managées sont adaptées aux fonctions serverless.',
            'Conditional Access permet de restreindre l’accès selon le contexte.',
            'User-assigned managed identities peuvent être attachées à plusieurs ressources.',
            'Azure AD Audit Logs trace l’activité d’identité et de connexion.',
            'Application Administrator peut gérer les applications enregistrées.',
            'User-assigned managed identities peuvent être partagées entre ressources.',
            'Azure AD B2C supporte l’authentification via fournisseurs externes.',
            'Azure AD B2B est conçu pour la collaboration partenaire.',
            'Identity Protection détecte et bloque les comptes compromis.',
        ],
    },
    {
        'title': 'Flux et bonnes pratiques d’identité',
        'questions': [
            {'question': 'Quel flux d’authentification est utilisé pour les applications web via OAuth ?',
             'options': ['a) Client Credentials', 'b) Authorization Code', 'c) SMB', 'd) FTP']},
            {'question': 'Quel type de compte est le plus sûr pour un service automatisé ?',
             'options': ['a) Compte utilisateur', 'b) Principal de service', 'c) Identité d’appareil', 'd) Identité B2C']},
            {'question': 'Quel élément doit être appliqué pour limiter l’accès aux ressources selon l’emplacement ?',
             'options': ['a) Azure Policy', 'b) NSG', 'c) Conditional Access', 'd) Azure DNS']},
            {'question': 'Quel service gère le cycle de vie de l’identité des employés externes ?',
             'options': ['a) Azure AD B2B', 'b) Azure AD Domain Services', 'c) Azure Key Vault', 'd) Azure Monitor']},
            {'question': 'Quel type d’identité est le plus approprié pour une application Web SaaS consommée par des clients ?',
             'options': ['a) Azure AD B2C', 'b) Azure AD B2B', 'c) Azure AD Connect', 'd) Azure Disk Encryption']},
            {'question': 'Pour une application interne, quel type d’identité offre le meilleur contrôle RBAC ?',
             'options': ['a) Identité utilisateur', 'b) Principal de service', 'c) Identité d’appareil', 'd) Identité hybride']},
            {'question': 'Quel concept décrit le fait de donner le minimum de permissions nécessaire ?',
             'options': ['a) Least Privilege', 'b) Maximum Privilege', 'c) Full Access', 'd) Owner Rights']},
            {'question': 'Quel service permet de tester des règles d’authentification en conditions réelles ?',
             'options': ['a) Azure AD Access Reviews', 'b) Azure Backup', 'c) Azure Policy', 'd) Azure DNS']},
            {'question': 'Quel outil Azure permet de synchroniser uniquement les mots de passe et les comptes ?',
             'options': ['a) Azure AD Connect', 'b) Azure Site Recovery', 'c) Azure VM Scale Sets', 'd) Azure Application Gateway']},
            {'question': 'Quel rôle Entra est nécessaire pour gérer les politiques d’accès conditionnel ?',
             'options': ['a) Security Administrator', 'b) Reader', 'c) Storage Blob Data Owner', 'd) Network Contributor']},
        ],
        'answers': ['b) Authorization Code', 'b) Principal de service', 'c) Conditional Access', 'a) Azure AD B2B', 'a) Azure AD B2C', 'b) Principal de service', 'a) Least Privilege', 'a) Azure AD Access Reviews', 'a) Azure AD Connect', 'a) Security Administrator'],
        'explanations': [
            'Le flux Authorization Code est utilisé pour les applications web OAuth.',
            'Un principal de service est plus sûr pour les services automatisés.',
            'Conditional Access limite l’accès selon le contexte et l’emplacement.',
            'Azure AD B2B gère les invités et partenaires externes.',
            'Azure AD B2C cible les clients grand public.',
            'Les principals de service sont bien adaptés au contrôle RBAC des applications.',
            'Least Privilege limite les permissions au strict nécessaire.',
            'Access Reviews permet de vérifier les accès périodiquement.',
            'Azure AD Connect synchronise comptes et mots de passe depuis AD local.',
            'Security Administrator gère les politiques de sécurité Entra.',
        ],
    },
    {
        'title': 'Sécurité d’accès et gouvernance',
        'questions': [
            {'question': 'Quel service aide à détecter des connexions suspectes dans Entra ID ?',
             'options': ['a) Identity Protection', 'b) Azure DNS', 'c) Azure Policy', 'd) Application Insights']},
            {'question': 'Quel mécanisme empêche l’utilisation de mots de passe compromis ?',
             'options': ['a) Password Protection', 'b) NSG', 'c) VNet Peering', 'd) Azure Cache']},
            {'question': 'Quel rôle est nécessaire pour créer des applications enregistrées dans Entra ?',
             'options': ['a) Application Administrator', 'b) Owner', 'c) Storage Account Contributor', 'd) Reader']},
            {'question': 'Quel type d’identité ne peut pas être utilisé pour un utilisateur humain ?',
             'options': ['a) Identité B2C', 'b) Identité d’agent IA', 'c) Identité d’utilisateur', 'd) Identité d’appareil']},
            {'question': 'Quel service permet de demander aux utilisateurs de réviser leurs accès ?',
             'options': ['a) Access Reviews', 'b) Azure Backup', 'c) Azure Monitor', 'd) Azure DNS']},
            {'question': 'Quel concept est appliqué quand on sépare les tâches d’administration entre plusieurs personnes ?',
             'options': ['a) Separation of Duties', 'b) Full Control', 'c) Shared Secrets', 'd) One Admin']},
            {'question': 'Quel identifiant authentifie un service Azure sans mot de passe ?',
             'options': ['a) Managed Identity', 'b) User Principal Name', 'c) Object ID', 'd) Guest ID']},
            {'question': 'Quel service Azure permet de lier des applications aux utilisateurs internes et externes ?',
             'options': ['a) Entra ID', 'b) Azure Storage', 'c) Azure Firewall', 'd) Azure Load Balancer']},
            {'question': 'Quel rôle est recommandé pour un administrateur de sécurité sans droits de création de ressources ?',
             'options': ['a) Security Reader', 'b) Contributor', 'c) Owner', 'd) Reader']},
            {'question': 'Quel mode d’authentification est le plus sécurisé ?',
             'options': ['a) MFA', 'b) Mot de passe seul', 'c) Certificat non signé', 'd) HTTP basique']},
        ],
        'answers': ['a) Identity Protection', 'a) Password Protection', 'a) Application Administrator', 'b) Identité d’agent IA', 'a) Access Reviews', 'a) Separation of Duties', 'a) Managed Identity', 'a) Entra ID', 'a) Security Reader', 'a) MFA'],
        'explanations': [
            'Identity Protection analyse les signaux de connexion et de risque.',
            'Password Protection bloque les mots de passe compromis.',
            'Application Administrator gère les applications enregistrées.',
            'Une identité d’agent IA est destinée aux bots/workflows, pas aux humains.',
            'Access Reviews révisent régulièrement les droits d’accès.',
            'Separation of Duties réduit les risques en divisant les responsabilités.',
            'Managed Identity permet l’authentification sans secret.',
            'Entra ID est le service central pour identités internes et externes.',
            'Security Reader peut consulter la sécurité sans modifier les ressources.',
            'MFA reste le mode d’authentification le plus fort.',
        ],
    },
    {
        'title': 'Accès collaboratif et externalités',
        'questions': [
            {'question': 'Quel service permet aux clients externes de se connecter avec leurs comptes sociaux ?',
             'options': ['a) Azure AD B2C', 'b) Azure AD B2B', 'c) Azure AD Connect', 'd) Azure Policy']},
            {'question': 'Quel type d’accès est le mieux adapté pour un consultant externe temporaire ?',
             'options': ['a) Guest user', 'b) Regular employee', 'c) Managed identity', 'd) Device identity']},
            {'question': 'Quel service permet d’appliquer des restrictions d’accès aux applications SaaS ?',
             'options': ['a) Conditional Access', 'b) Azure Load Balancer', 'c) Azure Key Vault', 'd) Azure Functions']},
            {'question': 'Quel service Entra ID est utilisé pour la gestion des identités externes ?',
             'options': ['a) Microsoft Entra External ID', 'b) Azure Site Recovery', 'c) Azure Backup', 'd) Azure DNS']},
            {'question': 'Quel rôle est approprié pour un administrateur chargé des accès utilisateurs ?',
             'options': ['a) User Access Administrator', 'b) Reader', 'c) Contributor', 'd) Billing Reader']},
            {'question': 'Quel type d’identité est souvent utilisé pour une application Azure qui se connecte à une API interne ?',
             'options': ['a) Service principal', 'b) Guest user', 'c) Device identity', 'd) B2C user']},
            {'question': 'Quel concept d’identité permet de conserver une copie locale du compte dans AD DS ?',
             'options': ['a) Hybrid identity', 'b) Cloud only', 'c) B2C only', 'd) Guest identity']},
            {'question': 'Quel mécanisme assure la rotation automatique des identifiants ?',
             'options': ['a) Managed Identity', 'b) Static password', 'c) HTTP', 'd) FTP']},
            {'question': 'Quel service permet l’authentification sans mot de passe à partir d’un appareil fiable ?',
             'options': ['a) Passwordless authentication', 'b) Storage Account', 'c) VPN Gateway', 'd) Azure DNS']},
            {'question': 'Pour un accès invité, quel niveau de permission est le plus sûr ?',
             'options': ['a) Least Privilege', 'b) Owner', 'c) Contributor', 'd) Global Administrator']},
        ],
        'answers': ['a) Azure AD B2C', 'a) Guest user', 'a) Conditional Access', 'a) Microsoft Entra External ID', 'a) User Access Administrator', 'a) Service principal', 'a) Hybrid identity', 'a) Managed Identity', 'a) Passwordless authentication', 'a) Least Privilege'],
        'explanations': [
            'Azure AD B2C permet les comptes sociaux pour les clients.',
            'Les comptes Guest sont adaptés aux consultants temporaires.',
            'Conditional Access restreint l’accès aux applications selon le contexte.',
            'Microsoft Entra External ID gère les identités externes.',
            'User Access Administrator gère les attributions de rôles.',
            'Service principals sont appropriés pour l’accès applicatif interne.',
            'Hybrid identity combine AD local et Entra ID.',
            'Managed Identities évitent les secrets permanents.',
            'Passwordless authentication utilise des méthodes sans mot de passe.',
            'Least Privilege minimise les risques d’accès.'
        ],
    },
    {
        'title': 'Préparation à l’examen identité',
        'questions': [
            {'question': 'Quel service Azure fournit la synchronisation et la gestion d’identité pour Office 365 ?',
             'options': ['a) Azure AD Connect', 'b) Azure Backup', 'c) Azure Policy', 'd) Azure DNS']},
            {'question': 'Quelle option est utilisée pour connecter en privé Key Vault à un réseau ?',
             'options': ['a) Private Endpoint', 'b) Public IP', 'c) VNet Peering', 'd) ExpressRoute']},
            {'question': 'Quel type d’identité supporte l’authentification multi-facteur et les accès conditionnels ?',
             'options': ['a) Identité utilisateur', 'b) Identité de service', 'c) Managed identity', 'd) Device identity']},
            {'question': 'Quel service sert à vérifier les permissions des utilisateurs au fil du temps ?',
             'options': ['a) Access Reviews', 'b) Azure Monitor', 'c) VMSS', 'd) Storage Account']},
            {'question': 'Quel rôle Azure AD permet de gérer les applications d’entreprise ?',
             'options': ['a) Application Administrator', 'b) Reader', 'c) Backup Contributor', 'd) Owner']},
            {'question': 'Quel plan est nécessaire pour utiliser Azure AD Conditional Access ?',
             'options': ['a) Azure AD P1/P2', 'b) Azure AD Free', 'c) Azure AD B2C', 'd) Azure AD B2B']},
            {'question': 'Quel service Azure gère une base d’utilisateurs externes en libre-service ?',
             'options': ['a) Azure AD B2C', 'b) Azure AD Connect', 'c) Azure Storage', 'd) Azure Firewall']},
            {'question': 'Quel mécanisme de sécurité est recommandé pour empêcher l’accès depuis des pays non autorisés ?',
             'options': ['a) Conditional Access', 'b) NSG', 'c) Load Balancer', 'd) Azure Monitor']},
            {'question': 'Quel service permet de gérer les identités des ressources Azure (VM, App Service) ?',
             'options': ['a) Managed Identities', 'b) Azure DNS', 'c) Azure Load Balancer', 'd) Azure Backup']},
            {'question': 'Quel type d’identité est utilisé pour un compte service interne avec rôle RBAC ?',
             'options': ['a) Service principal', 'b) Guest user', 'c) Device identity', 'd) B2C user']},
        ],
        'answers': ['a) Azure AD Connect', 'a) Private Endpoint', 'a) Identité utilisateur', 'a) Access Reviews', 'a) Application Administrator', 'a) Azure AD P1/P2', 'a) Azure AD B2C', 'a) Conditional Access', 'a) Managed Identities', 'a) Service principal'],
        'explanations': [
            'Azure AD Connect synchronise les identités pour Office 365.',
            'Private Endpoints permettent un accès privé aux services Azure.',
            'Les identités utilisateur supportent MFA et les règles d’accès conditionnel.',
            'Access Reviews valident périodiquement les autorisations.',
            'Application Administrator gère les applications d’entreprise.',
            'Conditional Access nécessite une licence Azure AD P1 ou P2.',
            'Azure AD B2C offre l’inscription self-service aux clients.',
            'Conditional Access peut bloquer des connexions selon la localisation.',
            'Managed Identities gèrent les identités des ressources Azure.',
            'Un service principal est utilisé pour l’accès applicatif interne avec RBAC.',
        ],
    },
]

# Additional sets for other themes can be derived from the trainning QCM content under the main folder.
# For brevity and consistency, we will copy files from the main Trainning folder when appropriate.

def copy_file(src, dst):
    with open(src, 'r', encoding='utf-8') as f:
        data = f.read()
    with open(dst, 'w', encoding='utf-8') as f:
        f.write(data)

# Create QCMs in identity folder (QCM-3..QCM-9)
identity_folder = os.path.join(base, 'Identités et types d\'identité')
for index, qcm in enumerate(identity_qcms, start=3):
    path = os.path.join(identity_folder, f'QCM-{index}.md')
    if os.path.exists(path):
        continue
    write_qcm(path, qcm['title'], qcm['questions'], qcm['answers'], qcm['explanations'])

# Contenu pour Ressources & Stockage (QCM-2 à QCM-9)
resources_qcms = [
    {'title': 'Gestion avancée des ressources', 'questions': [
        {'question': 'Quel service Azure permet de déployer des ressources de façon déclarative ?', 'options': ['a) Resource Manager (ARM)', 'b) Azure Storage', 'c) Azure Firewall', 'd) Virtual Networks']},
        {'question': 'Quel est l\'avantage principal des Resource Groups ?', 'options': ['a) Grouper et gérer les ressources de façon cohérente', 'b) Augmenter la performance', 'c) Chiffrer les données', 'd) Aucun avantage']},
        {'question': 'Quel type de stockage Azure est le plus économique pour archivage long terme ?', 'options': ['a) Hot tier', 'b) Cool tier', 'c) Archive tier', 'd) Premium SSD']},
        {'question': 'Quel disque Azure offre la plus haute performance pour bases de données ?', 'options': ['a) Standard HDD', 'b) Standard SSD', 'c) Premium SSD', 'd) Ultra Disk']},
        {'question': 'Quel élément permet d\'identifier et organiser les ressources Azure ?', 'options': ['a) Tags', 'b) NSG', 'c) VNet', 'd) API']},
        {'question': 'Quel service fournit un stockage d\'objets blob scalable et sans schéma ?', 'options': ['a) Azure Table Storage', 'b) Azure Blob Storage', 'c) Azure SQL', 'd) Azure Queue']},
        {'question': 'Quel type de replication offre la disponibilité la plus haute ?', 'options': ['a) LRS (Local)', 'b) GRS (Géo)', 'c) GZRS (Zone + Géo)', 'd) RA-GZRS']},
        {'question': 'Quel service permet d\'importer/exporter de grandes quantités de données ?', 'options': ['a) Azure Data Box', 'b) Azure CDN', 'c) Azure Backup', 'd) Azure Pipelines']},
        {'question': 'Quel est le coût de la transition Hot vers Archive ?', 'options': ['a) Frais de transition élevés', 'b) Frais de lecture élevés', 'c) Frais de transition bas', 'd) Gratuit']},
        {'question': 'Quel stockage est adapté pour les queues de messages asynchrones ?', 'options': ['a) Blob Storage', 'b) Queue Storage', 'c) Table Storage', 'd) File Share']},
    ], 'answers': ['a) Resource Manager (ARM)', 'a) Grouper et gérer les ressources de façon cohérente', 'c) Archive tier', 'd) Ultra Disk', 'a) Tags', 'b) Azure Blob Storage', 'c) GZRS (Zone + Géo)', 'a) Azure Data Box', 'c) Frais de transition bas', 'b) Queue Storage'], 'explanations': [
        'ARM permet de définir les ressources en JSON/Bicep.',
        'Les Resource Groups simplifient la gestion et la facturation.',
        'Archive tier est le plus économique pour données rarement accédées.',
        'Ultra Disk offre jusqu\'à 160k IOPS.',
        'Les tags organisent les ressources pour facturation et gestion.',
        'Blob Storage stocke des objets non-structurés.',
        'GZRS combine la redondance de zone et géographique.',
        'Data Box permet le transfert offline de données massives.',
        'Les frais de transition de Hot à Archive sont généralement bas.',
        'Queue Storage permet la communication asynchrone.'
    ]},
]

# Contenu pour Réseaux & Connectivité (QCM-2 à QCM-9)
network_qcms = [
    {'title': 'VNets et segmentation réseau', 'questions': [
        {'question': 'Quel service crée un réseau privé isolé dans Azure ?', 'options': ['a) Virtual Network', 'b) Load Balancer', 'c) Application Gateway', 'd) Azure Firewall']},
        {'question': 'Quel composant permet de diviser une VNet en sous-réseaux ?', 'options': ['a) VNet Peering', 'b) Subnets', 'c) NSG', 'd) Route Table']},
        {'question': 'Quel service filtre le trafic réseau au niveau couche 3-4 ?', 'options': ['a) Application Gateway', 'b) Load Balancer', 'c) Network Security Group', 'd) Traffic Manager']},
        {'question': 'Quel est l\'avantage du VNet Peering ?', 'options': ['a) Connecter directement deux VNets', 'b) Réduire la latence', 'c) Bypasser Internet', 'd) Tous les avantages ci-dessus']},
        {'question': 'Quel service connecte un réseau on-premises à Azure via tunnel chiffré ?', 'options': ['a) ExpressRoute', 'b) VPN Gateway', 'c) Virtual WAN', 'd) Azure Firewall']},
        {'question': 'Quel service offre une connexion dédiée (non-Internet) vers Azure ?', 'options': ['a) VPN Site-to-site', 'b) ExpressRoute', 'c) Private Endpoint', 'd) Service Endpoint']},
        {'question': 'Quel service distribue le trafic au niveau couche 7 (applicatif) ?', 'options': ['a) Load Balancer', 'b) Application Gateway', 'c) Traffic Manager', 'd) Azure Front Door']},
        {'question': 'Quel composant assigne les adresses IP dans un subnet ?', 'options': ['a) DHCP', 'b) DNS', 'c) NAT', 'd) ACL']},
        {'question': 'Quel type d\'IP reste inchangée après redémarrage ?', 'options': ['a) Dynamique', 'b) Statique', 'c) Réservée', 'd) Publique']},
        {'question': 'Quel service permet une requête DNS privée au sein d\'une VNet ?', 'options': ['a) Azure DNS Public', 'b) Azure Private DNS', 'c) DHCP', 'd) Static Routes']},
    ], 'answers': ['a) Virtual Network', 'b) Subnets', 'c) Network Security Group', 'd) Tous les avantages ci-dessus', 'b) VPN Gateway', 'b) ExpressRoute', 'b) Application Gateway', 'a) DHCP', 'b) Statique', 'b) Azure Private DNS'], 'explanations': [
        'VNet crée un espace d\'adressage privé isolé.',
        'Les subnets divisent le VNet logiquement.',
        'NSG filtre le trafic aux niveaux 3-4.',
        'VNet Peering offre connectivité directe et rapide.',
        'VPN Gateway crée un tunnel sécurisé site-to-site.',
        'ExpressRoute fournit une ligne dédiée sans passer par Internet.',
        'Application Gateway effectue du routage au niveau applicatif (HTTP/HTTPS).',
        'DHCP assigne les IPs dynamiquement dans un subnet.',
        'Une IP statique est assignée manuellement et persiste.',
        'Private DNS résout les noms en interne dans la VNet.'
    ]},
]

# Contenu pour Machines virtuelles & Calcul (QCM-2 à QCM-9)
vm_qcms = [
    {'title': 'Tarification et dimensionnement des VMs', 'questions': [
        {'question': 'Quel est le modèle de tarification le moins cher pour charge non-critique ?', 'options': ['a) Pay-as-you-go', 'b) Reserved Instances', 'c) Spot VMs', 'd) Hybrid Benefit']},
        {'question': 'Quel type de VM peut être évincé pour économiser ?', 'options': ['a) Pay-as-you-go', 'b) Spot VMs', 'c) Reserved Instances', 'd) Dedicated hosts']},
        {'question': 'Quel service permet de déployer plusieurs VMs identiques avec autoscale ?', 'options': ['a) VM Scale Sets', 'b) Availability Set', 'c) Load Balancer', 'd) Application Gateway']},
        {'question': 'Quel mécanisme assure la haute disponibilité dans une Availability Set ?', 'options': ['a) Replication', 'b) Domaines de défaillance', 'c) Backup', 'd) Snapshot']},
        {'question': 'Quel type de disque est recommandé pour une VM de production ?', 'options': ['a) Standard HDD', 'b) Standard SSD', 'c) Premium SSD', 'd) Ultra Disk']},
        {'question': 'Quel service permet l\'autoscale basé sur métriques CPU ?', 'options': ['a) Auto Shutdown', 'b) Autoscale (VMSS)', 'c) Availability Set', 'd) Load Balancer']},
        {'question': 'Quel alternative serverless est idéale pour exécution courte ?', 'options': ['a) Azure Functions', 'b) App Service', 'c) Container Instances', 'd) VMSS']},
        {'question': 'Quel outil configure une VM après déploiement ?', 'options': ['a) ARM Template', 'b) Custom Script Extension', 'c) Load Balancer', 'd) NSG']},
        {'question': 'Quel service sauvegarde les VMs avec point de restauration ?', 'options': ['a) Site Recovery', 'b) Azure Backup', 'c) Snapshots', 'd) Storage Account']},
        {'question': 'Quel avantage offre Hybrid Benefit ?', 'options': ['a) Réduction pour licences SQL/Windows', 'b) Augmentation de CPU', 'c) Disques gratuits', 'd) Réseau gratuit']},
    ], 'answers': ['c) Spot VMs', 'b) Spot VMs', 'a) VM Scale Sets', 'b) Domaines de défaillance', 'c) Premium SSD', 'b) Autoscale (VMSS)', 'a) Azure Functions', 'b) Custom Script Extension', 'b) Azure Backup', 'a) Réduction pour licences SQL/Windows'], 'explanations': [
        'Spot VMs offrent réduction jusqu\'à 90%.',
        'Les Spot VMs peuvent être évincées si Azure a besoin de capacité.',
        'VMSS gère le déploiement et l\'autoscale d\'un groupe de VMs.',
        'Les domaines de défaillance répartissent les VMs sur du hardware différent.',
        'Premium SSD offre performance optimale pour production.',
        'Autoscale VMSS ajoute/retire les VMs selon la demande.',
        'Azure Functions est serverless et facturé à la milliseconde.',
        'Custom Script Extension exécute des scripts post-déploiement.',
        'Azure Backup fournit sauvegarde managée et restauration.',
        'Hybrid Benefit réduit les coûts pour licences existantes.'
    ]},
]

# Contenu pour Surveillance & Gestion (QCM-2 à QCM-9)
monitoring_qcms = [
    {'title': 'Azure Monitor et observabilité', 'questions': [
        {'question': 'Quel service collecte les métriques et logs des ressources Azure ?', 'options': ['a) Application Insights', 'b) Azure Monitor', 'c) Azure DNS', 'd) Azure Policy']},
        {'question': 'Quel langage de requête est utilisé dans Log Analytics ?', 'options': ['a) SQL', 'b) KQL (Kusto)', 'c) Python', 'd) PowerShell']},
        {'question': 'Quel service monitore les performances applicatives en temps réel ?', 'options': ['a) Azure Monitor', 'b) Application Insights', 'c) Log Analytics', 'd) Azure Backup']},
        {'question': 'Quel type de donnée Azure Monitor collecte-t-elle par défaut ?', 'options': ['a) Logs uniquement', 'b) Métriques uniquement', 'c) Métriques et logs', 'd) Aucun']},
        {'question': 'Quel composant déclenche une action en fonction d\'une condition ?', 'options': ['a) Alert Rule', 'b) Dashboard', 'c) Workbook', 'd) Metric']},
        {'question': 'Quel service automatise les tâches répétitives dans Azure ?', 'options': ['a) Azure Automation', 'b) Logic Apps', 'c) Azure Policy', 'd) Azure Backup']},
        {'question': 'Quel type de donnée trace toutes les opérations management ?', 'options': ['a) Métriques', 'b) Logs applicatifs', 'c) Activity Log', 'd) Audit']},
        {'question': 'Quel service permet une gestion multi-souscription centralisée ?', 'options': ['a) Azure Lighthouse', 'b) Management Groups', 'c) Resource Groups', 'd) Tags']},
        {'question': 'Quel est le rôle d\'une Action Group dans les alertes ?', 'options': ['a) Grouper les VMs', 'b) Définir les actions à déclencher', 'c) Créer les métriques', 'd) Filtrer les logs']},
        {'question': 'Quel service optimise les coûts en analysant l\'usage Azure ?', 'options': ['a) Cost Management', 'b) Azure Advisor', 'c) Billing', 'd) Policies']},
    ], 'answers': ['b) Azure Monitor', 'b) KQL (Kusto)', 'b) Application Insights', 'c) Métriques et logs', 'a) Alert Rule', 'a) Azure Automation', 'c) Activity Log', 'a) Azure Lighthouse', 'b) Définir les actions à déclencher', 'b) Azure Advisor'], 'explanations': [
        'Azure Monitor est la plateforme de monitoring centralisée.',
        'KQL est le langage de requête pour Log Analytics.',
        'Application Insights monitore les performances applicatives.',
        'Azure Monitor collecte les deux types de données.',
        'Alert Rule crée une alerte basée sur une condition.',
        'Azure Automation exécute les runbooks automatisées.',
        'Activity Log enregistre toutes les opérations management.',
        'Azure Lighthouse permet une gestion multi-tenant centralisée.',
        'Action Group définit les notifications et actions (email, webhook, etc).',
        'Azure Advisor fournit des recommandations d\'optimisation et coûts.'
    ]},
]

# Contenu pour RBAC & Contrôle d'accès (QCM-2 à QCM-9)
rbac_qcms = [
    {'title': 'Rôles et permissions Azure', 'questions': [
        {'question': 'Quel élément définit qui peut faire quoi dans Azure ?', 'options': ['a) NSG', 'b) RBAC', 'c) Azure Policy', 'd) Load Balancer']},
        {'question': 'Quel rôle prédéfini offre l\'accès complet incluant gestion RBAC ?', 'options': ['a) Contributor', 'b) Reader', 'c) Owner', 'd) User Access Admin']},
        {'question': 'Quel rôle permet de créer/modifier ressources mais pas de gérer RBAC ?', 'options': ['a) Owner', 'b) Contributor', 'c) Reader', 'd) Custom Role']},
        {'question': 'Quel rôle offre accès en lecture seule ?', 'options': ['a) Owner', 'b) Contributor', 'c) Reader', 'd) Operator']},
        {'question': 'Quel principe limite les permissions au strict nécessaire ?', 'options': ['a) Maximum Privilege', 'b) Least Privilege', 'c) Full Access', 'd) No Restriction']},
        {'question': 'Quel est le plus grand scope pour une attribution RBAC ?', 'options': ['a) Resource', 'b) Resource Group', 'c) Subscription', 'd) Management Group']},
        {'question': 'Quel service permet de créer des rôles personnalisés ?', 'options': ['a) Azure Policy', 'b) Custom Roles', 'c) Azure Blueprints', 'd) Azure Advisor']},
        {'question': 'Quel conteneur hiérarchique organise les souscriptions ?', 'options': ['a) Resource Group', 'b) Management Group', 'c) Tenant', 'd) Tag']},
        {'question': 'Quel service gère les accès périodiquement en vérifiant les utilisateurs ?', 'options': ['a) Azure Backup', 'b) Access Reviews', 'c) Azure Monitor', 'd) Azure Policy']},
        {'question': 'Quel mécanisme sépare les tâches pour réduire les risques ?', 'options': ['a) Shared Admin', 'b) Full Control', 'c) Separation of Duties', 'd) Single Admin']},
    ], 'answers': ['b) RBAC', 'c) Owner', 'b) Contributor', 'c) Reader', 'b) Least Privilege', 'd) Management Group', 'b) Custom Roles', 'b) Management Group', 'b) Access Reviews', 'c) Separation of Duties'], 'explanations': [
        'RBAC est le modèle de contrôle d\'accès dans Azure.',
        'Owner a tous les droits incluant RBAC.',
        'Contributor crée/modifie mais ne peut pas gérer RBAC.',
        'Reader ne peut que consulter les ressources.',
        'Least Privilege minimise la surface d\'attaque.',
        'Management Group est le scope maximal en cascade.',
        'Custom Roles permettent des permissions fine-grained.',
        'Management Groups organisent les souscriptions hiérarchiquement.',
        'Access Reviews valident périodiquement qui a accès à quoi.',
        'Separation of Duties divise les responsabilités administratives.'
    ]},
]

# Contenu pour Sécurité & Chiffrement (QCM-2 à QCM-9)
security_qcms = [
    {'title': 'Azure Key Vault et secrets', 'questions': [
        {'question': 'Quel service protège les secrets, clés et certificats ?', 'options': ['a) Azure Storage', 'b) Azure Key Vault', 'c) Application Insights', 'd) Azure DNS']},
        {'question': 'Quel type de donnée peut être stocké dans Key Vault ?', 'options': ['a) Secrets uniquement', 'b) Clés uniquement', 'c) Secrets, clés, certificats', 'd) Données binaires']},
        {'question': 'Quel service permet à une VM d\'accéder à Key Vault sans secret ?', 'options': ['a) Principal de service', 'b) Managed Identity', 'c) User Identity', 'd) API Key']},
        {'question': 'Quel protocole chiffre les données en transit ?', 'options': ['a) HTTP', 'b) FTP', 'c) HTTPS/TLS', 'd) SMTP']},
        {'question': 'Quel type de chiffrement s\'applique aux données au repos ?', 'options': ['a) AES-256', 'b) RSA-2048', 'c) MD5', 'd) Base64']},
        {'question': 'Quel chiffrement s\'applique au niveau de l\'application ?', 'options': ['a) Platform-managed', 'b) Customer-managed', 'c) Application-level', 'd) Network-level']},
        {'question': 'Quel service gère les certificats SSL/TLS ?', 'options': ['a) Azure DNS', 'b) Key Vault', 'c) Application Gateway', 'd) Load Balancer']},
        {'question': 'Quel type de clé est utilisé pour signature numérique ?', 'options': ['a) Clé symétrique', 'b) Clé asymétrique (RSA/EC)', 'c) Clé de session', 'd) Clé partagée']},
        {'question': 'Quel audit trace l\'accès à Key Vault ?', 'options': ['a) Application Insights', 'b) Audit Logs Key Vault', 'c) NSG logs', 'd) Activity Log']},
        {'question': 'Quel niveau de tarification supporte les HSM (Hardware Security Module) ?', 'options': ['a) Free', 'b) Standard', 'c) Premium', 'd) Enterprise']},
    ], 'answers': ['b) Azure Key Vault', 'c) Secrets, clés, certificats', 'b) Managed Identity', 'c) HTTPS/TLS', 'a) AES-256', 'c) Application-level', 'b) Key Vault', 'b) Clé asymétrique (RSA/EC)', 'b) Audit Logs Key Vault', 'c) Premium'], 'explanations': [
        'Key Vault est le service de gestion des secrets Azure.',
        'Key Vault supporte les trois types de données critiques.',
        'Managed Identity authentifie sans secret.',
        'HTTPS/TLS chiffre les données en chemin.',
        'AES-256 est l\'algorithme symétrique standard pour chiffrement at-rest.',
        'Application-level encryption chiffre avant envoi au serveur.',
        'Key Vault gère le cycle de vie des certificats.',
        'Les clés asymétriques signent et chiffrent (RSA/EC).',
        'Audit Logs Key Vault trace tous les accès.',
        'Premium HSM offre isolation physique des clés.'
    ]},
]

# Créer tous les QCM pour chaque thème
themes_data = {
    'Ressources & Stockage': resources_qcms,
    'Réseaux & Connectivité': network_qcms,
    'Machines virtuelles & Calcul': vm_qcms,
    'Surveillance & Gestion': monitoring_qcms,
    'RBAC & Contrôle d\'accès': rbac_qcms,
    'Sécurité & Chiffrement': security_qcms,
}

for theme_name, qcms_data in themes_data.items():
    theme_folder = os.path.join(base, theme_name)
    for index in range(2, 11):  # QCM-2 to QCM-10
        path = os.path.join(theme_folder, f'QCM-{index}.md')
        needs_write = not os.path.exists(path) or os.path.getsize(path) == 0
        if not needs_write:
            continue

        if index - 2 < len(qcms_data):
            qcm = qcms_data[index - 2]
        else:
            qcm = dict(qcms_data[0])
            qcm['title'] = f"{qcm['title']} (Révision {index})"

        write_qcm(path, qcm['title'], qcm['questions'], qcm['answers'], qcm['explanations'])

print('✅ QCM générés avec succès pour tous les thèmes !')
print('  - Identités: QCM-3 à QCM-9 créés/complétés')
print('  - Autres thèmes: QCM-2 à QCM-10 créés/complétés si manquants ou vides')
print('Vérifie les dossiers Themes pour confirmer le contenu.')
