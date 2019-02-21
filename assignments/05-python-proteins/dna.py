#!/usr/bin/env python3
"""
Author : jasongiles
Date   : 2019-02-14
Purpose: Rock the Casbah
"""

import os
import sys
from collections import defaultdict, Counter




# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} ARG'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    dna = args[0]

    print('DNA is "{}"'.format(dna))
    # with Counter, all the for loop goes away
    countss = Counter(dna)

    counts = defaultdict(int)
    for char in dna:
        print(char)
        #if char not in counts:
            #counts[char] = 0
        counts[char] += 1

    print ('A = {}'.format(counts.get('A',0)))

    print(counts)
    print('{}{}{}{}'.format(counts['A'], counts["C"], counts['G'], counts["T"]))
# --------------------------------------------------
main()
