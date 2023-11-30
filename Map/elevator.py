from Map.tunnel import Tunnel
from image import Image


class Elevator(Tunnel):
    def __init__(self):
        super().__init__("elevator")