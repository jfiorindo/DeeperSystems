@echo off
echo ============================
echo 🚀 Starting the project...
echo ============================

REM 
echo Activating backend environment...
cd backend
call venv\Scripts\activate

REM 
echo Importing user data into MongoDB...
python parser.py

REM 
echo Starting Flask backend...
start cmd /k "python app.py"

cd ..

REM Start frontend (Vue)
echo 💻 Starting Vue frontend...
cd frontend
start cmd /k "npm run dev"

cd ..

echo ============================
echo - Project started successfully!
echo - Backend: http://localhost:5000/users
echo - Frontend: http://localhost:5173
echo ============================

pause
