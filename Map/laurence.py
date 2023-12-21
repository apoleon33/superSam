from Map.block import Block
from coordinate import Coordinate
from hitbox import Hitbox
from image import Image


class Laurence(Block):
    def __init__(self, coordinate: Coordinate):
        width = 32
        height = 128

        super().__init__(
            texture=Image("assets/blocks/laurence/laurence.png"),
            width=width,
            height=height,
            coordinate=coordinate
        )
        self.setHitbox(Hitbox(
            width=width,
            height=height,
            initialCoordinate=coordinate
        ))
