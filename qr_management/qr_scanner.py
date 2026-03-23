import qrcode

def generate_qr(dog_id):
    qr_img = qrcode.make(str(dog_id))
    filename = f'qr_{dog_id}.png'
    qr_img.save(filename)
    return filename
