from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_session import Session
from config import Config

# Initialize db, migrate, login_manager here
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the app with db and other extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    Session(app)

    # Import the User model *after* db is initialized to avoid circular import
    from app.models import User

    # Register Blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.admin_routes import admin_bp
    from app.routes.user_routes import user_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(user_bp, url_prefix='/user')

    # Set up the user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Add before_request to set up the current user globally
    @app.before_request
    def before_request():
        g.user = get_current_user()  # Set the current user globally

    # Add a context processor to inject 'user' into all templates
    @app.context_processor
    def inject_user():
        return {'user': g.user}

    return app

# Function to retrieve the current user (you need to implement this)
def get_current_user():
    # Example: Retrieve user from session or JWT token
    # For example, you could use Flask-Login's `current_user`:
    from flask_login import current_user
    return current_user if current_user.is_authenticated else None
