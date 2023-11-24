from Character.character import Character
from Items.inventory import Inventory
from animationSet import AnimationSet
from coordinate import Coordinate
from image import Image


class MainCharacter(Character):
    __inventory = Inventory

    def __init__(self, coordinate: Coordinate):
        moveAnimation = AnimationSet()

        moveAnimation.setImageFromDirectory("assets/character/sam", [8, 8, 7])
        super().__init__("Sam", moveAnimation)
