======================================================================
PROGRAM 6: RESTful API with Bearer Token Authentication
======================================================================

1. DESCRIPTION & WHAT IT DOES:
-----------------------------
This program demonstrates how to build a secure REST API with Flask:
- Creating modular API endpoints under the `/api` URL prefix using Flask Blueprints.
- Returning structured JSON responses using `jsonify()`.
- Handling JSON payload data from incoming POST requests via `request.get_json()`.
- Proper HTTP status codes (200 OK, 201 Created, 400 Bad Request, 401 Unauthorized).
- Securing specific endpoints using Token-based authentication via `Flask-HTTPAuth` (`HTTPTokenAuth(scheme='Bearer')`).
  * Public Route: `GET /api/posts` (fetches all posts).
  * Protected Route: `POST /api/posts` (requires valid Bearer token: 'mysecrettoken123').

2. REQUIREMENTS / PREREQUISITES:
--------------------------------
- Python 3.x
- Flask (`pip install Flask`)
- Flask-HTTPAuth (`pip install Flask-HTTPAuth`)

3. HOW TO RUN:
--------------
Step 1: Open terminal in this folder ("Program 6").
Step 2: (Optional) Activate your virtual environment:
        .\venv\Scripts\activate
Step 3: Run the application:
        python app.py

4. HOW TO TEST:
---------------
A. In Browser / Postman / cURL:
   - View public posts (GET):
     http://127.0.0.1:5000/api/posts

B. Using cURL in Terminal:
   - GET all posts:
     curl -X GET http://127.0.0.1:5000/api/posts

   - Create a post (Without Token -> Returns 401 Unauthorized):
     curl -X POST http://127.0.0.1:5000/api/posts -H "Content-Type: application/json" -d "{\"title\":\"My Title\",\"body\":\"My Body\"}"

   - Create a post (With Bearer Token -> Returns 201 Created):
     curl -X POST http://127.0.0.1:5000/api/posts -H "Authorization: Bearer mysecrettoken123" -H "Content-Type: application/json" -d "{\"title\":\"My Title\",\"body\":\"My Body\"}"
