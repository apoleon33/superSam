from Map.level import Level


class Story:
    __story: dict

    def __init__(self):
        self.__story = {}

    def getStory(self) -> dict:
        return self.__story

    def setStory(self, story: dict):
        self.__story = story

    def addToStory(self, level: Level, story: str):
        self.__story[level.getName()] = story

    def needAStory(self, level: Level) -> str | bool:
        for cle, valeur in self.__story:
            if cle == level.getName():
                return valeur
        return False


