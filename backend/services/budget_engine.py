def generate_budget_logic(data):
    salary = data.salary
    rent = data.rent
    emi = data.emi
    bills = data.bills
    priority = data.savings_priority

    remaining = salary - (rent + emi + bills)

    if priority == "high":
        savings = remaining * 0.5
    elif priority == "medium":
        savings = remaining * 0.3
    else:
        savings = remaining * 0.2

    # expenses = remaining - savings

    emergency_fund = savings * 0.3

    final_savings = savings - emergency_fund

    # return {
    #     "savings": round(savings, 2),
    #     "expenses": round(expenses, 2),
    #     "rent": rent,
    #     "emi": emi,
    #     "bills": bills
    # }


    return {
    "needs": rent + emi + bills,
    "savings": final_savings,
    "surplus_money": remaining - savings,
    "emergency_fund": emergency_fund
}
