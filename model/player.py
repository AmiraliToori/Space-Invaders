
import pyxel


class Player:
    PLAYER_IMG = 0
    PLAYER_WIDTH = 16
    PLAYER_HEIGHT = 8
    U = 0
    V = 0
    PLAYER_SPEED = 2
    SCREEN_WIDTH = 128
    
    def __init__(self) -> None:
        self.x = 55
        self.y = 90
        self.lives = 3
        self.is_alive = True
        
    def move_right(self) -> None:
        if self.x + self.PLAYER_WIDTH < self.SCREEN_WIDTH:
            self.x += self.PLAYER_SPEED
        
    def move_left(self) -> None:
        if self.x > 0:
            self.x -= self.PLAYER_SPEED
            
    def shoot(self) -> None:
        self.bullet = Bullet()
        
    def death(self) -> None:
        if self.lives <= 0:
            self.is_alive = False



class Bullet(Player):
    BULLET_WIDTH = 2
    BULLET_HEIGHT = 6
    BULLET_COLOR = 3
    BULLET_SPEED = 4
    
    def __init__(self) -> None:
        self.x = self.player.x
        self.y = self.player.y
        self.width = Bullet.BULLET_WIDTH
        self.height = Bullet.BULLET_HEIGHT
        self.is_alive = True
        # super().__init__()
                                       
    def update(self) -> None:
        self.y -= Bullet.BULLET_SPEED
        
    def draw(self) -> None:
        pyxel.rect(self.x,
                   self.y,
                   self.width,
                   self.height,
                   Bullet.BULLET_COLOR)

    