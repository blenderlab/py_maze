import pygame
import random
import time
# https://pad.blenderlab.fr/p/labyrinth

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

# some gfx :
img_grass=pygame.image.load("assets/grass.png")
img_grass=pygame.transform.scale(img_grass, (30,25))
img_sand=pygame.image.load("assets/sand.png")
img_sand=pygame.transform.scale(img_sand, (30,25))
img_spot=pygame.image.load("assets/spot.png")
img_spot=pygame.transform.scale(img_spot, (30,25))
# and a little tree 
img_tree1=pygame.image.load("assets/tree1.png")
img_tree1=pygame.transform.scale(img_tree1, (30,40))

img_player=pygame.image.load("assets/player.png")
img_player=pygame.transform.scale(img_player, (10,20))
def countn(x,y):
    n=0
    if x>0 and maze[x-1][y]>0   : n=n+1
    if x<NBCELL-1 and maze[x+1][y]>0 : n=n+1
    if y>0 and maze[x][y-1]>0 : n=n+1
    if y<NBCELL-1 and maze[x][y+1]>0 : n=n+1
    return n


def preparerLaby():
    """
    # Function to generate an empty field:
    # all places are walls
    # all places are unvisited
    # start & end are marked as SPOT
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
        afficherLaby(x,y)
        #... try to find a way out :
        if genererLaby(choix[0],choix[1]):
            # if it is, adding our point.
            maze[choix[0]][choix[1]]=0
            return True
            
    # all the possible ways are wrong : return false...
    # and count backtracking
    backtrack = backtrack +1
    return False
    


def afficherLaby(curx,cury):
    """
    procedure to draw the maze on the screen (isometric view)
    curx & cury is coordinate of current point
    """
    screen.fill((0,0,0)) # Beware : the parameter is a tuple
    # size of a square on the screen : 
    # Make sure start/end are marked as spot : 
    maze[1][1]=3
    maze[NBCELL-2][NBCELL-2]=3
    # define the cell Width :
    cellw = 400//NBCELL
    
    for j in range(0,NBCELL):
        for i in range(0,NBCELL):
            # choose the picture to draw : 
            if (maze[i][j]==1):
                screen.blit(img_grass,(280+i*(cellw-6)-j*12,40+j*(cellw-13)+i*7))
            if (maze[i][j]==0):
                screen.blit(img_sand,(280+i*(cellw-6)-j*12,40+j*(cellw-13)+i*7))
            if (maze[i][j]==2):
                screen.blit(img_grass,(280+i*(cellw-6)-j*12,40+j*(cellw-13)+i*7))
                screen.blit(img_tree1,(280+i*(cellw-6)-j*12,10+j*(cellw-13)+i*7))
            if (maze[i][j]==3):
                screen.blit(img_spot,(280+i*(cellw-6)-j*12,40+j*(cellw-13)+i*7))
    screen.blit(img_player,(290+curx*(cellw-6)-cury*12,25+cury*(cellw-13)+curx*7))

    # text rendering
    if generating :
        img = font.render('Rendering', True, (255,255,255))
    else :
        img = font.render('Finished', True, (255,255,255))
    screen.blit(img, (20, 20))
    
    img = font.render(("BackTracking=" + str(backtrack)), True, (255,255,255))
    screen.blit(img, (20, 40))

    # update the screen display :   
    pygame.display.flip()
    #some slow down procedure ...
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

font = pygame.font.SysFont(None, 24)


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
    # fill the screen in white : 
    screen.fill((0,0,0)) # Beware : the parameter is a tuple
    if generating:
        if genererLaby(1,1):
            print("Finished !")
            generating=False
        else :
            print("No way found...trying again")
            maze,visited = preparerLaby()

   
pygame.quit()


