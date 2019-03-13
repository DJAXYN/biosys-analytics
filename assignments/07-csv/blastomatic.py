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
        '--out',
        help='output file name',
        metavar='FILE',
        type=str,
        default= sys.stdout)

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
    outfh = args.out
    blastf = args.blast_file

    for file in [blastf, annotate_file]:
        if not os.path.isfile(file):
            die('"{}" is not a file'.format(file))
    '''
    with open(blastf) as blast:
        rd = csv.reader(blast)
        data = [line for line in rd]
    with open(blastf,'wt') as blast:
        header = ["qaccver", "saccver", "pident", "length", "mismatch", "gapopen", "qstart", "qend", "sstart", "send","evalue", "bitscore"]
        app = csv.DictWriter(blast,fieldnames=header,delimiter = "\t")
        app.writeheader()
        rad = csv.writer(blast)
        rad.writerows(data)
        #app = csv.writer(blast,delimiter= '\t')
        #app.writerow(header)
    blast.close()
    '''
    anndict = {}
    with open(annotate_file, 'r') as annotate_fh:
        reader = csv.DictReader(annotate_fh, delimiter=',')
        for row in reader:
            anndict[row['centroid']] = row
        #print(anndict)

    outfh.write('\t'.join(["seq_id" "pident" "genus", "species\n"]))
    with open(blastf,'r') as blastfh:
        header = ["qaccver", "saccver", "pident", "length", "mismatch", "gapopen", "qstart", "qend", "sstart", "send",
                  "evalue", "bitscore"]
        blastfh = csv.DictReader(blastfh, delimiter='\t', fieldnames=header)
        for row in blastfh:
            #print(row['saccver'])
            seqid = row['saccver']
            pct = row['pident']
            if seqid not in anndict:
                warn('Cannot find seq "{}" in lookup'.format(seqid))
                continue
            info = anndict.get(seqid)
            genus = info.get('genus') or 'NA'
            #print(genus)
            species = info.get('species') or "NA"
            #print(seqid,pct,genus,species)
            outfh.write('\t'.join([seqid,pct,genus,species,'\n']))









# --------------------------------------------------
if __name__ == '__main__':
    main()
