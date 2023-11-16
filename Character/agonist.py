from Character.character import Character
from animationSet import AnimationSet


class Agonist(Character):
    def __init__(self, name: str, animationSet: AnimationSet):
        super().__init__(name, animationSet)
