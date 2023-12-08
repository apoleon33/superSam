import pygame

from Character.behaviorMove.behaviorMoveKeyboard import BehaviorMoveKeyboard
from Character.mainCharacter import MainCharacter
from Map.door import Door
from Map.level import Level
from Map.map import Map
from System.game import Game
from System.musicPlayer import MusicPlayer
from config import WIDTH, HEIGHT, FPS, GRAVITY, MAIN_CHARACTER_HEIGHT
from coordinate import Coordinate
from image import Image

sami = MainCharacter(Coordinate(0, 0))
sami.setBehaviorMove(BehaviorMoveKeyboard())
sami.Coordinate.Y, sami.Coordinate.X = HEIGHT - MAIN_CHARACTER_HEIGHT, 0

# création de la map
accueil = Level("Accueil")
accueil.Background = Image("assets/levels/atrium.png")

sortie = Door()
sortie.Coordinate.X = 250 + int(256 / 2) * 9
sortie.Coordinate.Y = HEIGHT - 123 - 538
accueil.addTunnel(sortie)

campus = Map(WIDTH, HEIGHT)
campus.addLevel(0, 0, accueil)

# création du jeux en lui même
game = Game(campus, sami)
game.Gravity = GRAVITY

accueil.setTmx("map2.tmx")
accueil.createLevel()

# images par secondes
clock = pygame.time.Clock()
game.FPS = FPS

# musique
travis = Image("assets/sounds/90210.mp3")
music = MusicPlayer(travis)
music.play()

while game.play() is True:  # on fait tourner le jeux
    clock.tick(game.FPS)
