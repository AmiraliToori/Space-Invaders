




import pygame as pg
from graphic.resolution_setting import screen
from .player import player

from icecream import ic


PLAYER_BULLET_IMG = "material/Icons/player/player-bullet-frame1.png"
ENEMY_BULLET_IMG = "material/Icons/enemy/enemy-bullet.png"

SCALE = 0.02
        

class PlayerBullet(pg.sprite.Sprite):
    
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
            
        self.x = player.player_x 
        self.y = player.player_y 
        
        self.image = pg.image.load(PLAYER_BULLET_IMG).convert_alpha()
        
        self.image_width = self.image.get_width()
        self.image_height = self.image.get_height()
        
        self.image = pg.transform.scale(self.image, (self.image_width * SCALE, self.image_height * SCALE))
        
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        
        
    def update(self):
        self.rect.move_ip(0, -1)
        
        if self.rect.y < 0:
            player.have_bullet = True
            self.kill()

        
    

player_bullet = pg.sprite.GroupSingle()
    