#! /usr/bin/python3
# findInCwd.py - search for occurrences of given regex in all text files of cwd

import os, sys, re

# if wrong use of script
if len(sys.argv) < 2:
    print('Usage: findInCwd.py <regex> - print all matches found')
    exit()
    
regex = re.compile(sys.argv[1])
for filename in os.listdir():
    if filename.endswith('.txt') or filename.endswith('.py'):
        #print(filename)
        file = open(filename, 'r')
        # search for a matchable obj
        mo = regex.search(file.read())
        if mo:
            print(mo.group() + ' in ' + filename)
        file.close()
