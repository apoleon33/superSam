from Character.behaviorMove.behaviorMove import BehaviorMove
from animationSet import AnimationSet
from coordinate import Coordinate
from image import Image


class Character:
    __name: str
    __coordinate: Coordinate
    __behaviorMove: BehaviorMove
    __animationSet: AnimationSet
    __leftStatus: bool

    __jumpStatus: bool
    __maxJumpHeight: int
    __jumpCount: int

    __currentAnimation: Image

    def __init__(self, name: str, animationSet: AnimationSet) -> None:
        self.__name = name
        self.__animationSet = animationSet
        self.__currentAnimation = self.__animationSet.getMoveRightAnimation()
        self.__coordinate = Coordinate(0, 0)

        self.__maxJumpHeight = 10
        self.__jumpStatus = False
        self.__jumpCount = 30

    def setBehaviorMove(self, behaviorMove: BehaviorMove) -> None:
        self.__behaviorMove = behaviorMove
        if self.__behaviorMove.Character is not self:
            self.__behaviorMove.Character = self

    def move_right(self):
        self.__behaviorMove.move_right()
        self.__currentAnimation = self.__animationSet.getMoveRightAnimation()
        self.__leftStatus = False

    def move_left(self):
        self.__behaviorMove.move_left()
        self.__currentAnimation = self.__animationSet.getMoveLeftAnimation()
        self.__leftStatus = True

    def jump(self):
        self.__jumpStatus = True
        self.__currentAnimation = self.__animationSet.getJumpAnimation()

    def checkJump(self):
        if self.__jumpStatus:
            self.__behaviorMove.jump()

            if self.__jumpCount > - self.__maxJumpHeight:
                self.__jumpCount -= 1
            else:
                self.__jumpStatus = False
                self.__jumpCount = 30

    def doNothing(self):
        self.__currentAnimation = self.__animationSet.afkImage
        self.__leftStatus = False

    def getCurrentAnimation(self) -> Image:
        return self.__currentAnimation

    @property
    def Coordinate(self) -> Coordinate:
        return self.__coordinate

    @property
    def leftStatus(self) -> bool:
        return self.__leftStatus

    @leftStatus.setter
    def leftStatus(self, leftStatus: bool) -> None:
        self.__leftStatus = leftStatus

    @property
    def jumpCount(self) -> int:
        return self.__jumpCount

    @jumpCount.setter
    def jumpCount(self, jumpCount: int) -> None:
        self.__jumpCount = jumpCount
