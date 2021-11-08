# loading the numpy libray
import numpy
import pygame

# setting the values :
ON = 1
OFF = 0

# size of array :
N=5

# define a 2D array (10x10):
grid = [[0]*N]*N
  

#Start pyGame Engine :
pygame.init()
screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1500)
w=300/N-3

CELLSIZE = int(300/N)
H_CELLSIZE = int(CELLSIZE / 2)


# A function to check if x, y is valid
# index for N * N Maze
def isSafe( maze, x, y ):
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
        return True
    return False

# A function to print solution matrix sol
def printSolution( sol ):
    for i in sol:
        for j in i:
            print(str(j) + " ", end ="")
        print("")
    print("")
    


# A function to print solution matrix sol
def drawSolution( sol ):
    
    screen.fill((0,0,0))
    for numligne in range(0,N):
        for numcol in range(0,N):
            if maze[numligne][numcol]==1:
                pygame.draw.rect(screen, (100,000,100), (numcol*CELLSIZE, numligne*CELLSIZE, w, w))
            if maze[numligne][numcol]==0:
                pygame.draw.rect(screen, (0,0,0), (numcol*CELLSIZE, numligne*CELLSIZE, w, w))
            if sol[numligne][numcol]==2:
                pygame.draw.rect(screen, (255,0,0), (numcol*CELLSIZE, numligne*CELLSIZE, w, w))
    pygame.display.flip()
    clock.tick(3)


# Main solving function :
def solveMaze( maze ):
    # Creating a 4 * 4 2-D list
    sol = [ [ 0 for j in range(N) ] for i in range(N) ]
    if solveMazeUtil(maze, 0, 0, sol) == False:
        print("Solution doesn't exist");
        return False
    printSolution(sol)
    
    return True

# A recursive utility function to solve Maze problem
def solveMazeUtil(maze, x, y, sol):
    drawSolution(sol)

    # if (x, y is goal) return True
    if x == N - 1 and y == N - 1 and maze[x][y]== 1:
        sol[x][y] = 1
        drawSolution(sol)

        return True


    # Check if maze[x][y] is valid
    if isSafe(maze, x, y) == True:
        drawSolution(sol)

        # Check if the current block is already part of solution path.
        if sol[x][y] == 2:
            return False
        
        # mark x, y as part of solution path
        sol[x][y] = 2
        
        # Move forward in x direction
        if solveMazeUtil(maze, x + 1, y, sol) == True:
            return True
            
        # If moving in x direction doesn't give solution
        # then Move down in y direction
        if solveMazeUtil(maze, x, y + 1, sol) == True:
            return True
        
        # If moving in y direction doesn't give solution then
        # Move back in x direction
        if solveMazeUtil(maze, x - 1, y, sol) == True:
            return True
            
        # If moving in backwards in x direction doesn't give solution
        # then Move upwards in y direction
        if solveMazeUtil(maze, x, y - 1, sol) == True:
            return True
        
        # If none of the above movements work then
        # BACKTRACK: unmark x, y as part of solution path
        sol[x][y] = 0
        print("backtracking :")
        drawSolution(sol)

        return False

    # Driver program to test above function
if __name__ == "__main__":
    # Initialising the maze
    maze = [[1, 1, 1, 1, 1],
            [0, 0, 1, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 0, 1] ]
            
    solveMaze(maze)



#pygame.quit()










