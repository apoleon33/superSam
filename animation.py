from image import Image


class Animation:
    __images: [Image]

    def __init__(self):
        self.__images = []

    def getFrame(self, i: int) -> Image:
        return self.__images[i]

    def addFrame(self, image: Image) -> None:
        self.__images.append(image)

    def removeFrame(self):
        del self.__images[-1]
