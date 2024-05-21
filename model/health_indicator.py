
import pyxel
from model.player import Player

HEALTH_COLOR = 7

HEALTH_TEXT_X = 0
HEALTH_TEXT_Y = 0

HEALTH_SHAPE_X = 2
HEALTH_SHAPE_Y = 3

U = 16
V = 0

IMG = 0

HEALTH_WIDTH = 8
HEALTH_HEIGHT = 8

class HealthIndicator(Player):
    
    def __init__(self, lives: int) -> None:
        
        super().__init__(lives = lives)
        self.lives = lives
    
    def update(self) -> None:
        pass
    
    def draw(self) -> None:
        pyxel.text(HEALTH_TEXT_X, HEALTH_TEXT_Y, str(self.lives), HEALTH_COLOR)
        pyxel.blt(HEALTH_SHAPE_X, HEALTH_SHAPE_Y, IMG, HEALTH_HEIGHT, HEALTH_WIDTH)
    
    
