from Character.behaviorMove.behaviorMove import BehaviorMove
from animation import Animation
from animationSet import AnimationSet
from coordinate import Coordinate


class Character:
    __name: str
    __coordinate: Coordinate
    __behaviorMove: BehaviorMove
    __animationSet: AnimationSet
    __jumpStatus: bool

    def __init__(self, name: str, animationSet: AnimationSet) -> None:
        self.__name = name
        self.__animationSet = animationSet

    def setBehaviorMove(self, behaviorMove: BehaviorMove) -> None:
        self.__behaviorMove = behaviorMove

    def move_right(self) -> None:
        self.__animationSet.MoveRightAnimation.getFrame()
        self.__behaviorMove.move_right()

    def move_left(self) -> None:
        self.__behaviorMove.move_left()

    def jump(self) -> None:
        self.__behaviorMove.jump()
