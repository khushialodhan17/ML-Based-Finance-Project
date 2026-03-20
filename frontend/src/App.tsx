import { useState } from "react";
import UploadTransactions from "./components/UploadTransactions";
import BudgetForm from "./components/BudgetForm";
import BudgetResult from "./components/BudgetResult";
import {
  generateBudget,
} from "./api/budgetApi";

import type {
  BudgetFormData,
  BudgetResultType,
} from "./api/budgetApi";



const App: React.FC = () => {
  const [budgetResult, setBudgetResult] = useState<BudgetResultType | null>(
    null
  );
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleGenerate = async (formData: BudgetFormData) => {
    try {
      setLoading(true);
      setError(null);
      const result = await generateBudget(formData);
      setBudgetResult(result);
    } catch (err) {
      console.error(err)
      setError("Backend not responding. Is server running?");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>AI-Based Monthly Budget Planner</h1>

      <BudgetForm onGenerate={handleGenerate} />

      {loading && <p>Generating budget...</p>}
      {error && <p className="error">{error}</p>}
      {budgetResult && <BudgetResult budget={budgetResult} />}

      <UploadTransactions />
    </div>
  );
};

export default App;