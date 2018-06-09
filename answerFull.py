import random as r

#fix
def fullGen(s):
    for i in range(s):
        for j in range(s):
            gridList = horizontal(i, j, s, gridList)
            gridList = vertical(i, j, s, gridList)
    return gridList

def blankGrid():
    grid = [['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]
    return grid

#for testing
def display(lst):
    for line in lst:
        for i in line:
            print(i, end=' ')
        print()

def threeLong(s):
    gL = []
    for x in range(s):
        for y in range(s):
            grid = blankGrid()
            if x+2 < s and x+1 < s and 'X' not in [x, x+1, x+2]: 
                grid[x][y], grid[x+1][y], grid[x+2][y] = 'X', 'X', 'X'
                gL.append(grid)
            grid = blankGrid()
            if y+2 < s and y+1 < s and 'X' not in [y, y+1, y+2]:
                grid[x][y], grid[x][y+1], grid[x][y+2] = 'X', 'X', 'X'
                gL.append(grid)
    display(r.choice(gL))
    #return r.choice(gL)

threeLong(10)



