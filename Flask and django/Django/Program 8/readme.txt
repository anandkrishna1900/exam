========================================================================
PROGRAM 8: Static Pages with TemplateView
========================================================================

WHAT THIS PROGRAM DOES:
----------------------
This program demonstrates how to configure and use Django's generic
class-based views (TemplateView) to render static HTML pages (Home and
About) with URL routing and template linking.

HOW TO RUN:
-----------
1. Open PowerShell or Terminal in this folder:
   cd "Program 8"

2. Activate the virtual environment:
   .\venv\Scripts\Activate.ps1

3. Run migrations (already applied):
   python manage.py migrate

4. Start the Django development server:
   python manage.py runserver

5. Open your browser and navigate to:
   - Home Page:  http://127.0.0.1:8000/
   - About Page: http://127.0.0.1:8000/about/

KEY FILES:
----------
- pages/views.py            : HomeView and AboutView subclassing TemplateView
- pages/templates/home.html : Template for home route
- pages/templates/about.html: Template for about route
- myproject/urls.py         : URL pattern definitions
========================================================================
