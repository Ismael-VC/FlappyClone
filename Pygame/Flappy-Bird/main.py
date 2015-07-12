#! /usr/bin/python

from classes import *
from pygame.locals import *
from random import randint
import pygame, sys

ancho_ventana, ancho_logo, ancho_piso, ancho_tubo = 400, 200, 25, 50
alto_ventana, alto_fondo, alto_logo, alto_tubo = 550, 450, 50, 300
#ancho_ave, alto_ave = 40, 30
pos_fondo = (0, 0)
pos_logo = (100, 100)
posY_tubo_min, posY_tubo_max = 400, 150
distanciaX_tubos, distanciaY_tubos = 175, 100
velocidad = 3
cuadros_x_segundo = 40

def main():
    pygame.init()
	# (*)Adaptar imagen a la ventana http://www.pygame.org/wiki/WindowResizing
    ventana = pygame.display.set_mode((ancho_ventana, alto_ventana), DOUBLEBUF) #*
    pygame.display.set_caption('Flappy Bird')
    fondo = Imagen('img/background.png', ancho_ventana, alto_fondo) #*
    logo = Imagen('img/logo.png', ancho_logo, alto_logo)
    piso = Imagen('img/ground.png', ancho_piso, alto_ventana - alto_fondo)
    #imagenes_ave = ['img/bird1.png', 'img/bird2.png', 'img/bird3.png']
    tubo = Imagen('img/pipe.png', ancho_tubo, alto_tubo)
    tubos = [pygame.transform.flip(tubo.image, False, True), tubo.image]
    posX_piso = 2 * ancho_ventana
    enc = False
    posX_tubo1, posY_tubo1 = ancho_ventana, randint(posY_tubo_max, posY_tubo_min)
    posX_tubo2, posY_tubo2 = posX_tubo1 + ancho_tubo + distanciaX_tubos, randint(posY_tubo_max, posY_tubo_min)
    while True:
	    ventana.blit(fondo.image, pos_fondo)
	    if not enc:
		    ventana.blit(logo.image, pos_logo)
	    else:
		    ventana.blit(tubos[0], (posX_tubo1, posY_tubo1 - distanciaY_tubos - alto_tubo))
		    ventana.blit(tubos[1], (posX_tubo1, posY_tubo1))
		    ventana.blit(tubos[0], (posX_tubo2, posY_tubo2 - distanciaY_tubos - alto_tubo))
		    ventana.blit(tubos[1], (posX_tubo2, posY_tubo2))
		    posX_tubo1 -= velocidad
		    posX_tubo2 -= velocidad
		    if posX_tubo1 < -1 * ancho_tubo:
			    posX_tubo1, posY_tubo1 = ancho_ventana, randint(posY_tubo_max, posY_tubo_min)		    
		    if posX_tubo2 < -1 * ancho_tubo:
			    posX_tubo2, posY_tubo2 = posX_tubo1 + ancho_tubo + distanciaX_tubos, randint(posY_tubo_max, posY_tubo_min)
	    for i in range(1, 2 * ancho_ventana / ancho_piso + 2):
		    ventana.blit(piso.image, pygame.Rect(posX_piso - ancho_piso * i, alto_fondo, ancho_piso, alto_ventana - alto_fondo))
	    posX_piso -= velocidad
	    if posX_piso < ancho_ventana:
		    posX_piso = 2 * ancho_ventana
	    for event in pygame.event.get():
		    if event.type == QUIT:
			    pygame.quit()
			    sys.exit()
		    elif event.type == pygame.MOUSEBUTTONDOWN:
			    enc = True
	    pygame.display.update()
	    pygame.time.Clock().tick(cuadros_x_segundo)

if __name__ == "__main__":
    main()
