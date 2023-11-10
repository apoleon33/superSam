class Coordinate:
    __x: int
    __y: int

    def __init__(self, x: int, y: int) -> None:
        self.__x = x
        self.__y = y

    def setCoordinates(self, x: int, y: int) -> None:
        self.setX(x)
        self.setY(y)

    def getX(self) -> int:
        return self.__x

    def setX(self, x: int) -> None:
        self.__x = x

    def getY(self) -> int:
        return self.__y

    def setY(self, y: int) -> int:
        self.__y = y
