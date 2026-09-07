========================================================================
PROGRAM 15: Live Deployment
========================================================================

WHAT THIS PROGRAM DOES:
----------------------
This program prepares a Django application for production deployment (e.g.
Heroku / Render) by isolating secrets into a .env file (python-dotenv),
serving static assets with WhiteNoise, creating a Procfile for Gunicorn,
and specifying python runtime & dependencies in requirements.txt.

HOW TO RUN:
-----------
1. Open PowerShell or Terminal in this folder:
   cd "Program 15"

2. Activate the virtual environment:
   .\venv\Scripts\Activate.ps1

   * NOTE: If you get an error like "cannot be loaded because running scripts
     is disabled on this system" (ExecutionPolicy error), run this command once
     in PowerShell and retry:
     Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

3. Collect static files (bundled with WhiteNoise):
   python manage.py collectstatic --noinput

4. Run locally with Django:
   python manage.py runserver

5. (Optional) Run with Gunicorn WSGI:
   gunicorn myproject.wsgi

KEY FILES & CONFIGURATIONS:
---------------------------
- .env                 : Environment variables (SECRET_KEY, DEBUG)
- .gitignore           : Excludes sensitive files and virtual environments
- Procfile             : Deployment process definition (web: gunicorn myproject.wsgi)
- runtime.txt          : Target Python runtime specification
- requirements.txt     : Frozen Python dependencies
- staticfiles/         : Compiled static assets processed by WhiteNoise
- myproject/settings.py: Dotenv integration, ALLOWED_HOSTS, WhiteNoise middleware & storage
========================================================================
