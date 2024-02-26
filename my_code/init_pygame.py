import pygame

size = (400, 400)

# ------------------------------------------ WINDOW ------------------------------------------

pygame.display.set_mode(size)
pygame.display.set_caption('')
# img = pygame.image.load('logo.png')
# pygame.display.set_icon(img)

# ------------------------------------------ CYCLE ------------------------------------------

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
