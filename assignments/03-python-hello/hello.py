#!/usr/bin/env python3
"""
Author : jasongiles
Date   : 2019-01-31
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    names = sys.argv[1:]

    if len(names) == 0:
        print('Usage: {} NAME [NAME...]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    if len(names) == 1:
        print(f'Hello to the 1 of you: {names[0]}!')
        #print('name is "{}"'.format(names))
    elif len(names) == 2:
        print(f'Hello to the 2 of you: {" and ".join(names)}!')
    elif len(names) > 2:
        names[-1] = "and " + names[-1]
        print(f'Hello to the {len(names)} of you: {", ".join(names)}!')




# --------------------------------------------------
main()
