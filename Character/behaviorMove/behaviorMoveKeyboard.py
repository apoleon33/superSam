from Character.behaviorMove.behaviorMove import BehaviorMove
from config import MAIN_CHARACTER_SPEED


class BehaviorMoveKeyboard(BehaviorMove):
    def move_right(self) -> None:
        self.Character.Coordinate.X += MAIN_CHARACTER_SPEED

    def move_left(self) -> None:
        self.Character.Coordinate.X -= MAIN_CHARACTER_SPEED

    def jump(self) -> None:
        self.Character.Coordinate.Y -= self.Character.jumpCount
