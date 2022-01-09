import pygame
import random

# https://pad.blenderlab.fr/p/labyrinth

"""
0 = path
1 = wall
2 = unknown
"""

NBCELL = 30
def prochaineCase(x,y):
    possibles = []
    if (x>0) : possibles.append((x-1,y))
    if (y>0) : possibles.append((x,y-1))
    if (y<NBCELL-1) : possibles.append((x,y+1))
    if (x<NBCELL-1) : possibles.append((x+1,y))
    return (random.choice(possibles))
        
def genererLaby():
    maze = []
    for i in range(0,NBCELL):
        line=[]
        for j in range(0,NBCELL):
            ## chose randomly a wall or a path 
            line.append(1)
        maze.append(line)
    # generate a path : 
    x,y = 0,0
    for i in range(0,300):
       x,y = prochaineCase(x,y)
       maze[x][y]=0
    return(maze)

def afficherLaby(l):
    for i in range(0,NBCELL):
        for j in range(0,NBCELL):
            if (l[i][j]==1):
                # size of a square on the screen : 
                cellw = 400//NBCELL
                rect=pygame.Rect( i*cellw,j*cellw , cellw,cellw)
                pygame.draw.rect(screen,(255,0,0),rect)

#Init the pygame engine 
pygame.init()
# Screen size :
size = [400,400]
# create a screen object :
screen = pygame.display.set_mode(size)
# important : the window's caption :
pygame.display.set_caption("Laby algo")
clock = pygame.time.Clock()
#main loop :
playing = True

laby = genererLaby()

while playing:
    # manage events (keys....)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing=False
    # fill the screen in white : 
    screen.fill((255,255,255)) # Beware : the parameter is a tuple
    afficherLaby(laby)
    pygame.display.update()
    clock.tick(20) # 20 fps
pygame.quit()


