from backend.ledger.bulletin_board import get_ledger

def verify_receipt(receipt_id):

    ledger = get_ledger()

    for i, block in enumerate(ledger):

        if block["receipt_id"] == receipt_id:

            return {
                "status": "FOUND",
                "block_position": i,
                "message": "Your ballot is included in the ledger."
            }

    return {
        "status": "NOT_FOUND",
        "message": "Receipt not found. No ballot recorded."
    }