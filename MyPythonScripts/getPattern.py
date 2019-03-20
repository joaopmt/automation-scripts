#! /usr/bin/python3
# getPattern.py - Uses regex to find phone numbers and emails in clipboard text

import re, pyperclip

# defines regex for phone numbers matching
phoneRegex = re.compile(r'''((        # for US phone format
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )|(                               # OR: for BR phone format
    (\s\d{10})|(                      # *gambiarra* to get 1938443031 alikes
    ((\d\d)|\(\d\d\))?                # area code (DDD)
    (\s|-|\.)?                        # separator
    (\d{4})                           # first 4 digits
    (\s|-|\.|\s-\s)?                  # separator
    (\d{4}))                          # last 4 digits
    ))''', re.VERBOSE)                # VERBOSE allow comments and whitespaces

# defines regex for emails matching
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
    )''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []  # list of matched strings
for groups in phoneRegex.findall(text):
    matches.append(groups[0])
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
