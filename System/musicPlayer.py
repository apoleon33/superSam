# lecteur de musique
import pygame

from image import Image


class MusicPlayer:
    __file: Image  # c'est pas vraiment une image mais les fonctions de la classe marchent

    def __init__(self, file: Image):
        self.__file = file
        self.__loadFile()

    def __loadFile(self):
        pygame.mixer.music.load(self.__file.getPath())

    def changeFile(self, newFile: Image):
        self.__file = newFile

    def play(self, iteration: int = -1):
        self.__loadFile()
        pygame.mixer.music.play(iteration)

    def stop(self):
        pygame.mixer.music.stop()
