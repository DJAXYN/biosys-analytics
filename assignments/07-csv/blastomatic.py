#!/usr/bin/env python3
"""
Author : jasongiles
Date   : 2019-03-12
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import csv

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'blast_file', metavar="File", help='BLAST output (-outfmt 6)')

    parser.add_argument(
        '-a',
        '--annotations',
        help='annotation file',
        metavar='str',
        required=True,
        type=str,
        default='')

    parser.add_argument(
        '-o',
        '--outfile',
        help='output file name',
        metavar='FILE',
        type=str,
        default='')

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
    annotate_file = args.annotations
    outfh = args.outfile
    blastf = args.blast_file

    for file in [blastf, annotate_file]:
        if not os.path.isfile(file):
            die('"{}" is not a file'.format(file))
    anndict = {}
    with open(annotate_file, 'r') as annotate_fh:
        reader = csv.DictReader(annotate_fh, delimiter=',')
        for row in reader:
            anndict[row['centroid']] = row
    out_fh = open(outfh,'w') if outfh else sys.stdout
    out_fh.write('\t'.join(["seq_id", "pident", "genus", "species"])+'\n')

    with open(blastf,'r') as blastfh:
        header = ["qaccver", "saccver", "pident", "length", "mismatch", "gapopen", "qstart", "qend", "sstart", "send",
                  "evalue", "bitscore"]
        blastfh = csv.DictReader(blastfh, delimiter='\t', fieldnames=header)
        for row in blastfh:
            seqid = row['saccver']
            pct = row['pident']
            if seqid not in anndict:
                warn('Cannot find seq "{}" in lookup'.format(seqid))
                continue
            info = anndict.get(seqid)
            genus = info.get('genus') or 'NA'
            species = info.get('species') or "NA"
            out_fh.write('\t'.join([seqid,pct,genus,species])+"\n")









# --------------------------------------------------
if __name__ == '__main__':
    main()
