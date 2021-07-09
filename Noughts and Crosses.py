import pygame, sys, numpy, random

#settings
WIDTH = 300
HEIGHT = 300
gridPos = (0,0)
gridPos2 = (0,300)
cellSize = (100)
gridSize = (cellSize*3)
BLACK = (0,0,0)
WHITE = (255,255,255)
X = 3 # number of columns
Y = 3 # number of rows
player = random.randint(1,2)
gameOver = False


#initialisation and main window
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('space to restart')
window.fill(WHITE)

#Grid index
grid = numpy.zeros((X,Y))

#Draw Grid and Lines
def drawGrid():
    pygame.draw.rect(window, WHITE, (gridPos[0],gridPos[1], WIDTH, HEIGHT),1) # height-50 if button
    for x in range(1,3):
                pygame.draw.line(window, BLACK, (gridPos[0] + (x*cellSize), gridPos[1]), (gridPos[0] + (x*cellSize), gridPos[1] + 300),8)
                pygame.draw.line(window, BLACK, (gridPos[0], gridPos[1] +(x*cellSize)) ,(gridPos[0] + 300, gridPos[1] + (x*cellSize)),8)
drawGrid()

def cellInput(x, y, player):
    grid[x][y] = player


# Is the Cell currently empty
def emptyCell(x,y):
    if grid[x][y] == 0:
        return True
    else: 
        return False

# do all cells contain an input
def compGrid():
    for x in range (X):
        for y in range(Y):
            if grid[x][y] != 0:
                return True
            else:
                return False

# draw symbols function
def draw_xo():
    for y in range(X):
        for x in range(Y):
            if grid[x][y] == 1:
                pygame.draw.circle( window, BLACK, (int( y * cellSize + (cellSize//2)), int( x * cellSize + (cellSize//2))), 40, 10 )
            elif grid[x][y] == 2:
                pygame.draw.line(window, BLACK, (y*cellSize + 15, x*cellSize+cellSize - 15),(y*cellSize+cellSize - 15, x*cellSize + 15),15)
                pygame.draw.line(window, BLACK, (y*cellSize + 15,x*cellSize + 15),(y*cellSize+cellSize - 15,  x*cellSize+cellSize - 15),15)

# checking functions
def checkWin(player):
    for x in range(X):
        if grid[0][x] == player and grid[1][x] == player and grid[2][x] == player:
            drawWinVer(x, player)
            return True

    for y in range(Y):
        if grid[y][0] == player and grid[y][1] == player and grid[y][2] == player:
            drawWinHor(y, player)
            return True

    if grid[2][0] == player and grid[1][1] == player and grid[0][2] == player:
        drawWinDia(player)
        return True

    if grid[0][0] == player and grid [1][1] == player and grid [2][2] == player:
        drawWinDia2(player)
        return True

    return False

#draw winning lines
def drawWinVer(x, player):
    posx = x * cellSize + (cellSize//2)
    
    pygame.draw.line(window, BLACK, (posx, 15), (posx, HEIGHT - 15), 10)

def drawWinHor(y, player):
    posy = y * cellSize + (cellSize//2)

    pygame.draw.line(window, BLACK, (15, posy), (WIDTH-15, posy), 10)

def drawWinDia(player):
    
    pygame.draw.line(window, BLACK, (15, HEIGHT-15), (WIDTH-15,15),15)

def drawWinDia2(player):
    
    pygame.draw.line(window, BLACK, (15,15), (WIDTH-15, HEIGHT-15),15)


# restart function
def restart():
    window.fill(WHITE)
    drawGrid()
    player = random.randint(1,2)
    for y in range(Y):
        for x in range(X):
            grid[y][x] = 0

# Running loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:

            coordy = event.pos[0]
            coordx = event.pos[1]

            mosPosx = int(coordx // cellSize)
            mosPosy = int(coordy // cellSize)

            if emptyCell(mosPosx, mosPosy):
                if player == 1:
                    cellInput(mosPosx,mosPosy , 1)
                    if checkWin(player):
                        gameOver = True
                    player = 2
                elif player == 2:
                    cellInput(mosPosx, mosPosy, 2)
                    if checkWin(player):
                        gameOver = True
                    player = 1
                
                draw_xo()
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                restart()
                gameOver = False      

    pygame.display.update()