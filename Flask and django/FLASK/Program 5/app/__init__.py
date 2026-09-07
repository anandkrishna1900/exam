# app/__init__.py - builds the app and registers blueprints
from flask import Flask
from flask_mail import Mail
from config import Config

mail = Mail()  # create the extension (not yet bound to an app)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    mail.init_app(app)  # bind the extension to this app

    # Register the blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
