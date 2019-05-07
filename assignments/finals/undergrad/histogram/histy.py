#!/usr/bin/env python3
"""
Author : jasongiles
Date   : 2019-05-07
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
        'positional', metavar='int', help='integers to print', nargs='+')

    parser.add_argument(
        '-c',
        '--character',
        help='character',
        metavar='str',
        type=str,
        default='|')

    parser.add_argument(
        '-m',
        '--minimum',
        help='min value to print a number',
        metavar='int',
        type=int,
        default=1)

    parser.add_argument(
        '-s',
        '--scale',
        help='min value to print a number',
        metavar='int',
        type=int,
        default=1)

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
    char = args.character
    min_num = args.minimum
    scale = args.scale
    values = args.positional

    if len(values)<1:
        print('length of characters(positional arguments) must be greater than 1')
    value = sorted([int(i) for i in values])
    #print(value)


    for val in value:
        scaler = int(val)/scale
        #print(scaler)
        if int(val) >= min_num:
            print('{:>3} {}'.format(val,char*int(scaler)))






# --------------------------------------------------
if __name__ == '__main__':
    main()
