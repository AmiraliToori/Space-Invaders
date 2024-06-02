




import pygame as pg

from .player import player

# from .enemy import enemy_gp_one

from icecream import ic


PLAYER_BULLET_IMG = "material/Icons/player/player-bullet-frame1.png"
ENEMY_BULLET_IMG = "material/Icons/enemy/enemy-bullet.png"

SCALE = 0.03
        

class PlayerBullet(pg.sprite.Sprite):
    
    def __init__(self) -> None:
        pg.sprite.Sprite.__init__(self)
            
        self.x, self.y = (player.player_x + player.image.get_width() // 2), (player.player_y + player.image.get_height() // 2)
        
        
        self.image = pg.image.load(PLAYER_BULLET_IMG).convert_alpha()
        
        self.image_width = self.image.get_width()
        self.image_height = self.image.get_height()
        
        self.image = pg.transform.scale(self.image, (self.image_width * SCALE, self.image_height * SCALE))
        
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        
        
        
    def update(self):
        self.rect.move_ip(0, -1)
        
        if self.rect.y < 0:
            self.kill()
            
        

class EnemyBullet(pg.sprite.Sprite):
    
    def __init__(self) -> None:
        pg.sprite.Sprite.__init__(self)
        
    
player_bullet = pg.sprite.Group()

    