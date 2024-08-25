@echo off
echo Enter server ip
set /p ip=
echo %ip%> data\settings\ip.server
python menu.py