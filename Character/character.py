from abc import ABC

from Character.behaviorMove.behaviorMove import BehaviorMove
from animationSet import AnimationSet
from coordinate import Coordinate
from hitbox import Hitbox
from image import Image

import pygame


class Character(ABC):
    __name: str
    __coordinate: Coordinate
    __behaviorMove: BehaviorMove

    __jumpStatus: bool
    __maxJumpHeight: int
    __jumpCount: int

    __velY: int
    __isInAir: bool

    __animationSet: AnimationSet
    __currentAnimation: Image

    __rect: pygame.Rect
    __direction: str
    __hitbox: Hitbox

    __px: int
    __py: int

    def __init__(self, name: str, animationSet: AnimationSet) -> None:
        """
        Classe abstraite des mobs, agonistes comme antagonistes.
        """
        self.__name = name
        self.__animationSet = animationSet
        self.__currentAnimation = self.__animationSet.getMoveRightAnimation()
        self.__coordinate = Coordinate(0, 0)

        self.__maxJumpHeight = 25
        self.__jumpStatus = False
        self.__jumpCount = 0

        self.__velY = 0
        self.__isInAir = False

        self.setHitbox(0, 0)
        self.__direction = "afk"  # autres versions possible: "droite", "gauche", "haut", "bas"

        self.__py = 0
        self.__px = 0

    def setBehaviorMove(self, behaviorMove: BehaviorMove) -> None:
        """
        On choisi de quelle manière la personne va se déplacer (keyboard, fast, slow).
        :param behaviorMove: la manière dont il va se déplacer
        :return: Rien
        """
        self.__behaviorMove = behaviorMove
        if self.__behaviorMove.Character is not self:  # double flèche en UML
            self.__behaviorMove.Character = self

    def move_right(self) -> int:
        """
        Fonction appelée dès que le mob doit se déplacer à gauche.
        :return: Rien
        """
        self.__currentAnimation = self.__animationSet.getMoveRightAnimation()
        self.__direction = "droite"
        return self.__behaviorMove.move_right()

    def move_left(self) -> int:
        """
        Fonction appelée dès que le mob doit se déplacer à droit.
        :return: Rien
        """
        self.__currentAnimation = self.__animationSet.getMoveLeftAnimation()
        self.__direction = "gauche"
        return self.__behaviorMove.move_left()

    def jump(self) -> int:
        """
        Fonction appelée dès que le mob doit sauter.
        :return: un entier pour ne plus rien casser
        """
        # if not self.__jumpStatus:
        #     self.__jumpStatus = True
        #     self.__jumpCount = self.__maxJumpHeight
        # self.__currentAnimation = self.__animationSet.getJumpAnimation()

        self.__velY = self.__behaviorMove.jump()
        self.__jumpStatus = True
        return 0

    def checkJump(self):
        """
        Fonction pour que le personnage saute.
        La prise en compte du saut doit se faire hors de la prise en compte des touches.
        :return: Rien
        """
        if self.__jumpStatus:
            self.__behaviorMove.jump()

            if self.__jumpCount > - self.__maxJumpHeight:
                self.__jumpCount -= 1
            else:
                self.__jumpStatus = False

            if self.__jumpCount > 0:
                self.__direction = "haut"
            else:
                self.__direction = "bas"

    def doNothing(self):
        """
        Assigne l'image actuelle comme l'image afk
        :return: Rien
        """
        self.__currentAnimation = self.__animationSet.afkImage
        self.__leftStatus = False

    def getCurrentAnimation(self) -> Image:
        """
        Récupère l'image actuelle à afficher
        :return: l'image à afficher
        """
        return self.__currentAnimation

    def changePrevisionnalX(self, newX: int):
        self.__px = newX

    def changePrevisionnalY(self, newY: int):
        self.__py = newY

    def getPrevisionnalCoordinate(self) -> (int, int):
        return self.__px, self.__py

    def updateCoordinate(self):
        self.__coordinate.X += self.__px
        self.__coordinate.Y += self.__py

        self.__px = 0
        self.__py = 0

    def setHitbox(self, width: int, height: int):
        """
        Définit la taille de la hitbox du personnage
        :param width: Sa largeur
        :param height: Sa hauteur
        :return: Rien
        """
        # self.__rect = pygame.Rect(self.__coordinate.X, self.__coordinate.Y, width, height)
        self.__hitbox = Hitbox(width, height, self.__coordinate)

    def getHitbox(self) -> pygame.Rect:
        return self.__hitbox.Rect

    @property
    def Coordinate(self) -> Coordinate:
        return self.__coordinate

    @property
    def jumpCount(self) -> int:
        return self.__jumpCount

    @jumpCount.setter
    def jumpCount(self, jumpCount: int) -> None:
        self.__jumpCount = jumpCount

    @property
    def JumpStatus(self) -> bool:
        return self.__jumpStatus

    @JumpStatus.setter
    def JumpStatus(self, jumpStatus: bool) -> None:
        self.__jumpStatus = jumpStatus

    @property
    def Direction(self) -> str:
        return self.__direction

    @Direction.setter
    def Direction(self, direction: str) -> None:
        self.__direction = direction

    @property
    def VelY(self) -> int:
        return self.__velY

    @VelY.setter
    def VelY(self, velY: int):
        self.__velY = velY

    @property
    def IsInAir(self) -> bool:
        return self.__isInAir

    @IsInAir.setter
    def IsInAir(self, value: bool):
        self.__isInAir = value
