import pygame


class Control:
    __leftKeys: [pygame.constants]
    __rightKeys: [pygame.constants]
    __jumpKeys: [pygame.constants]
    __quitKeys: [pygame.constants]

    def __init__(self):
        self.__leftKeys = [pygame.K_LEFT, pygame.K_KP4, pygame.K_q]
        self.__rightKeys = [pygame.K_RIGHT, pygame.K_KP6, pygame.K_d]
        self.__jumpKeys = [pygame.K_UP, pygame.K_KP8, pygame.K_z, pygame.K_SPACE]
        self.__quitKeys = [pygame.QUIT]

    def getLeftKeys(self) -> list:
        return self.__leftKeys

    def getRightKeys(self) -> list:
        return self.__rightKeys

    def getJumpKeys(self) -> list:
        return self.__jumpKeys

    def getQuitKeys(self) -> list:
        return self.__quitKeys

    def isAControl(self, key) -> str | bool:
        """
        On demande si la touche key est associée à une action.
        Si c'est le cas, on renvoie l'action associée, faux sinon
        """

        returnStatus = False

        if key.key in self.__rightKeys:
            returnStatus = "RIGHT"
        elif key.key in self.__leftKeys:
            returnStatus = "LEFT"
        elif key.key in self.__jumpKeys:
            returnStatus = "JUMP"
        elif key.key in self.__quitKeys:
            returnStatus = "QUIT"

        return returnStatus
