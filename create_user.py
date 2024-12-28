from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

# Create the Flask app
app = create_app()

# Define user credentials
USER_USERNAME = "your_username"  # Replace with the desired username
USER_PASSWORD = "your_password"  # Replace with the desired password

# Create the user
with app.app_context():
    hashed_password = generate_password_hash(USER_PASSWORD)  # Generate hashed password
    user = User(username=USER_USERNAME, password_hash=hashed_password, role="user")  # You can set the role as "user"

    db.session.add(user)
    db.session.commit()

    print(f"User '{USER_USERNAME}' created successfully.")
