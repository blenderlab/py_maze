import pygame
import random
import time
from  py_maze_gfx import *
# available on git : https://github.com/blenderlab/py_maze.git

"""
0 = path
1 = wall
2 = unknown
3 = spot (start/end)
"""


NBCELL = 20 #size of the square maze (width) 
maze = [] # contains the area
visited = [] # contains the visited spots
backtrack = 0

def countn(x,y):
    '''
    Function to count free cells around the (x,y) one.
    '''
    n=0
    if x>0 and maze[x-1][y]>0   : n=n+1
    if x<NBCELL-1 and maze[x+1][y]>0 : n=n+1
    if y>0 and maze[x][y-1]>0 : n=n+1
    if y<NBCELL-1 and maze[x][y+1]>0 : n=n+1
    return n


def preparerLaby():
    """
    Function to generate an empty field:
    - all places are walls
    - all places are unvisited
    - start & end are marked as SPOT
    """
    maze=[]
    visited=[]
    backtrack=0
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
    # mark start & end as SPOT places :
    maze[1][1]=3
    maze[NBCELL-2][NBCELL-2]=3
    # send the 2 arrays : maze & visited 
    return(maze,visited)

def prochainesCase(x,y):
    """
    returns a collection of tuples (x,y) of available places to go
    """
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
 
def genererLaby(x,y): 
    """
    return True if a path is found
    return false if no path found 
    """
    global backtrack
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
        afficherLaby(maze,x,y)
        #... try to find a way out :
        if genererLaby(choix[0],choix[1]):
            # if it is, adding our point.
            maze[choix[0]][choix[1]]=0
            return True
            
    # all the possible ways are wrong : return false...
    # and count backtracking
    backtrack = backtrack +1
    return False

# get a new maze & its visited array :
maze,visited = preparerLaby()

#main loop :
playing = True
generating = True
while playing:
    # manage events (keys....)
    # force all events to be processed : 
    pygame.event.pump()
    for event in pygame.event.get():
        # if a key is pressed :
        if event.type == pygame.KEYDOWN :
            # and the key is ESCAPE :
            if event.key == pygame.K_ESCAPE:
                pygame.quit() # close pygame
                raise SystemExit #for a system close
            # and if the key is G
            if event.key == pygame.K_g:
                maze,visited = preparerLaby()
                generating=True
    if generating:
        if genererLaby(1,1):
            print("Finished !")
            generating=False
        else :
            print("No way found...trying again")
            maze,visited = preparerLaby()

   
pygame.quit()


