class Coordinate:
    __x: int
    __y: int

    def __init__(self, x: int, y: int) -> None:
        self.__x = x
        self.__y = y

    @property
    def X(self) -> int:
        return self.__x

    @X.setter
    def X(self, x: int) -> None:
        self.__x = x

    @property
    def Y(self) -> int:
        return self.__y

    @Y.setter
    def Y(self, y: int) -> None:
        self.__y = y
