from backend.ledger.bulletin_board import get_ledger
from backend.crypto.decrypt_vote import decrypt_vote

def tally_votes(private_key):
    ledger = get_ledger()

    vote_counts = {0: 0, 1: 0, 2: 0}

    for block in ledger:
        ciphertext = block["ciphertext"]

        # decrypt each vote
        vote = decrypt_vote(private_key, ciphertext)

        vote_counts[vote] += 1

    return vote_counts