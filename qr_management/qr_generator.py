# qr_management/qr_generator.py
import qrcode

def generate_qr(dog_id):
    filename = f"qr_{dog_id}.png"
    img = qrcode.make(f"DOG:{dog_id}")
    img.save(filename)
    return filename
