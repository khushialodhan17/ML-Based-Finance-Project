#  code when only csv was working


# import pandas as pd

# def process_transactions(file):

#     # Step 1: Read CSV
#     df = pd.read_csv(file)

#     # Step 2: Clean column names
#     df.columns = df.columns.str.strip().str.lower()

#     # Step 3: Validate columns
#     required_cols = ["date", "description", "amount"]
#     for col in required_cols:
#         if col not in df.columns:
#             raise ValueError(f"Missing column: {col}")

#     # Step 4: Clean description
#     df["description"] = df["description"].astype(str).str.strip().str.lower()

#     # Step 5: Clean amount
#     df["amount"] = (
#         df["amount"]
#         .astype(str)
#         .str.replace("₹", "", regex=False)
#         .str.replace(",", "", regex=False)
#     )

#     df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

#     # Step 6: Remove invalid rows
#     df = df.dropna(subset=["amount"])

#     # Step 7: Add transaction type
#     df["type"] = df["amount"].apply(lambda x: "credit" if x > 0 else "debit")

#     # Step 8: Convert to JSON
#     transactions = df.to_dict(orient="records")

#     return transactions

# code when both csv and pdf are working

import pandas as pd
import pdfplumber
import io


def process_transactions(file, filename: str):

    #  CASE 1: CSV FILE
    if filename.endswith(".csv"):
        df = pd.read_csv(file)

    #  CASE 2: PDF FILE
    elif filename.endswith(".pdf"):
        text_data = ""

        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text_data += page.extract_text() + "\n"

        #  Convert text → lines
        lines = text_data.split("\n")

        data = []

        for line in lines:
            # VERY basic parsing (you can improve later)
            parts = line.split()

            if len(parts) >= 3:
                try:
                    date = parts[0]
                    amount = parts[-1].replace(",", "").replace("₹", "")
                    description = " ".join(parts[1:-1])

                    data.append({
                        "date": date,
                        "description": description.lower(),
                        "amount": float(amount)
                    })
                except:
                    continue

        df = pd.DataFrame(data)

    else:
        raise ValueError("Only CSV and PDF files are supported")

    # ---------------- CLEANING (COMMON) ----------------

    df.columns = df.columns.str.strip().str.lower()

    required_cols = ["date", "description", "amount"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")

    df["description"] = df["description"].astype(str).str.strip().str.lower()

    df["amount"] = (
        df["amount"]
        .astype(str)
        .str.replace("₹", "", regex=False)
        .str.replace(",", "", regex=False)
    )

    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    df = df.dropna(subset=["amount"])

    df["type"] = df["amount"].apply(lambda x: "credit" if x > 0 else "debit")

    transactions = df.to_dict(orient="records")

    return transactions