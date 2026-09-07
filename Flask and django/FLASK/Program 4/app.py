# app.py - Database and Models (Flask-SQLAlchemy + Flask-Migrate)
from flask import Flask
from flask_migrate import Migrate
from models import db, Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return """
    <h1>Flask SQLAlchemy CRUD</h1>
    <p>Available Routes:</p>
    <ul>
        <li><a href="/add">Add Student</a></li>
        <li><a href="/students">View Students</a></li>
        <li><a href="/update/1">Update Student (ID 1)</a></li>
        <li><a href="/delete/1">Delete Student (ID 1)</a></li>
    </ul>
    """

@app.route('/add')
def add_student():
    student = Student(
        name="John",
        email="john@gmail.com"
    )
    db.session.add(student)
    db.session.commit()
    return "Student Added"

@app.route('/students')
def get_students():
    students = Student.query.all()
    if not students:
        return "No students found"
    result = "<h1>Student List</h1>"
    for student in students:
        result += f"ID: {student.id} | Name: {student.name} | Email: {student.email}<br>"
    return result

@app.route('/update/<int:id>')
def update_student(id):
    student = db.session.get(Student, id) if hasattr(db.session, 'get') else Student.query.get(id)
    if student:
        student.name = "Updated Name"
        db.session.commit()
        return "Student Updated"
    return "Student Not Found"

@app.route('/delete/<int:id>')
def delete_student(id):
    student = db.session.get(Student, id) if hasattr(db.session, 'get') else Student.query.get(id)
    if student:
        db.session.delete(student)
        db.session.commit()
        return "Student Deleted"
    return "Student Not Found"

if __name__ == '__main__':
    app.run(debug=True)
