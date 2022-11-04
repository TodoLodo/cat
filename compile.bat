pyinstaller -F src/cat.py -n cat --icon=ico/cat.ico --clean --distpath ./bin
rmdir /s /q build
del cat.spec cat_setup.spec
pause