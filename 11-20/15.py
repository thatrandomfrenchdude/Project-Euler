# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly  routes to the bottom right corner.

# How many such routes are there through a 20x20 grid?

memo = {}

def lattice_paths(x, y):
    if x == 0 or y == 0:
        return 1
    if (x, y) in memo:
        return memo[(x, y)]
    memo[(x, y)] = lattice_paths(x - 1, y) + lattice_paths(x, y - 1)
    return memo[(x, y)]

# use dynamic programming
def problem15(x, y):
    return lattice_paths(x, y)
    
if __name__ == '__main__':
    print(problem15(20, 20))