#!/usr/bin/env python3
"""
Author : jasongiles
Date   : 2019-04-29
Purpose: Rock the Casbah
"""

import argparse
import sys
import logging
import os
from tabulate import tabulate
import io
import re
from itertools import product


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'files', metavar='FILE', type=argparse.FileType('r', encoding='UTF-8'),
        help='The files for countering the Number of Words',
        nargs=2)

    parser.add_argument(
        '-m',
        '--min_len',
        help='shortest word lenght to compare',
        metavar='int',
        type=int,
        default=0)

    parser.add_argument(
        '-n',
        '--hamming_distance',
        help='hamming distance allowed',
        metavar='int',
        type=int,
        default=0)

    parser.add_argument(
        '-l',
        '--logfile',
        help='log file ',
        metavar='str',
        type=str,
        default='.log')

    parser.add_argument(
        '-d', '--debug', help='Turn on debugging', action='store_true', default=False)

    parser.add_argument(
        '-t', '--table', help='table format for log file', action='store_true', default=False)

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
# hamming distance between two list of words
def dist(s1, s2):
    d = abs((len(s1)) - len(s2))
    dif = 0
    for a, b in zip(s1, s2):
        if a != b:
            dif += 1
        logging.debug("s1 = {}, s2 = {}, d = {}".format(a, b, dif))
    tot = d + dif
    return tot


# --------------------------------------------------
def test_dist():
    """dist ok"""

    tests = [('foo', 'boo', 1), ('foo', 'faa', 2), ('foo', 'foobar', 3),
             ('TAGGGCAATCATCCGAG', 'ACCGTCAGTAATGCTAC',
              9), ('TAGGGCAATCATCCGG', 'ACCGTCAGTAATGCTAC', 10)]

    for s1, s2, n in tests:
        d = dist(s1, s2)
        assert d == n


# --------------------------------------------------

def uniq_words(file, min_len):
    wordset = set()
    '''
    for line in file:
        for word in line.split():
            matcher = re.sub('[^a-zA-Z0-9]', '', word.lower())
            if len(matcher)>=min_len:
                wordset.add(matcher)
    '''
    for word in file.read().split():
        matcher = re.sub('[^a-zA-Z0-9]', '', word.lower())
        if len(matcher) >= min_len:
            wordset.add(matcher)
    return wordset


def test_uniq_words():
    """Test uniq_words"""

    s1 = '?foo, "bar", FOO: $fa,'
    s2 = '%Apple.; -Pear. ;bANAna!!!'

    assert uniq_words(io.StringIO(s1), 0) == set(['foo', 'bar', 'fa'])

    assert uniq_words(io.StringIO(s1), 3) == set(['foo', 'bar'])

    assert uniq_words(io.StringIO(s2), 0) == set(['apple', 'pear', 'banana'])

    assert uniq_words(io.StringIO(s2), 4) == set(['apple', 'pear', 'banana'])

    assert uniq_words(io.StringIO(s2), 5) == set(['apple', 'banana'])


# --------------------------------------------------
def common(words1, words2, distance):
    commonlist = list()
    wordprod = sorted(product(words1, words2))
    for w1, w2 in wordprod:
        td = dist(w1, w2)
        if td <= distance:
            commonlist.append((w1, w2, td))
    return commonlist


# --------------------------------------------------

def test_common():
    w1 = ['foo', 'bar', 'quux']
    w2 = ['bar', 'baz', 'faa']

    assert common(w1, w2, 0) == [('bar', 'bar', 0)]

    assert common(w1, w2, 1) == [('bar', 'bar', 0), ('bar', 'baz', 1)]

    assert common(w1, w2, 2) == [('bar', 'bar', 0), ('bar', 'baz', 1),
                                 ('bar', 'faa', 2), ('foo', 'faa', 2)]


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    fh1, fh2 = args.files
    min_word_compare = args.min_len
    hamming = args.hamming_distance
    log_file = args.logfile
    debug = args.debug
    tableau = args.table

    logging.basicConfig(
        filename=log_file,
        filemode="w",
        level=logging.DEBUG if args.debug else logging.CRITICAL, )

    logging.debug('file1 = {}, files2 = {}'.format(fh1, fh2))

    if hamming < 0:
        die('--distance "{}" must be > 0'.format(hamming))

    # read.split

    words1 = uniq_words(fh1, min_word_compare)
    words2 = uniq_words(fh2, min_word_compare)
    common_words = common(words1, words2, hamming)

    if len(common_words) < 1:
        print('No words in common.')
    else:
        if tableau:
            print(tabulate(common_words, headers=['word1', 'word2', 'distance'], tablefmt='psql'))
        else:
            print('word1\tword2\tdistance')
            for w1, w2, dis in common_words:
                print(f'{w1}\t{w2}\t{dis}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
