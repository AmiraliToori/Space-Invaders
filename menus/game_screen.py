
import pygame as pg
import random

from graphic.resolution_setting import screen

from objects.player import player_group, player
from objects.bullet import player_bullet, enemy_bullet, EnemyBullet
from objects.enemy import enemy_gp
from objects.tools.text import Text

from icecream import ic

FONT_PATH = "material/font/Pixelify_Sans/PixelifySans-VariableFont_wght.ttf"

class GameScreen:
    
    
    def __init__(self,
                 screen,
                 width: int,
                 height: int) -> None:
        
        self.screen = screen
        self.width = width
        self.height = height
        
        self.score_label = Text(f"SCORE: {player.score}",
                                FONT_PATH,
                                30,
                                "#06ff06",
                                "black",
                                80,
                                20)
        
        self.lives_label = Text(f"LIVES: {player.health}",
                                FONT_PATH,
                                30,
                                "#06ff06",
                                "black",
                                730,
                                20)
    
    
    
    @staticmethod
    def enemy_gps_collide(enemy_group) -> None:
    
        hits = pg.sprite.groupcollide(enemy_group, player_bullet, False, True)
            
        for enemy in hits:
            
            if enemy.enemy_type == 1:
                player.score += 1
            elif enemy.enemy_type == 2:
                player.score += 2
            elif enemy.enemy_type == 3:
                player.score += 3
                
            enemy.is_dead = True
            enemy.set_death_image()
            
        for enemy in enemy_group:
            if enemy.is_dead:
                enemy.death()
    
    
    def draw(self) -> None:
        self.screen.fill('black')
        
        ######################################################
        player_group.update()
        player_group.draw(self.screen)
        
        ################################################################################
        if len(player_bullet) == 1:                                  #TODO - Add power effect for unlimited magazine
            player_bullet.update()
            player_bullet.draw(self.screen)    
        ##################################################################################
        
        enemy_gp.draw(self.screen)
        
        ##################################################################################
        self.enemy_gps_collide(enemy_gp)
        
        ####################################################################################
        self.score_label.draw(self.screen)
        self.score_label.update(f"SCORE: {player.score}")
        
        self.lives_label.draw(self.screen)
        self.lives_label.update(f"LIVES: {player.health}")
        ######################################################################################
        
        # enemy_bullet.update()
        enemy_bullet.draw(self.screen)  
        
        
        for enemy in enemy_gp.sprites():
            fire = random.choices([1,0], [0.001, 99.999])[0]
            
            if fire == 1:
                enemy_bullet.add(EnemyBullet(enemy.rect.x + enemy.image.get_width() // 2, enemy.rect.y + enemy.image.get_height() // 2))
        
        if len(enemy_gp.sprites()) == 0:
            pass
        
        
        
game = GameScreen(screen.display(),
                  screen.get_width(),
                  screen.get_height())
        
    