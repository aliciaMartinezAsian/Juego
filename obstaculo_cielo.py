import pygame
import random
from constantes import WIDTH, HEIGHT

class Obstaculo_cielo:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.speed = 5

        imagen_path = "res/elementos/roca.png"

        # Genera posición aleatoria en X
        self.x =  random.randint(0, WIDTH - self.width)
        self.y = 0

        # Carga y escala la imagen
        self.imagen = pygame.image.load(imagen_path)
        self.imagen = pygame.transform.scale(self.imagen, (self.width, self.height))

    def mover(self):
        #Actualiza la posición del obstáculo.
        self.y += self.speed

    def fuera_de_pantalla(self):
        #Devuelve True si el obstáculo está fuera de la pantalla
        return self.y > HEIGHT

    def dibujar(self, screen):
        #Dibuja la imagen en la posición actual
        screen.blit(self.imagen, (self.x, self.y))
