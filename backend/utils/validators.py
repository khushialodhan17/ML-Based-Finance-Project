def validate_priority(priority):
    allowed = ["low", "medium", "high"]
    if priority not in allowed:
        raise ValueError("Savings priority must be low, medium, or high")
