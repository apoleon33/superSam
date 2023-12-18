from Map.offensiveBlock import OffensiveBlock
from animationSet import AnimationSet
from coordinate import Coordinate
from image import Image


class Fire(OffensiveBlock):
    __animationSet: AnimationSet

    def __init__(self, coordinate: Coordinate):
        """
        Bloc de feux, seul bloc ayant une animation.
        :param coordinate: les coordonnées de spawn du feu
        """
        super().__init__(
            texture=Image("assets/blocks/fire/fire.png"),
            width=32,
            height=32,
            coordinate=coordinate
        )

        self.createAnimation(
            directory="assets/blocks/fire_animation",
            nbImages=6
        )
