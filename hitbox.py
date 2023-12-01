import pygame

from config import HEIGHT
from coordinate import Coordinate


class Hitbox:
    __width: int
    __height: int
    __rect: pygame.Rect

    def __init__(self, width: int, height: int, initialCoordinate: Coordinate):
        """
        Classe stockant la hitbox des personnages
        :param width: largeur de la hitbox
        :param height: hauteur de la hitbox
        :param initialCoordinate: les coordonnées ou son créées la hitbox
        """
        self.__rect = pygame.Rect(initialCoordinate.X, initialCoordinate.Y, width, height)

    @property
    def Rect(self) -> pygame.Rect:
        return self.__rect

    @Rect.setter
    def Rect(self, rect: pygame.Rect) -> None:
        self.__rect = rect
