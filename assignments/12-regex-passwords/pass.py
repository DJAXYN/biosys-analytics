#!/usr/bin/env python3
"""
Author : jasongiles
Date   : 2019-04-06
Purpose: Rock the Casbah
"""

import os
import sys
import re


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 2:
        print('Usage: {} PASSWORD ALT'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    password = args[0]
    alternative = args[1]

    effup_check = re.compile('.?'
                             +password+
                             '.?')

    if password == alternative or password.upper() == alternative:
        print('ok')

    elif password.title() == alternative:
        print('ok')

    elif effup_check.match(alternative):
        print('ok')

    else:
        print('nah')


# --------------------------------------------------
main()
