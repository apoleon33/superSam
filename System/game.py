import pygame

from Character.mainCharacter import MainCharacter
from Map.map import Map
from System.control import Control
from System.story import Story
from coordinate import Coordinate


class Game:
    __mainCharacter: MainCharacter
    __gravity: int
    __map: Map
    __story: Story
    __pygame: pygame
    __control: Control

    __camera: Coordinate  # ou on est, dans quel niveau

    def __init__(self, carte: Map, mainCharacter: MainCharacter, motor: pygame):
        self.__map = carte
        self.__mainCharacter = mainCharacter
        self.__gravity = 0  # à modifier
        self.__story = Story()
        self.__control = Control()
        self.__camera = Coordinate(0, 0)

        # on initialise pygame
        self.__pygame = motor
        self.__pygame.init()
        self.__screen = self.__pygame.display.set_mode((self.__map.Width, self.__map.Height))
        pygame.display.set_caption("Super Sam")

    def play(self) -> bool:
        """
        Fonction principale du jeux, qui gère tout (gameplay/affichage)
        :return: un booléen selon que le jeux doit continuer ou que la personne est morte/a quitté le jeux
        """

        if not self.handleControls():  # si la personne veut quitter la partie
            return False

        self.displayGame()

        self.__pygame.display.update()

    def displayGame(self):
        """
        Affichage du jeux, de ses mobs et de son fond
        :return: Rien
        """
        actualLevel = self.__map.getLevel(self.__camera.X, self.__camera.Y)

        background = self.__pygame.image.load(actualLevel.Background.getPath()).convert()
        backgroundSize: tuple = (int(background.get_rect().width / 2), int(background.get_rect().height / 2))
        background = pygame.transform.scale(background, backgroundSize)
        # image = pygame.transform.scale(image, (width * 2, height * 2))

        self.__screen.blit(background, (0, 0))

    def setStory(self, story: Story):
        pass

    def handleControls(self) -> bool:
        for event in self.__pygame.event.get():
            match self.__control.isAControl(event.type):
                case False:
                    pass
                case "RIGHT":
                    self.__mainCharacter.move_right()
                case "LEFT":
                    self.__mainCharacter.move_left()
                case "JUMP":
                    self.__mainCharacter.jump()
                case "QUIT":
                    return False
        return True
