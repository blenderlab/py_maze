import pygame
import random

# Code dispo : 
# https://pad.blenderlab.fr/p/algolaby


#start pygame :
pygame.init()

#our maze : 
maze=[]
#size of the maze :
mazeW=20


#define a window :
win = pygame.display.set_mode((600,600))
# set a clock :
clock = pygame.time.Clock()

#physical size of the cell : 
cellw = 600/mazeW

class Cell:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.wTop = True
        self.wBot = True
        self.wLeft = True
        self.wRight= True
        self.visited = False
        self.walked=False
        
    def pickNeighbour(self):
        listevoisins=[]
        if self.y>0:
            top = maze[self.x][self.y-1]
            if top.visited==False : listevoisins.append(top) 

        if self.y<mazeW-1:
            #point to the cell bottom
            bottom = maze[self.x][self.y+1]
            if bottom.visited==False : listevoisins.append(bottom)
            
        if self.x>0:
            #point to the left cell
            left = maze[self.x-1][self.y]
            if left.visited==False : listevoisins.append(left)
        if self.x<mazeW-1:
            #point to the right cell
            right = maze[self.x+1][self.y]
            if right.visited==False : listevoisins.append(right)
       
        if (len(listevoisins)>0):
            return random.choice(listevoisins)
        
        return False
            
def removeWalls(cellA,cellB):
    dy = cellA.x - cellB.x
    dx = cellA.y - cellB.y
    if dy==1:
        cellA.wLeft =False
        cellB.wRight=False
    if dy==-1:
        cellA.wRight =False
        cellB.wLeft=False
     
    if dx==-1:
        cellA.wBot=False
        cellB.wTop=False
    if dx==1:
        cellA.wTop=False
        cellB.wBot=False

def generateMaze(maze,x,y):
    #get current cell at x,y :
    current=maze[x][y]
    
    #set current as visited (!)
    current.visited=True
    
    #We try to pick a neighbour
    nextcell = current.pickNeighbour()

    #no neighbor ? We leave the loop (backtrack)
    if not nextcell:
        return False
    
    removeWalls(current,nextcell)

    #We have a neighbor ! 
    #remove walls between our cell & next one :
    removeWalls(current,nextcell)
    
    #let's draw something now :
    drawmaze(maze,nextcell)
    
    # trying to generateMaze from the next cell : 
    if generateMaze(maze,nextcell.x,nextcell.y)==True:
        return True
    # if it fails, we try elsewhere around : 
    if nextcell.x>0 and nextcell.x<mazeW-1 and nextcell.y>0 and nextcell.y<mazeW-1:
        if generateMaze(maze,nextcell.x+1,nextcell.y)==True:
            removeWalls(current,maze[nextcell.x+1][nextcell.y])
            return True
    
    
        
        return False
    return False
        

def drawmaze(maze,current):    # drawing the maze :

    for cx in range(mazeW) :
        for cy in range(mazeW):
            x=cx*cellw
            y=cy*cellw
            #draw a cell : 
            color= (100,100,100) # standard color
            if maze[cx][cy].visited : color = (0,155,0)
            if maze[cx][cy].walked : color = (100,255,100)
            pygame.draw.rect(win,color,(x,y,cellw,cellw))
            # draw the walls : 
            if maze[cx][cy].wTop : pygame.draw.line(win,(0,0,0), (x,y), (x+cellw,y))
            if maze[cx][cy].wBot : pygame.draw.line(win,(0,0,0), (x+cellw,y), (x+cellw,y+cellw))
            if maze[cx][cy].wLeft : pygame.draw.line(win,(0,0,0), (x,y), (x,y+cellw))
            if maze[cx][cy].wRight : pygame.draw.line(win,(0,0,0), (x+cellw,y), (x+cellw,y+cellw))
    # draw the current position : 
    pygame.draw.rect(win,(255,0,0),(current.x*cellw,current.y*cellw,cellw,cellw))
    pygame.display.flip()
    clock.tick(30)


def escapeMaze():
    global out
    # current cell is last of the path :
    current_cell = rat_path[-1]
    # bakup the current to temp (so the current can be backtrcked)
    tmpc=current_cell

    drawmaze(maze,current_cell)

    if out :
        return True
    

    if current_cell.x == finish.x and current_cell.y==finish.y:
        out=True
        return True

    
    if tmpc.x>0:
        nextx=tmpc.x -1
        nexty=tmpc.y 
        if maze[nextx][nexty].wRight==False: 
            if maze[nextx][nexty].walked==False:
                maze[nextx][nexty].walked=True
                maze[nextx][nexty].visited=True
                rat_path.append(maze[nextx][nexty])
                escapeMaze()
        
    if tmpc.y>0:
        nextx=tmpc.x 
        nexty=tmpc.y -1
        if maze[nextx][nexty].wBot==False: 
            if maze[nextx][nexty].walked==False:
                maze[nextx][nexty].walked=True
                maze[nextx][nexty].visited=True

                rat_path.append(maze[nextx][nexty])
                escapeMaze()
    
    if tmpc.x<mazeW-1:
        nextx=tmpc.x +1
        nexty=tmpc.y
        if maze[nextx][nexty].wLeft==False: 
            if maze[nextx][nexty].walked==False:
                maze[nextx][nexty].walked=True
                maze[nextx][nexty].visited=True

                rat_path.append(maze[nextx][nexty])
                escapeMaze()

    if tmpc.y<mazeW-1:
        nextx=tmpc.x 
        nexty=tmpc.y +1
        if maze[nextx][nexty].wTop==False: 
            if maze[nextx][nexty].walked==False:
                maze[nextx][nexty].walked=True
                maze[nextx][nexty].visited=True

                rat_path.append(maze[nextx][nexty])
                escapeMaze()
    
   
    # If we get here, this means that we made a wrong decision, so we need to
    # backtrack
    if  current_cell.x != finish.x and current_cell.y!=finish.y :
        current_cell.walked=False
        rat_path.remove(rat_path[-1])


#let's create the maze :
maze=[]
for j in range(mazeW):
    line=[]
    for i in range(mazeW):
        line.append(Cell(j,i))
    maze.append(line)

#let's build a maze :
generateMaze(maze,0,0)
pygame.image.save(win, "laby.png")

out=False

start=Cell(0,0)
finish=Cell(mazeW-1,mazeW-1)

maze[0][0].walked=True
rat_path=[]
rat_path.append(start)
for j in range(mazeW):
    line=[]
    for i in range(mazeW):
        maze[j][i].visited=False
    
escapeMaze() 

if out:
    print("Solution trouvée!")
    pygame.image.save(win, "laby_out.png")

else:
    print("pas de solution ")




