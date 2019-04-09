#!/usr/bin/env python3

import os
import sys
import time
import webbrowser


args = sys.argv[1:]

if len(args) <1:
    teatime = 2
else:
    teatime = args[0]


#if not teatime.isdigit():
    #print('enter a number in mins/secs')

teatime = int(teatime)

if teatime > 11:
    print('''
    Read this to yourself. Read it silently.
    Don't move your lips. Don't make a sound.
    Listen to yourself. Listen without hearing anything.
    What a wonderfully weird thing, huh?
    
    NOW MAKE THIS PART LOUD!
    SCREAM IT IN YOUR MIND!
    DROWN EVERYTHING OUT.
    Now, hear a whisper. A tiny whisper.
    
    Now, read this next line with your best crochety- old-man voice:
    "Hello there, sonny. Does your town have a post office?"
    Awesome! Who was that? Whose voice was that?
    It sure wasn't yours!
    
    How do you do that?
    How?!
    Must be magic.  ''')
    time.sleep(teatime)
    print('\nYour tea is ready')

if teatime <11:
    teatime = teatime*60
    print('Here is something to hold you over while you wait')
    time.sleep(4)
    webbrowser.open('https://www.youtube.com/watch?v=bsYa4eZfqIU')
    time.sleep(teatime)
    print('\nYour tea is ready')

