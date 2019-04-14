#! /bin/usr/python3
# Open google map with location from command line or clipboard

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    #Get address from command line
    address = ' '.join(sys.argv[1:])

    #Get address from clipboard
else:
    address = pyperclip.paste()

webbrowser.open('http://google.com/maps/place/' + address)
