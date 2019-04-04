#!/usr/bin/env python3
"""
Author : jasongiles
Date   : 2019-04-03
Purpose: Rock the Casbah
"""

import os
import sys
import re

# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} STATE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    stater = args[0].upper()
    #print(stater)

    win_state =re.compile('[XO.]*?'
                            '([X]{3})'  
                             '[XO.]*?')

    win_state1 = re.compile('[XO.]*?'
                            '([O]{3})'
                            '[XO.]*?')

    win_state2 = re.compile(
                            '([XO]{1})'
                            '[XO.]{2}'
                            '([XO]{1})' #potentially need to make these groups too and check is Ken is gonna be sneaky...Hi KEN
                            '[XO.]{2}'
                            '([XO]{1})')


    win_state3 = re.compile('([XO]{1})'
                            '[XO.]{3}'
                            '([XO]{1})'  #cannot figure out why X..OX.O.X is not found
                            '[XO.]{3}'
                            '([XO]{1})' )


    win_state4 = re.compile('[XO.]{2}'
                            '([XO]{1})'
                            '[XO.]{1}'
                            '([XO]{1})'  
                            '[XO.]{1}' #cannot figure out why O.X.X.X.O is not found
                            '([XO]{1})'
                            '[XO.]{2}')

    for item in stater:
        if item not in ['X','O','.'] or len(stater)!=9:
            print('State "{}" must be 9 characters of only ., X, O'.format(stater))
            sys.exit(1)

    win = win_state.match(stater)
    win1 = win_state1.match(stater)
    win2 = win_state2.search(stater) or win_state3.search(stater) or win_state4.search(stater)
    #win3 = win_state3.match(stater) or win_state4.match(stater)
    if win:
        print('{} has won'.format('X'))
    elif win1:
        print('{} has won'.format("O"))
    elif win2 and win2.group(1)==win2.group(2)==win2.group(3):
        #print(win2.group())
        print('{} has won'.format("X" if "X" in win2.groups() else "O"))
    else:
        print('No winner')







# --------------------------------------------------
main()
