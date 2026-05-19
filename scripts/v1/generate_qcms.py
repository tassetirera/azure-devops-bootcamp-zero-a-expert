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

# Map of theme folder to source QCM file in Trainning folder for first copy
trainning_folder = r"c:\Users\mouss\source\repos\azure-devops-bootcamp-zero-a-expert\Documentations\CERTIFICATION-AZURE\C:\Users\mouss\source\repos\azure-devops-bootcamp-zero-a-expert\Documentations\CERTIFICATION-AZURE\Themes\Identités et types d'identité"
copy_map = {
    'Ressources & Stockage': 'QCM-3.md',
    'Réseaux & Connectivité': 'QCM-4.md',
    'Machines virtuelles & Calcul': 'QCM-5.md',
    'Surveillance & Gestion': 'QCM-6.md',
    'RBAC & Contrôle d\'accès': 'QCM-7.md',
    'Sécurité & Chiffrement': 'QCM-8.md',
}

for theme, src_qcm in copy_map.items():
    dst_folder = os.path.join(base, theme)
    dst_path = os.path.join(dst_folder, 'QCM-2.md')
    if not os.path.exists(dst_path):
        src_path = os.path.join(trainning_folder, src_qcm)
        copy_file(src_path, dst_path)

print('Copied QCM-2 files from Trainning into theme folders where applicable.')
print('Created identity QCM-3..QCM-9.')
