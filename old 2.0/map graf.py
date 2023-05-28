import pygame
import random
#grafick map witch is in progres but i hate it 

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))


wall_color = (255, 0, 0)
corridor_color = (255, 255, 255)


wall_width = 20
corridor_width = 40


maze = []
for i in range(screen_height // corridor_width):
    row = []
    for j in range(screen_width // corridor_width):
        row.append(1)
    maze.append(row)

start_pos = (random.randint(0, len(maze[0])-1), 0)
end_pos = (random.randint(0, len(maze[0])-1), len(maze)-1)


walls = []
for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == 1:
            if i == 0 or maze[i-1][j] == 0:
                walls.append((j*corridor_width, i*corridor_width, corridor_width, wall_width))
            if j == 0 or maze[i][j-1] == 0:
                walls.append((j*corridor_width, i*corridor_width, wall_width, corridor_width))


for wall in walls:
    pygame.draw.rect(screen, wall_color, wall)
for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == 0:
            pygame.draw.rect(screen, corridor_color, (j*corridor_width+wall_width, i*corridor_width+wall_width, corridor_width-wall_width, corridor_width-wall_width))


pygame.draw.circle(screen, (0, 255, 0), (start_pos[0]*corridor_width+corridor_width//2, start_pos[1]*corridor_width+corridor_width//2), corridor_width//2-wall_width//2)
pygame.draw.circle(screen, (0, 0, 255), (end_pos[0]*corridor_width+corridor_width//2, end_pos[1]*corridor_width+corridor_width//2), corridor_width//2-wall_width//2)


pygame.display.update()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
