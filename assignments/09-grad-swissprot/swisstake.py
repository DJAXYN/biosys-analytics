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
from Bio import SeqIO







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
    #print(keylist)

    outfile = open(out_fh,"w")

    fandle = open(in_fh)
    print('Processing "{}"'.format(in_fh))
    records = SwissProt.parse(fandle)
    records = SeqIO.parse(fandle, 'swiss')
    print(records)
    #print(records)
    i = 0
    j = 0
    for record in records:
        print(record)
        docset = record.keywords
        docsetlower=[i.lower() for i in docset]
        docsetlower=set(docsetlower)
        userset = set(keylist)
        i+=1

        organismset = record.organism_classification
        organismsetlower = [i.lower() for i in organismset]
        organismsetlower = set(organismsetlower)
        skipsetlower = [i.lower() for i in skips]
        skipsetlower = set(skipsetlower)

        if docsetlower.intersection(userset) and len(organismsetlower.intersection(skipsetlower)) == 0:
            j +=1
            SeqIO.write(record, outfile, 'fasta')

    print('Done, skipped {} and took {}. See output in "{}".'.format((i-j),j,out_fh))









# --------------------------------------------------
if __name__ == '__main__':
    main()
