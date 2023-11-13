maze = []
row = 0
col =0 

def loadMaze():
    f = open("maze.txt")
    row = 0 
    for line in f:
        col = 0
        for c in line:
            if c != '\n'
            maze.append([])
            col = 0
            for c in line:
                maze[row].append(c)
                col += 1
            row +=1
        print(maze, row, col)

def printMaze(maze, row, col):
    for r in range(row): 
        for c in range(col): 
            print(maze[r][c], end="")
        print()
 
#https://www.youtube.com/watch?v=rRUtQRB82os