import pygame

class Gato:
    def __init__(self):
        # Cargamos los frames de la animación del gato para cada dirección
        self.framesDerecha = list()
        for i in range(1, 5):
           self.framesDerecha.append(f"res/walk/gato_walk{i}.png")
           pygame.image.load(f"res/walk/gato_walk{i}.png")

        self.framesIzquierda = list()
        for i in range(1, 5):
            self.framesIzquierda.append(f"res/walk/gato_walk-{i}.png")
            pygame.image.load(f"res/walk/gato_walk-{i}.png")

        self.frame_index = 0
        self.animation_speed = 4
        self.frame_counter = 0
        self.direction = "right"

        # Definimos la posición inicial del gato
        self.gatorect = self.framesDerecha[0].get_rect()
        self.gatorect.center = (555 // 2, 260 - 28)
        self.speed = [1, 1]

    def walk(self):
        # Compruebo si se ha pulsado alguna tecla
        keys = pygame.key.get_pressed()

        # Mover a la izquierda
        if keys[pygame.K_LEFT]:
            self.gatorect = self.gatorect.move(-1, 0)
            self.direction = "left"  # Actualiza la dirección
            self.frame_counter += 1

        # Mover a la derecha
        elif keys[pygame.K_RIGHT]:
            self.gatorect = self.gatorect.move(1, 0)
            self.direction = "right"  # Actualiza la dirección
            self.frame_counter += 1


        # Selecciona el frame actual según la dirección
        if self.direction == "right":
            current_frame = self.framesDerecha[self.frame_index]
        else:
            current_frame = self.framesIzquierda[self.frame_index]

        # Devolver el frame actual y su rectángulo (posición)
        return current_frame, self.gatorect
