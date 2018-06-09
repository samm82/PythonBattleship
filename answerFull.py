import random as r

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

def threeLong(s):
    gridList = []
    for i in range(s):
        for j in range(s):
            gridList = horizontalThree(i, j, s, gridList)
            gridList = verticalThree(i, j, s, gridList)
    return gridList

def horizontalThree(x, y, s, gL):
    grid = blankGrid()
    if x+2 < s and x+1 < s: 
        grid[x][y], grid[x+1][y], grid[x+2][y] = 'X', 'X', 'X'
        gL.append(grid)
    return gL

def verticalThree(x, y, s, gL):
    grid = blankGrid()
    if y+2 < s and y+1 < s:
        grid[x][y], grid[x][y+1], grid[x][y+2] = 'X', 'X', 'X'
        gL.append(grid)
    return gL    
