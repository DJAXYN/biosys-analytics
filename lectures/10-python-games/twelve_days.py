#!/usr/bin/env python3
"""
Author : jasongiles
Date   : 2019-03-24
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
        '-o',
        '--outfile',
        help='outfile (STDOUT)',
        metavar='str',
        type=str,
        default='')

    parser.add_argument(
        '-n',
        '--number_days',
        help='nubmer of days to sing',
        metavar='int',
        type=int,
        default=12)


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
    outfile = args.outfile
    num_days = args.number_days

    out_fh = open(outfile, 'wt') if outfile else sys.stdout

    days = {
    12: 'Twelve drummers drumming',
    11: 'Eleven pipers piping',
    10: 'Ten lords a leaping',
    9: 'Nine ladies dancing',
    8: 'Eight maids a milking',
    7: 'Seven swans a swimming',
    6: 'Six geese a laying',
    5: 'Five gold rings',
    4: 'Four calling birds',
    3: 'Three French hens',
    2: 'Two turtle doves',
    1: 'a partridge in a pear tree',
    }

    cardinal = {
        12: 'twelfth',
        11: 'eleven',
        10: 'tenth',
        9: 'ninth',
        8: 'eighth',
        7: 'seventh',
        6: 'sixth',
        5: 'fifth',
        4: 'fourth',
        3: 'third',
        2: 'second',
        1: 'first',
    }

    if num_days not in days:
        die(f'cannot wign about {num_days} as this is greater that song days')

    def ucfirst(s):
        return s[0].upper() +s[1:]

    for i in range(1,num_days +1):
        first = 'On the {} day of Christmas,\nMy true love gave to me,'
        out_fh.write(first.format(cardinal[i])+'\n')
        for j in reversed(range(1,i+1)):
            if j==1:
                if i==1:
                    out_fh.write('{}.\n'.format(ucfirst(days[j])))
                else:
                    out_fh.write('and {}.\n'.format(days[j]))
            else:
                out_fh.write('{},\n'.format(days[j]))

        if i < max(days.keys()):
            out_fh.write('\n')


# --------------------------------------------------
if __name__ == '__main__':
    main()
