import answerSub as aS
import random as r
from display import display

def play():
    size, attempts, hits = 5, 10, 0
    answer = r.choice(aS.subGen())
    blank = [[], ['   A', 'B', 'C', 'D', 'E'], [],
             ['1 ', '.', '.' ,'.', '.', '.'],
             ['2 ', '.', '.' ,'.', '.', '.'],
             ['3 ', '.', '.' ,'.', '.', '.'],
             ['4 ', '.', '.' ,'.', '.', '.'],
             ['5 ', '.', '.' ,'.', '.', '.'], []]
    guess(size, attempts, hits, answer, blank)

def guess(size, attempts, hits, answer, blank):
    while attempts != 0:
        display(blank)
        print("You have %s attempts left." % attempts)
        if attempts == 10:
            g = input("Enter your guess (eg. D2): ") #variable 'g' to not confuse with guess()
        else:
            g = input("Enter your guess: ")
        if (len(g)<2) or g[0].upper() not in ['A', 'B', 'C', 'D', 'E'] or (g[1] not in ['1', '2', '3', '4', '5']):
            print("\nINVALID GUESS. Try again.\n")
            guess(size, attempts, hits, answer, blank)
        else:
            x, y = guessIdentify(g)
            if blank[y+3][x+1] != '.': # to navigate "filler" text for display to work properly
                print("\nYou already guessed here. Try again.\n")
                guess(size, attempts, hits, answer, blank)
            else:
                blank[y+3][x+1] = answer[x][y]
                if answer[x][y] == "O":
                    print("\nMM    MM IIIIII  SSSS   SSSS \nMMM  MMM   II   SS  SS SS  SS\nMMMMMMMM   II    SS     SS   \nMM MM MM   II      SS     SS \nMM    MM   II   SS  SS SS  SS\nMM    MM IIIIII  SSSS   SSSS \n")
                elif answer[x][y] == "X":
                    print("\nHH  HH IIIIII TTTTTT !!\nHH  HH   II     TT   !!\nHHHHHH   II     TT   !!\nHH  HH   II     TT   !!\nHH  HH   II     TT     \nHH  HH IIIIII   TT   !!\n")
                    hits += 1
                else:
                    print("ERROR") #should never run, but just in case
                attempts -= 1
        if hits == 3:
            display(blank)
            print("\nYY  YY  OOOO  UU  UU     WW    WW IIIIII NN  NN !!\nYY  YY OO  OO UU  UU     WW    WW   II   NNN NN !!\n YYYY  OO  OO UU  UU     WW WW WW   II   NNNNNN !!\n  YY   OO  OO UU  UU     WWWWWWWW   II   NN NNN !!\n  YY   OO  OO UU  UU     WWW  WWW   II   NN  NN   \n  YY    OOOO   UUUU      WW    WW IIIIII NN  NN !!\n")
    display(blank)
    print("\nYY  YY  OOOO  UU  UU     LL      OOOO   SSSS  EEEEEE\nYY  YY OO  OO UU  UU     LL     OO  OO SS  SS EE    \n YYYY  OO  OO UU  UU     LL     OO  OO  SS    EEEE  \n  YY   OO  OO UU  UU     LL     OO  OO    SS  EE    \n  YY   OO  OO UU  UU     LL     OO  OO SS  SS EE    \n  YY    OOOO   UUUU      LLLLLL  OOOO   SSSS  EEEEEE\n")
    print("The boat was here:\n")
    for i in range(5):
        for j in range(5):
            if answer[i][j] == "X":
                blank[j+3][i+1] = answer[i][j]
            else:
                continue
    display(blank)

def guessIdentify(g):
    guessLocation = [0, 0] #default is A1
    if g[0].upper() == 'B':
        guessLocation[0] = 1
    elif g[0].upper() == 'C':
        guessLocation[0] = 2
    elif g[0].upper() == 'D':
        guessLocation[0] = 3
    elif g[0].upper() == 'E':
        guessLocation[0] = 4
    #else: not needed - default is 0
    guessLocation[1] = int(g[1]) - 1 #minus one to convert A1 to [0, 0] etc.
    return guessLocation[0], guessLocation[1]

