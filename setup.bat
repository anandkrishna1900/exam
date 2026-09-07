@echo off
setlocal enabledelayedexpansion

echo ================================================================
echo         Python Virtual Environment Setup Script (1 to 15)
echo ================================================================
echo.

REM 1. Fix PowerShell Execution Policy for the current user
echo [*] Enabling PowerShell script execution (RemoteSigned)...
powershell -NoProfile -ExecutionPolicy Bypass -Command "Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force" >nul 2>&1
echo [OK] Execution policy configured.
echo.

REM 2. Check for Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH! Please install Python first.
    pause
    exit /b 1
)

set "ROOT_DIR=%~dp0"
set "REQ_FILE=%ROOT_DIR%requirements.txt"

REM Array of all Program folders across Flask and Django
set "FOLDERS[0]=Flask and django\FLASK\Program 1"
set "FOLDERS[1]=Flask and django\FLASK\Program 2"
set "FOLDERS[2]=Flask and django\FLASK\Program 3"
set "FOLDERS[3]=Flask and django\FLASK\Program 4"
set "FOLDERS[4]=Flask and django\FLASK\Program 5"
set "FOLDERS[5]=Flask and django\FLASK\Program 6"
set "FOLDERS[6]=Flask and django\FLASK\Program 7"
set "FOLDERS[7]=Flask and django\Django\Program 8"
set "FOLDERS[8]=Flask and django\Django\Program 9"
set "FOLDERS[9]=Flask and django\Django\Program 10"
set "FOLDERS[10]=Flask and django\Django\Program 11"
set "FOLDERS[11]=Flask and django\Django\Program 12"
set "FOLDERS[12]=Flask and django\Django\Program 13"
set "FOLDERS[13]=Flask and django\Django\Program 14"
set "FOLDERS[14]=Flask and django\Django\Program 15"

for /L %%i in (0,1,14) do (
    set "TARGET_FOLDER=!FOLDERS[%%i]!"
    set "FULL_PATH=%ROOT_DIR%!TARGET_FOLDER!"
    
    echo ----------------------------------------------------------------
    echo Processing: !TARGET_FOLDER!
    echo ----------------------------------------------------------------
    
    if not exist "!FULL_PATH!" (
        echo Directory does not exist, creating: !FULL_PATH!
        mkdir "!FULL_PATH!"
    )
    
    pushd "!FULL_PATH!"
    
    if not exist "venv\Scripts\python.exe" (
        echo [*] Creating virtual environment (venv)...
        python -m venv venv
    ) else (
        echo [*] Virtual environment already exists.
    )
    
    echo [*] Installing required packages...
    if exist "%REQ_FILE%" (
        ".\venv\Scripts\python.exe" -m pip install --upgrade pip >nul 2>&1
        ".\venv\Scripts\pip.exe" install -r "%REQ_FILE%"
    ) else (
        ".\venv\Scripts\pip.exe" install Flask Django Flask-WTF email-validator Flask-SQLAlchemy Flask-Migrate Flask-Mail Flask-HTTPAuth asgiref gunicorn python-dotenv sqlparse tzdata whitenoise
    )
    
    echo [DONE] Setup complete for !TARGET_FOLDER!
    echo.
    popd
)

echo ================================================================
echo    All 15 Program virtual environments are successfully setup!
echo ================================================================
echo.
pause
