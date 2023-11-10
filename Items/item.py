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

    @abstractmethod
    def action(self):
        pass

    def getName(self) -> str:
        return self.__name
