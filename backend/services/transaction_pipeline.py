import pandas as pd

def process_transactions(file):

    # Step 1: Read CSV
    df = pd.read_csv(file)

    # Step 2: Clean column names
    df.columns = df.columns.str.strip().str.lower()

    # Step 3: Validate columns
    required_cols = ["date", "description", "amount"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")

    # Step 4: Clean description
    df["description"] = df["description"].astype(str).str.strip().str.lower()

    # Step 5: Clean amount
    df["amount"] = (
        df["amount"]
        .astype(str)
        .str.replace("₹", "", regex=False)
        .str.replace(",", "", regex=False)
    )

    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    # Step 6: Remove invalid rows
    df = df.dropna(subset=["amount"])

    # Step 7: Add transaction type
    df["type"] = df["amount"].apply(lambda x: "credit" if x > 0 else "debit")

    # Step 8: Convert to JSON
    transactions = df.to_dict(orient="records")

    return transactions