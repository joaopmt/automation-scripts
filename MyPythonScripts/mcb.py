#! /usr/bin/python3
# mcb.py - MultiClipboard: saves text to a file and loads
# desirable text from the file to clipboard
# Usage: mcb.py save <keyword> - Saves clipboard content under given keyword.
#        mcb.py load <keyword> - Loads content under <keyword> to clipboard.
#        mcb.py del <keyword> - Deletes entry from the shelf
#        mcb.py list - Loads all content to clipboard.

import sys, pyperclip, shelve

mcbShelf = shelve.open('mcb')

# saves clipboard content to mcb file in given keyword
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()

# load content in given keyword to the clipboard
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'load':
    if sys.argv[2] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[2]])
    else:
        print('\'' + sys.argv[2] + '\''+ ' content is null.')

# del given keyword and its content from shelf
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'del':
    del mcbShelf[sys.argv[2]] 

# list all saved keywords and its contents
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'list':
    for k, v in mcbShelf.items():
        print(k + ': ' + v + '\n')

# if user used invalid args
else:
    print('Usage: mcb.py save <keyword> - Saves clipboard content under given keyword.')
    print('       mcb.py load <keyword> - Loads content under <keyword> to clipboard.')
    print('       mcb.py del <keyword> - Deletes entry from the shelf')
    print('       mcb.py list - Loads all content to clipboard.')
    
mcbShelf.close()
