from pytmx import TiledTileset

from Character.character import Character
from Items.item import Item
from Map.block import Block
from Map.concrete import Concrete
from Map.door import Door
from Map.elevator import Elevator
from Map.fire import Fire
from Map.grass import Grass
from Map.offensiveBlock import OffensiveBlock
from Map.tmxMap import TmxMap
from Map.tunnel import Tunnel
from hitbox import Hitbox
from image import Image
from coordinate import Coordinate


class Level:
    __name: str
    __background: Image

    __items: [Item]
    __characters: [Character]
    __tunnels: [Tunnel]
    __blocks: list[Block]
    __offensiveBlocks: list[OffensiveBlock]

    __organisation: []  # je sais même pas si je l'utilise
    __hitboxes: list[Hitbox]
    __offensiveHitboxes: list[Hitbox]
    __mainCharacterSpawn: Coordinate

    __tmx: TmxMap

    def __init__(self, name: str):
        self.__name = name
        self.__items = []
        self.__characters = []
        self.__tunnels = []
        self.__background = Image("assets/levels/forest.jpg")  # à mettre: image de fond par défault
        self.__organisation = []
        self.__blocks = []
        self.__offensiveBlocks = []
        self.__offensiveHitboxes = []
        self.__hitboxes = []
        self.__mainCharacterSpawn = Coordinate(0, 0)

    @property
    def Background(self) -> Image:
        return self.__background

    @Background.setter
    def Background(self, background: Image) -> None:
        self.__background = background

    def getName(self) -> str:
        return self.__name

    def createLevel(self):
        """
        on remplis les listes de tunnels et de blocks, en se basant sur les données du tmx
        :return:
        """
        possibleName = ["beton", "grass", "door", "elevator"]
        possibleBlocs = [Concrete, Grass, Door, Elevator]

        data = self.__tmx.getData()
        # création des blocs de la map
        tilesets: list[TiledTileset] = data.tilesets

        blocs: list[list[int]] = data.layers[0].data
        tiledGildmap = data.tiledgidmap

        x, y = 0, 0
        for ligne in range(len(blocs)):
            for colonne in range(len(blocs[ligne])):
                bloc = blocs[ligne][colonne]
                if bloc != 0:
                    convertedBloc = tiledGildmap[bloc]
                    for elements in tilesets:
                        if elements.firstgid == convertedBloc:
                            match elements.name:
                                case "grass":
                                    self.addBlock(Grass(Coordinate(x, y)))
                                case "beton":
                                    self.addBlock(Concrete(Coordinate(x, y)))

                                case "door":
                                    self.addTunnel(Door(Coordinate(x, y)))

                                case "elevator":
                                    self.addTunnel(Elevator(Coordinate(x, y)))

                                case "fire":
                                    self.addOffensiveBlock(Fire(Coordinate(x, y)))

                x += 32
            y += 32
            x = 0

        # création des hitboxes de la map
        objets = self.__tmx.getObject()
        for object in objets:
            if object.type == "collision":
                self.addHitbox(
                    Hitbox(
                        width=object.width,
                        height=object.height,
                        initialCoordinate=Coordinate(
                            x=object.x,
                            y=object.y
                        )
                    )
                )
            elif object.type == "fire":
                self.addOffensiveHitbox(
                    Hitbox(
                        width=object.width,
                        height=object.height,
                        initialCoordinate=Coordinate(
                            x=object.x,
                            y=object.y
                        )
                    )
                )

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

    def getCharacters(self) -> list[Character]:
        """
        On récupère les personnages du niveau
        :return: les personnages du niveau
        """
        return self.__characters

    def getBlocks(self) -> list[Block]:
        """
        On récupère les blocs du niveau
        :return: les blocs du niveau
        """
        return self.__blocks

    def getItems(self) -> list[Item]:
        """
        On récupère les items du niveau
        :return: les items du niveau
        """
        return self.__items

    def getTunnels(self) -> list[Tunnel]:
        """
        On récupère les tunnels du niveau
        :return: les tunnels du niveau
        """
        return self.__tunnels

    def addHitbox(self, hitbox: Hitbox):
        self.__hitboxes.append(hitbox)

    def addOffensiveHitbox(self, hitbox: Hitbox):
        self.__offensiveHitboxes.append(hitbox)

    def getHitboxes(self) -> list[Hitbox]:
        return self.__hitboxes

    def getOffensiveHitboxes(self) -> list[Hitbox]:
        return self.__offensiveHitboxes

    def setTmx(self, path: str):
        self.__tmx = TmxMap(path)

    def getTmx(self) -> TmxMap:
        return self.__tmx

    @property
    def MainCharacterSpawn(self) -> Coordinate:
        return self.__mainCharacterSpawn

    @MainCharacterSpawn.setter
    def MainCharacterSpawn(self, coodinate: Coordinate):
        self.__mainCharacterSpawn = coodinate

    def addOffensiveBlock(self, offensiveBlock: Block):
        self.__offensiveBlocks.append(offensiveBlock)

    def getOffensiveBlocks(self) -> list[OffensiveBlock]:
        return self.__offensiveBlocks
