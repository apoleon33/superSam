from animation import Animation


class AnimationSet:
    __moveRightAnimation: Animation
    __moveLeftAnimation: Animation
    __jumpAnimation: Animation

    @property
    def MoveRightAnimation(self) -> Animation:
        return self.__moveRightAnimation

    @MoveRightAnimation.setter
    def MoveRightAnimation(self, moveRightAnimation: Animation) -> None:
        self.__moveRightAnimation = moveRightAnimation

    @property
    def MoveLeftAnimation(self) -> Animation:
        return self.__moveLeftAnimation

    @MoveLeftAnimation.setter
    def MoveLeftAnimation(self, moveLeftAnimation: Animation) -> None:
        self.__moveLeftAnimation = moveLeftAnimation

    @property
    def JumpAnimation(self) -> Animation:
        return self.__jumpAnimation

    @JumpAnimation.setter
    def JumpAnimation(self, jumpAnimation: Animation) -> None:
        self.__jumpAnimation = jumpAnimation
