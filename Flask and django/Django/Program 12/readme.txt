========================================================================
PROGRAM 12: Authentication Flow
========================================================================

WHAT THIS PROGRAM DOES:
----------------------
This program implements a complete user authentication flow using Django's
built-in LoginView and LogoutView along with a custom SignUpView powered by
a custom UserCreationForm. It redirects authenticated users to the home page
and displays their login state.

HOW TO RUN:
-----------
1. Open PowerShell or Terminal in this folder:
   cd "Program 12"

2. Activate the virtual environment:
   .\venv\Scripts\Activate.ps1

3. Start the development server:
   python manage.py runserver

4. Open your browser and navigate to:
   - Home Page: http://127.0.0.1:8000/
   - Login:     http://127.0.0.1:8000/login/
   - Sign Up:   http://127.0.0.1:8000/signup/

5. Test the flow:
   - Sign up a new user at /signup/
   - Log in at /login/
   - View authenticated username on the home page and click "Log Out"

KEY FILES:
----------
- accounts/forms.py             : SignUpForm extending UserCreationForm
- accounts/views.py             : SignUpView extending CreateView
- accounts/templates/home.html  : Shows login status and logout button
- accounts/templates/login.html : Login form
- accounts/templates/signup.html: Sign-up form
- myproject/settings.py         : LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL, LOGIN_URL
========================================================================
