import os
import logging
from datetime import datetime

def setup_logging():
    log_dir = os.path.join('logs', datetime.now().strftime('%Y-%m'))
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log_file = os.path.join(log_dir, f"{datetime.now().strftime('%d-%b-%Y')}.log")
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

def log_action(action, user_id):
    setup_logging()
    logging.info(f"User {user_id} performed: {action}")
