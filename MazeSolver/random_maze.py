import random
import numpy as np

def generate(dim):
    maze = np.ones((dim, dim))
    path = []
    dir = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    path.append((1, 1))
    maze[1][1] = 0

    while len(path) > 0:
        (x, y) = path[-1]
        random.shuffle(dir)
        for i in range(4):
            (xr, yr) = sum(dir[i], (x, y)) 
            if xr > 0 and yr > 0 and xr < dim - 1  and yr < dim - 1 and maze[xr][yr] == 1:
                if neighbour_count(maze, xr, yr) == 1:
                    x, y = xr, yr
                    maze[xr][yr] = 0
                    path.append((xr, yr))
                    break
        else:
            path.pop()
    maze[1][0] = 0
    while True:
        r = random.randint(0, dim - 1)
        if maze[-2][r] == 0:
            maze[-1][r] = 0
            end = (dim - 1, r)
            break
        
    return maze, end

def neighbour_count(maze, x, y):
    count = 0
    if maze[x - 1][y] == 0:
        count += 1
    if maze[x + 1][y] == 0:
        count += 1
    if maze[x][y - 1] == 0:
        count += 1
    if maze[x][y + 1] == 0:
        count += 1
    return count

def sum(x, y):
    return (x[0] + y[0], x[1] + y[1])

