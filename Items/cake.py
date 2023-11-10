from Items.item import Item
from coordinate import Coordinate
from image import Image


class Cake(Item):

    def __init__(self, coordinate: Coordinate):
        super().__init__("gâteau", Image(""), coordinate)

    def action(self):
        pass