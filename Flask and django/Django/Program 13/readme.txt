========================================================================
PROGRAM 13: Password Resets
========================================================================

WHAT THIS PROGRAM DOES:
----------------------
This program implements password change and password reset workflows using
Django's built-in auth views. Password reset emails with verification links
and security tokens are printed directly to the terminal using Django's
console email backend.

HOW TO RUN:
-----------
1. Open PowerShell or Terminal in this folder:
   cd "Program 13"

2. Activate the virtual environment:
   .\venv\Scripts\Activate.ps1

   * NOTE: If you get an error like "cannot be loaded because running scripts
     is disabled on this system" (ExecutionPolicy error), run this command once
     in PowerShell and retry:
     Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

3. Start the development server:
   python manage.py runserver

4. Test Password Change (while logged in):
   - Navigate to: http://127.0.0.1:8000/password-change/
   - Enter old password and set a new password

5. Test Password Reset (forgot password):
   - Navigate to: http://127.0.0.1:8000/password-reset/
   - Enter registered email address and submit
   - Check the terminal where runserver is running to find the generated reset link
   - Copy the link into your browser, enter a new password, and log in

KEY FILES:
----------
- myproject/settings.py                        : EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
- accounts/templates/password_change_form.html : Form to change password
- accounts/templates/password_change_done.html : Password change success page
- accounts/templates/password_reset_form.html  : Form to request reset email
- accounts/templates/password_reset_done.html  : Message indicating reset email was sent
- accounts/templates/password_reset_confirm.html: Form to enter new password from reset link
- accounts/templates/password_reset_complete.html: Password reset completion page
========================================================================
