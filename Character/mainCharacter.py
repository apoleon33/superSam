from Character.character import Character
from Items.inventory import Inventory
from animationSet import AnimationSet
from coordinate import Coordinate


class MainCharacter(Character):
    __inventory = Inventory

    def __init__(self, coordinate: Coordinate):
        moveAnimation = AnimationSet()
        # ici on ajoutera les différentes animations à la main
        super().__init__("Sam", moveAnimation)
