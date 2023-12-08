from Character.character import Character
from Items.item import Item
from Map.block import Block
from Map.concrete import Concrete
from Map.door import Door
from Map.elevator import Elevator
from Map.tmxMap import TmxMap
from Map.tunnel import Tunnel
from image import Image
from coordinate import Coordinate


def loadFromBnp(self, image: Image):
    """
    On charge un niveau à partir d'une image
    :param image:
    :return:
    """
    pass


class Level:
    __name: str
    __background: Image
    __items: [Item]
    __characters: [Character]
    __tunnels: [Tunnel]
    __organisation: []
    __blocks: [Block]

    __tmx: TmxMap

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

    def createLevel(self):

        blocs: list[list[int]] = self.__tmx.getData().layers[0].data
        x, y = 0, 0

        for ligne in range(len(blocs)):
            for colonne in range(len(blocs[ligne])):
                match blocs[ligne][colonne]:
                    # TODO: unifier pour que les codes soient les mêmes pour tt les fichiers
                    case 1:  # béton
                        self.addBlock(Concrete(Coordinate(x, y)))

                    case 25:  # porte
                        self.addTunnel(Door(Coordinate(x, y)))

                    case _:  # si c'est vide
                        pass
                x += 32
            y += 32
            x = 0

    def addCharacter(self, character: Character):
        """
        On ajoute un personnage au niveau
        :param character: le personnage à ajouter
        :return: Rien
        """
        self.__characters.append(character)

    def addBlock(self, block: Block):
        """
        On ajoute un bloc au niveau
        :param block: le bloc à ajouter
        :return: Rien
        """
        self.__blocks.append(block)

    def addItem(self, item: Item):
        """
        On ajoute un item au niveau
        :param item: l'item à ajouter
        :return: Rien
        """
        self.__items.append(item)

    def addTunnel(self, tunnel: Tunnel):
        """
        On ajoute un tunnel au niveau
        :param tunnel: le tunnel à ajouter
        :return: Rien
        """
        self.__tunnels.append(tunnel)

    def getCharacters(self) -> [Character]:
        """
        On récupère les personnages du niveau
        :return: les personnages du niveau
        """
        return self.__characters

    def getBlocks(self) -> [Block]:
        """
        On récupère les blocs du niveau
        :return: les blocs du niveau
        """
        return self.__blocks

    def getItems(self) -> [Item]:
        """
        On récupère les items du niveau
        :return: les items du niveau
        """
        return self.__items

    def getTunnels(self) -> [Tunnel]:
        """
        On récupère les tunnels du niveau
        :return: les tunnels du niveau
        """
        return self.__tunnels

    def setTmx(self, path: str):
        self.__tmx = TmxMap(path)

    def getTmx(self) -> TmxMap:
        return self.__tmx
