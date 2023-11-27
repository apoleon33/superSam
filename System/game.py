import pygame

from Character.mainCharacter import MainCharacter
from Map.map import Map
from System.control import Control
from System.story import Story
from config import FPS, MAIN_CHARACTER_HEIGHT, HEIGHT, WIDTH, MAIN_CHARACTER_SPEED
from coordinate import Coordinate
from image import Image


class Game:
    __mainCharacter: MainCharacter
    __gravity: int
    __map: Map
    __story: Story
    __control: Control

    __camera: Coordinate  # ou on est, dans quel niveau
    __fps: int

    __alreadyLoadedImages: [Image]
    __alreadyLoadedPygameImages: [pygame.surface.Surface]

    def __init__(self, carte: Map, mainCharacter: MainCharacter):
        self.__map = carte
        self.__mainCharacter = mainCharacter
        self.__gravity = MAIN_CHARACTER_SPEED
        self.__fps = FPS
        self.__story = Story()
        self.__control = Control()
        self.__camera = Coordinate(0, 0)

        # on initialise pygame
        pygame.init()
        self.__screen = pygame.display.set_mode((self.__map.Width, self.__map.Height))
        pygame.display.set_caption("Super Sam")
        pygame.key.set_repeat(1, 1)

        # optimisation
        self.actualBackground = None
        self.__alreadyLoadedImages = []
        self.__alreadyLoadedPygameImages = []

    def play(self) -> bool:
        """
        Fonction principale du jeux, qui gère tout (gameplay/affichage)
        :return: un booléen selon que le jeux doit continuer ou que la personne est morte/a quitté le jeux
        """

        movePlayed = self.handleControls()
        if movePlayed is False:  # si la personne veut quitter la partie
            return False

        # gravité
        self.__mainCharacter.checkJump()
        if self.__mainCharacter.Coordinate.Y < self.__map.Height - MAIN_CHARACTER_HEIGHT:
            if not self.__mainCharacter.JumpStatus:  # si la personne saute la gravité pose problème
                self.__mainCharacter.Coordinate.Y += self.__gravity

        self.displayGame()
        pygame.display.update()

    def displayGame(self):
        """
        Affichage du jeux, de ses mobs et de son fond
        :return: Rien
        """

        actualLevel = self.__map.getLevel(self.__camera.X, self.__camera.Y)

        self.actualBackground = self.loadImage(actualLevel.Background, darken=True)

        # fond de l'image
        backgroundWidth = self.actualBackground.get_rect().width
        backgroundHeight = self.actualBackground.get_rect().height

        backgroundSize: tuple = (WIDTH, HEIGHT)
        # self.actualBackground = pygame.transform.scale(self.actualBackground, backgroundSize)

        self.__screen.blit(self.actualBackground, (0, 0))

        # affichage de Samy
        samySprite = self.loadImage(self.__mainCharacter.getCurrentAnimation(),
                                    rescale=[True, 80, MAIN_CHARACTER_HEIGHT])

        if self.__mainCharacter.leftStatus:
            samySprite = pygame.transform.flip(samySprite, True, False)
        # samySprite = pygame.transform.scale(samySprite, (80, MAIN_CHARACTER_HEIGHT))
        self.__screen.blit(samySprite, (self.__mainCharacter.Coordinate.X, self.__mainCharacter.Coordinate.Y))

    def setStory(self, story: Story):
        pass

    def handleControls(self) -> bool | Image:
        """
        Fonction de prise en charge des contrôles du clavier
        :return: L'image à afficher de Sami, False si la personne veut quitter le jeux.
        """
        keys = pygame.key.get_pressed()
        # print the key pressed
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # print("Keydown")
                if event.key in self.__control.getRightKeys():
                    return self.__mainCharacter.move_right()
                elif event.key in self.__control.getLeftKeys():
                    return self.__mainCharacter.move_left()
                elif event.key in self.__control.getJumpKeys():
                    return self.__mainCharacter.jump()

            elif event.type == pygame.QUIT:
                return False

        return self.__mainCharacter.doNothing()

    @property
    def FPS(self) -> int:
        return self.__fps

    @FPS.setter
    def FPS(self, fps: int) -> None:
        self.__fps = fps

    @property
    def Gravity(self) -> int:
        return self.__gravity

    @Gravity.setter
    def Gravity(self, gravity: int) -> None:
        self.__gravity = gravity

    def loadImage(self, image: Image, darken: bool = False,
                  rescale: list[bool, int, int] = (False, 0, 0)) -> pygame.surface.Surface:
        """
        Ne charge l'image que si cela n'a pas déjà été fait.
        :param image: l'image à afficher
        :param darken: Si l'on doit assombrir l'image avant de l'enregistrer
        :param rescale: Une liste, avec en premier indice un booléen, suivi des deux dimensions
        :return: l'image chargée
        """

        for i in range(len(self.__alreadyLoadedImages)):
            if self.__alreadyLoadedImages[i].getPath() == image.getPath():  # si l'image est déjà chargé dans la liste
                return self.__alreadyLoadedPygameImages[i]

        self.__alreadyLoadedImages.append(image)
        loadedImage = pygame.image.load(image.getPath()).convert_alpha()

        if darken:
            brighten = 85
            loadedImage.fill((brighten, brighten, brighten), special_flags=pygame.BLEND_SUB)

        if rescale[0]:
            loadedImage = pygame.transform.scale(loadedImage, (rescale[1], rescale[2]))

        self.__alreadyLoadedPygameImages.append(loadedImage)
        return loadedImage
