pyinstaller -F scripts/cat.py -n cat --icon=ico/cat.ico --clean --distpath ./bin
pyinstaller -F scripts/cat_setup.py -n cat_setup --icon=ico/cat.ico -w --uac-admin --clean --distpath ./
rmdir /s /q build
del cat.spec cat_setup.spec
pause