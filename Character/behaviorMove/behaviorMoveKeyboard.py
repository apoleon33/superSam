from Character.behaviorMove.behaviorMove import BehaviorMove


class BehaviorMoveKeyboard(BehaviorMove):
    def move_right(self) -> None:
        self.Character.Coordinate.X += 5

    def move_left(self) -> None:
        self.Character.Coordinate.X -= 5

    def jump(self) -> None:
        self.Character.Coordinate.Y -= self.Character.jumpCount
