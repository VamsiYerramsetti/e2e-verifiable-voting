from backend.crypto.keygen import generate_keys
from backend.crypto.encrypt_vote import encrypt_vote
from backend.ledger.bulletin_board import add_vote, get_ledger
from backend.data.generate_votes import generate_votes
from backend.ledger.ledger_verify import verify_ledger
from backend.tally.tally_votes import tally_votes
from backend.audit.audit_engine import run_audit
from backend.audit.audit_report import generate_report
from backend.audit.dispute_resolution import verify_receipt
from backend.audit.attack_simulation import simulate_ballot_deletion, simulate_ballot_modification
SHOW_CIPHERTEXT = False   # change to True if you want to see ciphertext



# 1️⃣ Generate Keys
public_key, private_key = generate_keys()

# 2️⃣ Generate Synthetic Votes
votes = generate_votes(20)  # start small for testing

print("Original Votes:", votes)

# 3️⃣ Convert Candidate Names to Numeric Values
candidate_map = {"A": 0, "B": 1, "C": 2}

# 4️⃣ Encrypt and Store Votes (THIS IS THE VOTE LOOP)
receipts = []

for vote in votes:
    numeric_vote = candidate_map[vote]

    cipher = encrypt_vote(public_key, numeric_vote)

    receipt = add_vote(cipher)
    receipts.append(receipt)

    if SHOW_CIPHERTEXT:
        print(f"Encrypted Vote (Ciphertext): {cipher}")

    print("Receipt issued:", receipt)

#print("Receipt issued:", receipt)




#-----------------------------------------------------------------------------#
# ---- SIMULATE ATTACK ----
#print("\nSimulating tampering attack...")

#ledger = get_ledger()

##if len(ledger) > 0:
  #  ledger[0]["ciphertext"] = (999999, 999999)   # hacker edits vote

#----------------------------------------------------------------------------------#





# 5️⃣ Print Ledger Size
ledger = get_ledger()
print("\nTotal Encrypted Ballots Stored:", len(ledger))

# 6️⃣ Verify Ledger Integrity
is_valid = verify_ledger()
print("\nLedger Integrity Verified:", is_valid)

# 7️⃣ Tally Votes
results = tally_votes(private_key)

print("\nElection Results:")
print("Candidate A:", results[0])
print("Candidate B:", results[1])
print("Candidate C:", results[2])

# Run audit
audit_results = run_audit(private_key)

# Print audit report
generate_report(audit_results)

# Example dispute check
ledger = get_ledger()
sample_receipt = ledger[0]["receipt_id"]

print("\nChecking Receipt:", sample_receipt)

result = verify_receipt(sample_receipt)

print("Dispute Resolution Result:")
print(result)

# Simulate attacks
#simulate_ballot_modification()

#print("\nRunning Ledger Verification After Attack...")
#is_valid = verify_ledger()

#print("Ledger Integrity After Attack:", is_valid)