from Items.item import Item
from coordinate import Coordinate
from image import Image


class Coffee(Item):

    def __init__(self, coordinate: Coordinate):
        super().__init__("Café", Image(""), coordinate)

    def action(self):
        pass