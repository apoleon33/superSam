from Items.item import Item
from coordinate import Coordinate
from image import Image


class Cutter(Item):

    def __init__(self, coordinate: Coordinate):
        super().__init__("Cutter", Image(""), coordinate)

    def action(self):
        pass