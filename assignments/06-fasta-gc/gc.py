#!/usr/bin/env python3
"""
Author : jasongiles
Date   : 2019-02-26
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
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
        help='Output directory to write to',
        metavar='str',
        type=str,
        default='out')

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

    j = 0

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    if not pct_gc in range(1,101):
        die('--pct_gc "{}" must be between 0 and 100'.format(pct_gc))

    for i, fasta_file in enumerate(fasta, 1):
        if not os.path.isfile(fasta_file):
            warn('"{}" is not a file'.format((fasta_file)))
            continue
        print("{:3}: {}".format(i,fasta_file))
        base,ext = os.path.splitext(os.path.basename(fasta_file))
        lowout = os.path.join(out_dir, base+'_low'+ext)
        highout = os.path.join(out_dir, base+'_high'+ext)
        lowout_fh = open(lowout,'w')
        highout_fh = open(highout,'w')
        for record in SeqIO.parse(fasta_file, 'fasta'):
            seq_len = len(record.seq)
            nucs = (Counter(record.seq))
            gc_num = nucs.get('G', 0) + nucs.get('C', 0)
            #print(record.seq)
            gc = (int(gc_num / seq_len * 100))
            if gc < pct_gc:
                SeqIO.write(record,lowout_fh,'fasta')
                j += 1
            else:
                SeqIO.write(record, highout_fh, 'fasta')
                j += 1

    print('Done, wrote {} sequences to out dir "{}"'.format(j,out_dir))

# --------------------------------------------------
if __name__ == '__main__':
    main()
