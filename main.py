import pygame, sys, mazeLogic as mL
from pygame.locals import QUIT

pygame.init()
width, height = 400, 300
DISPLAYSURF = pygame.display.set_mode((width, height))
pygame.display.set_caption('Hello world!')
clock = pygame.time.Clock()

# maze
maze = []
row = 0
col = 0

player = 'm'
wall = '1'  
path = '3'   
deadend = '4'  
target = 'e'

prow = 0
pcol = 0

trow = 0
tcol = 0

# ordem: direita[R], esquerda[L], baixo[D] e cima[U](alterar depois).
moveOrder = ['d', 'r', 'l', 'u']
ourMoves = []
moveStack = []  # Pilha para armazenar os movimentos

maze, row, col, prow, pcol, trow, tcol = mL.loadMaze()

mL.printMaze(maze, row, col)

cellWidth = width // col
cellHeight = height // row

def drawMaze(maze, row, col):
    for r in range(row):
        for c in range(col):
            cellColor = 'grey'
            if maze[r][c] == player:
                cellColor = 'blue'
            elif maze[r][c] == target:
                cellColor = 'green'
            elif maze[r][c] == wall:
                cellColor = 'red'
            elif maze[r][c] == deadend:
                cellColor = 'black'
            elif maze[r][c] == path:
                cellColor = 'pink'

            # Usar dimensões calculadas dinamicamente
            pygame.draw.rect(DISPLAYSURF, cellColor, (c * cellWidth, r * cellHeight, cellWidth, cellHeight),
                             width=cellWidth // 4)

moveMade = False
while True:
    DISPLAYSURF.fill('white')
    drawMaze(maze, row, col)

    if prow == trow and pcol == tcol:
        print("Jerry está livre! 🐀")
        print(ourMoves, len(ourMoves))
        break

    moveMade = False
    #moveOrder = mL.findMoveOrder(maze, row, col, prow, pcol, trow, tcol)
    for move in moveOrder:
        print(move, ourMoves)
        # user_input = input()
        # time.sleep(0.4)
        if mL.checkMoveDirection(maze, row, col, prow, pcol, move):
            maze, prow, pcol = mL.moveDirection(maze, row, col, prow, pcol, move)
            ourMoves.append(move)
            moveStack.append(move)  # Adiciona o movimento à pilha
            moveMade = True
            mL.printMaze(maze, row, col)
            drawMaze(maze, row, col)
            break

    if not moveMade and moveStack:
        moveToUndo = moveStack.pop()  # Remove o último movimento da pilha
        maze, prow, pcol = mL.undoMoveDirection(maze, row, col, prow, pcol, moveToUndo)
        mL.printMaze(maze, row, col)
        drawMaze(maze, row, col)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(10)
