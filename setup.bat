@echo off
setlocal

rem Check if venv directory exists, and create it if it doesn't
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

rem Activate the virtual environment
call venv\Scripts\activate.bat

rem Install the requirements
echo Installing requirements...
pip install -r requirements.txt

echo Setup complete!
