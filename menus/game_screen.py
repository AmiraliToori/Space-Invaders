
import pygame as pg

from graphic.resolution_setting import screen

from objects.player import player_group
from objects.bullet import player_bullet
from objects.enemy import enemy_gp_one, enemy_gp_two, enemy_gp_three


from icecream import ic



class GameScreen:
    
    
    def __init__(self,
                 screen,
                 width: int,
                 height: int) -> None:
        
        self.screen = screen
        self.width = width
        self.height = height
    
    
    
    @staticmethod
    def enemy_gps_collide(enemy_group) -> None:
    
        hits = pg.sprite.groupcollide(enemy_group, player_bullet, False, True)
            
        for enemy in hits:
            enemy.is_dead = True
            enemy.set_death_image()
            
        for enemy in enemy_group:
            if enemy.is_dead:
                enemy.death()
    
    
    def draw(self) -> None:
        self.screen.fill('black')
        
        player_group.update()
        player_group.draw(self.screen)
        
        if len(player_bullet) == 1:
            player_bullet.update()
            player_bullet.draw(self.screen)    
        
        
        enemy_gp_one.draw(self.screen)
        enemy_gp_two.draw(self.screen)
        enemy_gp_three.draw(self.screen)
        
        self.enemy_gps_collide(enemy_gp_one)
        self.enemy_gps_collide(enemy_gp_two)
        self.enemy_gps_collide(enemy_gp_three)
        
        # hits = pg.sprite.groupcollide(enemy_gp_one, player_bullet, False, True)
        
        # for enemy in hits:
        #     enemy.is_dead = True
        #     enemy.set_death_image()
            
        # for enemy in enemy_gp_one:
        #     if enemy.is_dead:
        #         enemy.death()
                
        
game = GameScreen(screen.display(),
                  screen.get_width(),
                  screen.get_height())
        
    