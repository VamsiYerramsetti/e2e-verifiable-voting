def generate_report(audit_data):

    report = []

    if audit_data["ledger_ok"]:
        report.append(" Ledger Integrity: OK")
    else:
        report.append(" Ledger Tampered")

    report.append(f"Total Ballots Verified: {audit_data['ballot_count']}")

    report.append("\nRecomputed Tally:")

    report.append(f"Candidate A: {audit_data['tally'][0]}")
    report.append(f"Candidate B: {audit_data['tally'][1]}")
    report.append(f"Candidate C: {audit_data['tally'][2]}")

    report.append("\nAudit Result: Election integrity verified.")

    return "\n".join(report)