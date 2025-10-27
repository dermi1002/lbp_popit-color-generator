@echo on

:: Confirmation of Internet Connection
SETLOCAL EnableDelayedExpansion
CHOICE /M "This script requires connection to the Internet. Continue?" 
if ERRORLEVEL 1 goto autoSetup
if ERRORLEVEL 2 goto eof

:autoSetup
echo Creating Virtual Environment...
python -m venv .venv_windows
echo Updating Pip, Setuptools, Wheel...
:: Calling python from the virtual environment eliminates the need to activate the virtual environment itself
.venv_windows\Scripts\python.exe -m pip install --upgrade pip --upgrade setuptools --upgrade wheel
echo Installing Requirements...
.venv_windows\Scripts\python.exe -m pip install -r src\requirements.txt

set PCGSCRIPT=lbp_pcg.bat

if exist %PCGSCRIPT% (
	CHOICE /M "A script named 'lbp_pcg.bat' already exists. Overwrite all data within it?"
	if ERRORLEVEL 1 goto writeScript
	if ERRORLEVEL 2 goto setupComplete
) else goto:writeScript

:writeScript
echo @echo off > %PCGSCRIPT%
echo start .venv_windows\Scripts\pythonw.exe src\main.py >> %PCGSCRIPT%

:setupComplete
CHOICE /M "Setup successfully completed! Would you like to run the Main Script?"
if ERRORLEVEL 1 goto startMain
if ERRORLEVEL 2 goto eof

:startMain
.venv_windows\Scripts\python.exe src\main.py

:eof
pause

ENDLOCAL
