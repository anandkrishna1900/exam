# app/main/routes.py - routes for the main blueprint
from app.main import bp

@bp.route('/')
def index():
    return '<h1>Home page (main blueprint)</h1>'
