# ХОЧУ СДЕЛАТЬ ПЕРВЫЙ МАКЕТ ДЛЯ ИГРЫ SPACE BATTLE, ГДЕ КОРАБЛИ ПРОТИВНИКА ЛЕТЯТ НА ТЕБЯ, А ТЕБЕ НУЖНО ИХ СБИВАТЬ

import pygame

pygame.init()

# ---------------------- variables ------------------------

FRAME_COLOR = (100, 100, 100)
RED = (155, 0, 0)
GREEN = (0, 155, 0)
BLUE = (0, 0, 155)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size = (500, 600)
block_size = 20
count_blocks = 10
MARGIN = 20

FPS = 3

direct_x = 1
direct_y = 1
x = 30
y = 100

score = 0
score_x = 300
score_y = 30

# ---------------------- window ------------------------

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Running blocks')
img = pygame.image.load('space_logo.png')
pygame.display.set_icon(img)
clock = pygame.time.Clock()
font = pygame.font.SysFont('Comic Sans MS', 30)

# ---------------------- objects ------------------------

score_text = font.render(f'Score: {score}', 1, WHITE)

# ---------------------- cycle ------------------------

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    clock.tick(FPS)

    screen.fill(FRAME_COLOR)

    screen.blit(score_text, (score_x, score_y))

    for row in range(3):
        for column in range(count_blocks):
            if (row + column) % 2 == 0:
                color = WHITE
            else:
                color = RED

            pygame.draw.rect(screen, color, [x + column * count_blocks + MARGIN * (column + 1),
                                             y + row * count_blocks + MARGIN * (row + 1),
                                             block_size,
                                             block_size])
            x += direct_x

            if x + (count_blocks * block_size) >= 370 or x == 0:
                direct_x = -direct_x
                # y -= direct_y
                # score += 1
                # print(score)



    pygame.display.update()
