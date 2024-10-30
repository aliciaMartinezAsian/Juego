import sys, pygame


def entrada():
    # Inicializamos pygame
    pygame.init()

    # Definimos dimensiones de la ventana
    size = width, height = 600, 300
    screen = pygame.display.set_mode(size)

    # Cambio el título de la ventana
    pygame.display.set_caption("Gato juego")

    # Inicializamos variables
    speed = [1, 1]
    fondo = 255,255,255

    # Crea un objeto imagen gato y obtengo su rectángulo
    gato = pygame.image.load("gato.png")
    gatorect = gato.get_rect()

    # Pongo el gato en el centro de la pantalla
    gatorect.center = (width // 2, height - 28)

    run = True
    while run:
        pygame.time.delay(10)

        # Capturamos los eventos que se han producido
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Compruebo si se ha pulsado alguna tecla
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            gatorect = gatorect.move(-1, 0)
        if keys[pygame.K_RIGHT]:
            gatorect = gatorect.move(1, 0)

        # Dibuja el fondo y el gato en la pantalla
        screen.fill(fondo)
        screen.blit(gato, gatorect)  # Dibuja el gato
        pygame.display.flip()

    # Salgo de pygame
    pygame.quit()


if __name__ == '__main__':
    entrada()

