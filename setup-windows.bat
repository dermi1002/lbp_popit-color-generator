@echo on

:: THIS IS AN UNTESTED APPROXIMATION. USE AT YOUR OWN RISK.

:: Confirmation of Internet Connection
SETLOCAL EnableDelayedExpansion
CHOICE /M "This script requires connection to the Internet. Continue?" 
goto sub_%ERRORLEVEL%

:sub_2
exit
goto:eof

:sub_1
ECHO Creating Virtual Environment...
python -m venv .venv_windows
ECHO Activating Virtual Environment...
.venv_windows\Scripts\Activate
ECHO Updating Pip, Setuptools, Wheel...
python -m pip install --upgrade pip --upgrade setuptools --upgrade wheel
ECHO Installing Requirements...
pip install -r src\requirements.txt

ENDLOCAL
