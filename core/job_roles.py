# core/job_roles.py

def get_job_data():
    return {
        "Information Technology": {
            "Software Developer": [
                "python", "java", "c++", "git", "api", "database"
            ],
            "Data Scientist": [
                "python", "machine learning", "pandas",
                "numpy", "tensorflow", "statistics"
            ],
            "DevOps Engineer": [
                "aws", "docker", "kubernetes",
                "ci/cd", "terraform"
            ],
            "Cybersecurity Analyst": [
                "network security", "penetration testing",
                "siem", "firewalls", "risk assessment"
            ]
        },

        "Finance & Accounting": {
            "Financial Analyst": [
                "financial modeling", "excel",
                "forecasting", "budgeting"
            ],
            "Accountant": [
                "accounting", "tax", "ledger",
                "tally", "compliance"
            ]
        },

        "Human Resources": {
            "HR Manager": [
                "recruitment", "employee relations",
                "payroll", "hr policies"
            ]
        },

        "Marketing & Sales": {
            "Digital Marketing Manager": [
                "seo", "google ads", "analytics",
                "campaign management"
            ],
            "Sales Executive": [
                "lead generation", "crm",
                "negotiation", "client relationship"
            ]
        },

        "Healthcare": {
            "Doctor": [
                "diagnosis", "patient care",
                "treatment", "clinical knowledge"
            ],
            "Nurse": [
                "patient care", "medication",
                "clinical procedures"
            ]
        },

        "Operations & Supply Chain": {
            "Operations Manager": [
                "process improvement", "logistics",
                "inventory management"
            ],
            "Supply Chain Analyst": [
                "procurement", "inventory",
                "forecasting"
            ]
        },

        "Design & Creative": {
            "UI/UX Designer": [
                "figma", "wireframing",
                "prototyping", "user research"
            ]
        },

        "Legal": {
            "Corporate Lawyer": [
                "contracts", "compliance",
                "litigation", "legal research"
            ]
        },

        # ---------------------------
        # NEW DEPARTMENT ADDED
        # ---------------------------

        "Facility Management": {

            "Technical Manager": [
                "facility operations",
                "preventive maintenance",
                "electrical systems",
                "hvac systems",
                "budget management",
                "vendor management",
                "team leadership",
                "safety compliance",
                "building management systems",
                "project management"
            ],

            "Shift Engineer": [
                "electrical maintenance",
                "mechanical systems",
                "hvac troubleshooting",
                "diesel generator",
                "plumbing systems",
                "fire fighting systems",
                "preventive maintenance",
                "breakdown maintenance",
                "technical reporting",
                "safety procedures"
            ]
        }
    }
