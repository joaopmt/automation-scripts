#! /usr/bin/python3
# renameDates.py - rename filenames in cwd with US MM-DD-YYYY
# date format to EU DD-MM-YYYY.

import shutil, os, re

# create regex for US MM-DD-YYYY or MM/DD/YYYY pattern
usDatePattern = re.compile(r"""^(.*?)  # all possible text before the date
    ((0|1)?\d)                         # one or two digits for the month (e.g.: 01, 11 or 1)
    (-|\\)                             # separator
    ((0|1|2|3)?\d)                     # one or two digits for the day (e.g.: 01, 11, 21, 31 or 1)
    (-|\\)                             # separator
    ((1|2)\d\d\d)                      # 1YYY to 2YYY for the year
    (.*?)$                             # all possible text after the date
    """, re.VERBOSE)                   # VERBOSE allow comments and whitespaces

# loop over the files in the cwd
for usFilename in os.listdir('.'):
    mo = usDatePattern.search(usFilename)
    
    if not mo:
        continue

    # get the different parts of the mo
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    separator1 = mo.group(4)
    dayPart    = mo.group(5)
    separator2 = mo.group(7)
    yearPart   = mo.group(8)
    afterPart  = mo.group(10)
    # ***OBS***
    # (each  '(' and ')' defines a group):
    #    datePattern = re.compile(r"""^(1) all text before the date
    #    (2 (3) )-                         one or two digits for the month
    #    (4)                               separator1
    #    (5 (6) )-                         one or two digits for the day
    #    (7)                               separator2
    #    (8 (9) )                          four digits for the year
    #    (10)$                             all text after the date
    #    """, re.VERBOSE)
    # ***OBS***

    euFilename = beforePart + dayPart + separator1 + monthPart + separator2 + yearPart + afterPart
    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    usFilename = os.path.join(absWorkingDir, usFilename)
    euFilename = os.path.join(absWorkingDir, euFilename)

    # Rename the files.
    print('Renaming "%s" to "%s"...' % (usFilename, euFilename))
    #shutil.move(amerFilename, euroFilename)   # uncomment after testing
