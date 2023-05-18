import pygame
import random

# размеры окна
WIN_WIDTH, WIN_HEIGHT = 800, 600

# цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# структура для представления карты
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

# функция для загрузки изображений карт из файлов
def load_card_textures():
    textures = []
    # загружаем текстуры для всех карт
    for i in range(1, 14):
        for j in range(1, 5):
            texture = pygame.image.load("cards/" + str(i) + "c.png").convert_alpha() # загружаем текстуру для карты "крести"
            textures.append(texture)

            texture = pygame.image.load("cards/" + str(i) + "d.png").convert_alpha() # загружаем текстуру для карты "бубны"
            textures.append(texture)

            texture = pygame.image.load("cards/" + str(i) + "h.png").convert_alpha() # загружаем текстуру для карты "червы"
            textures.append(texture)

            texture = pygame.image.load("cards/" + str(i) + "s.png").convert_alpha() # загружаем текстуру для карты "пики"
            textures.append(texture)
    return textures

# функция для отображения карты на экране
def draw_card(screen, textures, card, pos):
    # создаем спрайт для карты
    sprite = pygame.sprite.Sprite()
    sprite.image = textures[4 * (card.suit - 1) + (card.rank - 1)]
    sprite.rect = sprite.image.get_rect()

    # устанавливаем позицию спрайта на доске
    sprite.rect.x, sprite.rect.y = pos

    # устанавливаем масштаб спрайта
    sprite.image = pygame.transform.scale(sprite.image, (sprite.image.get_width() // 2, sprite.image.get_height() // 2))

    # отрисовываем спрайт на экране
    screen.blit(sprite.image, sprite.rect)

# инициализируем Pygame
pygame.init()

# создаем окно размером 800x600
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# устанавливаем название окна
pygame.display.set_caption("Покер")

# загружаем текстуры карт
card_textures = load_card_textures()

# создаем колоду карт
deck = []
for i in range(1, 14):
    for j in range(1, 5):
        card = Card(i, j)
        deck.append(card)

# перемешиваем колоду карт
random.shuffle(deck)

# раздаем карты игрокам
player1_cards, player2_cards = [], []
for i in range(5):
    player1_cards.append(deck.pop())
    player2_cards.append(deck.pop())

# отрисовываем карты на доске
# отрисовываем карты на доске
screen.fill(WHITE)

for i in range(5):
    draw_card(screen, card_textures, player1_cards[i], (100 + i * 100, 400))
    draw_card(screen, card_textures, player2_cards[i], (100 + i * 100, 100))

# запускаем основной цикл программы
running = True
while running:
    # обрабатываем события Pygame
    for event in pygame.event.get():
        # если нажата кнопка "закрыть" - завершаем программу
        if event.type == pygame.QUIT:
            running = False

    # обновляем экран
    pygame.display.flip()

# завершаем Pygame
pygame.quit()

