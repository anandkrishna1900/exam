# app/main/__init__.py - define the main blueprint
from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes  # import at the bottom (avoids circular import)
