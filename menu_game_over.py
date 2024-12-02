import pygame
import sys
from constantes import WIDTH_MENU, HEIGHT_MENU

class Menu_Game_Over:
    def __init__(self):
        pygame.init()

        # Inicializar el sistema de sonido
        pygame.mixer.init()

        # Cargar y reproducir la música de fondo para el Game Over
        self.musica_end = pygame.mixer.Sound("res/sounds/end.mp3")
        self.musica_end.play(loops=-1)  # Reproducir indefinidamente

        # Configuración de pantalla
        self.screen = pygame.display.set_mode((WIDTH_MENU, HEIGHT_MENU))
        pygame.display.set_caption("Game Over")

        icono = pygame.image.load("res/elementos/icon.png")
        pygame.display.set_icon(icono)

        # Color de fondo
        self.fondo_color = (0, 0, 0)  # Negro

        # Ruta de la fuente personalizada
        fuente_path = "res/fuentes/pixel.ttf"

        # Configurar fuente
        self.fuente = pygame.font.Font(fuente_path, 60)
        self.fuente_titulo = pygame.font.Font(fuente_path, 100)  # Fuente más grande para el título

        # Configurar colores
        self.color_normal = (255, 255, 255)  # Blanco
        self.color_hover = (200, 200, 0)    # Amarillo

        # Crear botones como listas de texto, posición y acción
        self.botones = [
            {"texto": "Volver a jugar", "x": WIDTH_MENU // 2 - 150, "y": HEIGHT_MENU // 2 - 60, "accion": self.volver_a_jugar},
            {"texto": "Salir", "x": WIDTH_MENU // 2 - 50, "y": HEIGHT_MENU // 2 + 20, "accion": self.salir_juego},
        ]

        self.running = True  # Estado del menú

    def volver_a_jugar(self):
        self.musica_end.stop()  # Detener la música al volver a jugar
        self.running = False  # Salir del menú para reiniciar el juego

    def salir_juego(self):
        self.musica_end.stop()  # Detener la música antes de salir
        pygame.quit()
        sys.exit()

    def _get_boton_rect(self, boton):

        texto_renderizado = self.fuente.render(boton["texto"], True, self.color_normal)
        return texto_renderizado.get_rect(topleft=(boton["x"], boton["y"]))

    def dibujar(self):

        self.screen.fill(self.fondo_color)  # Pintar el fondo

        # Título "Game Over"
        titulo = self.fuente_titulo.render("Game Over", True, self.color_normal)
        titulo_rect = titulo.get_rect(center=(WIDTH_MENU // 2, HEIGHT_MENU // 4))
        self.screen.blit(titulo, titulo_rect.topleft)

        # Dibujar botones
        for boton in self.botones:
            # Determinar si el mouse está sobre el botón
            mouse_pos = pygame.mouse.get_pos()
            rect = self._get_boton_rect(boton)
            color = self.color_hover if rect.collidepoint(mouse_pos) else self.color_normal

            # Renderizar el texto del botón
            texto_renderizado = self.fuente.render(boton["texto"], True, color)
            self.screen.blit(texto_renderizado, rect.topleft)

        pygame.display.flip()  # Actualizar la pantalla

    def manejar_eventos(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.salir_juego()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for boton in self.botones:
                    rect = self._get_boton_rect(boton)
                    if rect.collidepoint(event.pos):
                        boton["accion"]()

    def ejecutar(self):

        clock = pygame.time.Clock()

        while self.running:
            self.manejar_eventos()
            self.dibujar()
            clock.tick(60)

