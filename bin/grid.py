#!/usr/bin/env python3
"""
Author : jasongiles
Date   : 2019-02-05
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    num = sys.argv[1:]
    numbers_list= [2, 3, 4, 5, 6, 7, 8, 9]

    if len(num) != 1:
        print('Usage: {} [NUMBER...(2-9)]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)
    if len(num) == 1:
        number = int(num[0])
        if num not in numbers_list:
            print(f'NUM {number} must be between 1 and 9')
            sys.exit(2)
        else:
            for i in range(1, number ** 2 + 1):
                print('{:3}'.format(i) if i % number != 0 else '{:3}\n'.format(i), end='')




# --------------------------------------------------
main()
