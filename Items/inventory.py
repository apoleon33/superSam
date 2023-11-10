from Items.item import Item


class Inventory:
    __items: [Item]

    def __init__(self):
        self.__items = []

    def addItem(self, item: Item) -> None:
        self.__items.append(item)

    def removeItem(self, item: Item) -> None:
        for i in range(len(self.__items)):
            if item.getName() == self.__items[i].getName():
                del self.__items[i]
                break