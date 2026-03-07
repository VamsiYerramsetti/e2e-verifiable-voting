import hashlib

ledger = []

def sha256(data):
    return hashlib.sha256(str(data).encode()).hexdigest()

def add_vote(ciphertext):

    prev_hash = ledger[-1]['hash'] if ledger else "GENESIS"

    # generate receipt id
    receipt_id = sha256(ciphertext)

    block_hash = sha256(str(ciphertext) + prev_hash)

    block = {
        "ciphertext": ciphertext,
        "receipt_id": receipt_id,
        "prev_hash": prev_hash,
        "hash": block_hash
    }

    ledger.append(block)

    return receipt_id

def get_ledger():
    return ledger