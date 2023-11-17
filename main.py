import pygame

from Character.mainCharacter import MainCharacter
from Map.map import Map
from System.game import Game
from coordinate import Coordinate

pygame.init()

sammy = MainCharacter(Coordinate(0, 0))
campus = Map(1920, 1080)
game = Game(campus, sammy)

screen = pygame.display.set_mode((campus.Width, campus.Height))

isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    pygame.display.update()
