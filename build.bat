@echo off
pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple send2trash
pip install pyinstaller
pyinstaller --onefile main.py
pause
