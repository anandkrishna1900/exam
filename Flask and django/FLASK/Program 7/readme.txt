======================================================================
PROGRAM 7: Unit Testing Flask Applications with unittest & Test Client
======================================================================

1. DESCRIPTION & WHAT IT DOES:
-----------------------------
This program demonstrates automated testing and test-driven workflows in Flask:
- `app.py`: A sample Flask web application with multiple routes (static text, JSON APIs, dynamic routes).
- `test_app.py`: Automated test suite built using Python's built-in `unittest` module.
- Uses Flask's built-in test client (`app.test_client()`) to simulate HTTP requests without spinning up a live web server.
- Verifies:
  * Status code assertions (`assertEqual(response.status_code, 200)`).
  * HTML content assertions (`assertIn`).
  * JSON payload inspection (`response.get_json()`).
  * 404 Not Found error handling.

2. REQUIREMENTS / PREREQUISITES:
--------------------------------
- Python 3.x
- Flask (`pip install Flask`)

3. HOW TO RUN:
--------------
Option A: Running the Application
Step 1: Open terminal in this folder ("Program 7").
Step 2: (Optional) Activate virtual environment:
        .\venv\Scripts\activate
Step 3: Run the web server:
        python app.py
Step 4: Visit http://127.0.0.1:5000/ or http://127.0.0.1:5000/api/data in your browser.

Option B: Running the Automated Unit Tests
Step 1: Open terminal in this folder ("Program 7").
Step 2: Run the test suite:
        python test_app.py
        (or `python -m unittest test_app.py`)
