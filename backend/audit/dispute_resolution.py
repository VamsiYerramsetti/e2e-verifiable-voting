from backend.ledger.bulletin_board import get_ledger


def verify_receipt(receipt_id):

    # remove accidental spaces or new lines
    receipt_id = receipt_id.strip()

    ledger = get_ledger()

    # search the ledger for the receipt
    for index, block in enumerate(ledger):

        stored_receipt = block.get("receipt_id", "").strip()

        if stored_receipt == receipt_id:

            return {
                "status": "FOUND",
                "block_position": index,
                "message": "Your ballot is included in the ledger."
            }

    return {
        "status": "NOT_FOUND",
        "message": "Receipt not found. No ballot recorded."
    }