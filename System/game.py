import pygame

from Character.mainCharacter import MainCharacter
from Map.map import Map
from System.control import Control
from System.story import Story


class Game:
    __mainCharacter: MainCharacter
    __gravity: int
    __map: Map
    __story: Story
    __pygame: pygame
    __control: Control

    def __init__(self, carte: Map, mainCharacter: MainCharacter, motor: pygame):
        self.__map = carte
        self.__mainCharacter = mainCharacter
        self.__gravity = 0  # à modifier
        self.__story = Story()
        self.__control = Control()

        # on initialise pygame
        self.__pygame = motor
        self.__pygame.init()
        self.__pygame.display.set_mode((self.__map.Width, self.__map.Height))

    def play(self) -> bool:
        """
        Fonction principale du jeux, qui gère tout (gameplay/affichage)
        :return: un booléen selon que le jeux doit continuer ou que la personne est morte/a quitté le jeux
        """
        handleControls = self.handleControls()
        if handleControls is False: # si la personne veut quitter la partie
            return False




    def displayGame(self):
        pass

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
