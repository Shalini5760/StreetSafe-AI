import qrcode
import os

def generate_qr(complaint_id):
    qr_data = f"Complaint ID: {complaint_id}"

    qr = qrcode.make(qr_data)

    folder = os.path.join("static", "qrcodes")
    os.makedirs(folder, exist_ok=True)

    filename = f"complaint_{complaint_id}.png"
    filepath = os.path.join(folder, filename)

    qr.save(filepath)

    # IMPORTANT: return relative path for url_for
    return f"qrcodes/{filename}"