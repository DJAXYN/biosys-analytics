#!/usr/bin/env python3
"""
Author : jasongiles
Date   : 2019-04-23
Purpose: Rock the Casbah
"""

import argparse
import sys
import re
import os
from collections import Counter


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'files', metavar='FILE', type=argparse.FileType('r', encoding='UTF-8'),
        help='The files for countering the Number of Words',
        nargs='+')

    parser.add_argument(
        '-s',
        '--sort',
        help='Whether you want it sorded by "word" or "frequency"',
        metavar='str',
        type=str,
        choices=['word', 'frequency'],
        default='word')

    parser.add_argument(
        '-m',
        '--min',
        help='The minimum lenght of the word to which to list',
        metavar='int',
        type=int,
        default=0)

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
    min_len = args.min
    giles = args.files
    sorting = args.sort

    dic_freq = Counter()

    for file in giles:
        for line in file:
            for word in line.split():
                matcher = re.sub('[^a-zA-Z0-9]', '', word.lower())
                if matcher:
                    dic_freq[matcher] += 1
                    # dic_freq.update(matcher)
    # print(dic_freq)

    if sorting == 'frequency':
        for count, word in sorted(map(lambda t: list(reversed(t)), dic_freq.items())):
            if count >= min_len:
                print('{:20} {}'.format(word, count))
    else:
        for word, count in sorted(dic_freq.items()):
            if count >= min_len:
                print('{:20} {}'.format(word, count))


# --------------------------------------------------
if __name__ == '__main__':
    main()
