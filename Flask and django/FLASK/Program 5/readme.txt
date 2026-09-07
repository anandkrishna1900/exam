======================================================================
PROGRAM 5: Modular Application Structure (Blueprints & Background Email)
======================================================================

1. DESCRIPTION & WHAT IT DOES:
-----------------------------
This program demonstrates modular large-scale Flask project architecture:
- Application Factory Pattern (`create_app()`) for scalable initialization.
- Modular code organization using Flask Blueprints:
  * `main` blueprint: handles general site routes (e.g., home page `/`).
  * `auth` blueprint: handles user authentication routes with url prefix `/auth` (e.g., `/auth/register`).
- Configuration management using environment variables and class-based config (`config.py`).
- Asynchronous background email sending using `Flask-Mail` and Python `threading.Thread` so user requests are not blocked during email delivery.

2. REQUIREMENTS / PREREQUISITES:
--------------------------------
- Python 3.x
- Flask (`pip install Flask`)
- Flask-Mail (`pip install Flask-Mail`)

3. HOW TO RUN:
--------------
Step 1: Open terminal in this folder ("Program 5").
Step 2: (Optional) Activate your virtual environment:
        .\venv\Scripts\activate
Step 3: Run the application via the entrypoint runner:
        python run.py

4. HOW TO TEST / VIEW IN BROWSER:
---------------------------------
Open your browser and visit:
- http://127.0.0.1:5000/              -> Home Page handled by `main` blueprint
- http://127.0.0.1:5000/auth/register -> Registration route handled by `auth` blueprint (triggers async email)
