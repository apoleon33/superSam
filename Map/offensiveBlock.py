from abc import ABC

from Map.block import Block
from animationSet import AnimationSet
from coordinate import Coordinate
from image import Image


class OffensiveBlock(Block, ABC):
    __animationSet: AnimationSet


    def __init__(self, texture: Image, width: int, height: int, coordinate: Coordinate):
        """
        classe abstraite pour les blocks ayant une animation et non pas une texture
        :param texture: texture de base
        :param width: largeur à afficher de l'image
        :param height: longueur à afficher de l'image
        :param coordinate: ses coordonnées de spawn
        """
        super().__init__(
            texture=texture,  # relativement inutile
            width=width,
            height=height,
            coordinate=coordinate
        )

        self.__animationSet = AnimationSet()

    def createAnimation(self, directory: str, nbImages: int):
        self.__animationSet.setImageFromDirectory(
            directory=directory,
            nbImage=[nbImages, 0, 0]
        )

    @property
    def Animation(self) -> AnimationSet:
        return self.__animationSet

    def getCurrentAnimation(self) -> Image:
        return self.__animationSet.getMoveRightAnimation()
