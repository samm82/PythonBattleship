##Battleship - Sam Crawford

import display as d
import random as r
import classic
import classicComp
import submarine
import subComp

def main():
    print("BBBBB   AAAA  TTTTTT TTTTTT LL     EEEEEE  SSSS  HH  HH IIIIII PPPPP \nBB  BB AA  AA   TT     TT   LL     EE     SS  SS HH  HH   II   PP  PP\nBBBBB  AA  AA   TT     TT   LL     EEEE    SS    HHHHHH   II   PP  PP\nBB  BB AAAAAA   TT     TT   LL     EE        SS  HH  HH   II   PPPPP \nBB  BB AA  AA   TT     TT   LL     EE     SS  SS HH  HH   II   PP    \nBBBBB  AA  AA   TT     TT   LLLLLL EEEEEE  SSSS  HH  HH IIIIII PP ")
    menu()

def menu():
    choice = input("\nWhich gamemode?\n\n[1] Classic\n[2] Find the Submarine\n[3] Exit\n\n> ")
    if choice.lower() in ['1', 'one', 'classic', 'c']:
        style = input("\nSelect computer difficulty:\n\n[1] Easy\n[2] Normal\n[3] Hard\n[4] No Computer\n\n> ")
        if style.lower() in ['1', 'easy', 'e']:
            play(classicComp, 0)
        elif style.lower() in ['2', 'normal', 'n', 'norm']:
            play(classicComp, 1)
        elif style.lower() in ['3', 'hard', 'h', 'difficult', 'd', 'diff']:
            play(classicComp, 2)
        elif style.lower() in ['4', 'no', 'none', 'single', 'singleplayer']:
            playSingle(classic)
        else:
            print("Invalid input. Try again.")
            menu()
        input("Press enter to go back to the menu.")
        print("\n"*100) #clear screen
        main()
    elif choice.lower() in ['2', 'two', 'submarine', 'sub', 's']:
        style = input("\nSelect computer difficulty:\n\n[1] Easy\n[2] Normal\n[3] Hard\n[4] No Computer\n\n> ")
        if style.lower() in ['1', 'easy', 'e']:
            play(subComp, 0)
        elif style.lower() in ['2', 'normal', 'n', 'norm']:
            play(subComp, 1)
        elif style.lower() in ['3', 'hard', 'h', 'difficult', 'd', 'diff']:
            play(subComp, 2)
        elif style.lower() in ['4', 'no', 'none', 'single', 'singleplayer']:
            playSingle(submarine)
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
    if m == submarine:
        s, p, c, a, bp, bc, gL, t, h = m.play(diff)
    else:
        s, p, c, a, bp, bc, gL, t, h, cL = m.play(diff)
    while (c != 3 and (m == submarine)) or (c != 17 and (m == classicComp)):
        if m == submarine:
            result = m.guess(p, a, bp, bc)
        else:
            result = m.guess(p, a, bp, bc, cL)
        if result == None:
            continue
        elif result == 'menu':
            print("\n"*100) #clear screen
            main()
        else:
            if m == submarine:
                [p, a, bp, bc] = result
            else:
                [p, a, bp, bc, cL] = result
            invalidGuess = True
            while invalidGuess:
                if (p != 3 and (m == submarine)) or (p != 17 and (m == classicComp)):
                    result = m.compGuess(c, bc, gL, t, h, diff)
                    if result == None:
                        continue
                    else:
                        c, bc, gL, t, h = result
                        invalidGuess = False
                else:
                    d.displayBoth(bp, bc)
                    print("\nYY  YY  OOOO  UU  UU     WW    WW IIIIII NN  NN !!\nYY  YY OO  OO UU  UU     WW    WW   II   NNN NN !!\n YYYY  OO  OO UU  UU     WW WW WW   II   NNNNNN !!\n  YY   OO  OO UU  UU     WWWWWWWW   II   NN NNN !!\n  YY   OO  OO UU  UU     WWW  WWW   II   NN  NN   \n  YY    OOOO   UUUU      WW    WW IIIIII NN  NN !!\n")
                    again(m, diff)
    d.displayBoth(bp, bc)
    print("\nYY  YY  OOOO  UU  UU     LL      OOOO   SSSS  EEEEEE\nYY  YY OO  OO UU  UU     LL     OO  OO SS  SS EE    \n YYYY  OO  OO UU  UU     LL     OO  OO  SS    EEEE  \n  YY   OO  OO UU  UU     LL     OO  OO    SS  EE    \n  YY   OO  OO UU  UU     LL     OO  OO SS  SS EE    \n  YY    OOOO   UUUU      LLLLLL  OOOO   SSSS  EEEEEE\n")
    print("The boat was here:\n")
    for i in range(s):
        for j in range(s):
            if a[i][j] == "X":
                bp[j+5][i+1] = a[i][j]
            else:
                continue
    d.display(bp)
    again(m, diff)
    
def again(m, d):
    replay = input("Do you want to play again? (Y/N): ")
    if replay[0].lower() == "y":
        print("\n"*100) # clear screen
        play(m, d)
    else:
        print("\n"*100) # clear screen
        main()
    
def playSingle(m):
    s, a, h, ans, b, cL = m.play()
    while a != 0:
        result = m.guess(a, h, ans, b, cL)
        if result == None:
            continue
        elif result == 'menu':
            print("\n"*100) #clear screen
            main()
        else:
            [a, h, ans, b, cL] = result
            if (m == submarine and (h == 3)) or (m == classic and (h==17)):
                d.display(b)
                print("\nYY  YY  OOOO  UU  UU     WW    WW IIIIII NN  NN !!\nYY  YY OO  OO UU  UU     WW    WW   II   NNN NN !!\n YYYY  OO  OO UU  UU     WW WW WW   II   NNNNNN !!\n  YY   OO  OO UU  UU     WWWWWWWW   II   NN NNN !!\n  YY   OO  OO UU  UU     WWW  WWW   II   NN  NN   \n  YY    OOOO   UUUU      WW    WW IIIIII NN  NN !!\n")
                againSingle(m)
    d.display(b)
    print("\nYY  YY  OOOO  UU  UU     LL      OOOO   SSSS  EEEEEE\nYY  YY OO  OO UU  UU     LL     OO  OO SS  SS EE    \n YYYY  OO  OO UU  UU     LL     OO  OO  SS    EEEE  \n  YY   OO  OO UU  UU     LL     OO  OO    SS  EE    \n  YY   OO  OO UU  UU     LL     OO  OO SS  SS EE    \n  YY    OOOO   UUUU      LLLLLL  OOOO   SSSS  EEEEEE\n")
    print("The answer:\n") #Better generic statement?
    for i in range(s):
        for j in range(s):
            if ans[i][j] == "X":
                b[j+3][i+1] = ans[i][j]
            else:
                continue
    d.display(b)
    againSingle(m)

def againSingle(m):
    replay = input("Do you want to play again? (Y/N): ")
    if replay[0].lower() == "y":
        print("\n"*100) # clear screen
        playSingle(m)
    else:
        print("\n"*100) # clear screen
        main()

main()
