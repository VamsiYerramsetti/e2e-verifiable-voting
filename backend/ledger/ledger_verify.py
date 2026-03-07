import hashlib
from backend.ledger.bulletin_board import get_ledger

def sha256(data):
    return hashlib.sha256(str(data).encode()).hexdigest()

def verify_ledger():
    ledger = get_ledger()

    for i in range(len(ledger)):
        block = ledger[i]

        # Check previous hash
        if i == 0:
            expected_prev = "GENESIS"
        else:
            expected_prev = ledger[i-1]['hash']

        if block['prev_hash'] != expected_prev:
            return False

        # Recalculate hash
        recalculated_hash = sha256(str(block['ciphertext']) + block['prev_hash'])

        if block['hash'] != recalculated_hash:
            return False

    return True