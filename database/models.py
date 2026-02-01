from .db_connection import get_connection  # keep relative import to db_connection


def init_db():
    conn = get_connection()
    c = conn.cursor()

    # Dogs table
    c.execute('''CREATE TABLE IF NOT EXISTS dogs (
                 dog_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 qr_code TEXT,
                 latitude REAL,
                 longitude REAL,
                 gender TEXT,
                 estimated_age INTEGER,
                 color TEXT,
                 health_status TEXT,
                 is_sterilized INTEGER,
                 last_seen_date TEXT
                 )''')

    # Complaints table
    c.execute('''CREATE TABLE IF NOT EXISTS complaints (
                 complaint_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 dog_id INTEGER,
                 complaint_type TEXT,
                 description TEXT,
                 latitude REAL,
                 longitude REAL,
                 priority TEXT,
                 status TEXT,
                 reported_at TEXT
                 )''')
    conn.commit()
    conn.close()

# ORM-like helper classes
class Dog:
    @staticmethod
    def create(data):
        conn = get_connection()
        c = conn.cursor()
        c.execute('''INSERT INTO dogs (qr_code, latitude, longitude, gender, estimated_age, color, health_status, is_sterilized, last_seen_date)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                  (data.get('qr_code',''), data.get('latitude',0), data.get('longitude',0), data.get('gender',''),
                   data.get('estimated_age',0), data.get('color',''), data.get('health_status','Healthy'),
                   int(data.get('is_sterilized',0)), data.get('last_seen_date','')))
        dog_id = c.lastrowid
        conn.commit()
        conn.close()
        data['dog_id'] = dog_id
        return type('DogObj', (), data)()

class Complaint:
    @staticmethod
    def create(data):
        conn = get_connection()
        c = conn.cursor()
        c.execute('''INSERT INTO complaints (dog_id, complaint_type, description, latitude, longitude, priority, status, reported_at)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                  (data.get('dog_id'), data.get('complaint_type',''), data.get('description',''),
                   data.get('latitude',0), data.get('longitude',0), data.get('priority','Medium'),
                   data.get('status','Open'), data.get('reported_at','')))
        complaint_id = c.lastrowid
        conn.commit()
        conn.close()
        data['complaint_id'] = complaint_id
        return type('ComplaintObj', (), data)()
