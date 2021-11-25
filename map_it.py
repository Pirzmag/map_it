import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    adress = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + adress)