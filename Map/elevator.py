from Map.tunnel import Tunnel
from coordinate import Coordinate
from image import Image


class Elevator(Tunnel):
    def __init__(self, coordinate: Coordinate):
        super().__init__("elevator", coordinate)
