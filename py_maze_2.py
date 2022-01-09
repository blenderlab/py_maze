import random
import pygame


class Cell:
    """A cell in the maze.
    A maze "Cell" is a point in the grid which may be surrounded by walls 
    """

    # A wall separates a pair of cells in the N-S or W-E directions.
    wall_pairs = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

    def __init__(self, x, y):
        """Initialize the cell at (x,y). At first it is surrounded by walls."""

        self.x, self.y = x, y
        self.walls = {'N': True, 'S': True, 'E': True, 'W': True}

    def has_all_walls(self):
        """Does this cell still have all its walls?"""

        return all(self.walls.values())

    def knock_down_wall(self, other, wall):
        """Knock down the wall between cells self and other."""

        self.walls[wall] = False
        other.walls[Cell.wall_pairs[wall]] = False


class Maze:

    def __init__(self, nx, ny, ix=0, iy=0):
        """Initialize the maze grid.
        The maze consists of nx x ny cells and will be constructed starting
        at the cell indexed at (ix, iy).

        """

        self.nx, self.ny = nx, ny
        self.ix, self.iy = ix, iy
        self.maze_map = [[Cell(x, y) for y in range(ny)] for x in range(nx)]

    def cell_at(self, x, y):
        """Return the Cell object at (x,y)."""

        return self.maze_map[x][y]

   
  
    def find_valid_neighbours(self, cell):
        """Return a list of unvisited neighbours to cell."""

        delta = [('W', (-1, 0)),
                 ('E', (1, 0)),
                 ('S', (0, 1)),
                 ('N', (0, -1))]
        neighbours = []
        for direction, (dx, dy) in delta:
            x2, y2 = cell.x + dx, cell.y + dy
            if (0 <= x2 < self.nx) and (0 <= y2 < self.ny):
                neighbour = self.cell_at(x2, y2)
                if neighbour.has_all_walls():
                    neighbours.append((direction, neighbour))
        return neighbours

    def make_maze(self):
        # Total number of cells.
        n = self.nx * self.ny
        cell_stack = []
        current_cell = self.cell_at(self.ix, self.iy)
        # Total number of visited cells during maze construction.
        nv = 1

        while nv < n:
            neighbours = self.find_valid_neighbours(current_cell)

            if not neighbours:
                # We've reached a dead end: backtrack.
                current_cell = cell_stack.pop()
                continue

            # Choose a random neighbouring cell and move to it.
            direction, next_cell = random.choice(neighbours)
            current_cell.knock_down_wall(next_cell, direction)
            cell_stack.append(current_cell)
            current_cell = next_cell
            nv += 1


    


# Maze dimensions (ncols, nrows)
nx, ny = 15, 15
# Maze entry position
ix, iy = 0, 0

maze = Maze(nx, ny, ix, iy)
maze.make_maze()


#Start pyGame Engine :
pygame.init()
screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()
w=300/nx-3
screen.fill((0,0,0))
for numligne in range(0,ny):
    for numcol in range(0,nx):
        if maze.maze_map[numligne][numcol].walls['N']:
            pygame.draw.line(screen, (100,000,100), (numcol*w,numligne*w),(numcol*w+w,numligne*w),2)
        if maze.maze_map[numligne][numcol].walls['S']:
            pygame.draw.line(screen, (100,000,100), (numcol*w,numligne*w+w),(numcol*w+w,numligne*w+w),2)
        if maze.maze_map[numligne][numcol].walls['W']:
            pygame.draw.line(screen, (100,000,100), (numcol*w,numligne*w),(numcol*w,numligne*w+w),2)
        if maze.maze_map[numligne][numcol].walls['E']:
            pygame.draw.line(screen, (100,000,100), (numcol*w+w,numligne*w),(numcol*w+w,numligne*w+w),2)
        
pygame.display.flip()
clock.tick(3)
