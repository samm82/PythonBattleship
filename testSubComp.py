import random as r
import subComp

def main():
    attempts = getAttempts()
    print(attempts)

def getAttempts():
    attempts = 0
    while attempts <= 0:
        test = input("Enter how many simulations to run: ")
        try:
            attempts = int(test)
            if attempts <= 0:
                print("You must enter an integer greater than zero.")
        except ValueError:
            print("You must enter an integer.")
    return attempts

main()