from Map.block import Block
from coordinate import Coordinate
from hitbox import Hitbox
from image import Image


class Concrete(Block):
    def __init__(self, coordinate: Coordinate):
        width = int(256 / 2)
        height = int(256 / 2)
        super().__init__(texture=Image("assets/blocks/beton/Beton.tiff"), width=width, height=height,
                         coordinate=coordinate)
        # self.setHitbox(Hitbox(width=width, height=height, initialCoordinate=coordinate))
