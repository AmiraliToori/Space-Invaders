

import pygame as pg

from graphic.resolution_setting import screen
from .tools.image_func import create_image
from .user import user_list

from sfx. sound_list import sounds

from icecream import ic

SCALE = 0.05
PLAYER_IMAGE = "material/Icons/player/player-frame1.png"

PLAYER_DEATH_FRAME_1 = "material/Icons/player/player-death-frame1.png"
PLAYER_DEATH_FRAME_2 = "material/Icons/player/player-death-frame2.png"

frame_lst = [PLAYER_DEATH_FRAME_1, PLAYER_DEATH_FRAME_2]

enemy_death_frames = [create_image(frame, SCALE) for frame in frame_lst]

class Player(pg.sprite.Sprite):
    
    def __init__(self) -> None:
        
        pg.sprite.Sprite.__init__(self)
        
        self.name = user_list.get_current_value()
        self.health = 3
        self.score = 0
        self.speed = 4
        
        self.player_x = screen.get_width() // 2
        self.player_y = screen.get_height() * 44 // 48
        
        
        self.image_file = pg.image.load(PLAYER_IMAGE)
        self.image_width = self.image_file.get_width()
        self.image_height = self.image_file.get_height()
        
        self.image = pg.transform.scale(self.image_file, (self.image_width * SCALE, self.image_height * SCALE)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (self.player_x, self.player_y)
        
        self.trigger = False
        self.is_win = False
        self.unlimited_gun = False
        
    
    def update(self):
        self.rect = (self.player_x, self.player_y)
    
    def move_right(self) -> None:
        if self.player_x < screen.get_width() - self.image.get_width():
            self.player_x += self.speed
        
    
    def move_left(self) -> None:
        if self.player_x > 0:
            self.player_x -= self.speed 
        
    def death(self) -> None:
        self.image = enemy_death_frames[0]
        sounds.play_player_explosion_sound()
        
    def player_name_update(self) -> None:
        self.name = user_list.get_current_value()
        
    
player = Player()
player_group = pg.sprite.GroupSingle()

player_group.add(player)