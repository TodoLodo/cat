pyinstaller -F scripts/cat.py -n cat --clean --distpath ./bin
rmdir /s /q build
pause