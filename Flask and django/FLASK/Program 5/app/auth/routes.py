# app/auth/routes.py - routes for the auth blueprint
from app.auth import bp
from app.email import send_email

@bp.route('/register')
def register():
    # pretend a user just registered, then send a welcome email
    send_email(
        subject='Welcome!',
        recipients=['student@example.com'],
        body='Thanks for registering with our Flask app.'
    )
    return '<p>Registered! A welcome email is being sent in the background.</p>'
