from animation import Animation
from image import Image


class AnimationSet:
    __moveRightAnimation: Animation
    __moveLeftAnimation: Animation
    __jumpAnimation: Animation
    __afkImage: Image

    __indexRight: int
    __indexLeft: int
    __indexJump: int

    __frame: int

    def __init__(self):
        self.__moveRightAnimation = Animation()
        self.__moveLeftAnimation = Animation()
        self.__jumpAnimation = Animation()

        self.__indexJump = 0
        self.__indexLeft = 0
        self.__indexRight = 0

        self.__frame = 0

    def getMoveRightAnimation(self):
        self.__indexJump = 0
        self.__indexLeft = 0

        if self.__frame == 0:
            self.__indexRight += 1

        previousIndex = self.__indexRight
        previousIndex -= 1

        self.__frame += 1
        self.__frame %= 4

        return self.__moveRightAnimation.getFrame(previousIndex % self.__moveRightAnimation.getLenImage())

    def getMoveLeftAnimation(self):
        self.__indexJump = 0
        self.__indexRight = 0

        if self.__frame == 0:
            self.__indexLeft += 1

        previousIndex = self.__indexLeft - 1

        self.__frame += 1
        self.__frame %= 4

        return self.__moveLeftAnimation.getFrame(previousIndex % self.__moveLeftAnimation.getLenImage())

    def getJumpAnimation(self):
        self.__indexRight = 0
        self.__indexLeft = 0

        if self.__frame ==0:
            self.__indexJump += 1

        previousIndex = self.__indexJump - 1

        self.__frame += 1
        self.__frame %= 4
        return self.__jumpAnimation.getFrame(previousIndex % self.__jumpAnimation.getLenImage())

    def addMoveRightAnimation(self, image: Image):
        self.__moveRightAnimation.addFrame(image)

    def addMoveLeftAnimation(self, image: Image):
        self.__moveLeftAnimation.addFrame(image)

    def addJumpAnimation(self, image: Image):
        self.__jumpAnimation.addFrame(image)

    # getter/setter afkImage
    @property
    def afkImage(self) -> Image:
        return self.__afkImage

    @afkImage.setter
    def afkImage(self, afkImage: Image) -> None:
        self.__afkImage = afkImage

    def setImageFromDirectory(self, directory: str, nbImage: list = [1, 1, 1]):
        """
        Va chercher directement les images dans leurs dossiers associés
        :param directory: le dossier du personnage
        :param nbImage: liste contenant le nombre d'image pour chaque animation de la forme [nbImageRight, nbImageLeft, nbImageJump]
        :return: None
        """
        for i in range(nbImage[0]):
            self.addMoveRightAnimation(Image(directory + "/right/" + str(i + 1) + ".png"))

        for i in range(nbImage[1]):  # les images de gauche sont les mêmes que celles de droite, mais retournées
            self.addMoveLeftAnimation(Image(directory + "/right/" + str(i + 1) + ".png"))

        for i in range(nbImage[2]):
            self.addJumpAnimation(Image(directory + "/jump/" + str(i + 1) + ".png"))

        self.afkImage = Image(directory + "/afk.png")
