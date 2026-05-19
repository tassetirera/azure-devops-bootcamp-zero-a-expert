# QCM + corrections détaillées pour l'AZ-104 - Surveillance et gestion

***

## QCM (10 questions) - Domaine : Surveillance, gestion et automatisation

1. **Quel est le rôle principal d'Azure Monitor ?**  
   a) Stocker les données permanentes uniquement  
   b) Collecter, analyser et agir sur les métriques et logs des ressources Azure  
   c) Authentifier uniquement les utilisateurs  
   d) Gérer uniquement le réseau  

2. **Quel composant Azure Monitor vous permet de visualiser et analyser les métriques en temps réel ?**  
   a) Log Analytics Workspace  
   b) Azure Dashboards ou Workbooks  
   c) Application Insights  
   d) Azure Alert Rules  

3. **Vous avez besoin de stocker et analyser des logs structurés (JSON) de plusieurs ressources. Quel service utiliser ?**  
   a) Application Insights uniquement  
   b) Log Analytics Workspace avec KQL (Kusto Query Language)  
   c) Storage Accounts uniquement  
   d) Azure SQL Database  

4. **Qu'est-ce qu'une Azure Alert Rule (alerte) ?**  
   a) Une ressource qui stocke des données  
   b) Une condition qui déclenche une action (notification, webhook, automation) si une métrique/log la valide  
   c) Une règle de réseau uniquement  
   d) Un type de VM  

5. **Quel service Azure vous permet de monitorer les performances applicatives en temps réel (requêtes, exceptions, dépendances) ?**  
   a) Azure Monitor uniquement  
   b) Application Insights  
   c) Azure Backup  
   d) Log Analytics Workspace uniquement  

6. **Comment gérer et automatiser les tâches répétitives (redémarrer VM, nettoyer les disques…) ?**  
   a) Les faire manuellement chaque jour  
   b) Utiliser Azure Automation ou Azure Logic Apps  
   c) C'est impossible  
   d) Télécharger un outil externe  

7. **Quel est l'avantage d'Azure Automation par rapport aux scripts PowerShell/Bash locaux ?**  
   a) Aucun avantage  
   b) Planifier, exécuter cloud-side, gérer les runbooks, pas de serveur local nécessaire  
   c) Azure Automation est plus lent  
   d) Les scripts locaux sont toujours meilleurs  

8. **Vous devez auditer toutes les modifications (création, modification, suppression) de ressources Azure. Quel service utiliser ?**  
   a) Azure Monitor uniquement  
   b) Azure Activity Log (suivi des opérations de gestion) + Azure Audit Logs  
   c) Application Insights  
   d) Log Analytics seul  

9. **Quel service Azure vous permet de mettre en place une solution de compliance automatisée (vérifier les tags, configuration…) et corriger les déviations ?**  
   a) Azure Policies  
   b) Azure Compliance Manager  
   c) Network Security Group  
   d) Azure Monitor uniquement  

10. **Vous avez plusieurs souscriptions Azure. Comment centraliser la surveillance et les alertes ?**  
    a) Créer un compte de stockage par souscription  
    b) Utiliser Azure Lighthouse ou un Log Analytics Workspace partagé  
    c) C'est impossible  
    d) Gérer manuellement chaque souscription  

***

## Corrections détaillées

1. **b) Collecter, analyser et agir sur les métriques et logs des ressources Azure**  
   - **Azure Monitor** est la solution centralisée de surveillance Azure : collecte métriques, logs, traces, déclenche alertes et automatisations. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)

2. **b) Azure Dashboards ou Workbooks**  
   - **Azure Dashboards** personnalisés et **Workbooks** permettent de visualiser métriques en temps réel, analyser les données, créer des rapports interactifs. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)

3. **b) Log Analytics Workspace avec KQL (Kusto Query Language)**  
   - **Log Analytics Workspace** est le dépôt centralisé pour logs structurés. **KQL** est le langage de requête puissant pour analyser (filtrer, agréger, corréler). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)

4. **b) Une condition qui déclenche une action (notification, webhook, automation) si une métrique/log la valide**  
   - Une **Alert Rule** définit : seuil à surveiller + action à exécuter (email, SMS, webhook, runbook automation) quand le seuil est franchi. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)

