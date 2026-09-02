# app/auth/__init__.py - define the auth blueprint
from flask import Blueprint

bp = Blueprint('auth', __name__)

from app.auth import routes
