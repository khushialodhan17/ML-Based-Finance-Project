import type { BudgetResultType } from "../api/budgetApi";

interface Props {
  budget: BudgetResultType;
}

const BudgetResult: React.FC<Props> = ({ budget }) => {
  return (
    <div className="result">
      <h2>Your Monthly Budget</h2>
      <table>
        <thead>
          <tr>
            <th>Category</th>
            <th>Amount (₹)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Needs</td>
            <td>₹ {budget.needs}</td>
          </tr>
          <tr>
            <td>Wants</td>
            <td>₹ {budget.surplus_money}</td>
          </tr>
          <tr>
            <td>Savings</td>
            <td>₹ {budget.savings}</td>
          </tr>
          <tr>
            <td>Emergency Fund</td>
            <td>₹ {budget.emergency_fund}</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
};

export default BudgetResult;