import answerSub as aS
import random as r
import subComp
import os, sys

class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = None

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self._original_stdout

def main():
    atts = getAttempts()
    easy   = [test(subComp, 0) for _ in range(atts)]
    medium = [test(subComp, 1) for _ in range(atts)]
    hard   = [test(subComp, 2) for _ in range(atts)]
    eAvg, mAvg, hAvg = sum(easy)/atts, sum(medium)/atts, sum(hard)/atts
    print("Easy:   {:5.2f}".format(eAvg))
    print("Medium: {:5.2f}".format(mAvg))
    print("Hard:   {:5.2f}".format(hAvg))
    print(len(easy), len(medium), len(hard))

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

def test(m, diff):
    c, bc, gL, t, h, tries = initialize(m, diff)
    with HiddenPrints():
        while c != 3:  
            c, bc, gL, t, h = m.compGuess(c, bc, gL, t, h, diff)
            tries += 1
    return tries

def initialize(m, diff):
    c, bc, t, h, tries = 0, r.choice(aS.subGen()), [], [], 0
    for i in range(len(bc)):
        for j in range(len(bc[i])):
            if bc[i][j] == "O":
                bc[i][j] = "."
            elif bc[i][j] == "X":
                bc[i][j] = "#"
        bc[i] = ['']+bc[i]
    bc = [[],[],[],[],[]] + bc
    gL = ['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5', 'D1', 'D2', 'D3', 'D4', 'D5', 'E1', 'E2', 'E3', 'E4', 'E5']
    if diff == 2:
        gL = m.halfGL(gL)
    return c, bc, gL, t, h, tries

main()