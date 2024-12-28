import os
from datetime import datetime

LOG_DIR = 'logs'

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def log_action(user_id, action):
    date = datetime.now()
    log_file = os.path.join(LOG_DIR, f"{date.strftime('%Y-%m-%d')}.log")
    with open(log_file, 'a') as file:
        file.write(f"[{date}] User {user_id}: {action}\n")
