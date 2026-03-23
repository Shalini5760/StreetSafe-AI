def mark_action_completed(complaint):
    complaint.status = "Resolved"
    print(f"Complaint {complaint.complaint_id} marked as resolved.")
