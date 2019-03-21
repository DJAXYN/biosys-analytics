#!/usr/bin/env python3
"""
Author : jasongiles
Date   : 2019-03-18
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
from Bio import SwissProt
from Bio.SwissProt import KeyWList






# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Filter Swissprot file for keywords, taxa',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'FILE', metavar='str', help='Uniprot File')

    parser.add_argument(
        '-k',
        '--keyword',
        help='argument of the keyword to match in the "keyword" field of the input record in order to determine which sequences to "take"',
        metavar='str',
        type=str,
        required=True,
        default=None)

    parser.add_argument(
        '-s',
        '--skip',
        help='Skip taxa',
        metavar='str',
        nargs='+',
        type=str,
        default='')
    parser.add_argument(
        '-o',
        '--output',
        help='output file',
        metavar='FILE',
        type=str,
        default='out.fa')

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
    in_fh = args.FILE
    keywords = args.keyword
    skips = args.skip
    out_fh = args.output

    if not os.path.isfile(in_fh):
        die('"{}" is not a file'.format(in_fh))

    #print(keywords)
    keylist = [keywords]
    print(keylist)

    #print(skips)
    #skiplist = [skip]
    #print(skiplist)



    fandle = open(in_fh)
    print('Processing "{}"'.format(in_fh))
    records = SwissProt.parse(fandle)
    #print(records)

    for record in records:
        #print(record.keywords)
        #print(record.organism_classification)
        docset = set(record.keywords)
        userset = set(keylist)
        organismset = set(record.organism_classification)
        skipset = set(skips)
        thelen = skipset.union(organismset)
        #print('THIS IS THE LENGHT', len(thelen))
        #print(thelen)
        #print(record.organism_classification)
        if organismset.intersection(skipset):
            print(record.keywords)
            print('check me out', record.organism_classification)



    '''
    for record in records:
        print(record['KW'])
        finder = record.get('KW') or 'NA'
        print(finder)
    '''





# --------------------------------------------------
if __name__ == '__main__':
    main()
