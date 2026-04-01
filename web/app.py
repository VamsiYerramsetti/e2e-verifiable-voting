from flask import Flask, render_template, request, send_file

# Backend imports
from backend.crypto.keygen import generate_keys
from backend.crypto.encrypt_vote import encrypt_vote
from backend.ledger.bulletin_board import add_vote, get_ledger
from backend.ledger.ledger_verify import verify_ledger
from backend.tally.tally_votes import tally_votes
from backend.audit.dispute_resolution import verify_receipt
from backend.audit.attack_simulation import auto_attack
from backend.generate_receipt_pdf import generate_receipt_pdf

app = Flask(__name__)

# -----------------------------
# GLOBAL SETUP
# -----------------------------
public_key, private_key = generate_keys()

candidate_map = {
    "A": 0,
    "B": 1,
    "C": 2
}


# -----------------------------
# DASHBOARD
# -----------------------------
@app.route('/')
def home():

    ledger = get_ledger()
    total = len(ledger)
    ledger_valid = verify_ledger()

    return render_template(
        "index.html",
        total=total,
        ledger_valid=ledger_valid
    )


# -----------------------------
# VOTE PAGE
# -----------------------------
@app.route('/vote', methods=["GET", "POST"])
def vote():

    if request.method == "POST":

        vote = request.form["candidate"]
        numeric_vote = candidate_map[vote]

        cipher = encrypt_vote(public_key, numeric_vote)
        receipt = add_vote(cipher)

        return render_template("result.html", receipt=receipt)

    return render_template("vote.html")


# -----------------------------
# VERIFY RECEIPT
# -----------------------------
@app.route('/verify', methods=["GET", "POST"])
def verify():

    result = None

    if request.method == "POST":

        receipt = request.form["receipt"]

        result = verify_receipt(receipt)

        # 🔥 IMPORTANT: attach receipt id for download button
        result["receipt"] = receipt

    return render_template("verify.html", result=result)


# -----------------------------
# DOWNLOAD PDF
# -----------------------------
@app.route('/download/<receipt_id>')
def download(receipt_id):

    voter_name = "User"
    voter_id = "123"

    filepath = generate_receipt_pdf(
        receipt_id,
        voter_name,
        voter_id,
        "SAFE"
    )

    return send_file(
        filepath,
        as_attachment=True,
        download_name=f"receipt_{receipt_id}.pdf",
        mimetype="application/pdf"
    )


# -----------------------------
# AUDIT PAGE
# -----------------------------
@app.route('/audit')
def audit():

    ledger = get_ledger()

    results = tally_votes(private_key)
    ledger_valid = verify_ledger()

    return render_template(
        "audit.html",
        results=results,
        ledger_valid=ledger_valid,
        total=len(ledger)
    )


# -----------------------------
# ATTACK PAGE (CONTROLLED)
# -----------------------------
@app.route('/attack', methods=["GET", "POST"])
def attack():

    message = None

    if request.method == "POST":
        auto_attack()
        message = "⚠️ Attack executed successfully!"

    return render_template("attack.html", message=message)


# -----------------------------
# RUN SERVER
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)