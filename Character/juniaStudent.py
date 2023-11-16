from Character.agonist import Agonist
from animationSet import AnimationSet


class JuniaStudent(Agonist):
    def __init__(self):
        juniaStudentAnimationSet = AnimationSet()
        # ici on ajoutera les différentes animations à la main
        super().__init__("JuniaStudent", juniaStudentAnimationSet)