import sys
import pygame
import random

from gato import Gato
from obstaculo_cielo import Obstaculo_cielo
from constantes import WIDTH, HEIGHT, FPS


def entrada():
    # Inicializamos pygame
    pygame.init()

    # Definimos dimensiones de la ventana
    size = WIDTH, HEIGHT
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

    # Lista para almacenar obstáculos
    obstaculos = []

    # Tiempo para generar nuevos obstáculos
    tiempo_ultimo_obstaculo = pygame.time.get_ticks()
    intervalo_generacion = 1000  # Intervalo en milisegundos

    # Reloj para controlar la velocidad del juego
    clock = pygame.time.Clock()

    # Bucle principal del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Obtiene el tiempo actual
        tiempo_actual = pygame.time.get_ticks()

        # Generar un nuevo obstáculo si ha pasado el intervalo
        if tiempo_actual - tiempo_ultimo_obstaculo > intervalo_generacion:
            nuevo_obstaculo = Obstaculo_cielo()
            obstaculos.append(nuevo_obstaculo)
            tiempo_ultimo_obstaculo = tiempo_actual

        # Dibuja el fondo en pantalla
        screen.blit(fondo, (0, 0))

        # Obtiene el frame actual del gato y la posición
        frame_actual, gatorect = gato.walk()

        # Dibuja el gato sobre el fondo
        screen.blit(frame_actual, gatorect)

        # Actualiza y dibuja cada obstáculo
        for obstaculo in obstaculos[:]:  # Usar copia para iterar
            obstaculo.mover()
            obstaculo.dibujar(screen)

            # Verifica colisión entre el gato y el obstáculo
            obstaculo_rect = pygame.Rect(obstaculo.x, obstaculo.y, obstaculo.width, obstaculo.height)
            if gatorect.colliderect(obstaculo_rect):
                print("Fin del juego")
                running = False

            # Elimina el obstáculo si está fuera de la pantalla
            if obstaculo.fuera_de_pantalla():
                obstaculos.remove(obstaculo)

        # Actualiza la pantalla
        pygame.display.flip()

        # Control de FPS
        clock.tick(FPS)

    # Salgo de pygame
    pygame.quit()
    print("Juego terminado")


if __name__ == '__main__':
    entrada()
