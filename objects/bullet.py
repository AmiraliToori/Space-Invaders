

import pygame as pg

from .player import player

from graphic.resolution_setting import screen

from .image_func import create_image

from icecream import ic

SCALE = 0.03

PLAYER_BULLET_IMG_PATH = "material/Icons/player/player-bullet-frame1.png"

PLAYER_BULLET_IMG = create_image(PLAYER_BULLET_IMG_PATH, SCALE)


###########################################################################################


ENEMY_BULLET_IMG_PATH = "material/Icons/enemy/enemy-bullet.png"

ENEMY_BULLET_IMG = create_image(ENEMY_BULLET_IMG_PATH, SCALE)


class PlayerBullet(pg.sprite.Sprite):
    
    def __init__(self) -> None:
        pg.sprite.Sprite.__init__(self)
        
        
        self.x, self.y = (player.player_x + player.image.get_width() // 2), (player.player_y + player.image.get_height() // 2)
        
        self.image = PLAYER_BULLET_IMG
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        
    
    def update(self):
        self.rect.move_ip(0, -1)
        
        if self.rect.y < 0:
            self.kill()
    
player_bullet = pg.sprite.Group()

    