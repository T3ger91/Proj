import pygame


pygame.init()


screen_width = 640
screen_height = 480


screen = pygame.display.set_mode((screen_width, screen_height))


image = pygame.image.load("image.png")


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            pygame.quit()
            quit()

    screen.blit(image, (0, 0))


    pygame.display.update()


color = (255, 255, 255)


pygame.draw.line(screen, color, (0, 0), (screen_width, screen_height))


pygame.draw.rect(screen, color, (x, y, width, height))

pygame.draw.circle(screen, color, (x, y), radius)


font = pygame.font.Font(None, 36)
text = font.render("Hello, world!", True, color)
screen.blit(text, (x, y))
