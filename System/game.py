import pygame
import pytmx
import pyscroll

from Character.character import Character
from Character.mainCharacter import MainCharacter
from Map.block import Block
from Map.map import Map
from Map.tunnel import Tunnel
from System.control import Control
from System.story import Story
from config import FPS, MAIN_CHARACTER_HEIGHT, HEIGHT, MAIN_CHARACTER_SPEED, HITBOX
from coordinate import Coordinate
from hitbox import Hitbox
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

        # essai chargement carte
        # tmx_data = self.__map.getLevel(self.__camera.X, self.__camera.Y).getTmx().getData()
        # map_data = pyscroll.data.TiledMapData(tmx_data)
        # map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.__screen.get_size())

        # self.group = pyscroll.PyscrollGroup(map_layer=map_layer)

        # optimisation
        self.actualBackground = None
        self.__alreadyLoadedImages = []
        self.__alreadyLoadedPygameImages = []

        # self.testCollision = pygame.Rect(500, HEIGHT - 100, 500, 100)

    def play(self) -> bool:
        """
        Fonction principale du jeux, qui gère tout (gameplay/affichage)
        :return: un booléen selon que le jeux doit continuer ou que la personne est morte/a quitté le jeux
        """

        # collision
        # self.handleCollisions(self.__mainCharacter)

        sammiBeforeControlsX, sammiBeforeControlsY = self.__mainCharacter.Coordinate.X, self.__mainCharacter.Coordinate.Y
        movePlayed = self.handleControls()
        if movePlayed is False:  # si la personne veut quitter la partie
            return False

        # gravité
        self.__mainCharacter.VelY += 1
        if self.__mainCharacter.VelY > 10:
            self.__mainCharacter.VelY = 10

        self.__mainCharacter.changePrevisionnalX(movePlayed)
        self.__mainCharacter.changePrevisionnalY(
            self.__mainCharacter.getPrevisionnalCoordinate()[1] + self.__mainCharacter.VelY
        )

        self.handleCollisions(self.__mainCharacter)

        self.__mainCharacter.updateCoordinate()

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
            for block in self.__map.getLevel(self.__camera.X, self.__camera.Y).getBlocks():
                pygame.draw.rect(self.__screen, (255, 0, 0), block.getHitbox().Rect)

        actualLevel = self.__map.getLevel(self.__camera.X, self.__camera.Y)

        # fond de l'image
        self.actualBackground = self.loadImage(actualLevel.Background, darken=True)
        self.__screen.blit(self.actualBackground, (0, 0))

        # self.group.draw(self.__screen)

        if hitbox:
            displayHitBox()

        # affichage de Samy
        samySprite = self.loadImage(self.__mainCharacter.getCurrentAnimation(),
                                    rescale=[True, 80, MAIN_CHARACTER_HEIGHT])

        if self.__mainCharacter.Direction == "gauche":
            samySprite = self.loadImage(self.__mainCharacter.getCurrentAnimation(),
                                        rescale=[True, 80, MAIN_CHARACTER_HEIGHT], inverse=True)
        self.__mainCharacter.setHitbox(samySprite.get_width(), samySprite.get_height())
        self.__screen.blit(samySprite, (self.__mainCharacter.Coordinate.X, self.__mainCharacter.Coordinate.Y))

        # affichage des blocks
        for block in self.__map.getLevel(self.__camera.X, self.__camera.Y).getBlocks():
            newBlock = self.loadImage(block.Texture, rescale=[True, block.Width, block.Height])
            block.setHitbox(Hitbox(newBlock.get_width(), newBlock.get_height(), block.Coordinate))
            self.__screen.blit(newBlock, (block.Coordinate.X, block.Coordinate.Y))

        # affichage des tunnels
        for tunnel in self.__map.getLevel(self.__camera.X, self.__camera.Y).getTunnels():
            tun: Tunnel = tunnel
            newTunnel = self.loadImage(tun.Sprite)
            self.__screen.blit(newTunnel, (tun.Coordinate.X, tun.Coordinate.Y))

    def setStory(self, story: Story):
        pass

    def handleControls(self) -> bool | int:
        """
        Fonction de prise en charge des contrôles du clavier
        :return: L'image à afficher de Sami, False si la personne veut quitter le jeux.
        """
        # print the key pressed
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key in self.__control.getJumpKeys() and not self.__mainCharacter.JumpStatus and not self.__mainCharacter.IsInAir:
                    # and self.isTouchingTheGround(self.__mainCharacter)
                    return self.__mainCharacter.jump()

                if event.key not in self.__control.getJumpKeys():
                    self.__mainCharacter.JumpStatus = False

                if event.key in self.__control.getRightKeys():
                    return self.__mainCharacter.move_right()
                if event.key in self.__control.getLeftKeys():
                    return self.__mainCharacter.move_left()

            elif event.type == pygame.QUIT:
                return False

            else:
                self.__mainCharacter.JumpStatus = False

        return 0

    def handleCollisions(self, character: Character):
        """
        Gère les collisions entre les personnages et les différents éléments du niveau.
        :param character: le personnage dont il faut tester les collisions.
        :return: Rien
        """

        character.IsInAir = True
        for block in self.__map.getLevel(self.__camera.X, self.__camera.Y).getBlocks():
            blok: Block = block  # histoire d'avoir l'autocomplétion

            prev = character.getPrevisionnalCoordinate()
            dx: int = prev[0]
            dy: int = prev[1]

            # on check les collisions théoriques en x
            if blok.getHitbox().Rect.colliderect(
                    character.Coordinate.X + dx,
                    character.Coordinate.Y,
                    character.getHitbox().width,
                    character.getHitbox().height):
                character.changePrevisionnalX(0)

            # on check pour les collisions théoriques en Y
            if blok.getHitbox().Rect.colliderect(character.Coordinate.X,
                                                 character.Coordinate.Y + dy,
                                                 character.getHitbox().width,
                                                 character.getHitbox().height):

                if character.VelY < 0:
                    character.changePrevisionnalY(
                        blok.getHitbox().Rect.bottom - character.getHitbox().top
                    )
                    character.VelY = 0

                elif character.VelY >= 0:
                    character.changePrevisionnalY(
                        blok.getHitbox().Rect.top - character.getHitbox().bottom
                    )
                    character.VelY = 0
                    character.IsInAir = False

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
                  rescale: list[bool, int, int] = (False, 0, 0), inverse: bool = False) -> pygame.surface.Surface:
        """
        Ne charge l'image que si cela n'a pas déjà été fait.
        :param image: l'image à afficher
        :param darken: Si l'on doit assombrir l'image avant de l'enregistrer
        :param rescale: Une liste, avec en premier indice un booléen, suivi des deux dimensions
        :param inverse: Doit-on inverser l'image ou non
        :return: l'image chargée
        """

        for i in range(len(self.__alreadyLoadedImages)):
            if self.__alreadyLoadedImages[i].getPath() == image.getPath() and not inverse:
                # si l'image est déjà chargé dans la liste
                return self.__alreadyLoadedPygameImages[i]

        self.__alreadyLoadedImages.append(image)
        loadedImage = pygame.image.load(image.getPath()).convert_alpha()

        if darken:
            brighten = 85
            loadedImage.fill((brighten, brighten, brighten), special_flags=pygame.BLEND_SUB)

        if rescale[0]:
            loadedImage = pygame.transform.scale(loadedImage, (rescale[1], rescale[2]))

        if inverse:
            loadedImage = pygame.transform.flip(loadedImage, True, False)

        self.__alreadyLoadedPygameImages.append(loadedImage)
        return loadedImage
