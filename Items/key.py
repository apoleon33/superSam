from Items.item import Item
from coordinate import Coordinate
from image import Image


class Key(Item):

    def __init__(self, coordinate: Coordinate):
        super().__init__("clé", Image(""), coordinate)

    def action(self):
        pass