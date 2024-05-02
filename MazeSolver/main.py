import pygame.gfxdraw
from random_maze import generate
import pygame
import ai

pygame.init()
dim = 36
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1024
main_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Solver")

SURFACE_WIDTH = 720
SURFACE_HEIGHT = 720
px_width = int(SURFACE_WIDTH / dim)
px_height = int(SURFACE_HEIGHT/dim)
game = generate(dim)
maze = game[0]
end_point = game[1]

title_font = pygame.font.SysFont('arialblack', 60)
font = pygame.font.SysFont("arialblack", 40)
TEXT_COL = (255, 255, 255)

explored = [(1, 0), [1, 1]]
stack = []
current_pos = (1, 1)
maze[1][1] = 2

main_screen.fill((80, 80, 80))
game_surface = pygame.Surface((720, 720))
game_surface.fill((160, 160, 160))

for i in range(dim):
    for j in range(dim):
        #i --> y, j --> x
        if maze[i][j] == 1: 
            pygame.draw.rect(game_surface, (0, 0, 0), pygame.Rect(j * px_width, i * px_height, px_height, px_width))

won = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    for i in range(dim):
        for j in range(dim):
            if maze[i][j] == 2:
                pygame.draw.rect(game_surface, (255, 0, 0), pygame.Rect(j * px_width, i * px_height, px_height, px_width))

    #ai model
    if not won:
        nearby = ai.neighbour(maze, current_pos)
        for i in nearby:
            if i not in explored:
                stack.append((i, ai.manhattan_distance(i, end_point)))
        stack = sorted(stack, key=lambda x:x[1], reverse=True)
        y, x = stack[-1][0]
        current_pos = (y, x)
        maze[y][x] = 2
        explored.append(current_pos)
        if current_pos == end_point:
            won = True
        stack.pop()
    else:
        pass

    pygame.time.delay(200)
    main_screen.blit(game_surface, (0, 0))
    pygame.display.flip()
