import pygame
from menu_principal import MenuPrincipal
from juego import Juego


def entrada():

    while True:
        # Mostrar menú principal
        menu = MenuPrincipal()
        menu.ejecutar()

        # Iniciar juego al salir del menú
        juego = Juego()


if __name__ == "__main__":
    entrada()
