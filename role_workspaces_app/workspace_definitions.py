WORKSPACE_DEFINITIONS = [

    {
        "label": "Sales Command Center",
        "module": "Selling",
        "icon": "cart",
        "color": "blue",
        "role": "Sales Manager",
        "sequence": 10,
        "sections": [
            {
                "title": "Sales Operations",
                "shortcuts": [
                    "Quotation",
                    "Sales Order",
                    "Delivery Note",
                    "Sales Invoice"
                ]
            },
            {
                "title": "Customer Data",
                "shortcuts": [
                    "Customer",
                    "Contact"
                ]
            }
        ]
    },

    {
        "label": "Inventory Control Center",
        "module": "Stock",
        "icon": "box",
        "color": "green",
        "role": "Stock Manager",
        "sequence": 20,
        "sections": [
            {
                "title": "Inventory Movements",
                "shortcuts": [
                    "Stock Entry",
                    "Material Request",
                    "Delivery Note"
                ]
            },
            {
                "title": "Inventory Setup",
                "shortcuts": [
                    "Item",
                    "Warehouse",
                    "Item Group"
                ]
            }
        ]
    },

    {
        "label": "Finance Operations",
        "module": "Accounts",
        "icon": "money",
        "color": "orange",
        "role": "Accounts Manager",
        "sequence": 30,
        "sections": [
            {
                "title": "Financial Transactions",
                "shortcuts": [
                    "Journal Entry",
                    "Payment Entry",
                    "Purchase Invoice",
                    "Sales Invoice"
                ]
            },
            {
                "title": "Financial Structure",
                "shortcuts": [
                    "Account",
                    "Cost Center"
                ]
            }
        ]
    }

]