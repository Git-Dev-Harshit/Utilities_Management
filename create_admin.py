from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

# Create the Flask app
app = create_app()

# Define admin credentials
ADMIN_USERNAME = "your_username"
ADMIN_PASSWORD = "your_password"  # Replace with your desired admin password

# Create the admin user
with app.app_context():
    hashed_password = generate_password_hash(ADMIN_PASSWORD)  # Generate hashed password
    admin = User(username=ADMIN_USERNAME, password_hash=hashed_password, role="admin")  # Note the password field mapping

    db.session.add(admin)
    db.session.commit()

    print(f"Admin user '{ADMIN_USERNAME}' created successfully.")
