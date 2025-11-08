@echo off
echo.
echo 🍽️  Starting Platter Compiler Webapp...
echo =======================================
echo.

set "PROJECT_ROOT=%~dp0"
set "BACKEND_DIR=%PROJECT_ROOT%backend"
set "FRONTEND_DIR=%PROJECT_ROOT%frontend"

if not exist "%BACKEND_DIR%" (
    echo ❌ Backend not found: %BACKEND_DIR%
    pause
    exit /b 1
)
if not exist "%FRONTEND_DIR%" (
    echo ❌ Frontend not found: %FRONTEND_DIR%
    pause
    exit /b 1
)

echo 🚀 Launching backend and frontend...
echo.

REM ---- Backend ----
cd /d "%BACKEND_DIR%"
start "Backend" cmd /k "call .\.venv\Scripts\activate && uvicorn main:app --reload --host 127.0.0.1 --port 8000"

REM ---- Frontend ----
cd /d "%FRONTEND_DIR%"
start "Frontend" cmd /k "npm run dev -- --host"

echo.
echo ✅ Backend:  http://127.0.0.1:8000
echo ✅ Frontend: http://localhost:5173
echo.
pause
