import os 

maze = []
row = 0
col =0 

player = 1
wall = 2 
path= 3
target = 5

prow = 0
pcol = 0

trow = 0
tcol = 0

def loadMaze():
    os.system("clear")
    f = open("maze.txt")
    row = 0 
    for line in f:
        maze.append([])
        col = 0
        for c in line:
            if c != '\n':
                maze[row].append(int(c))
                if int(c) == player:
                    prow, pcol = row, col 
                elif int(c) == target: 
                    trow, tcol = row, col
                col += 1 
        row +=1
    return (maze, row, col, prow, pcol, trow, tcol)    

def printMaze(maze, row, col):
    os.system("clear")
    for r in range(row): 
        for c in range(col): 
            print(maze[r][c], end="")
        print()

maze, row, col, prow, pcol, trow, tcol = loadMaze()
printMaze(maze, row, col)
print(row, col, prow, pcol, trow, tcol)


#check valid move - down
def checkMoveDown(maze, row, col, prow, pcol):
    if prow+1 < row and maze[prow+1][col] == 0:
        return True
    return False 

def checkMoveDirection(maze, row, col, prow, pcol, direction):
    nprow = prow 
    npcol = pcol
    if direction == 'd':
        nprow +=1
    elif direction == 'u':
        nprow-=1
    elif direction == 'r':
        npcol +=1
    elif direction == 'l':
        npcol-=1   
    if nprow < row and nprow >= 0 and npcol >= 0 and npcol < col and (maze[nprow][npcol] == 0 or maze[nprow][npcol] == target):
        return True
    return False
# down           
def moveDown(maze, row, col, prow, pcol):
    maze[prow][pcol] = path
    prow+=1
    maze[prow][pcol] = player
    return (maze, prow, pcol)

def moveDirection(maze, row, col, prow,pcol, direction):
    maze[prow][pcol] = path
    if direction == 'd':
        prow+=1
    elif direction == 'u':
        prow-=1
    elif direction == 'r':
        pcol+=1
    elif direction == 'l':
        pcol-=1
    maze[prow][pcol] = player
    return (maze, prow, pcol)

while(True):
    if prow == trow and pcol == tcol:
        print("Success")
        break
    move = input("Which direction? r, l, d, u: ")
    
    #print(prow, pcol, maze)
    if checkMoveDirection(maze, row, col, prow, pcol, move):
        maze, prow, pcol = moveDirection(maze, row, col, prow, pcol, move)
        printMaze(maze, row, col)
                        
 
    
 
#https://www.youtube.com/watch?v=rRUtQRB82os