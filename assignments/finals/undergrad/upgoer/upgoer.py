#!/usr/bin/env python3
"""
Author : jasongiles
Date   : 2019-05-07
Purpose: Rock the Casbah
"""

import argparse
import sys
import re
import os



# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'FILE', metavar='FILE', type=str,
        help='file to check the number for top 1000 words')

    parser.add_argument(
        '-w',
        '--wordlist',
        help='list for top 100 words',
        metavar='str',
        type=str,
        default='1000.txt')

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
def word_ls_maker(file):
    ls = []
    for line in file:
        for word in line.split():
            matcher = re.sub("[^a-zA-Z0-9']", '', word.lower())
            if matcher:
                ls.append(matcher)

    return ls
# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    compare_file = args.FILE
    word_lsfile = args.wordlist

    for file in [compare_file,word_lsfile]:
        if not os.path.isfile(file):
            die('"{}" is not a file'.format(file))

    dictionar_fh = open(word_lsfile,'rt')
    compare_fh = open(compare_file,'rt')

    topword_list = word_ls_maker(dictionar_fh)
    compare_fh_ls = word_ls_maker(compare_fh)

    i = 0
    for word in compare_fh_ls:
        if word not in topword_list:
            i +=1
            print('{:3}: {}'.format(i,word),file=sys.stderr)
    print('{} {} to change.'.format(i,'words' if i>1 else 'word'))



# --------------------------------------------------
if __name__ == '__main__':
    main()
