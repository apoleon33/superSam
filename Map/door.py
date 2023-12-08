from Map.tunnel import Tunnel
from coordinate import Coordinate


class Door(Tunnel):
    def __init__(self, coordinate: Coordinate):
        super().__init__("door", coordinate)
