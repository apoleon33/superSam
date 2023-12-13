from coordinate import Coordinate
from hitbox import Hitbox
from image import Image


class Tunnel:
    __type: str  # est-ce une porte ou un ascenseur
    __sprite: Image
    __coordinate: Coordinate

    __rect: Hitbox

    def __init__(self, type: str, coordinate: Coordinate):
        """
        Les tunnels sont les moyens de passer d'un niveau à l'autre

        Il en existe 2 types:

        - les ascenseurs (monter ou descendre)
        - les portes
        """
        self.__type = type
        self.__coordinate = coordinate

        if self.__type == "elevator":
            self.__sprite = Image("assets/blocks/tunnel/elevator/elevator1.png")
            self.__rect = Hitbox(
                width=128,
                height=160,
                initialCoordinate=self.__coordinate
            )
        else:
            self.__sprite = Image("assets/blocks/tunnel/porte/porte.png")
            self.__rect = Hitbox(
                width=96,
                height=160,
                initialCoordinate=self.__coordinate
            )

    @property
    def Sprite(self) -> Image:
        return self.__sprite

    @Sprite.setter
    def Sprite(self, sprite: Image) -> None:
        self.__sprite = sprite

    @property
    def Coordinate(self) -> Coordinate:
        return self.__coordinate

    @property
    def Rect(self) -> Hitbox:
        return self.__rect

    @property
    def Type(self) -> str:
        return self.__type
