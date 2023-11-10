class Image:
    __path: str

    def __init__(self, path: str):
        self.__path = path

    def getPath(self) -> str:
        return self.__path

    def setPath(self, path: str) -> None:
        self.__path = path
