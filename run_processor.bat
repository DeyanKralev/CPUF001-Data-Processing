@echo off
REM ============================================================
REM Script Name : run_processor.bat
REM Purpose     : Executes the Data Processing Program
REM               from the Command Line Interface
REM ============================================================

echo.
echo ========================================
echo   Starting Data Processing Program
echo ========================================
echo.

REM Run the Python program and pass the data file as an argument
python data_processor.py sample_data.txt

echo.
echo ========================================
echo   Script execution finished
echo ========================================
echo.
pause