from Map.tunnel import Tunnel
from image import Image


class Door(Tunnel):
    def __init__(self):
        super().__init__("door")
        self.Image = Image("assets/blocks/porte/porte.png")
