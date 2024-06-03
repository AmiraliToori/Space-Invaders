
import pygame as pg
import random


from objects.custom_timer import enemy_death_frame_timer
from objects.player import player


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
ENEMY_TYPE_1_BLOW_EFFECT_PATH = "material/Icons/enemy/enemy_type1/enemy-type1-blow-effect.png"

frame_lst = [ENEMY_TYPE_1_FRAME_ONE_PATH, ENEMY_TYPE_1_FRAME_TWO_PATH, ENEMY_TYPE_1_BLOW_EFFECT_PATH]

enemy_one = [create_image(frame, SCALE) for frame in frame_lst]

###############################################################################################
ENEMY_TYPE_2_FRAME_ONE_PATH = "material/Icons/enemy/enemy_type2/enemy-type2-frame1.png"
ENEMY_TYPE_2_FRAME_TWO_PATH = "material/Icons/enemy/enemy_type2/enemy-type2-frame2.png"
ENEMY_TYPE_2_BLOW_EFFECT_PATH = "material/Icons/enemy/enemy_type2/enemy-type2-blow-effect.png"

frame_lst = [ENEMY_TYPE_2_FRAME_ONE_PATH, ENEMY_TYPE_2_FRAME_TWO_PATH, ENEMY_TYPE_2_BLOW_EFFECT_PATH]

enemy_two = [create_image(frame, SCALE) for frame in frame_lst]

################################################################################################
ENEMY_TYPE_3_FRAME_ONE_PATH = "material/Icons/enemy/enemy_type3/enemy-type3-frame1.png"
ENEMY_TYPE_3_FRAME_TWO_PATH = "material/Icons/enemy/enemy_type3/enemy-type3-frame2.png"
ENEMY_TYPE_3_BLOW_EFFECT_PATH = "material/Icons/enemy/enemy_type3/enemy-type3-blow-effect.png"

frame_lst = [ENEMY_TYPE_3_FRAME_ONE_PATH, ENEMY_TYPE_3_FRAME_TWO_PATH, ENEMY_TYPE_3_BLOW_EFFECT_PATH]

enemy_three = [create_image(frame, SCALE) for frame in frame_lst]

#################################################################################################3

ENEMY_MYSTERY_PATH = "material/Icons/enemy/mystery/mystery-frame1.png"
ENEMY_MYSTERY_DEATH_PATH = "material/Icons/enemy/mystery/mystery-blow-effect.png"


ENEMY_MOVE_LEFT = -10
ENEMY_MOVE_RIGHT = 10
ENEMY_MOVE_DOWN = 35

class EnemyBox:
    
    
    def __init__(self, enemy_group) -> None:
        
        self.group = enemy_group
        self.move_to_right_toggle = True
        self.move_to_left_toggle = False
        self.move_to_down = False
        
    def box_movement(self):
        
        if [enemy for enemy in self.group.sprites() if enemy.rect.x + enemy.image.get_width() * 2 >= screen.get_width()]:
            self.move_to_left_toggle = True
            self.move_to_right_toggle = False
            self.move_down()
            
            
        if self.move_to_left_toggle:
            self.move_left()
            
            
        if [enemy for enemy in self.group.sprites() if enemy.rect.x - enemy.image.get_width() // 2 <= 0]:
            self.move_to_left_toggle = False
            self.move_to_right_toggle = True
            self.move_down()
            
            
        if self.move_to_right_toggle:
            self.move_right()
        
        [enemy.kill() for enemy in self.group.sprites() if enemy.rect.y > screen.get_width()]
    
    def update_group(self, group) -> None:
        self.group = group
        
    
    def move_right(self) -> None:
        for enemy in self.group.sprites():
            enemy.move_to_right()
            
            
    def move_left(self) -> None:
        for enemy in self.group.sprites():
            enemy.move_to_left()
            
            
    def move_down(self) -> None:
        for enemy in self.group.sprites():
            enemy.move_down()
                
                
                
                

class Enemy(pg.sprite.Sprite):
    
    
    def __init__(self,
                 x: int,
                 y: int,
                 enemy_frame_lst: list,
                 enemy_type: int) -> None:
        pg.sprite.Sprite.__init__(self)
        
        self.x = x
        self.y = y
        self.enemy_type = enemy_type
        
        self.frame_lst = enemy_frame_lst
        self.image = self.frame_lst[0]
        
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        self.move_right = True
        self.move_left = False

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

        
    def move_to_right(self) -> None:
        self.rect.move_ip(ENEMY_MOVE_RIGHT, 0)
    
    def move_to_left(self) -> None:
        self.rect.move_ip(ENEMY_MOVE_LEFT, 0)
        
    def move_down(self) -> None:
        self.rect.move_ip(0, ENEMY_MOVE_DOWN)
    
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
        self.image = self.frame_lst[2]
        
    # def fire(self):
        
    #     fire_choice = random.choices([1, 0], [0.1, 99.9])
    #     if fire_choice[0] == 1:
    #         enemy_bullet.add(EnemyBullet(self.rect.x, self.rect.y))
            
        
        
        
class Mystery(Enemy):
    
    def __init__(self,
                 x: int,
                 y: int,
                 enemy_frame_lst: list,
                 enemy_type: int) -> None:
        super().__init__(x, y, enemy_frame_lst, enemy_type)
    
    
    
        
mystery = pg.sprite.GroupSingle()
enemy_gp = pg.sprite.Group()



for x in range(2, 35, 3):
    enemy_gp.add(Enemy(screen.get_width() * x // 50, screen.get_height() * 9 // 48, enemy_three, 3))
    
for x in range(2, 35, 3):
    enemy_gp.add(Enemy(screen.get_width() * x // 50, screen.get_height() * 12 // 48, enemy_two, 2))
    
for x in range(2, 35, 3):
    enemy_gp.add(Enemy(screen.get_width() * x // 50, screen.get_height() * 15 // 48, enemy_two, 2))
    
for x in range(2, 35, 3):
    enemy_gp.add(Enemy(screen.get_width() * x // 50, screen.get_height() * 18 // 48, enemy_one, 1))
    
for x in range(2, 35, 3):
    enemy_gp.add(Enemy(screen.get_width() * x // 50, screen.get_height() * 21 // 48, enemy_one, 1))
        
enemy_box = EnemyBox(enemy_gp)
            
        