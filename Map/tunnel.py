from coordinate import Coordinate
from image import Image


class Tunnel:
    __type: str  # est-ce une porte ou un ascenseur
    __sprite: Image
    __coordinate: Coordinate

    def __init__(self, type: str):
        """
        Les tunnels sont les moyens de passer d'un niveau à l'autre

        Il en existe 2 types:

        - les ascenseurs (monter ou descendre)
        - les portes
        """
        self.__type = type

        if self.__type == "elevator":
            self.__sprite = Image("assets/tunnel/elevator/elevator1.png")
        else :
            self.__sprite = Image("assets/blocks/tunnel/porte/porte.png")

    @property
    def Sprite(self) -> Image:
        return self.__sprite

    @Sprite.setter
    def Sprite(self, sprite: Image) -> None:
        self.__sprite = sprite

    def Tunnel(self, type: str): #On un type, une image et une position à l'attribut Tunnel
       self.__type = type
       self.__sprite = Image("")
       self.__coordinate = Coordinate(0, 0)








