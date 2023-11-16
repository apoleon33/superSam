from Character.antagonist import Antagonist
from animationSet import AnimationSet


class Watcher(Antagonist):
    def __init__(self):
        watcherAnimationSet = AnimationSet()
        # ici on ajoutera les différentes animations à la main
        super().__init__("Watcher", watcherAnimationSet)
