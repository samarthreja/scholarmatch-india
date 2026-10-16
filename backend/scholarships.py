
scholarships = [
    {
        "id": 1,
        "name": "Scholarship Demo A",
        "provider": "Government",
        "amount": 12000,
        "level": "Undergraduate",
        "min_percentage": 75,
        "income_limit": 300000
    },
    {
        "id": 2,
        "name": "Scholarship Demo B",
        "provider": "Private Company",
        "amount": 25000,
        "level": "Undergraduate",
        "min_percentage": 80,
        "income_limit": 500000
    },
    {
        "id": 3,
        "name": "Scholarship Demo C",
        "provider": "NGO",
        "amount": 10000,
        "level": "Undergraduate",
        "min_percentage": 60,
        "income_limit": 250000
    }
]


def find_eligible_scholarships(percentage, income, level):
    eligible = []

    for scholarship in scholarships:
        if (
            percentage >= scholarship["min_percentage"]
            and income <= scholarship["income_limit"]
            and level.lower() == scholarship["level"].lower()
        ):
            eligible.append(scholarship)

    return eligible
