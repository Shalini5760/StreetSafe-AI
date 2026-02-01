from flask import Flask, request, jsonify, render_template
from database.models import init_db, Dog, Complaint
from qr_management.qr_generator import generate_qr
from complaints.complaint_intake import create_complaint
from municipal_actions.task_assigner import assign_task
import sqlite3
from config import DB_PATH
from qr_management.qr_generator import generate_qr


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

@app.route('/dog/register', methods=['GET','POST'])
def register_dog():
    if request.method == 'POST':
        data = request.form.to_dict()
        dog = Dog.create(data)
        qr = generate_qr(dog.dog_id)
        return f"Dog Registered! ID: {dog.dog_id}, QR: {qr} <br><a href='/dashboard'>Go to Dashboard</a>"
    return render_template('register_dog.html')

@app.route('/complaint', methods=['GET','POST'])
def submit_complaint():
    if request.method == 'POST':
        data = request.form.to_dict()
        complaint = create_complaint(data)
        assign_task(complaint)
        return f"Complaint Submitted! ID: {complaint.complaint_id}, Status: {complaint.status} <br><a href='/dashboard'>Go to Dashboard</a>"
    return render_template('complaint_form.html')

@app.route('/dashboard')
def dashboard():
    dogs = fetch_all("dogs")
    complaints = fetch_all("complaints")
    return render_template('dashboard.html', dogs=dogs, complaints=complaints)

if __name__ == '__main__':
    app.run(debug=True)
