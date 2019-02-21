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
    vowels = sys.argv[1:]
    i=0

    if len(vowels) != 1:
        print(f'Usage: {os.path.basename(sys.argv[0])} STRING')
        sys.exit(1)
    elif len(vowels)==1:
        for vowel in str(vowels):
            if vowel == 'a' or vowel == "e" or vowel == "i" or vowel == "u":
                i += 1
    if i == 1:
        print(f"There is {i} vowel in \"{(''.join(vowels))}.\"")
    else:
        print(f"There are {i} vowel in \"{(''.join(vowels))}.\"")





# --------------------------------------------------
main()
