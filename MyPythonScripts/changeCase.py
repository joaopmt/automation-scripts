#! /usr/bin/python3
# changeCase.py - change text content in clipboard to lowercase or uppercase

import sys, pyperclip

# if user runs this script without any argument
if len(sys.argv) < 2:
    print('Usage: changeCase.py [low] - change text in clipboard to lowercase')
    print('       changeCase.py [up]  - change text in clipboard to uppercase')
    exit()
    
text = pyperclip.paste()
if sys.argv[1] == 'low':
    pyperclip.copy(text.lower())
    print('Text content in clipboard changed to lowercase.')
if sys.argv[1] == 'up':
    pyperclip.copy(text.upper())
    print('Text content in clipboard changed to uppercase.')
