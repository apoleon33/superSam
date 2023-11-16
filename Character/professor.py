from Character.antagonist import Antagonist
from animationSet import AnimationSet


class Professor(Antagonist):
    def __init__(self):
        professorAnimationSet = AnimationSet()
        # ici on ajoutera les différentes animations à la main
        super().__init__("Professeur", professorAnimationSet)