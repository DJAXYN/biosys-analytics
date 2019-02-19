#!/usr/bin/env python3
"""
Author : jasongiles
Date   : 2019-02-18
Purpose: Rock the Casbah
"""

import argparse
import sys
import os



# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='STR', help='DNA/RNA sequence')

    parser.add_argument(
        '-c',
        '--codons',
        help='A file with codon translations',
        metavar='FILE',
        required=True,
        type=str,
        default=None)

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output filename',
        metavar='FILE',
        type=str,
        default='out.txt')


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
    codon = args.codons
    output = args.outfile
    raw_seq = args.positional

    if not os.path.isfile(codon):
        die('--codons "{}" is not a file'.format(codon))
    #print(codon)
    dna_protein ={}
    with open(codon) as cfile:
        for line in cfile:
            line = line.split()
            dna_protein[line[0]] = line[1]
    #print(dna_protein)
    protein = ''
    #print(raw_seq)
    k = 3
    n = len(raw_seq) - k +1
    raw_seq = raw_seq.upper()
    #print(raw_seq)
    for i in range(0, n, k):
        if raw_seq[i:i + k] in dna_protein:
            #print(raw_seq[i:i + k])
            protein += dna_protein[raw_seq[i:i + k]]
        elif raw_seq[i:i + k] not in dna_protein:
            protein += '-'
        elif dna_protein[raw_seq[i:i+k]] == 'Stop':
            break
    #print(protein)

    with open(output, 'w') as outs:
        print('Output written to "{}"'.format(output))
        outs.write(protein)






    #print('str_arg = "{}"'.format(codon))
    #print('int_arg = "{}"'.format(output))
    #print('positional = "{}"'.format(pos_arg))


# --------------------------------------------------
if __name__ == '__main__':
    main()
