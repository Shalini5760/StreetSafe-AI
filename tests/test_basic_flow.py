from database.models import init_db, Dog
from qr_management.qr_generator import generate_qr

def test_flow():
    init_db()
    dog = Dog.create({"qr_code":"DOG001","latitude":0,"longitude":0,"gender":"Male","estimated_age":2,"color":"Brown"})
    qr = generate_qr(dog.dog_id)
    print(f"Test dog created: ID={dog.dog_id}, QR={qr}")

if __name__ == "__main__":
    test_flow()
