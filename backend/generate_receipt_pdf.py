from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import os


def generate_receipt_pdf(receipt_id, voter_name, voter_id, system_status):

    # 🔥 Unique filename (important for download)
    filename = f"receipt_{receipt_id}.pdf"

    # Absolute path (needed for Flask send_file)
    filepath = os.path.abspath(filename)

    styles = getSampleStyleSheet()
    content = []

    # -----------------------------
    # TITLE
    # -----------------------------
    content.append(Paragraph("<b>Electronic Voting Receipt</b>", styles['Title']))
    content.append(Spacer(1, 20))

    # -----------------------------
    # BASIC DETAILS
    # -----------------------------
    content.append(Paragraph(f"<b>Voter Name:</b> {voter_name}", styles['Normal']))
    content.append(Paragraph(f"<b>Voter ID:</b> {voter_id}", styles['Normal']))
    content.append(Paragraph(f"<b>Receipt ID:</b> {receipt_id}", styles['Normal']))
    content.append(Paragraph(f"<b>Date:</b> {datetime.now()}", styles['Normal']))

    content.append(Spacer(1, 15))

    # -----------------------------
    # SYSTEM STATUS
    # -----------------------------
    if system_status == "COMPROMISED":

        content.append(
            Paragraph(
                "<b>System Status:</b> <font color='red'>COMPROMISED</font>",
                styles['Normal']
            )
        )

        content.append(
            Paragraph(
                "⚠️ WARNING: Unauthorized modification detected in election ledger.",
                styles['Normal']
            )
        )

    else:

        content.append(
            Paragraph(
                "<b>System Status:</b> <font color='green'>SAFE</font>",
                styles['Normal']
            )
        )

        content.append(
            Paragraph(
                "✔ Your vote has been securely recorded and verified.",
                styles['Normal']
            )
        )

    content.append(Spacer(1, 20))

    # -----------------------------
    # DESCRIPTION
    # -----------------------------
    content.append(
        Paragraph(
            "This receipt confirms that your encrypted ballot has been securely "
            "stored in the hash-chained election ledger and validated through "
            "post-election cryptographic auditing.",
            styles['Normal']
        )
    )

    content.append(Spacer(1, 20))

    # -----------------------------
    # FOOTER NOTE
    # -----------------------------
    content.append(
        Paragraph(
            "<i>Note: This receipt does not reveal your vote, ensuring voter privacy.</i>",
            styles['Normal']
        )
    )

    # -----------------------------
    # BUILD PDF
    # -----------------------------
    doc = SimpleDocTemplate(filepath)
    doc.build(content)

    print("\nPDF Receipt Generated:", filepath)

    # 🔥 VERY IMPORTANT: Return file path
    return filepath