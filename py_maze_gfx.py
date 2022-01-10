import pygame
import random

# https://pad.blenderlab.fr/p/labyrinth

"""
0 = path
1 = wall
2 = unknown
"""

NBCELL = 20
maze = []
visited = []
img_grass=pygame.image.load("assets/grass.png")
img_grass=pygame.transform.scale(img_grass, (30,25))
img_sand=pygame.image.load("assets/sand.png")
img_sand=pygame.transform.scale(img_sand, (30,25))
img_tree1=pygame.image.load("assets/tree1.png")
img_tree1=pygame.transform.scale(img_tree1, (30,40))

img_tree2=pygame.image.load("assets/tree2.png")
img_tree2=pygame.transform.scale(img_tree2, (30,30))
img_tree3=pygame.image.load("assets/tree3.png")
img_tree3=pygame.transform.scale(img_tree3, (30,40))

def countn(x,y):
    n=0
    if x>0 and maze[x-1][y]>0 : n=n+1
    if x<NBCELL-1 and maze[x+1][y]>0 : n=n+1
    if y>0 and maze[x][y-1]>0 : n=n+1
    if y<NBCELL-1 and maze[x][y+1]>0 : n=n+1
    return n

def prochainesCase(x,y):
    possibles = []
    if (x>0 and visited[x-1][y]==0)  :
        if (countn(x-1,y)>2):possibles.append((x-1,y))
    if (y>0  and visited[x][y-1]==0) :
         if (countn(x,y-1)>2):possibles.append((x,y-1))
    if (y<NBCELL-1  and visited[x][y+1]==0) :
         if (countn(x,y+1)>2): possibles.append((x,y+1))
    if (x<NBCELL-1  and visited[x+1][y]==0) :
         if (countn(x+1,y)>2):possibles.append((x+1,y))
    random.shuffle(possibles)
    return (possibles)

def genererLaby():
    maze=[]
    visited=[]
    for i in range(0,NBCELL):
        line=[]
        for j in range(0,NBCELL):
            ## chose randomly a wall or a path 
            if (random.randint(0,10)==5):
                line.append(random.randint(1,4))
            else :
                line.append(1)     
        maze.append(line)
    # generate a visited array; filled of 0:    
    for i in range(0,NBCELL):
        line=[]
        for j in range(0,NBCELL):
            line.append(0)
        visited.append(line)
    return(maze,visited)
 
def sortirLaby(x,y): 
    """
    return True if a path is found
    return false if no path found 
    """
    #we are on the last cell (EXIT ! yeaaah!) :
    if x==NBCELL-2 and y==NBCELL-2 :
         return True
    visited[x][y]=1
    maze[x][y]=0

    listechoix = prochainesCase(x,y)
    for choix in listechoix :
        afficherLaby()
        if sortirLaby(choix[0],choix[1]):
            return True
        # No exit on this way :
        # BAcktracking !
        else :
            visited[choix[0]][choix[1]]=1
            maze[choix[0]][choix[1]]=0
            return False



def afficherLaby():
    # size of a square on the screen : 
    cellw = 400//NBCELL
    for j in range(0,NBCELL):
        for i in range(0,NBCELL):
            if (maze[i][j]==1):
                screen.blit(img_grass,(280+i*(cellw-6)-j*12,40+j*(cellw-13)+i*7))
            if (maze[i][j]==0):
                screen.blit(img_sand,(280+i*(cellw-6)-j*12,40+j*(cellw-13)+i*7))
            if (maze[i][j]==2):
                screen.blit(img_grass,(280+i*(cellw-6)-j*12,40+j*(cellw-13)+i*7))
                screen.blit(img_tree1,(280+i*(cellw-6)-j*12,10+j*(cellw-13)+i*7))
            if (maze[i][j]==3):
                screen.blit(img_grass,(280+i*(cellw-6)-j*12,40+j*(cellw-13)+i*7))
                screen.blit(img_tree2,(280+i*(cellw-6)-j*12,10+j*(cellw-13)+i*7))
            if (maze[i][j]==4):
                screen.blit(img_grass,(280+i*(cellw-6)-j*12,40+j*(cellw-13)+i*7))
                screen.blit(img_tree3,(280+i*(cellw-6)-j*12,10+j*(cellw-13)+i*7))
    pygame.display.flip()
     
#Init the pygame engine 
pygame.init()
# Screen size :
size = [600,400]
# create a screen object :
screen = pygame.display.set_mode(size)
# important : the window's caption :
pygame.display.set_caption("Laby algo")
clock = pygame.time.Clock()
#main loop :
playing = True

maze,visited = genererLaby()

while playing:
    # manage events (keys....)
    # force all events to be processed : 
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE:
                pygame.quit() # close pygame
                raise SystemExit #for a system close
            if event.key == pygame.K_g:
               laby = genererLaby()
    # fill the screen in white : 
    screen.fill((0,0,0)) # Beware : the parameter is a tuple
    sortirLaby(1,1)
    afficherLaby()
    pygame.display.update()
    clock.tick(20) # 20 fps
pygame.quit()


