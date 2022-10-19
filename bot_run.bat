@echo off

call %~dp0venv\Scripts\activate

set TOKEN=5721543457:AAHWQannTuyFu_fCEkRep6cnjvZuN-cUcto
set LOGIN=login
set PASSWORD=password
python bot_telegram.py

pause