from pydantic import BaseModel

class BudgetRequest(BaseModel):
    salary: float
    rent: float
    emi: float
    bills: float
    savings_priority: str
