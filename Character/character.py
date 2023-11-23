from Character.behaviorMove.behaviorMove import BehaviorMove
from animation import Animation
from animationSet import AnimationSet
from coordinate import Coordinate
from image import Image


class Character:
    __name: str
    __coordinate: Coordinate
    __behaviorMove: BehaviorMove
    __animationSet: AnimationSet
    __jumpStatus: bool

    __currentAnimation: Image

    def __init__(self, name: str, animationSet: AnimationSet) -> None:
        self.__name = name
        self.__animationSet = animationSet
        self.__currentAnimation = self.__animationSet.getmoveRightAnimation()
        self.__coordinate = Coordinate(0, 0)

    def setBehaviorMove(self, behaviorMove: BehaviorMove) -> None:
        self.__behaviorMove = behaviorMove
        if self.__behaviorMove.Character is not self:
            self.__behaviorMove.Character = self

    def move_right(self):
        self.__behaviorMove.move_right()
        self.__currentAnimation = self.__animationSet.getmoveRightAnimation()

    def move_left(self):
        self.__behaviorMove.move_left()
        self.__currentAnimation = self.__animationSet.getmoveLeftAnimation()

    def jump(self):
        self.__behaviorMove.jump()
        self.__currentAnimation = self.__animationSet.getJumpAnimation()

    def doNothing(self):
        self.__currentAnimation = self.__animationSet.afkImage

    # getter de __currentAnimation
    def getCurrentAnimation(self) -> Image:
        return self.__currentAnimation

    @property
    def Coordinate(self) -> Coordinate:
        return self.__coordinate
