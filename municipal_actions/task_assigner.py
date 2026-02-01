# municipal_actions/task_assigner.py

def assign_task(complaint):
    """
    Simple rule-based task assigner for municipal staff.
    For demo purposes, it just sets status to 'Assigned'.
    """
    complaint.status = "Assigned"
    return complaint
