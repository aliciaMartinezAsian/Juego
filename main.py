import sys
import pygame

from gato import Gato


def entrada():
    # Inicializamos pygame
    pygame.init()

    # Definimos dimensiones de la ventana
    size = width, height = 555, 260
    screen = pygame.display.set_mode(size)
    #screen = pygame.display.set_mode(size,pygame.FULLSCREEN)

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
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #if event.type ==  pygame.K_ESCAPE:
            #    running = False

        # Obtiene el frame actual del gato y la posición
        frame_actual, gatorect = gato.walk()

        # Dibuja el fondo en pantalla
        screen.blit(fondo, (0, 0))  # Coloca el fondo en la esquina superior izquierda

        # Dibuja el gato sobre el fondo
        screen.blit(frame_actual, gatorect)
        pygame.display.flip()

        clock = pygame.time.Clock()
        # Control de FPS
        clock.tick(30)
    pygame.quit()

    # Actualizamos y dibujamos el gato

    # # Salgo de pygame
    # pygame.quit()


if __name__ == '__main__':
    entrada()
