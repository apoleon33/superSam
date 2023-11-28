from Map.tunnel import Tunnel


class Elevator(Tunnel):
    def __init__(self):
        super().__init__("elevator")
        self.Image = Image("assets/blocks/tunnel/elevator/elevator.png")