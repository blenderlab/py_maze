#MAze size :
N = 5

def isSafe(maze,x,y):
    if x>=0 and x<N and y >=0 and y<N and maze[x][y]==1:
        return True
    return False

def printSol(sol):
    for line in sol :
        for col in line :
            print(col,end='')
        print()
        
def trySolve(maze,x,y,sol):
    # Found the exit ? Nice !
    if x==N-1 and y==N-1 :
        #mark the way on sol array :
        sol[x][y]=1
        return True
    
    # IF ONLY THE x,y is safe !
    if isSafe(maze,x,y):
        # Already went here.....
        if sol[x][y]==1:
            return False
        #0- mark current position as GOOD :
        sol[x][y]=1
        print("Trying...")
        printSol(sol)
       
        #1- try downstairs :
        if trySolve(maze,x,y+1,sol) == True:
            return True
        #2- try right :
        if trySolve(maze,x+1,y,sol) == True:
            return True
        #1- try left :
        if trySolve(maze,x-1,y,sol) == True:
            return True
        #1- try upstairs :
        if trySolve(maze,x,y-1,sol) == True:
            return True

        # BACKTRACKING : 
        print("BackTraking...")
        printSol(sol)
        sol[x][y]=0
        return False

def solvemaze(maze):
    #array to store the output : 
    sol = [[0,0,0,0,0],
           [0,0,0,0,0],
           [0,0,0,0,0],
           [0,0,0,0,0],
           [0,0,0,0,0]]
    if trySolve(maze,0,0,sol) == False:
        print ("No solution found ....")
        return False
    # display output : 
    printSol(sol)
    return True

#0 = obstacle
#1 = free way

maze = [[1,0,0,1,0],
        [1,1,1,1,1],
        [0,1,0,0,0],
        [0,1,1,1,0],
        [0,0,0,1,1]]

solvemaze(maze)









