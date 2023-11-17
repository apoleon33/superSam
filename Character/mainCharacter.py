from Character.character import Character
from Items.inventory import Inventory
from animationSet import AnimationSet
from coordinate import Coordinate
from image import Image


class MainCharacter(Character):
    __inventory = Inventory

    def __init__(self, coordinate: Coordinate):
        moveAnimation = AnimationSet()

        # right animation
        moveAnimation.MoveRightAnimation.addFrame(Image("assets/character/sam/right/1.png"))
        moveAnimation.MoveRightAnimation.addFrame(Image("assets/character/sam/right/2.png"))
        moveAnimation.MoveRightAnimation.addFrame(Image("assets/character/sam/right/3.png"))

        super().__init__("Sam", moveAnimation)