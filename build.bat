@echo off
pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple send2trash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
pause
