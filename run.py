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


#This Function for display of the grid
def display_grid(grid):
    size = len(grid)
    for row in grid:
        print(" ".join(str(cell) for cell in row))

#This  Function is to check if a coordinate is valid
def is_valid_coordinate(grid, x, y):
    size = len(grid)
    return 0 <= x < size and 0 <= y < size

#This Function is to check if a coordinate is a ship
def is_ship(grid, x, y):
    return grid[x][y] == SHIP


# Function to check if a coordinate has been hit
def is_hit(grid, x, y):
    return grid[x][y] == HIT

# Function to check if a coordinate has been missed
def is_miss(grid, x, y):
    return grid[x][y] == MISS

# Function to update the grid after a shot
def update_grid(grid, x, y):
    if is_valid_coordinate(grid, x, y):
        if is_ship(grid, x, y):
            grid[x][y] = HIT
            return True
        elif is_empty(grid, x, y):
            grid[x][y] = MISS
    return False

