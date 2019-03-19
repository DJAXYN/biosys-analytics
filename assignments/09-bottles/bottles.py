#!/usr/bin/env python3
"""
Author : jasongiles
Date   : 2019-03-18
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument(
        '-n',
        '--num_bottles',
        help='Number of bottles you want to count',
        metavar='int',
        type=int,
        default=10)


    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    bottles = args.num_bottles

    if bottles < 1:
        die("N {} must be a positive integer".format(bottles))

    for bottles in range(bottles,0, -1):
        if bottles > 2:
            print('{} bottles of beer on the wall,\n'
                  '{} bottles of beer,\n'
                  'Take one down, pass it around,\n'
                  '{} bottles of beer on the wall!\n'.format(bottles,bottles,(bottles-1)))
        elif bottles==2:
            print(
                '{} bottles of beer on the wall,\n'
                '{} bottles of beer,\n'
                'Take one down, pass it around,\n'
                '{} bottle of beer on the wall!\n'.format(bottles, bottles, (bottles - 1)))
        else:
            print('{} bottle of beer on the wall,\n'
                  '{} bottle of beer,\n'
                  'Take one down, pass it around,\n'
                  '{} bottles of beer on the wall!'.format(bottles,bottles,(bottles-1)))





# --------------------------------------------------
if __name__ == '__main__':
    main()
