from database.models import Complaint
from datetime import datetime

def create_complaint(data):
    data['reported_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    complaint = Complaint.create(data)
    return complaint
