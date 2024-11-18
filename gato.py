import pygame

class Gato:
    def __init__(self):
        # Cargamos los frames de la animación del gato para cada dirección
        self.framesDerecha = []
        self.framesIzquierda = []

        # Cargamos y escalamos los frames de la animación para la derecha
        for i in range(1, 5):
            img = pygame.image.load(f"res/walk/gato_walk{i}.png")
            #img = pygame.transform.scale(img, (30, 30))
            self.framesDerecha.append(img)

        # Cargamos y escalamos los frames de la animación para la izquierda
        for i in range(1, 5):
            img = pygame.image.load(f"res/walk/gato_walk-{i}.png")
            #img = pygame.transform.scale(img, (40, 40))
            self.framesIzquierda.append(img)

        # Variables de animación
        self.frame_index = 0
        self.animation_speed = 4
        self.frame_counter = 0
        self.direction = "right"  # Dirección inicial

        # Posición inicial del gato
        self.gatorect = self.framesDerecha[0].get_rect()  # Usamos el rectángulo de la primera imagen
        self.gatorect.center = (555/2, 260-26)  # Posición inicial en pantalla
        self.speed = 5  # Velocidad del movimiento

    def walk(self):
        # Comprueba si se ha pulsado alguna tecla
        keys = pygame.key.get_pressed()

        # Mover a la izquierda
        if keys[pygame.K_LEFT]:
            self.gatorect.x -= self.speed
            self.direction = "left"  # Actualiza la dirección
            self.frame_counter += 1

        # Mover a la derecha
        elif keys[pygame.K_RIGHT]:
            self.gatorect.x += self.speed
            self.direction = "right"  # Actualiza la dirección
            self.frame_counter += 1

        # Actualiza el índice de frame en función de la velocidad de animación
        if self.frame_counter >= self.animation_speed:
            self.frame_counter = 0
            self.frame_index = (self.frame_index + 1) % len(self.framesDerecha)

        # Selecciona el frame actual según la dirección
        if self.direction == "right":
            current_frame = self.framesDerecha[self.frame_index]
        else:
            current_frame = self.framesIzquierda[self.frame_index]

        # Devuelve el frame actual y su rectángulo (posición)
        return current_frame, self.gatorect
