from Character.character import Character
from animationSet import AnimationSet


class Antagonist(Character):
    def __init__(self, name: str, moveAnimation: AnimationSet):
        super().__init__(name, moveAnimation)

    # jsp quoi mettre d'autre
