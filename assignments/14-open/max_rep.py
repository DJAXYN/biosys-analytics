#!/usr/bin/env python3
"""
Author : jasongiles
Date   : 2019-04-20
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import time


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-w',
        '--weight',
        help='The weight you lifted in pounds',
        metavar='str',
        type=str,
    required=True)

    parser.add_argument(
        '-r',
        '--reps',
        help='number of reps at specific weight',
        metavar='str',
        type=str,
    required=True)

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
    weight = args.weight
    reps = args.reps

    for i in [weight,reps]:
        if not i.isdigit():
            die('the value given "{}" is not a digit'.format(i))
    weight = int(weight)
    reps = int(reps)
    if weight<1:
        print("This is not a valid weight for an average human...")
    max_rep = weight * (1 + (reps / 30))
    # print(max_rep)

    print('Based upon your {} reps at a weight of {} lbs, your 1 rep max is {:.2f} lbs'.format(reps, weight, max_rep))
    time.sleep(3)
    if max_rep>=400:
        print('That is quite the weight you have there...')
        time.sleep(3)
        print('Arnold Schwarzenegger is that you...?')
        time.sleep(3)
        print('''
======================================================David Riley


          _                                       _
    _  _ | |                                     | | _  _
   | || || |                                     | || || |
 =H| || || |========nnnn=============nnnn========| || || |H=
   |_||_|| |        |  |             |  |        | ||_||_|
         |_|        /  |             |  \        |_|
                   |   |             |   |
                   \   (_   /~~~\   _)   /
                    \    \ ( '_' ) /    /
                     \    )\  =  /(    /
                      \   (_)   (_)   /
                       \ /   ~~~   \ /
                       (             )
                        \           /
                         \         /
                          )==(O)==(
                         /         \ 
                        /____/ \____\ 
                        /   /   \   \ 
                       /   /     \   \ 
                      (   )      (   )
                      |   |      |   |
                      |   |      |   |
                      |___|      |___|
                      (___)      (___)
======================================================  David Riley     
              ''')

    die('\nHappy Lifting\n')



# --------------------------------------------------
if __name__ == '__main__':
    main()
