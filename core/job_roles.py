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
            ],
            "Investment Banker": [
                "valuation", "m&a", "equity",
                "financial modeling"
            ]
        },

        "Human Resources": {
            "HR Manager": [
                "recruitment", "employee relations",
                "payroll", "hr policies"
            ],
            "Talent Acquisition Specialist": [
                "sourcing", "screening",
                "interviewing", "hiring"
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
            ],
            "Brand Manager": [
                "branding", "market research",
                "strategy", "advertising"
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
            ],
            "Hospital Administrator": [
                "healthcare management",
                "operations", "compliance"
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
            ],
            "Graphic Designer": [
                "photoshop", "illustrator",
                "branding", "layout design"
            ]
        },

        "Legal": {
            "Corporate Lawyer": [
                "contracts", "compliance",
                "litigation", "legal research"
            ],
            "Legal Advisor": [
                "regulatory law", "documentation",
                "negotiation"
            ]
        }
    }
