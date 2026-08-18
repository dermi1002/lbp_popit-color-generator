@echo on
setlocal EnableDelayedExpansion

rem Confirmation of Internet Connection
choice /m "This script requires connection to the Internet. Continue?"
if ERRORLEVEL 2 goto:setupAborted
if ERRORLEVEL 1 goto:checkVirtualEnv

:checkVirtualEnv
set VIRTUALENV=.venv_windows\

if exist %VIRTUALENV% (
	choice /m "A folder named '.venv_windows' already exists. Overwrite all data within it?"
	if ERRORLEVEL 2 goto:createMainScript
	if ERRORLEVEL 1 goto:deleteVirtualEnv
) else goto:createVirtualEnv

:deleteVirtualEnv
echo Removing Virtual Environment...
rd /s /q %VIRTUALENV%
goto:createVirtualEnv

:createVirtualEnv
echo Creating Virtual Environment...
python -m venv .venv_windows
echo Updating Pip...
.venv_windows\Scripts\python.exe -m pip install --upgrade pip
echo Installing Requirements...
.venv_windows\Scripts\python.exe -m pip install -r src\requirements.txt
goto:createMainScript

:createMainScript
set PCGSCRIPT=lbp_pcg.bat

if exist %PCGSCRIPT% (
	choice /m "A script named 'lbp_pcg.bat' already exists. Overwrite all data within it?"
	if ERRORLEVEL 2 goto:setupComplete
	if ERRORLEVEL 1 goto:writeScript
) else goto:writeScript

:writeScript
echo @echo off> %PCGSCRIPT%

echo.>> %PCGSCRIPT%
echo set virtualEnvironment=.venv_windows\>> %PCGSCRIPT%

echo.>> %PCGSCRIPT%
echo if not exist %%virtualEnvironment%% goto:errorMessage>> %PCGSCRIPT%

echo.>> %PCGSCRIPT%
echo goto:startMainScript>> %PCGSCRIPT%

echo.>> %PCGSCRIPT%
echo :errorMessage>> %PCGSCRIPT%
echo set msgboxTitle=Virtual Environment Missing>> %PCGSCRIPT%
echo set msgboxBody=The Virtual Environment folder '.venv_windows' doesn't exist. Run the Setup script or make the Virtual Environment yourself.>> %PCGSCRIPT%

echo.>> %PCGSCRIPT%
echo set temporaryMsgbox=%%temp%%\~lbp-pcg_venv-error.vbs>> %PCGSCRIPT%
echo echo msgbox "%%msgboxBody%%",0,"%%msgboxTitle%%"^>"%%temporaryMsgbox%%">> %PCGSCRIPT%
echo WSCRIPT "%%temporaryMsgbox%%">> %PCGSCRIPT%
echo if exist %%temporaryMsgbox%% del /F /Q "%%temporaryMsgbox%%">> %PCGSCRIPT%

echo.>> %PCGSCRIPT%
echo exit>> %PCGSCRIPT%

echo.>> %PCGSCRIPT%
echo :startMainScript>> %PCGSCRIPT%
echo start .venv_windows\Scripts\pythonw.exe src\main.py>> %PCGSCRIPT%

rem It's ugly, I know...

:setupComplete
choice /m "Setup successfully completed^! Would you like to run the Main Script?"
if ERRORLEVEL 2 goto:endOfFile
if ERRORLEVEL 1 goto:startMain

:startMain
.venv_windows\Scripts\python.exe src\main.py
goto:endOfFile

:setupAborted
echo Setup Aborted.
goto:endOfFile

:endOfFile
pause

ENDLOCAL
