from abc import ABC, abstractmethod
from typing import Any


class BehaviorMove(ABC):
    __character: Any  # Any pour éviter une dépendance circulaire

    def __init__(self):
        self.__character = None

    @abstractmethod
    def move_right(self) -> int:
        pass

    @abstractmethod
    def move_left(self) -> int:
        pass

    @abstractmethod
    def jump(self) -> int:
        pass

    @property
    def Character(self) -> Any:
        return self.__character

    @Character.setter
    def Character(self, character: Any) -> None:
        self.__character = character
