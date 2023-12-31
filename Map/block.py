import pygame

from coordinate import Coordinate
from hitbox import Hitbox
from image import Image


class Block:
    __texture: Image
    __width: int
    __height: int
    __coordinate: Coordinate

    # hitbox
    __rect: Hitbox

    def __init__(self, texture: Image, width: int, height: int, coordinate: Coordinate):
        self.__texture = texture
        self.__width = width
        self.__height = width
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

    @property
    def Texture(self) -> Image:
        return self.__texture

    @Texture.setter
    def Texture(self, texture: Image) -> None:
        self.__texture = texture

    def setHitbox(self, rect: Hitbox):
        self.__rect = rect

    def getHitbox(self) -> Hitbox:
        return self.__rect
