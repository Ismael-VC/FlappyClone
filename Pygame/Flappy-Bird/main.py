#! /usr/bin/python

import pygame, sys
from pygame.locals import *
from classes import Imagen

largo_ventana = 350
ancho_ventana = 600

def main():
    pygame.init()
    # (*)Adaptar imagen a la ventana http://www.pygame.org/wiki/WindowResizing
    ventana = pygame.display.set_mode((largo_ventana, ancho_ventana), HWSURFACE|DOUBLEBUF|RESIZABLE) #*
    pygame.display.set_caption('Flappy Bird')
    fondo = Imagen('img/background.png', [0, 0])
    tubo = Imagen('img/pipe.png', [100, 400])
    imagen_ave = 'img/bird1.png'
    estado = 1
    posX = largo_ventana + 25
    posY = 330
    while True:
	    ventana.blit(pygame.transform.scale(fondo.image, (largo_ventana, 500)), fondo.rect) #*
	    ventana.blit(pygame.transform.scale(tubo.image, (50, 300)), tubo.rect)
	    for i in range(1, 16):
		    piso = Imagen('img/ground.png', [posX - 25 * i, 500])
		    ventana.blit(pygame.transform.scale(piso.image, (25, 100)), piso.rect)
	    posX -= 5
	    if posX < largo_ventana:
		    posX = largo_ventana + 25
	    ventana.blit(pygame.transform.scale(pygame.transform.flip(tubo.image, True, True), (50, 300)), pygame.Rect(100, 0, tubo.rect.width, tubo.rect.height))	    
	    if estado == 5:
		    imagen_ave = 'img/bird1.png'
	    elif estado == 10:
		    imagen_ave = 'img/bird2.png'
	    elif estado == 15:
		    imagen_ave = 'img/bird3.png'
	    if estado != 15:
		    estado += 1
	    else:
		    estado = 1
	    ave = Imagen(imagen_ave, [105, posY])
	    ventana.blit(pygame.transform.scale(ave.image, (40, 30)), ave.rect)
	    for event in pygame.event.get():
		    if event.type == QUIT:
			    pygame.quit()
			    sys.exit()	    
	    pygame.display.update()

if __name__ == "__main__":
    main()
