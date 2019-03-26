#!/usr/bin/env python3
"""
Author : jasongiles
Date   : 2019-03-21
Purpose: Rock the Casbah
"""

import argparse
import sys
import random
import os
from itertools import product


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument(
        '-s',
        '--seed',
        help='Seed for RNG',
        metavar='int',
        type=int,
        default=None)


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
    seed = args.seed

    suits = ['♥','♠','♣','♦']

    deck = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

    deck_codes = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
              'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    cards=sorted(product(suits,deck))
    #print(cards)

    if seed is not None:
        random.seed(seed)

    random.shuffle(cards)
    #print(cards)

    p1_wins = 0
    p2_wins = 0
    draws = 0
    while len(cards)>0:
        p1_card = cards.pop()
        p2_card = cards.pop()
        p1_code = deck_codes.get(p1_card[1])
        p2_code = deck_codes.get(p2_card[1])
        if p1_code>p2_code:
            print('{:>3} {:>3} {}'.format(p1_card[0]+p1_card[1], p2_card[0]+p2_card[1], 'P1'))
            p1_wins+=1
        elif p1_code<p2_code:
            print('{:>3} {:>3} {}'.format(p1_card[0]+p1_card[1], p2_card[0]+p2_card[1], 'P2'))
            p2_wins+=1
        else:
            print('{:>3} {:>3} {}'.format(p1_card[0]+p1_card[1], p2_card[0]+p2_card[1],'WAR!'))
    if p1_wins>p2_wins:
        print('P1 {} P2 {}: Player 1 wins'.format(p1_wins,p2_wins))
    elif p1_wins<p2_wins:
        print('P1 {} P2 {}: Player 2 wins'.format(p1_wins,p2_wins))
    else:
        print('P1 {} P2 {}: DRAW'.format(p1_wins, p2_wins))






# --------------------------------------------------
if __name__ == '__main__':
    main()
