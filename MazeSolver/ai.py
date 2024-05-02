def neighbour(maze, pos):
    y = pos[0]
    x = pos[1]
    re = []
    if maze[y + 1][x] == 0:
        re.append((y + 1, x))
    if maze[y - 1][x] == 0:
        re.append((y - 1, x))
    if maze[y][x + 1] == 0:
        re.append((y, x + 1))
    if maze[y][x - 1] == 0:
        re.append((y, x - 1))
    return re

def manhattan_distance(goal, pos):
    dist = ((goal[0]- pos[0]) ** 2 + (goal[1] - pos[1]) ** 2) ** 0.5
    return round(dist, 2)