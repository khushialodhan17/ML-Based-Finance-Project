from fastapi import FastAPI
from schemas.budget_schema import BudgetRequest, BudgetResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Backend running successfully"}

@app.post("/generate-budget", response_model=BudgetResponse)
def generate_budget(data: BudgetRequest):
    income = data.salary - (data.rent + data.emi + data.bills)

    if data.savings_priority == "high":
        savings = income * 0.4
    elif data.savings_priority == "medium":
        savings = income * 0.3
    else:
        savings = income * 0.2

    remaining = income - savings

    return {
        "food": round(remaining * 0.35),
        "shopping": round(remaining * 0.25),
        "entertainment": round(remaining * 0.15),
        "transport": round(remaining * 0.15),
        "misc": round(remaining * 0.10),
    }
