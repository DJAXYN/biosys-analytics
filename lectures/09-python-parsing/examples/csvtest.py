#!/usr/bin/env python3
"""
Author : jasongiles
Date   : 2019-02-21
Purpose: Rock the Casbah
"""

import os
import sys
import csv

# dict reader takes comma seperated file


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} ARG'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    arg = args[0]


    print('Arg is "{}"'.format(arg))
    with open(arg) as csvfile:
        reader = csv.DictReader( csvfile, delimiter = '\t')
        for row in reader:
            print(row)


# --------------------------------------------------
main()
