======================================================================
PROGRAM 1: Basic Flask Routing and URL Dynamic Parameters
======================================================================

1. DESCRIPTION & WHAT IT DOES:
-----------------------------
This program demonstrates the fundamentals of Flask web framework:
- Creating a basic Flask application instance.
- Setting up static URL routes ('/' and '/about').
- Defining dynamic URL routes with variable parameters:
  * String parameter route: '/user/<name>' which greets the user.
  * Integer converter route: '/square/<int:number>' which calculates the square of a given integer.

2. REQUIREMENTS / PREREQUISITES:
--------------------------------
- Python 3.x
- Flask (`pip install Flask`)

3. HOW TO RUN:
--------------
Step 1: Open terminal in this folder ("Program 1").
Step 2: (Optional) Activate your virtual environment:
        .\venv\Scripts\activate
Step 3: Run the application:
        python app.py

4. HOW TO TEST / VIEW IN BROWSER:
---------------------------------
Open your browser and visit:
- http://127.0.0.1:5000/              -> Home Page ("Welcome to my Flask App")
- http://127.0.0.1:5000/about         -> About Page ("About Page")
- http://127.0.0.1:5000/user/Alice    -> Greets user ("Hello Alice!")
- http://127.0.0.1:5000/square/5      -> Returns square ("The square of 5 is 25")
