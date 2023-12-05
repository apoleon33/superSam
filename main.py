import pygame

from Character.behaviorMove.behaviorMoveKeyboard import BehaviorMoveKeyboard
from Character.mainCharacter import MainCharacter
from Map.concrete import Concrete
from Map.level import Level
from Map.map import Map
from System.game import Game
from config import WIDTH, HEIGHT, FPS, GRAVITY, MAIN_CHARACTER_HEIGHT
from coordinate import Coordinate
from image import Image

sami = MainCharacter(Coordinate(0, 0))
sami.setBehaviorMove(BehaviorMoveKeyboard())
sami.Coordinate.Y, sami.Coordinate.X = HEIGHT - MAIN_CHARACTER_HEIGHT, 0

# création de la map
accueil = Level("Accueil")
accueil.Background = Image("assets/levels/atrium.png")
accueil.addBlock(Concrete(Coordinate(250, HEIGHT - 123)))
accueil.addBlock(Concrete(Coordinate(250 + int(256 / 2), HEIGHT - 246)))
accueil.addBlock(Concrete(Coordinate(250 + int(256 / 2) * 2, HEIGHT - 246)))
accueil.addBlock(Concrete(Coordinate(250 + int(256 / 2) * 3, HEIGHT - (246 + 123))))
accueil.addBlock(Concrete(Coordinate(250 + int(256 / 2) * 3, HEIGHT - 246)))
accueil.addBlock(Concrete(Coordinate(250 + int(256 / 2) * 3, HEIGHT - (246 + 123 + 123))))
accueil.addBlock(Concrete(Coordinate(0, HEIGHT - 123)))
accueil.addBlock(Concrete(Coordinate(250 + int(256 / 2) * 4, HEIGHT - (246 + (2 * 123)))))
accueil.addBlock(Concrete(Coordinate(250 + int(256 / 2) * 7, HEIGHT - (246 + (1 * 123)))))

campus = Map(WIDTH, HEIGHT)
campus.addLevel(0, 0, accueil)

# création du jeux en lui même
game = Game(campus, sami)
game.Gravity = GRAVITY

# images par secondes
clock = pygame.time.Clock()
game.FPS = FPS

while game.play() is True:  # on fait tourner le jeux
    clock.tick(game.FPS)
