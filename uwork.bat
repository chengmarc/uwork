@echo off
python --version
echo Starting virtual environment setup.
echo.
python -m venv __venv__
call __venv__\Scripts\activate.bat
pip install dependencies\dist\uwork-dependencies-1.0.tar.gz
echo.
echo Virtual environment setup completed.
call core-process\uwork_gui.py