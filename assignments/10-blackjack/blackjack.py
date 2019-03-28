#!/usr/bin/env python3
"""
Author : jasongiles
Date   : 2019-03-27
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

    parser.add_argument(
        '-d',
        '--dealer_hits',
        help='The player will hit another card',
        action='store_true')

    parser.add_argument(
        '-p',
        '--player_hits',
        help='The player will hit another card', action='store_true')

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
    player_hit = args.player_hits
    dealer_hit = args.dealer_hits
    seed = args.seed

    suits = ['♥', '♠', '♣', '♦']

    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    deck_codes = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                  'J': 10, 'Q': 10, 'K': 10, 'A': 1}

    cards = sorted(list(product(suits, deck)))
    #print(cards)

    if seed is not None:
        random.seed(seed)

    random.shuffle(cards)
    #print(cards)
    p1_card = cards.pop()
    d1_card = cards.pop()
    p2_card = cards.pop()
    d2_card = cards.pop()


    p1card_val = deck_codes.get(p1_card[1])
    p2card_val = deck_codes.get(p2_card[1])
    d1card_val = deck_codes.get(d1_card[1])
    d2card_val = deck_codes.get(d2_card[1])

    p3card_val = 0
    d3card_val = 0
    p3_card = 0
    d3_card = 0
    if dealer_hit and player_hit:
        p3_card = cards.pop()
        p3card_val = deck_codes.get(p3_card[1])
        d3_card = cards.pop()
        d3card_val = deck_codes.get(d3_card[1])
    if player_hit and not dealer_hit:
        p3_card = cards.pop()
        p3card_val = deck_codes.get(p3_card[1])
    if dealer_hit and not player_hit:
        d3_card = cards.pop()
        d3card_val = deck_codes.get(d3_card[1])


    #p3card_val = '0' if None else p3card_val
    #d3card_val = '0' if None else d3card_val
    #print(p3_card)
    p_tot = int(p1card_val) + int(p2card_val) + int(p3card_val)
    d_tot = int(d1card_val) + int(d2card_val) + int(d3card_val)


    if d3_card==0 and p3_card==0:
        print('D [{:>2}]: {} {}'.format(d_tot, d1_card[0] + d1_card[1], d2_card[0] + d2_card[1]))
        print('P [{:>2}]: {} {}'.format(p_tot, p1_card[0] + p1_card[1], p2_card[0] + p2_card[1]))
    elif d3_card==0 and p3_card!=0:
        print('D [{:>2}]: {} {}'.format(d_tot, d1_card[0] + d1_card[1], d2_card[0]+d2_card[1]))
        print('P [{:>2}]: {} {} {}'.format(p_tot, p1_card[0] + p1_card[1], p2_card[0] + p2_card[1], p3_card[0] + p3_card[1]))
    elif p3_card==0 and d3_card!=0:
        print('D [{:>2}]: {} {} {}'.format(d_tot, d1_card[0] + d1_card[1], d2_card[0] + d2_card[1],
                                           d3_card[0] + d3_card[1]))
        print('P [{:>2}]: {} {}'.format(p_tot, p1_card[0] + p1_card[1], p2_card[0] + p2_card[1]))
    else:
        print('D [{:>2}]: {} {} {}'.format(d_tot, d1_card[0] + d1_card[1], d2_card[0] + d2_card[1],
                                           d3_card[0] + d3_card[1]))
        print('P [{:>2}]: {} {} {}'.format(p_tot, p1_card[0] + p1_card[1], p2_card[0] + p2_card[1],
                                           p3_card[0] + p3_card[1]))

    if p_tot> 21:
        print('Player busts! You lose, loser!')
        sys.exit(0)
    if d_tot >21:
        print('Dealer busts.')
        sys.exit(0)
    if p_tot ==21:
        print('Player wins. You probably cheated.')
        sys.exit(0)
    if d_tot ==21:
        print('Dealer wins!')
        sys.exit(0)
    if d_tot<18:
        print('Dealer should hit.')
    if p_tot<18:
        print('Player should hit.')




# --------------------------------------------------
if __name__ == '__main__':
    main()
