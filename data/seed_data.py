from database.models import Dog

sample_dog = {
    "qr_code": "DOG001",
    "latitude": 12.9716,
    "longitude": 77.5946,
    "gender": "Male",
    "estimated_age": 2,
    "color": "Brown",
    "health_status": "Healthy",
    "is_sterilized": 0,
    "last_seen_date": "2026-01-27"
}

dog = Dog.create(sample_dog)
print(f"Sample dog registered with ID: {dog.dog_id}")
