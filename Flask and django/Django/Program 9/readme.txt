========================================================================
PROGRAM 9: Models and the Admin
========================================================================

WHAT THIS PROGRAM DOES:
----------------------
This program demonstrates how to create a database model (Student) using
Django ORM, apply schema migrations, and register the model with the
Django admin interface to manage records (Create, Read, Update, Delete).

HOW TO RUN:
-----------
1. Open PowerShell or Terminal in this folder:
   cd "Program 9"

2. Activate the virtual environment:
   .\venv\Scripts\Activate.ps1

3. Apply database migrations:
   python manage.py makemigrations
   python manage.py migrate

4. Create your own admin account:
   python manage.py createsuperuser
   - Enter your desired Username, Email, and Password when prompted.

5. Start the Django development server:
   python manage.py runserver

6. Open your browser and navigate to:
   - Admin Panel: http://127.0.0.1:8000/admin/
   
   Default / Seeded Credentials (or use your own created above):
   - Username: admin
   - Password: admin123

KEY FILES:
----------
- pages/models.py   : Student model (name, email, course, age)
- pages/admin.py    : admin.site.register(Student)
- myproject/settings.py: App registration in INSTALLED_APPS
========================================================================
