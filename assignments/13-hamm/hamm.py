#!/usr/bin/env python3
"""
Author : jasongiles
Date   : 2019-04-15
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import logging
from itertools import zip_longest



# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Hamming Distance',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'FILE', metavar='FILE', help='File inputs', nargs=2)

    parser.add_argument(
        '-d', '--debug', help='logging file',action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def test_dist():
    """dist ok"""
    tests = [('foo', 'boo', 1), ('foo', 'faa', 2), ('foo', 'foobar', 3),
             ('TAGGGCAATCATCCGAG', 'ACCGTCAGTAATGCTAC',
              9), ('TAGGGCAATCATCCGG', 'ACCGTCAGTAATGCTAC', 10)]

    for s1, s2, n in tests:
        d = dist(s1, s2)
        print(s1)
        print(s2)
        assert d == n

def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


def dist(a,b):
    if type(a) is str:
        a = a.split()
    if type(b) is str:
        b = b.split()
    zipped = zip(a,b)
    #print(list((zipped)))
    i = 0
    for zip1, zip2 in zipped:
        if len(zip1)>len(zip2):
            longest = zip1
        else:
            longest = zip2
        j = 0
        for letter in range(len(longest)):
            #print(zip1[letter:letter+1],'ballz')
            if zip1[letter:letter+1] != zip2[letter:letter+1]:
                i+=1
                j+=1
                #print(zip1[letter:letter+1],'hello')
        logging.debug('s1 = {}, s2 = {}, d = {}'.format(zip1,zip2,j))
        #print('s1 = {}, s2 = {}, d = {}'.format(zip1,zip2,j))
    #print(i)
    return i




# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    giles = args.FILE
    debug = args.debug

    logging.basicConfig(
        filename='.log',
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL
    )

    for gile in giles:
        if not os.path.isfile(gile):
            die('"{}" is not a file'.format(gile))

    text1 = open(giles[0])
    text2 = open(giles[1])


    text1_list =[]
    text2_list = []

    for line in text1:
        text1_list = text1_list+line.split()
    #print(text1_list)
    for line in text2:
        text2_list = text2_list+line.split()
    #print(text2_list)

    #print(sum(map(dist,text1_list,text2_list)),'checker1')
    logging.debug('file1 = {}, file2 = {}'.format(giles[0], giles[1]))
    d = dist(text1_list,text2_list)
    print(d)





# --------------------------------------------------
if __name__ == '__main__':
    main()
