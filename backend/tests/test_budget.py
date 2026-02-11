from services.budget_engine import generate_budget

def test_high_priority():
    result = generate_budget(50000, 10000, 5000, 3000, "high")
    assert result["savings"] == 12500

def test_low_salary_case():
    result = generate_budget(15000, 10000, 4000, 3000, "medium")
    assert result["food"] == 0  # disposable becomes zero
