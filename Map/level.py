from Character.character import Character
from Items.item import Item
from Map.block import Block
from Map.door import Door
from Map.elevator import Elevator
from Map.tunnel import Tunnel
from image import Image
from coordinate import Coordinate


class Level:
    __name: str
    __background: Image
    __items: [Item]
    __characters: [Character]
    __tunnels: [Tunnel]
    __organisation: []
    __blocks: [Block]

    def __init__(self, name: str):
        self.__name = name
        self.__items = []
        self.__characters = []
        self.__tunnels = []
        self.background = Image("")  # à mettre: image de fond par défault
        self.__organisation = []
        self.__blocks = []

    @property
    def Background(self) -> Image:
        return self.__background

    @Background.setter
    def Background(self, background: Image) -> None:
        self.__background = background

    def getName(self) -> str:
        return self.__name

    def CreateLevel(self):
        """
        On crée un niveau avec un nom, un fond, des items, des personnages, des tunnels, une organisation et des blocs
        :return:
        """

        for mob in self.__characters:
            self.__organisation.append(mob)
        for item in self.__items:
            self.__organisation.append(item)
        for tunnel in self.__tunnels:
            self.__organisation.append(tunnel)
        for block in self.__blocks:
            self.__organisation.append(block)






