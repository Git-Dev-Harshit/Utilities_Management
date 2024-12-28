from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from ..models import User, Task, UserTask
from .. import db

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/manage-users', methods=['GET', 'POST'])
@login_required
def manage_users():
    if current_user.role != 'admin':
        return "Unauthorized", 403
    users = User.query.all()
    return render_template('manage_users.html', users=users)

@admin_bp.route('/assign_task/<int:user_id>', methods=['GET', 'POST'])
@login_required
def assign_task(user_id):
    if current_user.role != 'admin':
        return redirect(url_for('user.dashboard'))

    user = User.query.get(user_id)
    if not user:
        flash('User not found.', 'danger')
        return redirect(url_for('admin.manage_users'))

    all_tasks = Task.query.all()
    user_task_ids = [ut.task_id for ut in UserTask.query.filter_by(user_id=user.id).all()]

    if request.method == 'POST':
        selected_task_ids = request.form.getlist('tasks')
        UserTask.query.filter_by(user_id=user.id).delete()  # Clear existing tasks
        for task_id in selected_task_ids:
            user_task = UserTask(user_id=user.id, task_id=task_id)
            db.session.add(user_task)
        db.session.commit()
        flash('Tasks updated successfully.', 'success')
        return redirect(url_for('admin.manage_users'))

    return render_template('assign_task.html', user=user, all_tasks=all_tasks, user_task_ids=user_task_ids)
