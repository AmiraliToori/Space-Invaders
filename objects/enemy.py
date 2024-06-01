


import pygame as pg
from graphic.resolution_setting import screen


ENEMY_TYPE_1_FRAME_ONE = "material/Icons/enemy/enemy_type1/enemy-type1-frame1.png"
ENEMY_TYPE_1_FRAME_ONE = "material/Icons/enemy/enemy_type1/enemy-type1-frame2.png"


ENEMY_TYPE_2_FRAME_ONE = "material/Icons/enemy/enemy_type2/enemy-type2-frame1.png"
ENEMY_TYPE_2_FRAME_ONE = "material/Icons/enemy/enemy_type2/enemy-type2-frame2.png"


ENEMY_TYPE_3_FRAME_ONE = "material/Icons/enemy/enemy_type3/enemy-type3-frame1.png"
ENEMY_TYPE_3_FRAME_ONE = "material/Icons/enemy/enemy_type3/enemy-type3-frame2.png"


ENEMY_MYSTERY = "material/Icons/enemy/mystery/mystery-frame1.png"

SCALE = 0.05

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
    
    
    def __init__(self,
                 x: int,
                 y: int) -> None:
        super().__init__( x, y)
        
        self.image_file = pg.image.load(ENEMY_TYPE_1_FRAME_ONE)
        
        self.image_width = self.image_file.get_width()
        self.image_height = self.image_file.get_height()
        
        self.image = pg.transform.scale(self.image_file, (self.image_height * SCALE, self.image_height * SCALE))
        
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        self.move_right = True
        self.move_left = False
    

    def move_left(self) -> None:
        self.rect.move_ip(- 0.1, 0)
    
    def move_right(self) -> None:
        self.rect.move_ip(0.1, 0)
    
    def move_down(self) -> None:
        self.rect.move_ip(0, 20)
    
    
    def update(self) -> None:
        
        
        if self.x < screen.get_width():
            self.rect.move_ip(0.1, 0)
        else:
            pass
            
        
        
    
            
        