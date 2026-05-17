import engine_main
import engine
from engine_nodes import Sprite2DNode, CameraNode


class Player(Sprite2DNode):
    def __init__(self):
        super().__init__(self)

    def tick(self, dt):
        pass

    def collision(self, contact):
        pass


player = Player()
camera = CameraNode()
engine.start()
