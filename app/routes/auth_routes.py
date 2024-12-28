from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User
from app import db
from app.utils.logging_utils import log_action

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def index():
    """Redirect to login page if the user is not logged in."""
    if current_user.is_authenticated:
        return redirect(url_for('user.dashboard'))  # Redirect to dashboard if logged in
    return redirect(url_for('auth.login'))  # Redirect to login page if not logged in

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            log_action(user.id, 'Logged in')
            return redirect(url_for('user.dashboard'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    log_action(current_user.id, 'Logged out')
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))
