from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from app.models import User
from app.utils.logging_utils import log_action

admin_bp = Blueprint('admin', __name__)

@admin_bp.before_request
@login_required
def restrict_to_admin():
    if current_user.role != 'admin':
        return "Access denied", 403

@admin_bp.route('/manage_users', methods=['GET', 'POST'])
def manage_users():
    users = User.query.all()
    log_action(current_user.id, 'Accessed manage users page')
    return render_template('manage_users.html', users=users, user=current_user)


@admin_bp.route('/assign_tasks/<int:user_id>', methods=['GET', 'POST'])
def assign_tasks(user_id):
    log_action(current_user.id, f'Accessed assign tasks page for user {user_id}')
    return render_template('assign_tasks.html', user_id=user_id)

