

import pygame as pg

from .player import player

from .tools.image_func import create_image


SCALE = 0.03

PLAYER_BULLET_IMG_PATH = "material/Icons/player/player-bullet-frame1.png"

PLAYER_BULLET_IMG = create_image(PLAYER_BULLET_IMG_PATH, SCALE)


class PlayerBullet(pg.sprite.Sprite):
    
    def __init__(self) -> None:
        pg.sprite.Sprite.__init__(self)
        
        
        self.x, self.y = (player.player_x + player.image.get_width() // 2), (player.player_y + player.image.get_height() // 2) # type: ignore
        
        self.image = PLAYER_BULLET_IMG
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
    
    def update(self):
        self.rect.move_ip(0, -4) 
        
        if self.rect.y < 0: 
            self.kill()
    
player_bullet = pg.sprite.Group()


    