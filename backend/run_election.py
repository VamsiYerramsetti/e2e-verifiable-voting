from backend.crypto.keygen import generate_keys
from backend.crypto.encrypt_vote import encrypt_vote
from backend.data.generate_votes import generate_votes
from backend.ledger.bulletin_board import add_vote, get_ledger
from backend.ledger.ledger_verify import verify_ledger
from backend.tally.tally_votes import tally_votes
from backend.audit.audit_engine import run_audit
from backend.audit.audit_report import generate_report
from backend.audit.dispute_resolution import verify_receipt
from backend.generate_receipt_pdf import generate_receipt_pdf


# -----------------------------
# 1️⃣ Generate Keys
# -----------------------------
public_key, private_key = generate_keys()


# -----------------------------
# 2️⃣ Generate Synthetic Votes
# -----------------------------
votes = generate_votes(20)

print("Original Votes:", votes)


# -----------------------------
# 3️⃣ Candidate Mapping
# -----------------------------
candidate_map = {
    "A": 0,
    "B": 1,
    "C": 2
}


# -----------------------------
# 4️⃣ Encrypt and Store Votes
# -----------------------------
receipts = []

for vote in votes:

    numeric_vote = candidate_map[vote]

    cipher = encrypt_vote(public_key, numeric_vote)

    receipt = add_vote(cipher)

    receipts.append(receipt)

    print("Receipt issued:", receipt)


# -----------------------------
# 5️⃣ Ledger Size
# -----------------------------
ledger = get_ledger()

print("\nTotal Encrypted Ballots Stored:", len(ledger))


# -----------------------------
# 6️⃣ Verify Ledger Integrity
# -----------------------------
is_valid = verify_ledger()

print("\nLedger Integrity Verified:", is_valid)


# -----------------------------
# 7️⃣ Tally Votes
# -----------------------------
results = tally_votes(private_key)

print("\nElection Results:")

print("Candidate A:", results[0])
print("Candidate B:", results[1])
print("Candidate C:", results[2])


# -----------------------------
# 8️⃣ Run Audit Engine
# -----------------------------
audit_results = run_audit(ledger, results)

print("\n====== POST-ELECTION AUDIT REPORT ======")

report = generate_report(audit_results)

print(report)


# -----------------------------
# 9️⃣ Show Receipts in Ledger (for testing)
# -----------------------------
print("\nReceipts stored in ledger:")

for block in ledger:
    print(block["receipt_id"])


# -----------------------------
# 🔟 Receipt Verification
# -----------------------------
print("\n====== RECEIPT VERIFICATION ======")

receipt_to_check = input("Enter your receipt ID: ").strip()

result = verify_receipt(receipt_to_check)

print("\nDispute Resolution Result:")
print(result)


# -----------------------------
# 1️⃣1️⃣ Generate PDF Receipt
# -----------------------------
if result["status"] == "FOUND":

    print("\nBallot confirmed in ledger!")

    voter_name = input("Enter your name: ")

    voter_id = input("Enter your voter ID: ")

    generate_receipt_pdf(receipt_to_check, voter_name, voter_id)

else:

    print("\nReceipt not found. PDF not generated.")