from datetime import datetime

def get_current_date():
    """Returns the current date in YYYY-MM-DD format."""
    return datetime.now().strftime('%Y-%m-%d')

def get_current_month():
    """Returns the current month in YYYY-MM format."""
    return datetime.now().strftime('%Y-%m')
