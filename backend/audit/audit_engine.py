from backend.ledger.ledger_verify import verify_ledger


def run_audit(ledger, results):

    audit_data = {}

    # verify ledger integrity
    audit_data["ledger_ok"] = verify_ledger()

    # count ballots
    audit_data["ballot_count"] = len(ledger)

    # store tally results
    audit_data["tally"] = results

    return audit_data