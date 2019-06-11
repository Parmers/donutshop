import pygame, sys

#Summer 2019 Python Game Project - Ashad's Donut Shop

from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((1000,700))

pygame.display.set_caption("Ashad's Donut Shop")

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()