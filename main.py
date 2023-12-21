import pygame

from Character.behaviorMove.behaviorMoveKeyboard import BehaviorMoveKeyboard
from Character.mainCharacter import MainCharacter
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
accueil.Background = Image("assets/levels/fondecran1.png")
accueil.MainCharacterSpawn = Coordinate(100, 703)

campus = Map(WIDTH, HEIGHT)

# création du jeux en lui même
game = Game(campus, sami)
game.Gravity = GRAVITY

game.Camera = Coordinate(2, 0)

mapstart = Level("tutoriel")
mapstart.Background = Image("assets/levels/fondecran0.png")
mapstart.MainCharacterSpawn = Coordinate(392, 704)
mapstart.setTmx("assets/map/mapstart.tmx")
mapstart.createLevel()
# 392,704

accueil.setTmx("assets/map/map1.tmx")
accueil.createLevel()
# zzzz
first_lvl = Level("un")
first_lvl.Background = Image("assets/levels/fondecran1.png")
first_lvl.MainCharacterSpawn = Coordinate(46, 515)
first_lvl.setTmx("assets/map/map1.tmx")
first_lvl.createLevel()

second_level = Level("deux")
second_level.Background = Image("assets/levels/fondecran2.png")
second_level.MainCharacterSpawn = Coordinate(61, 353)
second_level.setTmx("assets/map/map2.tmx")
second_level.createLevel()

third_level = Level("trois")
third_level.Background = Image("assets/levels/fondecran3.png")
third_level.MainCharacterSpawn = Coordinate(105, 700)
third_level.setTmx("assets/map/map3.tmx")
third_level.createLevel()

fourth_level = Level("quatre")
fourth_level.Background = Image("assets/levels/fondecran4.png")
fourth_level.MainCharacterSpawn = Coordinate(150, 704)
fourth_level.setTmx("assets/map/map4.tmx")
fourth_level.createLevel()
# 150,704
final_level = Level("final")
final_level.Background = Image("assets/levels/fondecran5.png")
final_level.MainCharacterSpawn = Coordinate(150, 160)
final_level.setTmx("assets/map/mapfinal.tmx")
final_level.createLevel()


campus.addLevel(0, 2, mapstart)
campus.addLevel(1, 2, first_lvl)
campus.addLevel(1, 1, second_level)
campus.addLevel(2, 1, third_level)
campus.addLevel(2, 0, fourth_level)
campus.addLevel(3, 0, final_level)

sami.Coordinate.Y, sami.Coordinate.X = mapstart.MainCharacterSpawn.Y, mapstart.MainCharacterSpawn.X

# images par secondes
clock = pygame.time.Clock()
game.FPS = FPS

# musique
travis = Image("assets/sounds/90210.mp3")
music = MusicPlayer(travis)
music.play()


heart = Image("assets/sounds/HeartOfCourage.mp3")


#if campus != Map(3, 0):
    #music.play()
#else:
    #music.changeFile(heart)
    #music.play()

while game.play() is True:  # on fait tourner le jeux
    clock.tick(game.FPS)

print("game over!")
...