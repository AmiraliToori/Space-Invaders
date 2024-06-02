
import pygame as pg

from graphic.resolution_setting import screen

from objects.player import player_group
from objects.bullet import player_bullet
from objects.enemy import enemy_gp_one


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
        
        if len(player_bullet) == 1:
            player_bullet.update()
            player_bullet.draw(self.screen)    
        
        
        enemy_gp_one.draw(self.screen)
        
        hits = pg.sprite.groupcollide(enemy_gp_one, player_bullet, False, True)
        
        for enemy in hits:
            enemy.is_dead = True
            enemy.set_death_image()
            
        for enemy in enemy_gp_one:
            if enemy.is_dead:
                enemy.death()
            
           
           
        
            
        
        
game = GameScreen(screen.display(),
                  screen.get_width(),
                  screen.get_height())
        
    