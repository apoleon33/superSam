from abc import abstractmethod

from coordinate import Coordinate
from image import Image


class Item:
    __name: str
    __coordinate: Coordinate
    __sprite: Image

    def __init__(self, name: str, sprite: Image, coordinate: Coordinate) -> None:
        self.__name = name
        self.__sprite = sprite
        self.__coordinate = coordinate

    def getCoordinate(self) -> tuple:
        return tuple([self.__coordinate.getX(), self.__coordinate.getY()])

    def changeCoordinate(self, x: int, y: int) -> None:
        self.__coordinate.X = x
        self.__coordinate.Y = y

    @abstractmethod
    def action(self):
        """
        Méthode appelée lorsqu'un joueur active l'item depuis sont inventaire
        """
        pass

    def getName(self) -> str:
        return self.__name
