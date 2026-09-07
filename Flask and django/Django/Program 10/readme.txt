========================================================================
PROGRAM 10: Generic Class-Based Views (CRUD)
========================================================================

WHAT THIS PROGRAM DOES:
----------------------
This program implements a full frontend CRUD (Create, Read, Update, Delete)
interface for the Student model using Django's generic class-based views:
ListView, CreateView, UpdateView, and DeleteView.

HOW TO RUN:
-----------
1. Open PowerShell or Terminal in this folder:
   cd "Program 10"

2. Activate the virtual environment:
   .\venv\Scripts\Activate.ps1

   * NOTE: If you get an error like "cannot be loaded because running scripts
     is disabled on this system" (ExecutionPolicy error), run this command once
     in PowerShell and retry:
     Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

3. Run the development server:
   python manage.py runserver

4. Open your browser and navigate to:
   - Student List (Home): http://127.0.0.1:8000/
   - Add Student:         http://127.0.0.1:8000/add/
   - Edit Student:        http://127.0.0.1:8000/edit/<id>/
   - Delete Student:      http://127.0.0.1:8000/delete/<id>/

KEY FILES:
----------
- pages/models.py                       : Student model
- pages/views.py                        : StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView
- pages/templates/student_list.html     : Lists students with links to Add/Edit/Delete
- pages/templates/student_form.html     : Form for creating and editing students
- pages/templates/student_confirm_delete.html: Confirmation page for deleting a student
- myproject/urls.py                     : URL patterns routing to CRUD views
========================================================================
