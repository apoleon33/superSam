from Map.level import Level
from image import Image


class EmptyLevel(Level):
    def __init__(self):
        """ Un niveau vide, que le personnage ne visitera probablement jamais"""
        super().__init__("empty")
        self.Background = Image(None)
