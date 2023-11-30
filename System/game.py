import pygame

from Character.character import Character
from Character.mainCharacter import MainCharacter
from Map.map import Map
from System.control import Control
from System.story import Story
from config import FPS, MAIN_CHARACTER_HEIGHT, HEIGHT, MAIN_CHARACTER_SPEED, HITBOX
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

        self.testCollision = pygame.Rect(500, HEIGHT - 100, 500, 100)

    def play(self) -> bool:
        """
        Fonction principale du jeux, qui gère tout (gameplay/affichage)
        :return: un booléen selon que le jeux doit continuer ou que la personne est morte/a quitté le jeux
        """

        # collision
        self.handleCollision(self.__mainCharacter)

        movePlayed = self.handleControls()
        if movePlayed is False:  # si la personne veut quitter la partie
            return False

        # gravité
        self.__mainCharacter.checkJump()
        if self.__mainCharacter.Coordinate.Y < self.__map.Height - MAIN_CHARACTER_HEIGHT:
            if not self.__mainCharacter.JumpStatus:  # si la personne saute la gravité pose problème
                self.__mainCharacter.Coordinate.Y += self.__gravity
                self.__mainCharacter.getHitbox().bottom += self.__gravity
                if self.isColliding(self.__mainCharacter):
                    self.__mainCharacter.Coordinate.Y -= self.__gravity
                    self.__mainCharacter.getHitbox().bottom -= self.__gravity

        self.displayGame(hitbox=HITBOX)
        pygame.display.update()
        return True

    def displayGame(self, hitbox=HITBOX):
        """
        Affichage du jeux, de ses mobs et de son fond
        :return: Rien
        """

        def displayHitBox():
            """
            Si l'on veut afficher les hitbox des différents éléments du level
            :return: Rien
            """
            pygame.draw.rect(self.__screen, (0, 255, 0), self.__mainCharacter.getHitbox())
            pygame.draw.rect(self.__screen, (255, 0, 0), self.testCollision)

        actualLevel = self.__map.getLevel(self.__camera.X, self.__camera.Y)

        self.actualBackground = self.loadImage(actualLevel.Background, darken=True)

        # fond de l'image
        self.__screen.blit(self.actualBackground, (0, 0))

        # affichage de Samy
        samySprite = self.loadImage(self.__mainCharacter.getCurrentAnimation(),
                                    rescale=[True, 80, MAIN_CHARACTER_HEIGHT])

        if self.__mainCharacter.Direction == "gauche":
            samySprite = pygame.transform.flip(samySprite, True, False)

        self.__mainCharacter.setHitbox(samySprite.get_width(), samySprite.get_height())

        if hitbox:
            displayHitBox()
        self.__screen.blit(samySprite, (self.__mainCharacter.Coordinate.X, self.__mainCharacter.Coordinate.Y))

    def setStory(self, story: Story):
        pass

    def handleControls(self) -> bool | Image:
        """
        Fonction de prise en charge des contrôles du clavier
        :return: L'image à afficher de Sami, False si la personne veut quitter le jeux.
        """
        # print the key pressed
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # print("Keydown")
                if event.key in self.__control.getRightKeys():
                    return self.__mainCharacter.move_right()
                elif event.key in self.__control.getLeftKeys():
                    return self.__mainCharacter.move_left()
                elif event.key in self.__control.getJumpKeys() and self.isTouchingTheGround(self.__mainCharacter):
                    return self.__mainCharacter.jump()

            elif event.type == pygame.QUIT:
                return False

        return self.__mainCharacter.doNothing()

    def isColliding(self, character: Character) -> bool:
        return pygame.Rect.colliderect(character.getHitbox(), self.testCollision)

    def isTouchingTheGround(self, character: Character) -> bool:
        """
        Vérifie si le personnage est en train de toucher le sol
        :param character: Le personnage à vérifier
        :return: un booléen selon que le personnage touche le sol ou non
        """
        return character.getHitbox().bottom == self.testCollision.top or character.Coordinate.Y >= self.__map.Height - MAIN_CHARACTER_HEIGHT

    def handleCollision(self, character: Character):
        """
        Gère les collisions entre les personnages et les différents éléments du niveau.
        :param character: le personnage dont il faut tester les collisions.
        :return: Rien
        """

        def handleXCollision():
            match character.Direction:
                case "droite":
                    character.getHitbox().right = self.testCollision.left - 10
                    character.Coordinate.X = self.testCollision.left - 80 - 10
                    character.onTopOf = False

                case "gauche":
                    character.getHitbox().left = self.testCollision.right + 10
                    character.Coordinate.X = self.testCollision.right + 10
                    character.onTopOf = False

        def handleYCollision():
            match character.Direction:
                case "bas":
                    character.getHitbox().bottom = self.testCollision.top
                    character.Coordinate.Y = self.testCollision.top - MAIN_CHARACTER_HEIGHT
                    character.onTopOf = True
                    return None

        if self.isColliding(character):
            handleYCollision()
            handleXCollision()

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
