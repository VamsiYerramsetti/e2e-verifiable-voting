from backend.ledger.bulletin_board import get_ledger
import random

def auto_attack():

    ledger = get_ledger()

    if len(ledger) == 0:
        return False

    index = random.randint(0, len(ledger)-1)

    # Modify ciphertext
    ledger[index]["ciphertext"] = (999999, 999999)

    print("\n⚠️ Attack executed on block:", index)

    return True