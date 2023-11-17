import pygame

from Character.mainCharacter import MainCharacter
from Map.map import Map
from System.game import Game
from coordinate import Coordinate

sammy = MainCharacter(Coordinate(0, 0))
campus = Map(1920, 1080)
game = Game(campus, sammy, pygame)

while game.play() is True: # on fait tourner le jeux
    pass
