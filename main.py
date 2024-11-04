import sys
import pygame

from gato import Gato


def entrada():
    # Inicializamos pygame
    pygame.init()

    # Definimos dimensiones de la ventana
    size = width, height = 555, 260
    screen = pygame.display.set_mode(size)

    # Cambiamos el título de la ventana
    pygame.display.set_caption("Gato juego")

    # Cambiamos el icono de la ventana
    icono = pygame.image.load("res/walk/gato_walk1.png")
    pygame.display.set_icon(icono)

    # Cargamos el fondo de la ventana
    fondo = pygame.image.load("res/elementos/fondo.jpg")

    # Creamos una instancia de la clase Gato
    gato = Gato()

    # Bucle principal del juego
    run = True
    while run:
         #Capturamos los eventos que se han producido
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 run = False

    # Dibujamos el fondo
    screen.blit(fondo, (0, 0))
    # Actualizamos y dibujamos el gato
    gato_frame, gato_rect = gato.walk()
    screen.blit(gato_frame, gato_rect)

    # Actualizamos la pantalla
    pygame.display.flip()

    # Control de la velocidad de refresco
    pygame.time.delay(20)

    # Salgo de pygame
    pygame.quit()



if __name__ == '__main__':
    entrada()

