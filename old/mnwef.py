import pygame
pygame.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
background_image = pygame.image.load("background.png")
title_image = pygame.image.load("title.png")
font = pygame.font.Font(None, 36)
text = font.render("Press SPACE to start", True, (255, 255, 255))
text_rect = text.get_rect()
text_rect.centerx = screen.get_rect().centerx
text_rect.centery = screen.get_rect().centery + 100


def start_game():
    pass


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start_game()


    screen.blit(background_image, (0, 0))
    screen.blit(title_image, (screen_width // 2 - title_image.get_width() // 2, 50))

   
    screen.blit(text, text_rect)

  
    pygame.display.update()
