def get_job_role_keywords(role):
    roles = {
        "Data Scientist": [
            "python", "machine learning", "pandas",
            "numpy", "tensorflow", "sql", "statistics"
        ],
        "Cybersecurity": [
            "network security", "penetration testing",
            "firewalls", "siem", "risk assessment"
        ],
        "Cloud DevOps": [
            "aws", "azure", "docker",
            "kubernetes", "ci/cd", "terraform"
        ],
        "Product Manager": [
            "roadmap", "agile", "stakeholders",
            "scrum", "product strategy"
        ],
        "Marketing": [
            "seo", "digital marketing",
            "branding", "campaign", "analytics"
        ],
        "Finance": [
            "financial analysis", "excel",
            "budgeting", "forecasting", "accounting"
        ],
        "Healthcare": [
            "patient care", "medical",
            "clinical", "ehr", "healthcare management"
        ],
        "HR": [
            "recruitment", "employee relations",
            "payroll", "hr policies", "talent acquisition"
        ],
        "Legal": [
            "contracts", "compliance",
            "litigation", "legal research", "corporate law"
        ],
        "Operations": [
            "logistics", "supply chain",
            "process improvement", "inventory"
        ],
        "Design": [
            "ui/ux", "figma",
            "adobe", "wireframing", "prototyping"
        ]
    }

    return roles.get(role, [])
