@echo off
echo ========================================
echo   Hackathon Idea Generator
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo.

REM Install requirements if needed
if not exist "venv\Lib\site-packages\streamlit\" (
    echo Installing requirements...
    pip install -r requirements.txt
    echo.
)

REM Check for .env file
if not exist ".env" (
    echo WARNING: .env file not found!
    echo Please create .env file with your OpenAI API key
    echo You can copy .env.example to .env and add your key
    echo.
    pause
    exit /b
)

REM Run the Streamlit app
echo Starting Hackathon Idea Generator...
echo The app will open in your browser at http://localhost:8501
echo.
echo Press Ctrl+C to stop the server
echo.
streamlit run app.py

pause
