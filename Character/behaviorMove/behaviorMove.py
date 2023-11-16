from abc import ABC, abstractmethod
from typing import Any


class BehaviorMove(ABC):
    __character: Any  # Any pour éviter une dépendance circulaire

    @abstractmethod
    def move_right(self) -> None:
        pass

    @abstractmethod
    def move_left(self) -> None:
        pass

    @abstractmethod
    def jump(self) -> None:
        pass

    @property
    def Character(self) -> Any:
        return self.__character

    @Character.setter
    def Character(self, character: Any) -> None:
        self.__character = character
