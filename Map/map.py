from Map.emptyLevel import EmptyLevel
from Map.level import Level


class Map:
    __levels: [[Level]]
    __width: int
    __height: int

    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height
        self.__levels = [[EmptyLevel()]]  # on commence au moins avec 1 niveau vide, en haut à gauche de la map

