#!/usr/bin/env python3
"""
Author : jasongiles
Date   : 2019-04-14
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
from Bio import SeqIO



# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'fasta_file', metavar='str', help='fasta file')

    parser.add_argument(
        '-k',
        '--overlap',
        help='number of nucleotides to align to',
        metavar='int',
        type=int,
        default=3)


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
    k_mer = args.overlap
    fasta_filez = args.fasta_file

    if len(k_mer)<1:
        print('')


# --------------------------------------------------
if __name__ == '__main__':
    main()
