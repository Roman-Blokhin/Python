import pygame
pygame.init()

# ------------------------------------------ VARIABLES ------------------------------------------

FRAME_COLOR = (100, 100, 100)
RED = (155, 0, 0)
GREEN = (0, 155, 0)
BLUE = (0, 0, 155)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size = (400, 400)
USERNAME = None


# ------------------------------------------ WINDOW ------------------------------------------

screen = pygame.display.set_mode(size)
pygame.display.set_caption('База данных юзеров')

# ------------------------------------------ CYCLE ------------------------------------------

def intro():
    is_find_name = False
    while not is_find_name:
        name = 'Enter your name:'
        font = pygame.font.SysFont('Comic Sans MS', 20)
        name_text = font.render(name, True, WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN:
                    global USERNAME
                    USERNAME = name
                    is_find_name = True

        screen.blit(name_text, (20, 20))

        pygame.display.update()

intro()