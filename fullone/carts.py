import pygame


pygame.init()


window_size = (640, 480)

screen = pygame.display.set_mode(window_size)

pygame.display.set_caption("My Pygame Window")

background_color = (255, 255, 255)


square_color = (255, 0, 0)


square_rect = pygame.Rect(100, 100, 50, 50)


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill(background_color)


    pygame.draw.rect(screen, square_color, square_rect)


    pygame.display.flip()


pygame.quit()
