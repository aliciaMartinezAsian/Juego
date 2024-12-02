import pygame
from constantes import WIDTH, HEIGHT

class Gato:
    def __init__(self):
        # Inicializamos como antes
        self.framesDerecha = []
        self.framesIzquierda = []
        self.framesSaltoDerecha = []
        self.framesSaltoIzquierda = []

        # Cargar animaciones
        for i in range(1, 5):
            img = pygame.image.load(f"res/jump/gato_jump{i}.png")
            img = pygame.transform.scale(img, (50, 50))
            self.framesSaltoDerecha.append(img)
            img = pygame.image.load(f"res/jump/gato_jump-{i}.png")
            img = pygame.transform.scale(img, (50, 50))
            self.framesSaltoIzquierda.append(img)
        for i in range(1, 5):
            img = pygame.image.load(f"res/walk/gato_walk{i}.png")
            img = pygame.transform.scale(img, (50, 50))
            self.framesDerecha.append(img)
            img = pygame.image.load(f"res/walk/gato_walk-{i}.png")
            img = pygame.transform.scale(img, (50, 50))
            self.framesIzquierda.append(img)

        # Variables de animación y posición
        self.frame_index = 0
        self.animation_speed = 4
        self.frame_counter = 0
        self.direction = "right"
        self.moving = False

        # Física del salto
        self.is_jumping = False
        self.jump_speed = 15
        self.vertical_speed = 0
        self.gravity = 1

        # Posición inicial
        self.gatorect = self.framesDerecha[0].get_rect()
        self.gatorect.center = (WIDTH / 2, HEIGHT - 26)
        self.speed = 5

    def walk_and_jump(self):
        # Manejo del teclado
        keys = pygame.key.get_pressed()

        self.moving = False

        # Movimiento horizontal
        if keys[pygame.K_LEFT]:
            self.gatorect.x -= self.speed
            self.direction = "left"
            self.moving = True
        elif keys[pygame.K_RIGHT]:
            self.gatorect.x += self.speed
            self.direction = "right"
            self.moving = True

        # Salto
        if not self.is_jumping and keys[pygame.K_SPACE]:
            self.is_jumping = True
            self.vertical_speed = -self.jump_speed

        # Física del salto
        if self.is_jumping:
            self.gatorect.y += self.vertical_speed
            self.vertical_speed += self.gravity

            # Terminar el salto al tocar el suelo
            if self.gatorect.bottom >= HEIGHT - 26:
                self.gatorect.bottom = HEIGHT - 26
                self.is_jumping = False

        # Actualizar frame de animación
        if self.moving or self.is_jumping:
            self.frame_counter += 1
            if self.frame_counter >= self.animation_speed:
                self.frame_counter = 0
                self.frame_index = (self.frame_index + 1) % len(self.framesDerecha)

        # Selección de frame actual
        if self.is_jumping:
            if self.direction == "right":
                current_frame = self.framesSaltoDerecha[self.frame_index]
            else:
                current_frame = self.framesSaltoIzquierda[self.frame_index]
        else:
            if self.direction == "right":
                current_frame = self.framesDerecha[self.frame_index]
            else:
                current_frame = self.framesIzquierda[self.frame_index]

        # Restricción de movimiento
        if self.gatorect.left < 0:
            self.gatorect.left = 0
        if self.gatorect.right > WIDTH:
            self.gatorect.right = WIDTH

        return current_frame, self.gatorect



