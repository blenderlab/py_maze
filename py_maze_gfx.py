import pygame
import random
import time

"""
0 = path
1 = wall
2 = unknown
3 = spot (start/end)
"""


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

def afficherLaby(maze,curx,cury):
    """
    procedure to draw the maze on the screen (isometric view)
    curx & cury is coordinate of current point
    """
    screen.fill((0,0,0)) # Beware : the parameter is a tuple
    # size of a square on the screen : 
    # Make sure start/end are marked as spot : 
    maze[1][1]=3
    NBCELL=len(maze)
    maze[NBCELL-2][NBCELL-2]=3
    # define the cell Width :
    cellw = 400//NBCELL
    
    for j in range(0,NBCELL):
        for i in range(0,NBCELL):
            # choose the pictcdpure to draw : 
            if (maze[i][j]==1):
                screen.blit(img_grass,(280+i*(cellw-6)-j*12,40+j*(cellw-14)+i*7))
            if (maze[i][j]==0):
                screen.blit(img_sand,(280+i*(cellw-6)-j*12,40+j*(cellw-14)+i*7))
            if (maze[i][j]==2):
                screen.blit(img_grass,(280+i*(cellw-6)-j*12,40+j*(cellw-14)+i*7))
                screen.blit(img_tree1,(280+i*(cellw-6)-j*12,10+j*(cellw-14)+i*7))
            if (maze[i][j]==3):
                screen.blit(img_spot,(280+i*(cellw-6)-j*12,40+j*(cellw-14)+i*7))
    screen.blit(img_player,(290+curx*(cellw-6)-cury*12,25+cury*(cellw-14)+curx*7))
    # update the screen display :   
    pygame.display.flip()
    #some slow down procedure ...
    time.sleep( 0.1 )
    
    