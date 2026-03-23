def assign_priority(complaint_type):
    if complaint_type == 'Bite':
        return 'High'
    elif complaint_type == 'Injury':
        return 'Medium'
    else:
        return 'Low'
