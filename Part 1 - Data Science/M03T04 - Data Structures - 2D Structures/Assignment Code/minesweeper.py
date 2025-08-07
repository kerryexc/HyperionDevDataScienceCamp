def mine(grid):
    if not grid or not all(len(row) == len(grid[0]) for row in grid):
        raise ValueError("Invalid grid: empty or irregular dimensions")
    
    for row in range (len(grid)):
        