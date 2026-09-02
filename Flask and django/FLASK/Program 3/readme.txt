======================================================================
PROGRAM 3: Form Handling & Validation using Flask-WTF
======================================================================

1. DESCRIPTION & WHAT IT DOES:
-----------------------------
This program demonstrates web form handling and validation in Flask:
- Creating a registration form class with WTForms (`FlaskForm`).
- Utilizing field types: StringField, PasswordField, SubmitField.
- Applying validation rules: DataRequired, Length, Email, and EqualTo (password confirmation).
- Processing GET and POST requests.
- Validating user submissions (`form.validate_on_submit()`).
- Utilizing flash messages (`flash()`) to provide user feedback upon successful form submission.
- Protection against CSRF attacks with application SECRET_KEY.

2. REQUIREMENTS / PREREQUISITES:
--------------------------------
- Python 3.x
- Flask (`pip install Flask`)
- Flask-WTF (`pip install Flask-WTF`)
- email-validator (`pip install email-validator`)

3. HOW TO RUN:
--------------
Step 1: Open terminal in this folder ("Program 3").
Step 2: (Optional) Activate your virtual environment:
        .\venv\Scripts\activate
Step 3: Run the application:
        python app.py

4. HOW TO TEST / VIEW IN BROWSER:
---------------------------------
Open your browser and visit:
- http://127.0.0.1:5000/
- Enter username, valid email, password, and confirm password.
- Submit the form to see validation in action and receive the success flash notification.
