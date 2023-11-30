from coordinate import Coordinate
from image import Image

class Block:
    __texture: Image
    __width: int
    __height: int
    __coordinate: Coordinate

    def __init__(self, texture: Image, width: int, height: int, coordinate: Coordinate):
        self.__texture = Image("assets/blocks/beton/Beton.tiff")
        self.__width = 0
        self.__height = 0
        self.__coordinate = coordinate

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

    @property
    def Coordinate(self) -> Coordinate:
        return self.__coordinate

    @Coordinate.setter
    def Coordinate(self, coordinate: Coordinate) -> None:
        self.__coordinate = coordinate


