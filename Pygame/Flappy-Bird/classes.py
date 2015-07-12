from pygame.locals import *
import pygame

pygame.init()

# Referencia: http://stackoverflow.com/questions/28005641/how-to-add-a-background-image-into-pygame
class Imagen(pygame.sprite.Sprite):
    def __init__(self, ruta_imagen, ancho, alto):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(ruta_imagen).convert_alpha(), (ancho, alto))