5. **b) Application Insights**  
   - **Application Insights** est l'outil de monitoring applicatif Azure : suivi des requêtes HTTP, exceptions, dépendances (bases de données, services externes), traces personnalisées. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)

6. **b) Utiliser Azure Automation ou Azure Logic Apps**  
   - **Azure Automation** exécute des runbooks (PowerShell/Python) selon un horaire. **Logic Apps** crée des workflows visuels pour orchestrer des tâches multi-services. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)

7. **b) Planifier, exécuter cloud-side, gérer les runbooks, pas de serveur local nécessaire**  
   - **Azure Automation** : pas d'infra locale, exécution dans le cloud, gestion centralisée, intégration native avec les services Azure, pas besoin de maintenir un serveur. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)

8. **b) Azure Activity Log (suivi des opérations de gestion) + Azure Audit Logs**  
   - L'**Activity Log** trace toutes les opérations (création, modification…) sur les ressources Azure. **Audit Logs** (dans Log Analytics) permettent l'analyse historique et compliance. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)

9. **a) Azure Policies**  
   - **Azure Policies** impose des règles (tags obligatoires, SKUs approuvés…) et peut corriger automatiquement les déviations (remediation). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)

10. **b) Utiliser Azure Lighthouse ou un Log Analytics Workspace partagé**  
    - **Azure Lighthouse** permet une gestion multi-souscription centralisée. Un **Log Analytics Workspace** partagé centralise les logs de toutes les souscriptions. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)

***

## Fiches de révision synthétiques

### 1. Azure Monitor – Architecture
- **Data sources** : métriques (ressources), logs (événements), traces (application), données custom. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)
- **Collectors** : Azure Monitor Agent, Application Insights SDK, Telegraf, Prometheus. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)
- **Processing** : normalisation, enrichissement, agrégation. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)
- **Storage** : Azure Monitor Metrics (série temporelle), Log Analytics Workspace (logs). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)
- **Consumption** : dashboards, workbooks, alertes, requêtes KQL. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)

### 2. Métriques
- **Azure Monitor Metrics** : données numériques agrégées (CPU %, mémoire, latence…). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)
- **Résolution** : 1 minute par défaut (toutes les ressources Azure). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)
- **Rétention** : 93 jours pour les métriques standard. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)

### 3. Logs
- **Log Analytics Workspace** : dépôt centralisé pour logs structurés. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)
- **KQL (Kusto Query Language)** : langage puissant pour requêter les logs (SELECT, WHERE, JOIN, aggregation…). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)
- **Rétention** : 30-2555 jours (configurable). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)

### 4. Application Insights
- **APM (Application Performance Monitoring)** : surveiller les performances applicatives en temps réel. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)
- **Dépendances trackées** : requêtes HTTP, appels base de données, services externes. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)
- **Exceptions & Traces** : capture automatique des erreurs et logs application. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)
- **Disponibilité (Web Tests)** : tester la disponibilité applicative depuis plusieurs emplacements géographiques. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)

### 5. Alertes et Actions
- **Alert Rules** : condition + seuil + action (notification, webhook, runbook). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)
- **Action Groups** : centralisateur d'actions (email, SMS, PagerDuty, webhook…). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)
- **Smart Alerts** : suppression du bruit (anomaly detection). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)

### 6. Automation
- **Azure Automation** : runbooks PowerShell/Python, exécution planifiée ou event-driven. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)
- **Logic Apps** : workflows visuels multi-services, intégrations SaaS. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)
- **Webhooks** : déclencher des actions externes via HTTP POST. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)

### 7. Audit & Compliance
- **Activity Log** : audit des opérations de gestion (Resource Manager). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)
- **Azure Policies** : enforce compliance (remediation automatique possible). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)
- **Azure Blueprints** : packager et déployer des configurations complètes (templates + policies). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)

### 8. Gestion multi-souscription
- **Azure Lighthouse** : délégation multi-tenant pour gestion centralisée. [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)
- **Management Groups** : organiser hiérarchiquement les souscriptions (RBAC, policies appliquées en cascade). [learn.microsoft](https://learn.microsoft.com/en-us/training/modules/analyze-resiliency-strategy/)
