import pygame
pygame.init()

size = (400, 400)

# ------------------------------------------ WINDOW ------------------------------------------

screen = pygame.display.set_mode(size)
pygame.display.set_caption('')
# img = pygame.image.load('logo.png')
# pygame.display.set_icon(img)

# ------------------------------------------ CYCLE ------------------------------------------

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
