export interface BudgetFormData {
  salary: number;
  rent: number;
  emi: number;
  bills: number;
  savings_priority: "low" | "medium" | "high";
}

export interface BudgetResultType {
  needs: number;
  surplus_money: number;
  savings: number;
  emergency_fund: number;
}

export async function generateBudget(
  data: BudgetFormData
): Promise<BudgetResultType> {
  const response = await fetch("http://127.0.0.1:8000/generate-budget", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    throw new Error("Failed to generate budget");
  }

  const result = await response.json();
  return result;
}