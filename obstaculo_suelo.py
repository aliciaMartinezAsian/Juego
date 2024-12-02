import pygame
import random
from constantes import WIDTH, HEIGHT

class Obstaculo_suelo:
    def __init__(self):
        self.width = 100
        self.height = 100
        self.speed = 5  # Velocidad en el eje X

        # Rutas de las imágenes para los coches
        self.imagen_coche1 = pygame.image.load("res/elementos/coche1.png")  # Coche moviéndose de derecha a izquierda
        self.imagen_coche2 = pygame.image.load("res/elementos/coche2.png")  # Coche moviéndose de izquierda a derecha

        # Escalamos las imágenes
        self.imagen_coche1 = pygame.transform.scale(self.imagen_coche1, (self.width, self.height))
        self.imagen_coche2 = pygame.transform.scale(self.imagen_coche2, (self.width, self.height))

        # Generar posición inicial aleatoria en un lado de la pantalla
        if random.choice([True, False]):  # Comenzar desde el lado izquierdo (mover hacia la derecha)
            self.x = -self.width
            self.speed = abs(self.speed)  # Mover hacia la derecha
            self.imagen = self.imagen_coche2  # Asignar imagen del coche moviéndose a la derecha
        else:  # Comenzar desde el lado derecho (mover hacia la izquierda)
            self.x = WIDTH
            self.speed = -abs(self.speed)  # Mover hacia la izquierda
            self.imagen = self.imagen_coche1  # Asignar imagen del coche moviéndose a la izquierda

        self.y = HEIGHT - self.height  # Posición fija en el suelo

    def mover(self):
        # Mover el obstáculo horizontalmente
        self.x += self.speed

    def fuera_de_pantalla(self):
        # Verifica si el obstáculo está fuera de la pantalla (completamente)
        return self.x + self.width < 0 or self.x > WIDTH

    def dibujar(self, screen):
        # Dibuja la imagen en la posición actual
        screen.blit(self.imagen, (self.x, self.y))
