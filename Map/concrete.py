from Map.block import Block
from coordinate import Coordinate
from image import Image


class Concrete(Block):
    def __init__(self, coordinate: Coordinate):
        super().__init__(texture=Image("assets/blocks/beton/Beton.tiff"), width=256, height=256, coordinate=coordinate)
