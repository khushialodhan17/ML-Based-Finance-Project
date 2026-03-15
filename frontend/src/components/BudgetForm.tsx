import { useState } from "react";
import type { BudgetFormData } from "../api/budgetApi";

interface Props {
  onGenerate: (data: BudgetFormData) => void;
}

const BudgetForm: React.FC<Props> = ({ onGenerate }) => {
  const [form, setForm] = useState<BudgetFormData>({
    salary: 0,
    rent: 0,
    emi: 0,
    bills: 0,
    savings_priority: "medium",
  });

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>
  ) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    onGenerate({
      salary: Number(form.salary),
      rent: Number(form.rent),
      emi: Number(form.emi),
      bills: Number(form.bills),
      savings_priority: form.savings_priority,
    });
  };

  return (
    <form className="form" onSubmit={handleSubmit}>
      <label>Monthly Salary</label>
      <input name="salary" type="number" onChange={handleChange} required />

      <label>Rent</label>
      <input name="rent" type="number" onChange={handleChange} required />

      <label>EMI</label>
      <input name="emi" type="number" onChange={handleChange} required />

      <label>Bills</label>
      <input name="bills" type="number" onChange={handleChange} required />

      <label>Savings Priority</label>
      <select name="savings_priority" onChange={handleChange}>
        <option value="low">Low</option>
        <option value="medium">Medium</option>
        <option value="high">High</option>
      </select>

      <button type="submit">Generate Budget</button>
    </form>
  );
};

export default BudgetForm;