#!/usr/bin/env python3
"""
Author : jasongiles
Date   : 2019-02-11
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Tic-Tac-Toe board',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument(
        '-s',
        '--state',
        help='Board state',
        metavar='str',
        type=str,
        default='.........')

    parser.add_argument(
        '-p',
        '--player',
        help='Player',
        metavar='str',
        type=str,
        default='')

    parser.add_argument(
        '-c',
        '--cell',
        help='Cell to apply -p',
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
board = ['']*9
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
def state_lister():
    if len(state) == 9:
        



# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    state = args.state
    cell = args.cell
    player = args.player
    #print(state)
    if state =='.........' and cell == None and player =='':
        print(print_board(test))
    if len(state) != 9:
        print('STATE "{}" must be 9 characters of only ., X, O'.format(state))
    if len(state) == 9:
        for i in state:
            if i not in ['.','X','O']:
                print('STATE "{}" must be 9 characters of only ., X, O'.format(state))
                sys.exit(1)
    if player.upper() not in ['X','O'] and player != '':
        print('Invalid player "{}", must be X or O'.format(player))
        die()



# --------------------------------------------------
if  __name__ == '__main__':
    main()
