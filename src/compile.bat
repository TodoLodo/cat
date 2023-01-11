pyinstaller -F cat.py -n cat --icon=cat.ico --clean --distpath ../bin
pyinstaller --uac-admin -F catToPath.py -n catToPath --icon=cat.ico --clean --distpath ../
rmdir /s /q build
del cat.spec catToPath.spec
pause