import random

# The Constants
EMPTY = 0
SHIP = 1
HIT = 2
MISS = 3

# This Function create an empty grid
def create_grid(size):
    return [[EMPTY] * size for _ in range(size)]

# This Function is to place ships randomly on the grid
def place_ships(grid, num_ships):
    size = len(grid)
    for _ in range(num_ships):
        while True:
            x = random.randint(0, size - 1)
            y = random.randint(0, size - 1)
            if grid[x][y] == EMPTY:
                grid[x][y] = SHIP
                break