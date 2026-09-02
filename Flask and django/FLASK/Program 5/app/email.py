# app/email.py - send email on a background thread
from threading import Thread
from flask import current_app
from flask_mail import Message
from app import mail

def send_async_email(app, msg):
    # the background thread needs its own application context
    with app.app_context():
        mail.send(msg)

def send_email(subject, recipients, body):
    # grab the real app object (not the context-bound proxy)
    app = current_app._get_current_object()
    msg = Message(subject, recipients=recipients)
    msg.body = body
    # start the thread and return immediately
    Thread(target=send_async_email, args=(app, msg)).start()
