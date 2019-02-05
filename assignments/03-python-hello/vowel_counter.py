#!/usr/bin/env python3
"""
Author : jasongiles
Date   : 2019-02-04
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]
    i=0

    if len(args) != 1:
        print(f'Usage: {os.path.basename(sys.argv[0])} STRING')
        sys.exit(1)
    elif len(args)==1:
        word = args[0]
        for letter in word.lower():
            if letter in ['a','e','i','o','u']:
                i += 1
    if i == 1:
        print(f"There is {i} vowel in \"{(''.join(word))}.\"")
    else:
        print(f"There are {i} vowels in \"{(''.join(word))}.\"")





# --------------------------------------------------
main()
