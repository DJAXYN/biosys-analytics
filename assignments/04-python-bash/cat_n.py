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
    args = sys.argv[1:]
    i=0

    if len(args) != 1:
        print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    file = args[0]
    if not os.path.isfile(file):
        print('{} is not a file'.format(file))
        sys.exit(1)

    for line in open(file).read().splitlines():
        i += 1
        print('{:4}: {}'.format(i,line))


# --------------------------------------------------
main()
