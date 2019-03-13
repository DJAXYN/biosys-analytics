#!/usr/bin/env python3
"""
Author : jasongiles
Date   : 2019-02-26
Purpose: Rock the Casbah
"""

import argparse
import sys
from Bio import SeqIO
from collections import Counter


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'fasta', metavar='FILE', help='fasta file', nargs='+')

    parser.add_argument(
        '-o',
        '--outdir',
        help='Output directory',
        metavar='Dir',
        type=str,
        default=out)

    parser.add_argument(
        '-p',
        '--pct_gc',
        help='Percent GC',
        metavar='int',
        type=int,
        default=50)

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
    fasta = args.fasta
    out_dir = args.outdir
    pct_gc = args.pct_gc

    for file in fasta:
        print(file)
        for record in SeqIO.parse(file, 'fasta'):
            seq_len = len(record.seq)
            nucs = (Counter(record.seq))
            gc_num = nucs.get('G',0) + nucs.get('C', 0)
            print(record.seq)
            gc = (int(gc_num/seq_len * 100))
            print(gc)
            print('High' if gc >= pct_gc else "Low")
            print()




# --------------------------------------------------
if __name__ == '__main__':
    main()
