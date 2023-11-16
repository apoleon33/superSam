from Character.agonist import Agonist
from animationSet import AnimationSet


class Lucas(Agonist):
    def __init__(self):
        lucasAnimationSet = AnimationSet()
        # ici on ajoutera les différentes animations à la main
        super().__init__("Lucas", lucasAnimationSet)
