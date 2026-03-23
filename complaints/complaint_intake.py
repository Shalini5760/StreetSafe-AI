# complaints/complaint_intake.py
import re
from datetime import datetime
from database.models import Complaint

def clean_complaint_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def create_complaint(data):
    data['reported_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return Complaint.create(data)
