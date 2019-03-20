#! /usr/bin/python3
# mapIt.py - open Google Maps using an address from the
# command line or clipboard.

import webbrowser, sys, pyperclip

# if command line args have been provided
if len(sys.argv) > 1:
    # join all args in one string, separated by ' '
    adress = ' '.join(sys.argv[1:])
else:
    adress = pyperclip.paste()

webbrowser.open('https://www.google.com.br/maps/place/' + adress)
