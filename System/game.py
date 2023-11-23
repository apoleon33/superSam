import pygame

from Character.mainCharacter import MainCharacter
from Map.map import Map
from System.control import Control
from System.story import Story
from coordinate import Coordinate
from image import Image


class Game:
    __mainCharacter: MainCharacter
    __gravity: int
    __map: Map
    __story: Story
    __pygame: pygame
    __control: Control

    __camera: Coordinate  # ou on est, dans quel niveau
    __fps: int

    def __init__(self, carte: Map, mainCharacter: MainCharacter, motor: pygame):
        self.__map = carte
        self.__mainCharacter = mainCharacter
        self.__gravity = 5  # à modifier
        self.__fps = 120
        self.__story = Story()
        self.__control = Control()
        self.__camera = Coordinate(0, 0)

        # on initialise pygame
        self.__pygame = motor
        self.__pygame.init()
        self.__screen = self.__pygame.display.set_mode((self.__map.Width, self.__map.Height))
        self.__pygame.display.set_caption("Super Sam")
        self.__pygame.key.set_repeat(1, 1)

        # le fond d'écran actuel, pour ne l'actualiser que quand il faut
        self.actualBackground = None

    def play(self) -> bool:
        """
        Fonction principale du jeux, qui gère tout (gameplay/affichage)
        :return: un booléen selon que le jeux doit continuer ou que la personne est morte/a quitté le jeux
        """

        movePlayed = self.handleControls()
        if movePlayed is False:  # si la personne veut quitter la partie
            return False

        # gravité
        if self.__mainCharacter.Coordinate.Y < self.__map.Height - 200:
            self.__mainCharacter.Coordinate.Y += self.__gravity

        self.displayGame()
        self.__pygame.display.update()

    def displayGame(self):
        """
        Affichage du jeux, de ses mobs et de son fond
        :return: Rien
        """
        actualLevel = self.__map.getLevel(self.__camera.X, self.__camera.Y)

        self.actualBackground = self.__pygame.image.load(actualLevel.Background.getPath()).convert_alpha()

        backgroundSize: tuple = (
            int(self.actualBackground.get_rect().width / 2), int(self.actualBackground.get_rect().height / 2))
        self.actualBackground = pygame.transform.scale(self.actualBackground, backgroundSize)
        # image = pygame.transform.scale(image, (width * 2, height * 2))

        self.__screen.blit(self.actualBackground, (0, 0))

        # affichage de Samy
        samySprite = self.__pygame.image.load(self.__mainCharacter.getCurrentAnimation().getPath()).convert_alpha()
        samySprite = pygame.transform.scale(samySprite, (200, 200))
        self.__screen.blit(samySprite, (self.__mainCharacter.Coordinate.X, self.__mainCharacter.Coordinate.Y))

    def setStory(self, story: Story):
        pass

    def handleControls(self) -> bool | Image:

        keys = pygame.key.get_pressed()
        # print the key pressed
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # print("Keydown")
                if event.key in self.__control.getRightKeys():
                    return self.__mainCharacter.move_right()
                elif event.key in self.__control.getLeftKeys():
                    return self.__mainCharacter.move_left()
                elif event.key in self.__control.getJumpKeys():
                    return self.__mainCharacter.jump()

            elif event.type == pygame.QUIT:
                return False

        return self.__mainCharacter.doNothing()

    @property
    def FPS(self) -> int:
        return self.__fps

    @FPS.setter
    def FPS(self, fps: int) -> None:
        self.__fps = fps

    @property
    def Gravity(self) -> int:
        return self.__gravity

    @Gravity.setter
    def Gravity(self, gravity: int) -> None:
        self.__gravity = gravity
