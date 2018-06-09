##Battleship

import random as r
import classic
import submarine

def main():
    print("BBBBB   AAAA  TTTTTT TTTTTT LL     EEEEEE  SSSS  HH  HH IIIIII PPPPP \nBB  BB AA  AA   TT     TT   LL     EE     SS  SS HH  HH   II   PP  PP\nBBBBB  AA  AA   TT     TT   LL     EEEE    SS    HHHHHH   II   PP  PP\nBB  BB AAAAAA   TT     TT   LL     EE        SS  HH  HH   II   PPPPP \nBB  BB AA  AA   TT     TT   LL     EE     SS  SS HH  HH   II   PP    \nBBBBB  AA  AA   TT     TT   LLLLLL EEEEEE  SSSS  HH  HH IIIIII PP ")
    while True:
        menu()

def menu():
    choice = input("\nWhich gamemode?\n\n[1] Classic\n[2] Find the Submarine\n[3] Exit\n\n>")
    if choice.lower() in ['1', 'one', 'classic', 'c']:
        classic.play()
        menu()
    elif choice.lower() in ['2', 'two', 'submarine', 'sub', 's']:
        submarine.play()
        menu()
    elif choice.lower() in ['3', 'three', 'exit', 'quit', 'kill', 'leave', 'no', 'nope']:
        raise SystemExit
    else:
        print("Invalid input. Try again.")
        menu()
    
main()
