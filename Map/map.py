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

    @property
    def Width(self) -> int:
        return self.__width

    @Width.setter
    def Width(self, width: int) -> None:
        self.__width = width

    @property
    def Height(self) -> int:
        return self.__height

    @Height.setter
    def Height(self, height: int) -> None:
        self.__height = height

    def addLevel(self, x: int, y: int, level: Level):
        while y > len(self.__levels):
            self.__levels.append([])

        while x > len(self.__levels[y]):
            self.__levels[y].append(EmptyLevel())

        self.__levels[y][x] = level

    def getLevel(self, x: int, y: int) -> Level:
        return self.__levels[y][x]
