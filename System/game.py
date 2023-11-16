from Character.mainCharacter import MainCharacter
from Map.map import Map


class Game:
    __mainCharacter: MainCharacter
    __gravity: int
    __map: Map
    __story: Story

    def __init__(self, map:Map, mainCharacter: MainCharacter):
        self.__map = map
        self.__mainCharacter = mainCharacter
        self.__gravity = 0 # à modifier
        self.__story = story

    def displayGame(self):
        pass

    def setStory(self, story: Story):
        pass