import pygame

# инициализация Pygame
pygame.init()

# определение размера окна
window_size = (640, 480)

# создание окна Pygame
screen = pygame.display.set_mode(window_size)

# установка заголовка окна
pygame.display.set_caption("My Pygame Window")

# установка цвета фона
background_color = (255, 255, 255)

# установка цвета квадрата
square_color = (255, 0, 0)

# определение координат и размеров квадрата
square_rect = pygame.Rect(100, 100, 50, 50)

# основной цикл игры
running = True
while running:
    # обработка событий Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # очистка экрана
    screen.fill(background_color)

    # отрисовка квадрата
    pygame.draw.rect(screen, square_color, square_rect)

    # обновление экрана
    pygame.display.flip()

# выход из Pygame
pygame.quit()
