======================================================================
PROGRAM 4: Database Operations (CRUD) with Flask-SQLAlchemy
======================================================================

1. DESCRIPTION & WHAT IT DOES:
-----------------------------
This program demonstrates database integration and CRUD operations:
- Database ORM modeling using `Flask-SQLAlchemy`.
- Database schema migration support using `Flask-Migrate`.
- SQLite database configuration (`students.db`).
- Full CRUD operations:
  * Create: `/add` creates a new Student record.
  * Read: `/students` queries and lists all student records.
  * Update: `/update/<id>` modifies an existing student's details.
  * Delete: `/delete/<id>` removes a student record from the database.

2. REQUIREMENTS / PREREQUISITES:
--------------------------------
- Python 3.x
- Flask (`pip install Flask`)
- Flask-SQLAlchemy (`pip install Flask-SQLAlchemy`)
- Flask-Migrate (`pip install Flask-Migrate`)

3. HOW TO RUN:
--------------
Step 1: Open terminal in this folder ("Program 4").
Step 2: (Optional) Activate your virtual environment:
        .\venv\Scripts\activate
Step 3: Run the application:
        python app.py

4. HOW TO TEST / VIEW IN BROWSER:
---------------------------------
Open your browser and visit:
- http://127.0.0.1:5000/           -> Menu with CRUD links
- http://127.0.0.1:5000/add        -> Adds a student record
- http://127.0.0.1:5000/students   -> Lists all stored students
- http://127.0.0.1:5000/update/1   -> Updates student with ID 1
- http://127.0.0.1:5000/delete/1   -> Deletes student with ID 1
