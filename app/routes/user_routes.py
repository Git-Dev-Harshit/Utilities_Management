from flask import Blueprint, render_template
from flask_login import login_required, current_user

user_bp = Blueprint('user', __name__)

@user_bp.route('/dashboard')
@login_required
def dashboard():
    tasks = current_user.tasks
    return render_template('dashboard.html', tasks=tasks)
