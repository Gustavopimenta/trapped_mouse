import os, time

maze = []
row = 0
col = 0

player = 'm'
wall = '1'  # Alterado para string
path = '3'   # Alterado para string
deadend = '4'  # Alterado para string
target = 'e'

prow = 0
pcol = 0

trow = 0
tcol = 0

moveOrder = ['r', 'l', 'd', 'u']
ourMoves = []

def loadMaze():
    os.system("clear")
    f = open("maze.txt")
    row = 0
    for line in f:
        maze.append(list(line.strip()))  # Alterado para ler cada caractere individualmente
        col = len(line.strip())
        if player in line:
            prow, pcol = row, line.index(player)
        elif target in line:
            trow, tcol = row, line.index(target)
        row += 1
    return (maze, row, col, prow, pcol, trow, tcol)

def printMaze(maze, row, col):
    os.system("clear")
    for r in range(row):
        for c in range(col):
            print(maze[r][c], end="")
        print()

# maze, row, col, prow, pcol, trow, tcol = loadMaze()
# printMaze(maze, row, col)
# print(row, col, prow, pcol, trow, tcol)

# check valid move
def checkMoveDirection(maze, row, col, prow, pcol, direction):
    nprow = prow
    npcol = pcol
    if direction == 'd':
        nprow += 1
    elif direction == 'u':
        nprow -= 1
    elif direction == 'r':
        npcol += 1
    elif direction == 'l':
        npcol -= 1
    if nprow < row and nprow >= 0 and npcol >= 0 and npcol < col and (maze[nprow][npcol] == '0' or maze[nprow][npcol] == target):
        return True
    return False

# down
def moveDirection(maze, row, col, prow, pcol, direction):
    maze[prow][pcol] = path
    if direction == 'd':
        prow += 1
    elif direction == 'u':
        prow -= 1
    elif direction == 'r':
        pcol += 1
    elif direction == 'l':
        pcol -= 1
    maze[prow][pcol] = player
    return (maze, prow, pcol)

def undoMoveDirection(maze, row, col, prow, pcol, direction):
    maze[prow][pcol] = deadend
    if direction == 'd':
        prow -= 1
    elif direction == 'u':
        prow += 1
    elif direction == 'r':
        pcol -= 1
    elif direction == 'l':
        pcol += 1
    maze[prow][pcol] = player
    return (maze, prow, pcol)

def findMoveOrder(maze, row, col, prow, pcol, trow, tcol):
    moveOrder = []
    if prow < trow:
        moveOrder.append('d')
    else:
        moveOrder.append('u')
    if pcol < tcol:
        moveOrder.append('r')
    else:
        moveOrder.append('l')

    while len(moveOrder) < 4:
        if 'r' not in moveOrder:
            moveOrder.append('r')
        if 'd' not in moveOrder:
            moveOrder.append('d')
        if 'l' not in moveOrder:
            moveOrder.append('l')
        if 'u' not in moveOrder:
            moveOrder.append('u')
    return moveOrder
