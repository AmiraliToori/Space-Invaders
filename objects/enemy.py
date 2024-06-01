


import pygame as pg
from graphic.resolution_setting import screen


ENEMY_TYPE_1_FRAME_ONE = "material/Icons/enemy/enemy_type1/enemy-type1-frame1.png"
ENEMY_TYPE_1_FRAME_ONE = "material/Icons/enemy/enemy_type1/enemy-type1-frame2.png"


ENEMY_TYPE_2_FRAME_ONE = "material/Icons/enemy/enemy_type2/enemy-type2-frame1.png"
ENEMY_TYPE_2_FRAME_ONE = "material/Icons/enemy/enemy_type2/enemy-type2-frame2.png"


ENEMY_TYPE_3_FRAME_ONE = "material/Icons/enemy/enemy_type3/enemy-type3-frame1.png"
ENEMY_TYPE_3_FRAME_ONE = "material/Icons/enemy/enemy_type3/enemy-type3-frame2.png"


ENEMY_MYSTERY = "material/Icons/enemy/mystery/mystery-frame1.png"

class Enemy(pg.sprite.Sprite):
    
    
    def __init__(self,
                 x: int,
                 y: int) -> None:
        pg.sprite.Sprite.__init__(self)
        
        self.x = x
        self.y = y
        
        
    def fire(self):
        pass
        
class EnemyOne(Enemy):
    
    
    def __init__(self) -> None:
        pg.sprite.Sprite.__init__(self)
        
        image_file = pg.image.load(ENEMY_TYPE_1_FRAME_ONE)
        
        