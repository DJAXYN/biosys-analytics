#!/usr/bin/env python3
"""
Author : jasongiles
Date   : 2019-02-11
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    file_info = sys.argv[1:]
    i = 0
    head_count = 3
    if len(file_info) < 1:
        print('Usage: {} FILE [HEAD]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    file = file_info[0]
    if not os.path.isfile(file):
        print('{} is not a file'.format(file))
        sys.exit(1)

    if len(file_info[1:]) < 1:
        head_count = 3
    else:
        head_count = file_info[1]
        if int(head_count) <= 1:
            print('lines ({}) must be a positive number'.format(head_count))
            sys.exit(2)

    for line in open(file).read().splitlines():
        i += 1
        print(line)
        if i==int(head_count):
            break

    #head = file_info[1] if not None else int(10)
    #print(head)



# --------------------------------------------------
main()
