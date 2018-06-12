##Battleship - Sam Crawford

import display as d
import random as r
import classic
import submarine
import subComp

def main():
    print("BBBBB   AAAA  TTTTTT TTTTTT LL     EEEEEE  SSSS  HH  HH IIIIII PPPPP \nBB  BB AA  AA   TT     TT   LL     EE     SS  SS HH  HH   II   PP  PP\nBBBBB  AA  AA   TT     TT   LL     EEEE    SS    HHHHHH   II   PP  PP\nBB  BB AAAAAA   TT     TT   LL     EE        SS  HH  HH   II   PPPPP \nBB  BB AA  AA   TT     TT   LL     EE     SS  SS HH  HH   II   PP    \nBBBBB  AA  AA   TT     TT   LLLLLL EEEEEE  SSSS  HH  HH IIIIII PP ")
    menu()

def menu():
    choice = input("\nWhich gamemode?\n\n[1] Classic\n[2] Find the Submarine\n[3] Exit\n\n> ")
    if choice.lower() in ['1', 'one', 'classic', 'c']:
        classic.play()
        print("\n"*100) #clear screen
        main()
    elif choice.lower() in ['2', 'two', 'submarine', 'sub', 's']:
        style = input("\nSelect computer difficulty:\n\n[1] Easy\n[2] Normal\n[3] Hard\n[4] No Computer\n\n> ")
        if style.lower() in ['1', 'easy', 'e']:
            play(subComp, 0)
        elif style.lower() in ['2', 'normal', 'n', 'norm']:
            print("WIP")
            menu()
        elif style.lower() in ['3', 'hard', 'h', 'difficult', 'd', 'diff']:
            print("WIP")
            menu()
        elif style.lower() in ['4', 'no', 'none', 'single', 'singleplayer']:
            submarine.play()
        else:
            print("Invalid input. Try again.")
            menu()
        input("Press enter to go back to the menu.")
        print("\n"*100) #clear screen
        main()
    elif choice.lower() in ['3', 'three', 'exit', 'quit', 'kill', 'leave', 'no', 'nope']:
        raise SystemExit
    else:
        print("Invalid input. Try again.")
        menu()

def play(m, diff):
    s, p, c, a, bp, bc, t = m.play()
    while c != 3:
        p, c, a, bp, bc = m.guess(p, c, a, bp, bc)
        if p != 3:
            p, c, a, bp, bc, t = m.compGuess(p, c, a, bp, bc, t)
        else:
            d.displayBoth(bp, bc)
            print("\nYY  YY  OOOO  UU  UU     WW    WW IIIIII NN  NN !!\nYY  YY OO  OO UU  UU     WW    WW   II   NNN NN !!\n YYYY  OO  OO UU  UU     WW WW WW   II   NNNNNN !!\n  YY   OO  OO UU  UU     WWWWWWWW   II   NN NNN !!\n  YY   OO  OO UU  UU     WWW  WWW   II   NN  NN   \n  YY    OOOO   UUUU      WW    WW IIIIII NN  NN !!\n")
            again(m, diff)
    d.displayBoth(bp, bc)
    print("\nYY  YY  OOOO  UU  UU     LL      OOOO   SSSS  EEEEEE\nYY  YY OO  OO UU  UU     LL     OO  OO SS  SS EE    \n YYYY  OO  OO UU  UU     LL     OO  OO  SS    EEEE  \n  YY   OO  OO UU  UU     LL     OO  OO    SS  EE    \n  YY   OO  OO UU  UU     LL     OO  OO SS  SS EE    \n  YY    OOOO   UUUU      LLLLLL  OOOO   SSSS  EEEEEE\n")
    print("The boat was here:\n")
    for i in range(s):
        for j in range(s):
            if answer[i][j] == "X":
                player[j+5][i+1] = answer[i][j]
            else:
                continue
    d.display(bp)
    again(m, diff)
    
def again(m, d):
    replay = input("Do you want to play again? (Y/N): ")
    if replay[0].lower() == "y":
        print("\n"*100)
        play(m, d)
    else:
        print("\n"*100)
        main()
    
main()
