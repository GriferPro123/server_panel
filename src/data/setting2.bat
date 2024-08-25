@echo off
echo Enter server port
set /p port=
echo %port%> data\settings\port.server
python menu.py