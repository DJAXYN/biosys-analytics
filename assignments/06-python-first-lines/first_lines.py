#!/usr/bin/env python3
"""
Author : jasongiles
Date   : 2019-02-23
Purpose: Rock the Casbah
"""

import argparse
import sys
import os


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='Dir', nargs='+', help='Directory now')

    parser.add_argument(
        '-w',
        '--width',
        help='A named string argument',
        metavar='int',
        type=int,
        default=55)

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
    line_length = args.width
    dirs = args.positional

    if len(dirs) < 1:
        die()
    '''
    for dir in dirs:
        if not os.path.isdir(dir):
            warn('"{}" is not a directory'.format(dir))
'''

    dick_list = {}
    for dir in dirs:
        if not os.path.isdir(dir):
            warn('"{}" is not a directory'.format(dir))
            continue
        else:
            print(dir)
            for file in os.listdir(dir):
                #print(file)
                fh = open(os.path.join(dir,file),'r')
                first_line = fh.readline().strip()
                #print(first_line)
                dick_list[file] = first_line
                sort_dict_list = sorted([(line[1],line[0]) for line in dick_list.items()])
            #print(sort_dict_list)
            for key,value in sort_dict_list:
                #print(len(key))
                dots_add = line_length +5 - len(key) - len(value)
                #print(dots_add)
                dots = '.'*dots_add
                print('{} {} {}'.format(key,dots,value))







# --------------------------------------------------
if __name__ == '__main__':
    main()
