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

    def Level(self, name: str):
        self.__name = name

    def CreateLevel(self):
        """
        On crée un niveau avec un nom, un fond, des items, des personnages, des tunnels, une organisation et des blocs
        :return:
        """
        self.__level = Level("")
        self.__level.Background = Image("")
        self.__level.addBlock(Block(Image(""), 0, 0, Coordinate(0, 0)))
        self.__level.addTunnel(Door(Image(""), 0, 0, Coordinate(0, 0)))
        self.__level.addTunnel(Elevator(Image(""), 0, 0, Coordinate(0, 0)))
        self.__level.addItem(Item(Image(""), 0, 0, Coordinate(0, 0)))
        self.__level.addCharacter(Character(Coordinate(0, 0)))

    def LoadFromImage(self, image: Image):
        self.__image = image

    def addBlock(self, param):
        pass

    def addTunnel(self, param):
        pass

    def addItem(self, param):
        pass

    def addCharacter(self, param):
        pass
