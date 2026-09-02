# Setup & Installation Guide

## 1. Fix "Script Execution is Disabled" (PowerShell Restriction Error)
If you see the error:
`File ...\venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system.`

Run this command in PowerShell (as normal user or Admin):
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```
*Alternatively, you can bypass for just the current terminal session:*
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

---

## 2. Virtual Environment (venv) Setup

### Step A: Create a Virtual Environment
From your terminal inside the project root:
```bash
python -m venv venv
```

### Step B: Activate the Virtual Environment
- **On Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
- **On Windows (CMD):**
  ```cmd
  .\venv\Scripts\activate.bat
  ```
- **On Linux / macOS:**
  ```bash
  source venv/bin/activate
  ```

---

## 3. Package Installation

### Option A: Install from requirements.txt
```bash
pip install -r requirements.txt
```

### Option B: Manual Installation of all dependencies used across Flask & Django programs
```bash
# Core Web Frameworks
pip install Flask Django

# Flask Extensions & Utilities
pip install Flask-WTF email-validator Flask-SQLAlchemy Flask-Migrate Flask-Mail Flask-HTTPAuth

# Django & Deployment Utilities
pip install asgiref gunicorn python-dotenv sqlparse tzdata whitenoise
```

---

## 4. Deactivating the Virtual Environment
When you are done working, exit the venv by running:
```bash
deactivate
```
