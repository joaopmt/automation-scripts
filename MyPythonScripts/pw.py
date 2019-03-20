#! /usr/bin/python3
# pw.py - An insecure password manager program.

PASSWORDS = {}

import sys, pyperclip

'''
The first item in the sys.argv list should always be a string containing
the program’s filename ('pw.py'), and THE SECOND ITEM WILL BE THE FIRST
COMMAND LINE ARGUMENT (sys.argv[1]). For this program, this argument is the name of the
account whose password you want. Since the command line argument is mandatory,
you display a usage message to the user if they forget to add it
(that is, if the sys.argv list has fewer than two values in it)
'''
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - displays account password')
    sys.exit()

account = sys.argv[1]  # sys.argv[1] == first command line argument
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' coppied to clipboard.')
else:
    print('There is no account named ' + account + '!')
