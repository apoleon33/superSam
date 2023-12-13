from Map.block import Block
from coordinate import Coordinate
from hitbox import Hitbox
from image import Image


class Grass(Block):
    def __init__(self, coordinate: Coordinate):
        width = 32
        height = 32
        super().__init__(
            texture=Image("assets/blocks/grass/grass.png"),
            width=width,
            height=height,
            coordinate=coordinate
        )
        self.setHitbox(Hitbox(
            width=width,
            height=height,
            initialCoordinate=coordinate
        ))
