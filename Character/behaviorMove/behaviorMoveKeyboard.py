from Character.behaviorMove.behaviorMove import BehaviorMove
from config import MAIN_CHARACTER_SPEED


class BehaviorMoveKeyboard(BehaviorMove):
    def move_right(self) -> int:
        return MAIN_CHARACTER_SPEED

    def move_left(self) -> int:
        return (-1) * MAIN_CHARACTER_SPEED

    def jump(self) -> int:
        return -20
