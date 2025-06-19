import pygame, sys
from pygame.locals import *

pygame.init() 

taille_ecran = (400,400)
screen = pygame.display.set_mode((1920,1080),pygame.FULLSCREEN)   #initiailisation de l'écran


def boucle():
    while True:
        for event in pygame.event.get():
            if event.type == quit:
                pygame.quit()
                sys.exit()

        pygame.display.update

boucle()