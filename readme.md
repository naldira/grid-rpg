v0.6
~~~ in progress
add interface to character class
add saves (to file)
------------------------------------
v0.5.1
added underline to compound noun names
replaced initialize functions with property and setter
fixed dragon moving with incorrect player input bug
fixed rematch bug
cleaned up main.py

v0.5
added the two missing typehints to 'func' and 'obj'
removed unnecessary imports from random and os
removed functions from main.py
minor code clean-up



------------------------------------
v0.4
1st version of OOP DnD:
current status:
the game is played in turns, indicated by player typing (up/down/left/right), even moving into a wall can trigger the dragon movement if conditions are met(intended design)
    dragon has sight and hearing abilties, the range is defined by chosen difficulty. sight has a 100% activatin chance by default (can be modified) and hearing has 30% (also modifiable).
    player also has sight based on difficulty that allowes them to see the door and dragon if in range.

    no flake8 errors

    doc strings done
----
most issues from previous version are fixed.
changed game grid from string blocks to list.
----
new features:
    added sight to player.
    added difficulty.
    added customizable map size

==========================================================
BUGS:
#1 dragon can move to exit door's cell. (to make it fair, if player moves into this cell, door has prio and player wins)
    
