@echo off
set /p ip=< data\settings\ip.server
set /p port=< data\settings\port.server
cd data\public_html
python -m http.server %port% --bind %ip%
python ..\menu.py