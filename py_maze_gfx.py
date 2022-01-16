import pygame
import random
import time
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

def countn(x,y):
    n=0
    if x>0 and maze[x-1][y]>0   : n=n+1
    if x<NBCELL-1 and maze[x+1][y]>0 : n=n+1
    if y>0 and maze[x][y-1]>0 : n=n+1
    if y<NBCELL-1 and maze[x][y+1]>0 : n=n+1
    return n


def preparerLaby():
    maze=[]
    visited=[]
    # generate a free array; filled of 1:   (walls) 
    for i in range(0,NBCELL):
        line=[]
        for j in range(0,NBCELL):
            line.append(1)     
        maze.append(line)
    # generate an unvisited array; filled of 0:    
    for i in range(0,NBCELL):
        line=[]
        for j in range(0,NBCELL):
            line.append(0)
        visited.append(line)
    return(maze,visited)

def prochainesCase(x,y):
    # if coordinates are in the field AND there is at least 3 cases free around next one :
    possibles = []
    if (x>1 and visited[x-1][y]==0 )  :
        if (countn(x-1,y)==3):possibles.append((x-1,y))
    if (y>1  and visited[x][y-1]==0) :
         if (countn(x,y-1)==3):possibles.append((x,y-1))
    if (y<NBCELL-1  and visited[x][y+1]==0) :
         if (countn(x,y+1)==3): possibles.append((x,y+1))
    if (x<NBCELL-1  and visited[x+1][y]==0) :
         if (countn(x+1,y)==3):possibles.append((x+1,y))
    random.shuffle(possibles)
    return (possibles)
 
def dessinerLaby(x,y): 
    """
    return True if a path is found
    return false if no path found 
    """
    #we are on the last cell (EXIT ! yeaaah!) :
    if x==NBCELL-2 and y==NBCELL-2 :
         return True
    # Stipulate that our position is part of the path.
    maze[x][y]=0
    visited[x][y]=1
    # find other possibles ways:
    listechoix = prochainesCase(x,y)

    # if no way out -> backtrack : position is not a path and return false.
    if len(listechoix)==0:
        maze[x][y]=1
        return False
    # for each choice...
    for choix in listechoix :
        afficherLaby()
        #... try to find a way out :
        if dessinerLaby(choix[0],choix[1]):
            # if it is, adding our point.
            maze[choix[0]][choix[1]]=0
            return True
            
    # all the possible ways are wrong : return false...
    return False
    


def afficherLaby():
    screen.fill((0,0,0)) # Beware : the parameter is a tuple
  
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
    time.sleep( 0.05 ) 
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

maze,visited = preparerLaby()

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
    if (dessinerLaby(1,1)):
        print("fini!")
    afficherLaby()
    pygame.display.update()
    clock.tick(20) # 20 fps
pygame.quit()


