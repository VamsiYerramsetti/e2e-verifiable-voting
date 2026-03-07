from backend.ledger.bulletin_board import get_ledger
from backend.ledger.ledger_verify import verify_ledger
from backend.tally.tally_votes import tally_votes

def run_audit(private_key):

    results = {}

    # Check ledger integrity
    results["ledger_ok"] = verify_ledger()

    # Count ballots
    ledger = get_ledger()
    results["ballot_count"] = len(ledger)

    # Recompute tally
    results["tally"] = tally_votes(private_key)

    return results