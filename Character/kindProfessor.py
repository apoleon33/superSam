from Character.agonist import Agonist
from animationSet import AnimationSet

class KindProfessor(Agonist):
    def __init__(self):
        kindProfessorAnimationSet = AnimationSet()
        # ici on ajoutera les différentes animations à la main
        super().__init__("KindProfessor", kindProfessorAnimationSet)