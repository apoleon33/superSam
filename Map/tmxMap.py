import pytmx
from pytmx import TiledMap

from image import Image


class TmxMap:
    __file: Image
    __tmxData: pytmx.TiledMap

    def __init__(self, path):
        self.__file = Image(path=path)
        self.__loadData()

    def __loadData(self):
        self.__tmxData = pytmx.util_pygame.load_pygame(self.__file.getPath())

    def getBlocks(self) -> list:
        blockList = []
        for objects in self.__tmxData.objects:
            if objects.type == "collision":
                blockList.append(objects)

        return blockList

    def getTunnels(self) -> list:
        tunnelList = []
        for objects in self.__tmxData.objects:
            if objects.type == "tunnel":
                tunnelList.append(objects)

        return tunnelList

    def getLayout(self) -> list:
        return self.__tmxData.layers

    def getData(self) -> TiledMap:
        return self.__tmxData
