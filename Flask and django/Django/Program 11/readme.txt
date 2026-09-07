========================================================================
PROGRAM 11: Custom User Models
========================================================================

WHAT THIS PROGRAM DOES:
----------------------
This program demonstrates how to extend Django's built-in authentication
system by subclassing AbstractUser to create a CustomUser model with custom
database fields (phone, address, age), configured via AUTH_USER_MODEL.

HOW TO RUN:
-----------
1. Open PowerShell or Terminal in this folder:
   cd "Program 11"

2. Activate the virtual environment:
   .\venv\Scripts\Activate.ps1

3. Start the development server:
   python manage.py runserver

4. Open your browser and navigate to:
   - Admin Panel: http://127.0.0.1:8000/admin/

   Admin Credentials:
   - Username: admin
   - Password: admin123

5. Inspect the Users section in admin to view custom fields (phone, address, age).

KEY FILES:
----------
- accounts/models.py   : CustomUser model extending AbstractUser
- accounts/admin.py    : CustomUser registered with UserAdmin
- myproject/settings.py: AUTH_USER_MODEL = 'accounts.CustomUser'
========================================================================
