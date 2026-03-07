from backend.ledger.bulletin_board import get_ledger

def simulate_ballot_deletion():
    ledger = get_ledger()

    if len(ledger) > 0:
        deleted_block = ledger.pop()
        print("\n⚠️ Attack Simulation: Ballot deleted from ledger!")
        return deleted_block

def simulate_ballot_modification():
    ledger = get_ledger()

    if len(ledger) > 0:
        ledger[0]["ciphertext"] = (999999, 999999)
        print("\n⚠️ Attack Simulation: Ballot ciphertext modified!")