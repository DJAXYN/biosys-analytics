#!/usr/bin/env python3
"""
Author : jasongiles
Date   : 2019-04-01
Purpose: Rock the Casbah
"""

import os
import sys
import re


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} DATE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    date_fh = args[0]

    date_match1 = re.compile('(\d{4})'  # capture year (group 1)
                             '[-]?'  # separator
                             '(\d{1,2})'  # capture month (group 2)
                             '[-]?'  # separator
                             '(\d{1,2})?')  # capture day (group 3)

    date_match2 = re.compile('(\d{1,2})'  # capture year (group 1)
                             '[/]'  # separator
                             '(\d{1,2})'  # capture month (group 2)
                             '[/]?'  # separator
                             '(\d{1,2})?')  # capture day (group 3)


    # 4 is seperate

    date_match4 = re.compile('([a-zA-Z]{1,10})'  # capture year (group 1)
                             '[/,-]?'  # separator
                             '\s*?'
                             '(\d{2,4})')  # capture year (group 2))

    months2 = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
    dates = date_fh
    match1 = date_match1.search(dates)
    notany = False
    if match1:
        notany = True
        checkday = match1.group(3)
        if checkday !=None and len(checkday)<2:
            checkday = str(0)+str(checkday)
        formater1= '{}-{}-{}'.format(match1.group(1),match1.group(2) if len(match1.group(2))>1 else str(0)+match1.group(2),'01' if match1.group(3)==None else checkday)
        print(formater1)

    match2 = date_match2.match(dates)

    if match2:
        notany = True
        formater2 = '{}-{}-{}'.format(match2.group(2) if len(match2.group(2)) == 4 else str(20) + match2.group(2),
                                          match2.group(1) if len(match2.group(1)) == 2 else str(0) + match2.group(1),
                                          '01' if match2.group(3) == None else match2.group(3))
        print(formater2)

    match4 = date_match4.search(dates)

    if match4:
        notany = True
        numb = match4.group(1).lower()
        if numb[:3] in months2:
            monthday = months2.index(numb[:3]) + 1
            formater4= '{}-{}-{}'.format(match4.group(2),str(0)+str(monthday) if monthday<10 else monthday,'01')
            print(formater4)
    if not notany:
        print('No match')

# --------------------------------------------------
main()
