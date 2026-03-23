from flask import Flask, request, render_template
from database.models import init_db, Dog
from complaints.complaint_intake import clean_complaint_text
from qr_management.qr_generator import generate_qr
from municipal_actions.task_assigner import assign_task
import sqlite3
from config import DB_PATH
from database.models import create_complaint

app = Flask(__name__)
init_db()

def fetch_all(table):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute(f"SELECT * FROM {table}")
    rows = c.fetchall()
    conn.close()
    return rows

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dog/register', methods=['GET', 'POST'])
def register_dog():
    if request.method == 'POST':
        data = request.form.to_dict()
        dog = Dog.create(data)
        qr = generate_qr(dog.dog_id)
        return f"Dog Registered! ID: {dog.dog_id}, QR: {qr} <br><a href='/dashboard'>Go to Dashboard</a>"
    return render_template('register_dog.html')

@app.route('/complaint', methods=['GET', 'POST'])
def submit_complaint():
    if request.method == 'POST':
        data = request.form.to_dict()

        complaint = create_complaint(data)

        # Generate QR
        qr_path = generate_qr(complaint.complaint_id)

        assign_task(complaint)

        print("Generated QR:", qr_path)  # Debug line

        return render_template(
            'complaint_form.html',
            success=True,
            complaint_id=complaint.complaint_id,
            qr_path=qr_path
        )

    return render_template(
        'complaint_form.html',
        success=False
    )

@app.route('/dashboard')
def dashboard():
    dogs = fetch_all("dogs")
    complaints = fetch_all("complaints")
    return render_template('dashboard.html', dogs=dogs, complaints=complaints)

if __name__ == '__main__':
    app.run(debug=True)
