call ".venv\Scripts\activate.bat"
cd /d "%~dp0"
set FLASK_APP=Backend.py
set FLASK_ENV=development
py -m flask run --host=0.0.0.0
pause