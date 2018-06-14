# PythonBattleship
A simple battleship game in Python. 

## Game Modes
The game modes are:

### Battleship 
A singleplayer game of Battleship with 40 tries to find the five ships in a 10x10 grid.

### Find the Submarine
A minigame in which you have to find a three-long submarine in a 5x5 grid. This game supports the following:
1. Computer (Easy) - The computer guesses randomly.
2. Computer (Normal) - The computer spaces around hits.
3. Computer (Hard) - The computer only guesses in a checkerboard pattern and guess in a line if there are two consecutive hits.
4. Singleplayer - The player has 10 tries.

## Folder Contents
|File|Purpose|
|---|---|
|answerFull.py|Generates a random board for a full game of Battleship.|
|answerSub.py|Generates a random board for the minigame "Find the Submarine"|
|battleship.py|The main file that calls the other functions. Run this to play the game.|
|classic.py|The functions for a full game of Battleship.|
|display.py|Defines functions for displaying boards nicely.|
|README.md|This file. Contains information about the repo.|
|subComp.py|The functions for a game of "Find the Submarine" against the computer.|
|submarine.py|The functions for a singleplayer game of "Find the Submarine".|