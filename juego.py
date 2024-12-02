import pygame
import sys
import random

from gato import Gato
from obstaculo_cielo import Obstaculo_cielo
from obstaculo_suelo import Obstaculo_suelo
from menu_game_over import Menu_Game_Over
from constantes import WIDTH, HEIGHT

class Juego:
    def __init__(self):
        pygame.init()

        # Dimensiones del fondo y ventana
        self.WIDTH, self.HEIGHT = WIDTH, HEIGHT
        size = (self.WIDTH, self.HEIGHT)
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Gato juego")
        icono = pygame.image.load("res/elementos/icon.png")
        pygame.display.set_icon(icono)

        # Cargar fondo
        self.fondo = pygame.image.load("res/elementos/fondo.jpeg")

        # Inicializar personaje y música
        self.gato = Gato()
        self.musica_juego = pygame.mixer.Sound("res/sounds/juego.mp3")
        self.musica_juego.play(loops=-1)

        # Gestión de obstáculos
        self.obstaculos = []
        self.tiempo_ultimo_obstaculo_cielo = pygame.time.get_ticks()
        self.tiempo_ultimo_obstaculo_suelo = pygame.time.get_ticks()
        self.intervalo_generacion_cielo = 1000  # Inicialmente, obstáculos que caen cada 1000 ms
        self.intervalo_generacion_suelo = 3000  # Inicialmente, obstáculos que cruzan cada 3000 ms
        self.tiempo_inicio = pygame.time.get_ticks()  # Guardar el tiempo de inicio del juego

        # Gestión de vidas
        self.vidas = 7
        self.corazon_img = pygame.image.load("res/elementos/vida.png")

        self.clock = pygame.time.Clock()
        self.running = True

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            tiempo_actual = pygame.time.get_ticks()
            tiempo_transcurrido = (tiempo_actual - self.tiempo_inicio) // 1000  # Tiempo en segundos

            # Aumentar dificultad reduciendo los intervalos de generación
            self.intervalo_generacion_cielo = max(300, 1000 - tiempo_transcurrido * 10)  # Mínimo 300 ms
            self.intervalo_generacion_suelo = max(1000, 3000 - tiempo_transcurrido * 20)  # Mínimo 1000 ms

            # Generar obstáculos del cielo
            if tiempo_actual - self.tiempo_ultimo_obstaculo_cielo > self.intervalo_generacion_cielo:
                nuevo_obstaculo_cielo = Obstaculo_cielo()
                self.obstaculos.append(nuevo_obstaculo_cielo)
                self.tiempo_ultimo_obstaculo_cielo = tiempo_actual

            # Generar obstáculos del suelo
            if tiempo_actual - self.tiempo_ultimo_obstaculo_suelo > self.intervalo_generacion_suelo:
                nuevo_obstaculo_suelo = Obstaculo_suelo()
                self.obstaculos.append(nuevo_obstaculo_suelo)
                self.tiempo_ultimo_obstaculo_suelo = tiempo_actual

            # Dibujar fondo
            self.screen.blit(self.fondo, (0, 0))

            # Dibujar vidas (corazones)
            for i in range(self.vidas):
                self.screen.blit(self.corazon_img, (10 + i * 40, 10))

            # Animar al gato
            frame_actual, gatorect = self.gato.walk_and_jump()
            self.screen.blit(frame_actual, gatorect)

            # Manejo de obstáculos
            for obstaculo in self.obstaculos[:]:
                obstaculo.mover()
                obstaculo.dibujar(self.screen)
                obstaculo_rect = pygame.Rect(obstaculo.x, obstaculo.y, obstaculo.width, obstaculo.height)

                # Colisión con el gato
                if gatorect.colliderect(obstaculo_rect):
                    self.vidas -= 1
                    self.obstaculos.remove(obstaculo)
                    if self.vidas == 0:
                        print("Fin del juego")
                        self.musica_juego.stop()
                        self.running = False
                        menu_game_over = Menu_Game_Over()
                        menu_game_over.ejecutar()

                # Eliminar obstáculos fuera de la pantalla
                if obstaculo.fuera_de_pantalla():
                    self.obstaculos.remove(obstaculo)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        print("Juego terminado")

