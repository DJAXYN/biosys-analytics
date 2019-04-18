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



def test_find_kmers():
    """Test the `find_kmers` function"""
    assert grph.find_kmers('ACTG', 2) == ['AC', 'CT', 'TG']
    assert grph.find_kmers('ACTG', 3) == ['ACT', 'CTG']
    assert grph.find_kmers('ACTG', 4) == ['ACTG']



# --------------------------------------------------

def find_kmers(string,k_mer):
    args = sys.argv[1:]
    num_args = len(args)
    if not 1 <= num_args <= 2:
        print('Usage: {} STR [K]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    string = args[0]
    k_mer= args[1] if num_args == 2 else '3'
    if not k_mer.isdigit():
        print('k "{}" is not a digit'.format(k_mer))
        sys.exit(1)
    k = int(k_mer)
    if len(string) < k:
        print('There are no {}-length substrings in "{}"'.format(k, string))
    else:
        n = len(string) - k + 1
        for i in range(0, n):
            print(string[i:i + k])



# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    k_mer = args.overlap
    fasta_filez = args.fasta_file

    if k_mer<1:
        die('-k "{}" must be a positive integer'.format(k_mer))

    if not os.path.isfile(fasta_filez):
        die('"{}" is not a file'.format(fasta_filez))

    base = dict()

    for record in SeqIO.parse(fasta_filez,"fasta"):
        #print(record.id)
        base[record.id] = record.seq

    for i in base.keys():
        for j in base.keys():
            seq1 = base.get(i)
            seq2 = base.get(j)
            #print(seq1,'hello')
            #print(seq1[-k_mer:])
            #print(seq1[:k_mer])
            back_seq1 = (seq1[-k_mer:])
            front_seq2 = (seq2[:k_mer])
            if j!=i and back_seq1==front_seq2:
                print('{} {}'.format(i,j))




# --------------------------------------------------
if __name__ == '__main__':
    main()
