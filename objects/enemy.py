


import pygame as pg

from objects.custom_timer import enemy_death_frame_timer

from graphic.resolution_setting import screen

from sfx.sound_list import sounds

from .image_func import create_image

from icecream import ic

SCALE = 0.04


ENEMY_DEATH_PATH = "material/Icons/enemy/enemy-blow-effect.png"

ENEMY_DEATH_IMG = create_image(ENEMY_DEATH_PATH, SCALE)

#############################################################################################
ENEMY_TYPE_1_FRAME_ONE_PATH = "material/Icons/enemy/enemy_type1/enemy-type1-frame1.png"
ENEMY_TYPE_1_FRAME_TWO_PATH = "material/Icons/enemy/enemy_type1/enemy-type1-frame2.png"

frame_lst = [ENEMY_TYPE_1_FRAME_ONE_PATH, ENEMY_TYPE_1_FRAME_TWO_PATH]

enemy_one = [create_image(frame, SCALE) for frame in frame_lst]

###############################################################################################
ENEMY_TYPE_2_FRAME_ONE_PATH = "material/Icons/enemy/enemy_type2/enemy-type2-frame1.png"
ENEMY_TYPE_2_FRAME_TWO_PATH = "material/Icons/enemy/enemy_type2/enemy-type2-frame2.png"

frame_lst = [ENEMY_TYPE_2_FRAME_ONE_PATH, ENEMY_TYPE_2_FRAME_TWO_PATH]

enemy_two = [create_image(frame, SCALE) for frame in frame_lst]

################################################################################################
ENEMY_TYPE_3_FRAME_ONE_PATH = "material/Icons/enemy/enemy_type3/enemy-type3-frame1.png"
ENEMY_TYPE_3_FRAME_TWO_PATH = "material/Icons/enemy/enemy_type3/enemy-type3-frame2.png"

frame_lst = [ENEMY_TYPE_3_FRAME_ONE_PATH, ENEMY_TYPE_3_FRAME_TWO_PATH]

enemy_three = [create_image(frame, SCALE) for frame in frame_lst]

#################################################################################################3

ENEMY_MYSTERY_PATH = "material/Icons/enemy/mystery/mystery-frame1.png"
ENEMY_MYSTERY_DEATH_PATH = "material/Icons/enemy/mystery/mystery-blow-effect.png"


ENEMY_MOVE_LEFT = -10
ENEMY_MOVE_RIGHT = 10
ENEMY_MOVE_DOWN = 35



class Enemy(pg.sprite.Sprite):
    
    
    def __init__(self,
                 x: int,
                 y: int,
                 enemy_frame_lst: list) -> None:
        pg.sprite.Sprite.__init__(self)
        
        self.x = x
        self.y = y
        
        self.frame_lst = enemy_frame_lst
        self.image = self.frame_lst[0]
        
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        self.move_right = True
        self.move_left = False
        
        self.cooldown_death_time = 500
        self.last_time = pg.time.get_ticks()

        self.frame_one = True
        self.frame_two = False
        
        self.is_dead = False
    
    def update(self) -> None:
        if not self.is_dead:
            if self.frame_one:
                self.image = self.frame_lst[0]
                self.frame_one = False
                self.frame_two = True
                
            elif self.frame_two:
                self.image = self.frame_lst[1]
                self.frame_one = True
                self.frame_two = False
        
        if self.move_right:
            
            
            self.rect.move_ip(ENEMY_MOVE_RIGHT, 0)
            if screen.get_width() - 2 * self.image.get_width() < self.rect.x + self.image.get_width():
                self.move_right = False
                self.move_left = True
                self.rect.move_ip(0, ENEMY_MOVE_DOWN)
            
        elif self.move_left:

            self.rect.move_ip(ENEMY_MOVE_LEFT, 0)
            if self.rect.x - self.image.get_width() < 0 + self.image.get_width():
                self.move_left = False
                self.move_right = True
                self.rect.move_ip(0, ENEMY_MOVE_DOWN)
                
        if self.rect.y > screen.get_width(): # Silence kill, if the Invaders get out window from the bottom of screen.
            self.kill()
            
            
    def death(self):
        if self.is_dead:
            enemy_death_frame_timer.activate()
            
            self.move_left = False
            self.move_right = False
            
            enemy_death_frame_timer.update()
            if not enemy_death_frame_timer.active:
                self.kill()
        
                
    def set_death_image(self):
        sounds.play_invader_killed()
        self.image = ENEMY_DEATH_IMG
        
    
    

enemy_gp_one = pg.sprite.Group()
enemy_gp_two = pg.sprite.Group()
enemy_gp_three = pg.sprite.Group()

for x in range(3, 9, 1):
    enemy_gp_one.add(Enemy(screen.get_width() * x // 12, screen.get_height() * 5 // 12, enemy_one))
    
for x in range(3, 9, 1):
    enemy_gp_two.add(Enemy(screen.get_width() * x // 12, screen.get_height() * 4 // 12, enemy_two))
    
for x in range(3, 9, 1):
    enemy_gp_two.add(Enemy(screen.get_width() * x // 12, screen.get_height() * 3 // 12, enemy_three))
        
    
            
        