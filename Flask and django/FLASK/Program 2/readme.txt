======================================================================
PROGRAM 2: Flask Jinja2 Templating & Bootstrap Integration
======================================================================

1. DESCRIPTION & WHAT IT DOES:
-----------------------------
This program demonstrates template rendering and UI styling in Flask:
- Rendering HTML templates using Jinja2 (`render_template`).
- Passing dynamic context variables (such as user name and list of courses) from Python to HTML templates.
- Using Jinja2 control flow (e.g., loops and template inheritance).
- Integrating Twitter Bootstrap via the `Bootstrap-Flask` (`flask_bootstrap.Bootstrap5`) extension for styling.

2. REQUIREMENTS / PREREQUISITES:
--------------------------------
- Python 3.x
- Flask (`pip install Flask`)
- Bootstrap-Flask (`pip install bootstrap-flask`)

3. HOW TO RUN:
--------------
Step 1: Open terminal in this folder ("Program 2").
Step 2: (Optional) Activate your virtual environment:
        .\venv\Scripts\activate
Step 3: Run the application:
        python app.py

4. HOW TO TEST / VIEW IN BROWSER:
---------------------------------
Open your browser and visit:
- http://127.0.0.1:5000/       -> Home Page displaying user greeting and list of courses styled with Bootstrap
- http://127.0.0.1:5000/about  -> About page loaded via template
