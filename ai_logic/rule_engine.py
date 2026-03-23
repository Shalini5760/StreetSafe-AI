from complaints.complaint_classifier import classify_complaint
from complaints.priority_engine import assign_priority

def process_complaint(description):
    cleaned = description.lower()
    complaint_type = classify_complaint(cleaned)
    priority = assign_priority(complaint_type)
    return complaint_type, priority
