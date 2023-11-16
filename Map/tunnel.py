from coordinate import Coordinate
from image import Image


class Tunnel:
    __type: str  # est-ce une porte ou un ascenseur
    __sprite: Image
    __coordinate: Coordinate

    def __init__(self, typ: str):
        """
        Les tunnels sont les moyens de passer d'un niveau à l'autre

        Il en existe 2 types:

        - les ascenseurs (monter ou descendre)
        - les portes
        """
        self.__type = typ
