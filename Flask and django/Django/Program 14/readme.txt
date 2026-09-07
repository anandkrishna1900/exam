========================================================================
PROGRAM 14: Permissions and Relationships
========================================================================

WHAT THIS PROGRAM DOES:
----------------------
This program demonstrates model relationships (ForeignKey) and view-level
permissions using Django's LoginRequiredMixin. Users must be logged in to
view posts or create new ones. When creating a post, the author field is
automatically assigned to the logged-in user in form_valid().

HOW TO RUN:
-----------
1. Open PowerShell or Terminal in this folder:
   cd "Program 14"

2. Activate the virtual environment:
   .\venv\Scripts\Activate.ps1

   * NOTE: If you get an error like "cannot be loaded because running scripts
     is disabled on this system" (ExecutionPolicy error), run this command once
     in PowerShell and retry:
     Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

3. Start the development server:
   python manage.py runserver

4. Open your browser:
   - Visit http://127.0.0.1:8000/posts/
   - If not logged in, you will be automatically redirected to /login/
   - Log in or create an account at /signup/
   - Add a new post at http://127.0.0.1:8000/posts/add/
   - View your post listed with your username automatically set as author

KEY FILES:
----------
- accounts/models.py               : Post model with ForeignKey to CustomUser
- accounts/views.py                : PostListView & PostCreateView using LoginRequiredMixin
- accounts/templates/post_list.html: Lists posts with author names
- accounts/templates/post_form.html: Form to add a new post
- myproject/urls.py                : Routes for /posts/ and /posts/add/
========================================================================
