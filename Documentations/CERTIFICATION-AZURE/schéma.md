# Schéma hiérarchique Microsoft Entra ID

```
Organisation
│
├── Locataire Microsoft Entra (annuaire) ou Tenant
│   ├── Utilisateurs, groupes, appareils
│   ├── Applications (registrées dans Entra)
│   └── Accès (RBAC global, politiques, etc.)
│
└── Abonnement Azure (ou plusieurs)
    │
    ├── Abonnement Azure 1 (ex. Production)
    │   ├── Rôle / RBAC par locataire
    │   ├── Facturation / Quotas
    │   │
    │   └── Groupes de ressources
    │       ├── Ressource Group 1 – rg-prod-web
    │       │   ├── App Service (site web prod)
    │       │   ├── Application Gateway
    │       │   └── Azure Monitor
    │       │
    │       ├── Ressource Group 2 – rg-prod-db
    │       │   ├── Azure SQL Managed Instance
    │       │   ├── Azure Cache for Redis
    │       │   └── Log Analytics Workspace
    │       │
    │       └── Ressource Group 3 – rg-prod-network
    │           ├── VNet, subnets
    │           ├── Azure Firewall
    │           └── Private DNS zones
    │
    ├── Abonnement Azure 2 (ex. Non‑prod)
    │   ├── Rôle / RBAC par locataire
    │   ├── Facturation / Quotas
    │   │
    │   └── Groupes de ressources
    │       ├── Ressource Group 1 – rg-dev-web
    │       ├── Ressource Group 2 – rg-dev-db
    │       └── Ressource Group 3 – rg-dev-network
    │
    └── Abonnement Azure 3 (ex. Data / Analytique)
        ├── Rôle / RBAC par locataire
        ├── Facturation / Quotas
        │
        └── Groupes de ressources
            ├── Ressource Group 1 – rg-data-dwh
            ├── Ressource Group 2 – rg-data-powerbi
            └── Ressource Group 3 – rg-data-logs
```

### Explication

- **Un locataire Entra** gère **toute l’identité** (utilisateurs, groupes, apps) et peut être associé à **plusieurs abonnements Azure**. [learn.microsoft](https://learn.microsoft.com/fr-fr/entra/fundamentals/how-subscriptions-associated-directory)
- **Chaque abonnement** correspond à un **cadre de facturation / quota**. [learn.microsoft](https://learn.microsoft.com/fr-fr/azure/cost-management-billing/manage/cloud-subscription)
- **Les groupes de ressources** servent à **regrouper les ressources par environnement / fonction** (web, db, réseau, etc.), tout en restant dans un seul abonnement. [openhost-network](https://www.openhost-network.com/blog/azure-hierarchie-ressources/)
