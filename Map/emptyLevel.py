from Map.level import Level


class EmptyLevel(Level):
    def __init__(self):
        """ Un niveau vide, que le personnage ne visitera probablement jamais"""
        super().__init__("empty")
