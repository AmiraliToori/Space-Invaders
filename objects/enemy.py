


import pygame as pg

from graphic.resolution_setting import screen

from objects.player import player
from objects.bullet import player_bullet

from sfx.sound_list import sounds

from icecream import ic

SCALE = 0.04

ENEMY_DEATH_PATH = "material/Icons/enemy/enemy-blow-effect.png"

DEATH_IMAGE = pg.image.load(ENEMY_DEATH_PATH)

image_width = DEATH_IMAGE.get_width()
image_height = DEATH_IMAGE.get_height()

ENEMY_DEATH_IMG = pg.transform.scale(DEATH_IMAGE, (image_width * SCALE, image_height * SCALE))



#############################################################################################
ENEMY_TYPE_1_FRAME_ONE_PATH = "material/Icons/enemy/enemy_type1/enemy-type1-frame1.png"
ENEMY_TYPE_1_FRAME_TWO_PATH = "material/Icons/enemy/enemy_type1/enemy-type1-frame2.png"


IMAGE_FILE_ONE = pg.image.load(ENEMY_TYPE_1_FRAME_ONE_PATH)
        
image_width = IMAGE_FILE_ONE.get_width()
image_height = IMAGE_FILE_ONE.get_height()

ENEMY_TYPE_1_IMG = pg.transform.scale(IMAGE_FILE_ONE, (image_width * SCALE, image_height * SCALE))

###############################################################################################
ENEMY_TYPE_2_FRAME_ONE_PATH = "material/Icons/enemy/enemy_type2/enemy-type2-frame1.png"
ENEMY_TYPE_2_FRAME_TWO_PATH = "material/Icons/enemy/enemy_type2/enemy-type2-frame2.png"


################################################################################################
ENEMY_TYPE_3_FRAME_ONE_PATH = "material/Icons/enemy/enemy_type3/enemy-type3-frame1.png"
ENEMY_TYPE_3_FRAME_TWO_PATH = "material/Icons/enemy/enemy_type3/enemy-type3-frame2.png"

#################################################################################################3

ENEMY_MYSTERY_PATH = "material/Icons/enemy/mystery/mystery-frame1.png"
ENEMY_MYSTERY_DEATH_PATH = "material/Icons/enemy/mystery/mystery-blow-effect.png"


ENEMY_MOVE_LEFT = -10
ENEMY_MOVE_RIGHT = 10




class EnemyOne(pg.sprite.Sprite):
    
    
    def __init__(self,
                 x: int,
                 y: int) -> None:
        pg.sprite.Sprite.__init__(self)
        
        self.x = x
        self.y = y
        
        self.image = ENEMY_TYPE_1_IMG
        
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        self.move_right = True
        self.move_left = False
    
    
    def update(self) -> None:
        
        if self.move_right:
            
            self.rect.move_ip(ENEMY_MOVE_RIGHT, 0)
            if screen.get_width() - 2 * self.image.get_width() < self.rect.x + self.image.get_width():
                self.move_right = False
                self.move_left = True
                self.rect.move_ip(0, 20)
            
        elif self.move_left:

            self.rect.move_ip(ENEMY_MOVE_LEFT, 0)
            if self.rect.x - self.image.get_width() < 0 + self.image.get_width():
                self.move_left = False
                self.move_right = True
                self.rect.move_ip(0, 20)

        
        # collisions = pg.sprite.spritecollide(self, player_bullet, False)
        # for each_enemy in collisions:
            
        #     sounds.play_invader_killed()
        #     player.have_bullet = True
            
        #     each_enemy.image = ENEMY_DEATH_IMG
            
        #     each_enemy.kill()
    
        
        
                
    

example = EnemyOne(screen.get_width() // 2, screen.get_height() * 1 // 4)
example2 = EnemyOne(screen.get_width() // 2, screen.get_height() * 3 // 8)
enemy_gp_one = pg.sprite.Group()
            
            
enemy_gp_one.add(example)
enemy_gp_one.add(example2)
        
        
    
            
        