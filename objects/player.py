
from graphic.resolution_setting import screen
import pygame as pg

from icecream import ic


PLAYER_IMAGE = "material/Icons/player/player-frame1.png"

PLAYER_DEATH_FRAME_1 = "material/Icons/player/player-death-frame1.png"
PLAYER_DEATH_FRAME_2 = "material/Icons/player/player-death-frame2.png"

SCALE = 0.05

class Player(pg.sprite.Sprite):
    
    def __init__(self,
                 name: str) -> None:
        
        pg.sprite.Sprite.__init__(self)
        
        self.name = name
        self.health = 3
        self.score = 0
        self.speed = 1
        
        self.player_x = screen.get_width() // 2
        self.player_y = screen.get_height() * 44 // 48
        
        
        self.image_file = pg.image.load(PLAYER_IMAGE).convert_alpha()
        self.image_width = self.image_file.get_width()
        self.image_height = self.image_file.get_height()
        
        self.image = pg.transform.scale(self.image_file, (self.image_width * SCALE, self.image_height * SCALE))
        self.rect = self.image.get_rect(center = (self.player_x, self.player_y))
        self.rect.center = (self.player_x, self.player_y)
        
        self.have_bullet = True
        
    
    def update(self):
        self.rect = (self.player_x, self.player_y)
    
    def move_right(self) -> None:
        if self.player_x < screen.get_width() - self.image.get_width():
            self.player_x += self.speed
        
    
    def move_left(self) -> None:
        if self.player_x > 0:
            self.player_x -= self.speed 
        

        
    def fire(self) -> None:
        # if self.bullet_exist == False
        pass
    
    def death(self) -> None:
        pass
    
player = Player("PLAYER")
player_group = pg.sprite.GroupSingle()

player_group.add(player)