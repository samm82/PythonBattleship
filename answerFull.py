import random as r

def blankGrid():
    blank = [['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
             ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
             ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
             ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
             ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
             ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
             ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
             ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
             ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
             ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]
    return blank

def initialize(coords):
    grid = blankGrid()
    for coord in coords:
        grid[coord[0]][coord[1]] = "X"
    grid.append(coords)
    return grid

def fullGen():
    grid1 = twoLong()
    grid2 = threeLong(grid1)
    grid3 = threeLong(grid2)
    grid4 = fourLong(grid3)
    grid5 = fiveLong(grid4)
    grid5[-1] = [grid5[-1][0:2], grid5[-1][2:5], grid5[-1][5:8], grid5[-1][8:12], grid5[-1][12:]]
    print(grid5)
    return grid5

def twoLong():
    gridList = []
    for i in range(10):
        for j in range(10):
            gridList = horizontalTwo(i, j, gridList)
            gridList = verticalTwo(i, j, gridList)
    return r.choice(gridList)

def threeLong(grid):
    gridList = []
    for i in range(10):
        for j in range(10):
            gridList = horizontalThree(i, j, gridList, grid)
            gridList = verticalThree(i, j, gridList, grid)
    return r.choice(gridList)

def fourLong(grid):
    gridList = []
    for i in range(10):
        for j in range(10):
            gridList = horizontalFour(i, j, gridList, grid)
            gridList = verticalFour(i, j, gridList, grid)
    return r.choice(gridList)

def fiveLong(grid):
    gridList = []
    for i in range(10):
        for j in range(10):
            gridList = horizontalFive(i, j, gridList, grid)
            gridList = verticalFive(i, j, gridList, grid)
    return r.choice(gridList)

##TWO
def horizontalTwo(x, y, gL):
    grid = blankGrid()
    if x+1 < 10: 
        grid[x][y], grid[x+1][y] = 'X', 'X'
        grid.append([[x, y], [x+1, y]]) #appends "X" coordinates
        gL.append(grid)
    return gL

def verticalTwo(x, y, gL):
    grid = blankGrid()
    if y+1 < 10:
        grid[x][y], grid[x][y+1] = 'X', 'X'
        grid.append([[x, y], [x, y+1]]) #appends "X" coordinates
        gL.append(grid)
    return gL 

##THREE

def horizontalThree(x, y, gL, g):
    grid = initialize(g[-1])
    if x+2 < 10 and x+1 < 10 and not any(i in [[x, y], [x+1, y], [x+2, y]] for i in grid[-1]): 
        grid[x][y], grid[x+1][y], grid[x+2][y] = 'X', 'X', 'X'
        grid[-1] = grid[-1]+[[x, y], [x+1, y], [x+2, y]] #adds "X" coordinates to previous list
        gL.append(grid)
    return gL

def verticalThree(x, y, gL, g):
    grid = initialize(g[-1])
    if y+2 < 10 and y+1 < 10 and not any(i in [[x, y], [x, y+1], [x, y+2]] for i in grid[-1]): 
        grid[x][y], grid[x][y+1], grid[x][y+2] = 'X', 'X', 'X'
        grid[-1] = grid[-1]+[[x, y], [x, y+1], [x, y+2]] #adds "X" coordinates to previous list
        gL.append(grid)
    return gL

##FOUR

def horizontalFour(x, y, gL, g):
    grid = initialize(g[-1])
    if x+3 < 10 and x+2 < 10 and x+1 < 10 and not any(i in [[x, y], [x+1, y], [x+2, y], [x+3, y]] for i in grid[-1]): 
        grid[x][y], grid[x+1][y], grid[x+2][y], grid[x+3][y] = 'X', 'X', 'X', 'X'
        grid[-1] = grid[-1]+[[x, y], [x+1, y], [x+2, y], [x+3, y]] #adds "X" coordinates to previous list
        gL.append(grid)
    return gL

def verticalFour(x, y, gL, g):
    grid = initialize(g[-1])
    if y+3 <10 and y+2 < 10 and y+1 < 10 and not any(i in [[x, y], [x, y+1], [x, y+2], [x, y+3]] for i in grid[-1]): 
        grid[x][y], grid[x][y+1], grid[x][y+2], grid[x][y+3] = 'X', 'X', 'X', 'X'
        grid[-1] = grid[-1]+[[x, y], [x, y+1], [x, y+2], [x, y+3]] #adds "X" coordinates to previous list
        gL.append(grid)
    return gL   

##FIVE

def horizontalFive(x, y, gL, g):
    grid = initialize(g[-1])
    if x+4 < 10 and x+3 < 10 and x+2 < 10 and x+1 < 10 and not any(i in [[x, y], [x+1, y], [x+2, y], [x+3, y], [x+4, y]] for i in grid[-1]): 
        grid[x][y], grid[x+1][y], grid[x+2][y], grid[x+3][y], grid[x+4][y] = 'X', 'X', 'X', 'X', 'X'
        grid[-1] = grid[-1]+[[x, y], [x+1, y], [x+2, y], [x+3, y], [x+4, y]] #adds "X" coordinates to previous list
        gL.append(grid)
    return gL

def verticalFive(x, y, gL, g):
    grid = initialize(g[-1])
    if y+4 < 10 and y+3 <10 and y+2 < 10 and y+1 < 10 and not any(i in [[x, y], [x, y+1], [x, y+2], [x, y+3], [x, y+4]] for i in grid[-1]): 
        grid[x][y], grid[x][y+1], grid[x][y+2], grid[x][y+3], grid[x][y+4] = 'X', 'X', 'X', 'X', 'X'
        grid[-1] = grid[-1]+[[x, y], [x, y+1], [x, y+2], [x, y+3], [x, y+4]] #adds "X" coordinates to previous list
        gL.append(grid)
    return gL 

fullGen()
