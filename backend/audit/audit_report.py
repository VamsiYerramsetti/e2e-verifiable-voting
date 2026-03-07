def generate_report(results):

    print("\n====== POST-ELECTION AUDIT REPORT ======\n")

    if results["ledger_ok"]:
        print("Ledger Integrity: OK")
    else:
        print(" Ledger Integrity: Tampering Detected")

    print("Total Ballots Verified:", results["ballot_count"])

    tally = results["tally"]

    print("\nRecomputed Tally:")
    print("Candidate A:", tally[0])
    print("Candidate B:", tally[1])
    print("Candidate C:", tally[2])

    if results["ledger_ok"]:
        print("\nAudit Result: Election integrity verified.")
    else:
        print("\nAudit Result: Integrity failure detected.")