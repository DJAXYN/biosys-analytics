#!/usr/bin/env python3
"""
Author : jasongiles
Date   : 2019-04-10
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
from Bio import SeqIO
import re


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument(
        '-c',
        '--cdhit',
        help='Output file from CD-HIT (clustered proteins)t',
        metavar='str',
        type=str,
        required=True,
        default=None)

    parser.add_argument(
        '-p',
        '--proteins',
        help='Proteins FASTA',
        metavar='str',
        type=str,
        required=True,
        default=None)

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='str',
        type=str,
        default='unclustered.fa')

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
    hits = args.cdhit
    protein = args.proteins
    out_file = args.outfile

    '''
    for file in [protein,hits]:
        if not os.path.isfile(file):
            die('--{} "{}" is not a file'.format('cdhit' if file==hits else "proteins", file))

    '''
    if not os.path.isfile(protein):
        die('--proteins "{}" is not a file'.format(protein))
    if not os.path.isfile(hits):
        die('--cdhit "{}" is not a file'.format(hits))

    protein_file = open(protein)
    out_fh = open(out_file,'w+')
    hits_fh = open(hits)

    hitss = re.compile('[|]'
                       '(\d+)'
                       '[|]')

    djset = set()

    for line in hits_fh:
        hit_match = hitss.search(line)
        if hit_match:
            djset.add(hit_match[1])
            #print(djset)

    num_proteins = 0
    num_uncluster = 0

    for record in SeqIO.parse(protein_file,'fasta'):
        num_proteins +=1
        #print(record.id)
        if record.id.split('|')[0] not in djset:
            num_uncluster +=1
            SeqIO.write(record,out_fh,'fasta')

    print('Wrote {:,} of {:,} unclustered proteins to "{}"'.format(num_uncluster,num_proteins,out_file))












# --------------------------------------------------
if __name__ == '__main__':
    main()
