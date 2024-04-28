import pygame
from data_base import get_best, insert_result

pygame.init()

# ------------------------------------------ VARIABLES ------------------------------------------

FRAME_COLOR = (100, 100, 100)
RED = (205, 0, 0)
GREEN = (0, 155, 0)
BLUE = (0, 0, 155)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size = (400, 400)
USERNAME = None
USERNUM = None
GAMERS_DB = get_best()

# ------------------------------------------ WINDOW ------------------------------------------

screen = pygame.display.set_mode(size)
pygame.display.set_caption('База данных юзеров')


# ------------------------------------------ CYCLE ------------------------------------------

def intro():
    is_find_name = False
    name = 'Enter your name:'
    while not is_find_name:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    if name == 'Enter your name:':
                        name = event.unicode
                    else:
                        name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN:
                    global USERNAME
                    USERNAME = name
                    is_find_name = True

        screen.fill(BLACK)
        font = pygame.font.SysFont('Comic Sans MS', 20)
        name_text = font.render(name, True, WHITE)
        screen.blit(name_text, (20, 20))
        pygame.display.update()


def score():
    is_find_num = False
    num = 'Enter your number:'
    while not is_find_num:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.unicode.isdigit():
                    if num == 'Enter your number:':
                        num = event.unicode
                    else:
                        num += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    num = num[:-1]
                elif event.key == pygame.K_RETURN:
                    global USERNUM
                    USERNUM = num
                    is_find_num = True

        screen.fill(BLACK)
        font = pygame.font.SysFont('Comic Sans MS', 20)
        num_text = font.render(num, True, WHITE)
        screen.blit(num_text, (20, 20))
        pygame.display.update()


def game_over():
    insert_result(USERNAME, USERNUM)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill(BLACK)
        font = pygame.font.SysFont('Comic Sans MS', 30)
        name_text = font.render('Total champions:', True, RED)
        screen.blit(name_text, (20, 20))

        font_gamers = pygame.font.SysFont('Comic Sans MS', 20)
        for index, gamer in enumerate(GAMERS_DB):
            name, score = gamer
            s = f'{index+1}. {name}: {score}'
            name_gamers = font_gamers.render(s, True, WHITE)
            screen.blit(name_gamers, (20, 75 + 22 * index))

        pygame.display.update()

intro()
score()
game_over()

