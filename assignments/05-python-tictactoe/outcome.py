#!/usr/bin/env python3
"""
Author : jasongiles
Date   : 2019-02-19
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='str', type=str, help='STATE')

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
board = list(range(1,10))
#print(board)
test = ['1','2','3','4','5','6','7','8','9']
def print_board(board):
    print('-------------')
    print('| ' +board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')



# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    state = args.positional

    if len(state) != 9:
        die(f'State "{state}" must be 9 characters of only ., X, O')

    #print(state)
    state = list(state)
    #print(state)
    #print(board)

    #if state and state not in 'XO.' or len(state) !=9:
        #die(f'State "{state}" must be 9 characters of only ., X, O')

    winning_state = [
       (1, 2, 3),
       (4, 5, 6),
       (7, 8, 9),
       (1, 4, 7),
       (2, 5, 8),
       (3, 6, 9),
       (1, 5, 9),
       (3, 5, 7),
    ]


# --------------------------------------------------
if __name__ == '__main__':
    main()
