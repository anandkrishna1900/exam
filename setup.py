import os
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).parent

folders = [
    r"Flask and django\FLASK\Program 1",
    r"Flask and django\FLASK\Program 2",
    r"Flask and django\FLASK\Program 3",
    r"Flask and django\FLASK\Program 4",
    r"Flask and django\FLASK\Program 5",
    r"Flask and django\FLASK\Program 6",
    r"Flask and django\FLASK\Program 7",
    r"Flask and django\Django\Program 8",
    r"Flask and django\Django\Program 9",
    r"Flask and django\Django\Program 10",
    r"Flask and django\Django\Program 11",
    r"Flask and django\Django\Program 12",
    r"Flask and django\Django\Program 13",
    r"Flask and django\Django\Program 14",
    r"Flask and django\Django\Program 15",
]

for folder in folders:
    path = ROOT_DIR / folder
    path.mkdir(parents=True, exist_ok=True)

    venv_path = path / "venv"

    if not (venv_path / "Scripts" / "python.exe").exists():
        subprocess.run(["python", "-m", "venv", str(venv_path)], check=True)

    pip = venv_path / "Scripts" / "pip.exe"

    subprocess.run([
        str(pip), "install",
        "Flask", "Django", "Flask-WTF",
        "email-validator", "Flask-SQLAlchemy",
        "Flask-Migrate", "Flask-Mail",
        "Flask-HTTPAuth", "asgiref",
        "gunicorn", "python-dotenv",
        "sqlparse", "tzdata", "whitenoise"
    ], check=True)

print("All environments created successfully.")