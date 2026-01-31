@echo off
REM Platter Compiler Webapp - Start Script (Frontend Only)
REM Runs the development server with Pyodide-based Python analysis

echo.
echo Starting Platter Compiler Webapp (Frontend)
echo ============================================
echo.
echo Running frontend dev server on http://localhost:5173
echo Python analysis runs in-browser via Pyodide
echo No backend server needed!
echo.

REM Get the directory where this batch file is located
set PROJECT_ROOT=%~dp0

REM Check if platter-compiler-sveltejs directory exists
if not exist "%PROJECT_ROOT%platter-compiler-sveltejs" (
    echo Application directory not found: %PROJECT_ROOT%platter-compiler-sveltejs
    echo Please make sure you're in the project root directory.
    pause
    exit /b 1
)

REM Change to platter-compiler-sveltejs directory and start dev server
cd /d "%PROJECT_ROOT%platter-compiler-sveltejs"

REM Check if node_modules exists, if not run npm install
if not exist "node_modules" (
    echo Installing dependencies...
    call npm install
    echo.
)

echo Starting development server...
echo.
call npm run dev

echo.
echo Press any key to exit...
pause > nul