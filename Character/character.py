from animation import Animation
from coordinate import Coordinate


class Character:
    __moveAnimation: Animation
    __coordinate: Coordinate
    __jumpAnimation: Animation

    def __init__(self, moveAnimation: Animation, coordinate: Coordinate, jumpAnimation: Animation) -> None:
        self.__moveAnimation = moveAnimation
        self.__coordinate = coordinate
        self.__jumpAnimation = jumpAnimation

    def move_right(self) -> None:
        pass

    def move_left(self) -> None:
        pass

    def getMoveAnimation(self) -> Animation:
        return self.__moveAnimation

    def getJumpAnimation(self) -> Animation:
        return self.__jumpAnimation
