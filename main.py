import pygame

from Character.mainCharacter import MainCharacter
from Map.level import Level
from Map.map import Map
from System.game import Game
from coordinate import Coordinate
from image import Image

sammy = MainCharacter(Coordinate(0, 0))

# création de la map
campus = Map(int(1920 / 2), int(1080 / 2))

accueil = Level("Accueil")
accueil.Background = Image("assets/levels/rei.png")
campus.addLevel(0, 0, accueil)

# création du jeux en lui même
game = Game(campus, sammy, pygame)

while game.play() is None:  # on fait tourner le jeux
    pass
