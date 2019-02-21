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





# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    state = args.state
    cell = args.cell
    player = args.player
    #print(state)

    # Check state
    if len(state) != 9:
        die('State "{}" must be 9 characters of only ., X, O'.format(state))

    for i in state.upper():
        if i not in '.XO':
            die('State "{}" must be 9 characters of only ., X, O'.format(state))

    # Check player
    if player.upper() not in ['X','O'] and player != '':
        die('Invalid player "{}", must be X or O'.format(player))

    # Check cell
    if cell is not None:
        if cell not in range(1,10):
            die('Invalid cell "{}", must be 1-9'.format(cell))

    #Check player and cell
    if any([cell,player]) and not all([cell,player]):
        die('Must provide both --player and --cell')

    #if cell in range(1,10) and player:

           #print_board(test)


    #print if no arguments given
    if state == '.........' and cell == None and player == '':
        print_board(test)

    # Print a valid state
    #print(state)
    #print(type(state))
    #if state !='.........':
        #print_board(state)
        #print(state_list)
        #for val in state:


# --------------------------------------------------
if  __name__ == '__main__':
    main()
