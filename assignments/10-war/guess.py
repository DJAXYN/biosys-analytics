#!/usr/bin/env python3
"""
Author : jasongiles
Date   : 2019-03-19
Purpose: Rock the Casbah
"""

import argparse
import sys
import random
import re


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument(
        '-m',
        '--min',
        help='A named string argument',
        metavar='int',
        type=int,
        default=1)

    parser.add_argument(
        '-x',
        '--max',
        help='A named integer argument',
        metavar='int',
        type=int,
        default=50)

    parser.add_argument(
        '-g',
        '--num_guess',
        help='A named integer argument',
        metavar='int',
        type=int,
        default=10)

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
    low = args.min
    high = args.max
    num_guesses = args.num_guess
    seed = args.seed
    secret = random.choice(range(low,high))

    if seed is not None:
        random.seed(seed)
    #print(secret)
    print(low,high,num_guesses)

    prompt = 'Guess a number between {} and {}: '.format(low,high)

    while num_guesses >0:
        num_guesses -= 1
        guess = input(prompt)
        print(guess)

        #if not re.match('[0-9]+', guess): # can also do \d+ insteand of [0-9]+

        if guess.isdigit():
            guess = int(guess)
        else:
            print('"{}" is not a digit. I hate you'.format(guess))
            continue
        if guess == secret:
            print('You win')
            sys.exit()
        elif guess < secret:
            print('Too Low')
        elif guess > secret:
            print('Too High')
    print('You loose, Loser')


# --------------------------------------------------
if __name__ == '__main__':
    main()
