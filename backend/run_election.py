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
from backend.audit.attack_simulation import auto_attack   # ✅ FIXED IMPORT

SHOW_CIPHERTEXT = False
SYSTEM_STATUS = "SAFE"

# -----------------------------
# 1️⃣ Generate Keys
# -----------------------------
public_key, private_key = generate_keys()


# -----------------------------
# 2️⃣ Generate Votes
# -----------------------------
votes = generate_votes(20)
print("\nOriginal Votes:", votes)


# -----------------------------
# 3️⃣ Candidate Mapping
# -----------------------------
candidate_map = {"A": 0, "B": 1, "C": 2}


# -----------------------------
# 4️⃣ Encrypt + Store Votes
# -----------------------------
receipts = []

for vote in votes:
    numeric_vote = candidate_map[vote]

    cipher = encrypt_vote(public_key, numeric_vote)

    if SHOW_CIPHERTEXT:
        print(f"Vote: {vote} → Cipher: {cipher}")

    receipt = add_vote(cipher)
    receipts.append(receipt)

    print("Receipt issued:", receipt)


# -----------------------------
# 5️⃣ Ledger Info
# -----------------------------
ledger = get_ledger()
print("\nTotal Encrypted Ballots Stored:", len(ledger))


# -----------------------------
# 6️⃣ Verify Ledger
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
# 8️⃣ Audit Engine
# -----------------------------
audit_results = run_audit(ledger, results)

print("\n====== POST-ELECTION AUDIT REPORT ======")
print(generate_report(audit_results))


# -----------------------------
# 9️⃣ Show Receipts
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
# 1️⃣1️⃣ ATTACK (CALL ONLY WHEN NEEDED)
# -----------------------------
# COMMENT THIS LINE IF YOU DON'T WANT ATTACK
attack_done = auto_attack()

if attack_done:

    SYSTEM_STATUS = "COMPROMISED"

    print("\n====== SECURITY ALERT ======")

    print("⚠️ Suspicious activity detected!")

    print("\nRunning Ledger Verification After Attack...")

    is_valid = verify_ledger()

    print("Ledger Integrity After Attack:", is_valid)

    if not is_valid:
        print("\n🚨 ALERT: Unauthorized modification detected!")



# -----------------------------
# 1️⃣2️⃣ Generate PDF Receipt
# -----------------------------
if result["status"] == "FOUND":

    print("\nBallot confirmed in ledger!")

    voter_name = input("Enter your name: ")
    voter_id = input("Enter your voter ID: ")

    generate_receipt_pdf(receipt_to_check, voter_name, voter_id, SYSTEM_STATUS)

else:
    print("\nReceipt not found. PDF not generated.")