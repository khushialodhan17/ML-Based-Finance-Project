from fastapi import APIRouter, UploadFile, File
from services.transaction_pipeline import process_transactions

router = APIRouter()

@router.post("/upload-transactions")
async def upload_transactions(file: UploadFile = File(...)):
    try:
        transactions = process_transactions(file.file)

        return {
            "count": len(transactions),
            "transactions": transactions
        }

    except Exception as e:
        return {"error": str(e)}