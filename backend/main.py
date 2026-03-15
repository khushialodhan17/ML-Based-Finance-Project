from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from schemas.budget_schema import BudgetRequest
from services.budget_engine import generate_budget_logic

app = FastAPI()

# Allow frontend (React) to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend is working perfectly 🚀"}

@app.post("/generate-budget")
def generate_budget(data: BudgetRequest):
    result = generate_budget_logic(data)
    return result
