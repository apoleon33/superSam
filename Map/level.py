from Character.character import Character
from Items.item import Item
from Map.block import Block
from Map.tunnel import Tunnel
from image import Image


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
        pass

    def LoadFromImage(self, image: Image):
        self.__image = image
