# Release instructions

First comment out pyfiglet!

To generate .exe executable run this in ./src folder:

pyinstaller --onefile --hidden-import pyfiglet.fonts main.py

The result file also want /template folder!