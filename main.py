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

# création de la map
accueil = Level("Accueil")
accueil.Background = Image("assets/levels/atrium.png")
accueil.MainCharacterSpawn = Coordinate(100, 703)

campus = Map(WIDTH, HEIGHT)

# création du jeux en lui même
game = Game(campus, sami)
game.Gravity = GRAVITY

game.Camera = Coordinate(0, 2)

mapstart = Level("tutoriel")
mapstart.Background = Image("assets/levels/atrium.png")
mapstart.MainCharacterSpawn = Coordinate(0, 704)
mapstart.setTmx("assets/map/mapstart.tmx")
mapstart.createLevel()

accueil.setTmx("assets/map/map1.tmx")
accueil.createLevel()
# zzzz
first_lvl = Level("un")
first_lvl.Background = Image("assets/levels/atrium.png")
first_lvl.MainCharacterSpawn = Coordinate(100, 703)
first_lvl.setTmx("assets/map/map1.tmx")
first_lvl.createLevel()

second_level = Level("deux")
second_level.Background = Image("assets/levels/atrium.png")
second_level.MainCharacterSpawn = Coordinate(0, 0)
second_level.setTmx("assets/map/map2.tmx")
second_level.createLevel()

third_level = Level("trois")
third_level.Background = Image("assets/levels/atrium.png")
third_level.MainCharacterSpawn = Coordinate(0, 0)
third_level.setTmx("assets/map/map3.tmx")

campus.addLevel(2, 0, mapstart)
campus.addLevel(1, 0, first_lvl)
campus.addLevel(0, 0, second_level)
campus.addLevel(0, 1, third_level)


sami.Coordinate.Y, sami.Coordinate.X = mapstart.MainCharacterSpawn.Y, mapstart.MainCharacterSpawn.X

# images par secondes
clock = pygame.time.Clock()
game.FPS = FPS

# musique
travis = Image("assets/sounds/90210.mp3")
music = MusicPlayer(travis)
music.play()

campus.printLevel()

while game.play() is True:  # on fait tourner le jeux
    clock.tick(game.FPS)

print("game over!")
