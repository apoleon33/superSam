import time

import pygame

from Character.behaviorMove.behaviorMoveKeyboard import BehaviorMoveKeyboard
from Character.mainCharacter import MainCharacter
from Map.level import Level
from Map.map import Map
from System.game import Game
from coordinate import Coordinate
from image import Image

sammy = MainCharacter(Coordinate(0, 0))
sammy.setBehaviorMove(BehaviorMoveKeyboard())

# création de la map
campus = Map(int(1920 / 2), int(1080 / 2))

accueil = Level("Accueil")
accueil.Background = Image("assets/levels/forest.jpg")
campus.addLevel(0, 0, accueil)

# création du jeux en lui même
game = Game(campus, sammy, pygame)
game.FPS = 120
game.Gravity = 10

while game.play() is None:  # on fait tourner le jeux
    time.sleep(1 / game.FPS)
