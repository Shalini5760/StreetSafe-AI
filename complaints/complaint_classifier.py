def classify_complaint(description):
    description = description.lower()
    if 'bite' in description:
        return 'Bite'
    elif 'injury' in description:
        return 'Injury'
    elif 'aggressive' in description:
        return 'Aggression'
    else:
        return 'Other'
