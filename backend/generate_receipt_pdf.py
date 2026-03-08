from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import os
import webbrowser


def generate_receipt_pdf(receipt_id, voter_name, voter_id):

    filename = "voting_receipt.pdf"

    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("<b>Electronic Voting Receipt</b>", styles['Title']))
    content.append(Spacer(1, 20))

    content.append(Paragraph(f"<b>Voter Name:</b> {voter_name}", styles['Normal']))
    content.append(Paragraph(f"<b>Voter ID:</b> {voter_id}", styles['Normal']))
    content.append(Paragraph(f"<b>Receipt ID:</b> {receipt_id}", styles['Normal']))
    content.append(Paragraph(f"<b>Status:</b> Vote Successfully Recorded", styles['Normal']))
    content.append(Paragraph(f"<b>Date:</b> {datetime.now()}", styles['Normal']))

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "This receipt confirms that your encrypted ballot has been securely "
            "recorded in the election ledger and verified by the audit system.",
            styles['Normal']
        )
    )

    doc = SimpleDocTemplate(filename)
    doc.build(content)

    print("\nPDF Receipt Generated:", filename)

    # Automatically open the PDF (makes it feel clickable)
    path = os.path.abspath(filename)
    webbrowser.open(f"file://{path}")