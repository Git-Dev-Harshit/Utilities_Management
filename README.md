# Flask Utilities Management

A scalable **Flask web application** that provides various utilities and task management features, with user role-based access control, authentication, and audit logging. This application is designed to allow admins to manage and assign tasks (utilities) to users and track user activities through detailed logs.

---

## Features

- **User Authentication**: Secure login, session management, and password hashing using `Flask-Login` and `Flask-Bcrypt`.
- **Role-Based Access**: Different user roles with task access control (Admin has full access; regular users see assigned utilities).
- **Task Management**: Admins can create, assign, and manage utilities (tasks), and regular users can access them based on permissions.
- **Audit Trail**: Detailed logs of user activity, including login attempts and page accesses, stored in a month-wise, date-wise structure.
- **Admin Panel**: Admins can manage users, their roles, and monitor activity logs.

---

## Folder Structure

```plaintext
/Utilities_management
│
├── app/
│   ├── __init__.py             # Initialize Flask app and extensions
│   ├── auth/                   # Authentication routes
│   ├── users/                  # User management routes
│   ├── admin/                  # Admin management routes
│   ├── models.py               # Database models
│   ├── routes/                 # Directory for all routes (auth, user, admin, etc.)
│   ├── utils/                  # Directory for utility functions
│   ├── templates/              # HTML files (Jinja2 templates)
│   ├── static/                 # Static files (CSS, JS, images)
│
├── config.py                   # Application configurations (DB, secret keys, etc.)
├── .env                        # Environment variables (e.g., DB credentials, secret key)
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── run.py                      # Entry point for running the app
```
