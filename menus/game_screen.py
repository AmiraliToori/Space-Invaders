
import pygame as pg

from graphic.resolution_setting import screen

from objects.player import player_group
from objects.bullet import player_bullet
from objects.enemy import enemy_gp_one
from objects.player import player

from sfx.sound_list import sounds

from icecream import ic

class GameScreen:
    
    
    def __init__(self,
                 screen,
                 width: int,
                 height: int) -> None:
        
        self.screen = screen
        self.width = width
        self.height = height
    
    
    def draw(self) -> None:
        self.screen.fill('black')
        
        player_group.update()
        player_group.draw(self.screen)
        
        player_bullet.update()
        player_bullet.draw(self.screen)    
        
        enemy_gp_one.draw(self.screen)
        
        
        if pg.sprite.groupcollide(enemy_gp_one, player_bullet, True, True):
            sounds.invader_killed_sound.play_sound()
            player.have_bullet = True
            
            # if pg.sprite.groupcollide(enemy_gp_one, player_bullet, True, True):
            #     for enemy_one in enemy_gp_one:
                    
        
        
game = GameScreen(screen.display(),
                  screen.get_width(),
                  screen.get_height())
        
    