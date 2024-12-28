import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Load the secret key from the environment
    SECRET_KEY = os.getenv('SECRET_KEY')  # Will raise an error if not found

    # Load the SQLAlchemy Database URI from the environment
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

    # Optional configurations
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = os.getenv('SESSION_TYPE')
    PERMANENT_SESSION_LIFETIME = int(os.getenv('SESSION_LIFETIME', 1800))  # Default 30 mins
