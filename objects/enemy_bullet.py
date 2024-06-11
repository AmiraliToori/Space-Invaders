
import pygame as pg

from .tools.image_func import create_image


SCALE = 0.03

ENEMY_BULLET_IMG_PATH = "material/Icons/enemy/enemy-bullet.png"

ENEMY_BULLET_IMG = create_image(ENEMY_BULLET_IMG_PATH, SCALE)

class EnemyBullet(pg.sprite.Sprite):
    
    def __init__(self,
                 x: int,
                 y: int) -> None:
        pg.sprite.Sprite.__init__(self)
        
        self.x = x
        self.y = y
        
        self.image = ENEMY_BULLET_IMG
        
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        
    def update(self) -> None:
        self.rect.move_ip(0, 1) 
        
        if self.rect.y > 0: 
            self.kill()
        
        
enemy_bullet = pg.sprite.Group()