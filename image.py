class Image:
    __path: str

    def __init__(self, path: str):
        """
        Fonction stockant une image, et ses métadonnées
        :param path: le chemin d'accès de l'image
        """
        self.__path = path

    def getPath(self) -> str:
        return self.__path

    def setPath(self, path: str) -> None:
        self.__path = path
