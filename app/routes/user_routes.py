from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.utils.logging_utils import log_action

user_bp = Blueprint('user', __name__)

@user_bp.route('/dashboard')
@login_required
def dashboard():
    log_action(current_user.id, 'Accessed dashboard')
    # You can fetch user-specific data like tasks here
    tasks = []  # Placeholder for tasks
    return render_template('dashboard.html', user=current_user, tasks=tasks)
