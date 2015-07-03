import pygame
from pygame.locals import *

pygame.init()

# Referencia: http://stackoverflow.com/questions/28005641/how-to-add-a-background-image-into-pygame
class Imagen(pygame.sprite.Sprite):
    def __init__(self, ruta_imagen, ubicacion):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(ruta_imagen)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = ubicacion
