# app/models.py

from app import db  # Now db is imported from the app package
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# Define the User model
class User(db.Model, UserMixin):  # db will be available after app creation
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(500), nullable=False)
    role = db.Column(db.String(20), default='user')  # Added role field (default is 'user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
