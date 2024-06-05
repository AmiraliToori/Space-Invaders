
import pygame as pg
import random

from graphic.resolution_setting import screen

from objects.player import player_group, player
from objects.bullet import player_bullet, enemy_bullet, EnemyBullet
from objects.enemy import enemy_gp, mystery_gp, Mystery
from extra.database import insert_values

from objects.tools.text import Text
from objects.tools.custom_timer import unlimited_gun_power_timer
from objects.tools.pause import pause


from sfx.sound_list import sounds

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
        self.save_state = False
        
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
    def enemy_bullet_collide(enemy_group) -> None:
    
        hits = pg.sprite.groupcollide(enemy_group, player_bullet, False, True)
            
        for enemy in hits:
            
            if enemy.enemy_type == 1:
                player.score += 1
            elif enemy.enemy_type == 2:
                player.score += 2
            elif enemy.enemy_type == 3:
                player.score += 3
            elif enemy.enemy_type == 4:
                sounds.play_power_up_sound()
                player.score += 10
                player.unlimited_gun = True 
                unlimited_gun_power_timer.activate()
                
                
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
        if len(player_bullet) >= 1:
            player_bullet.update()
            player_bullet.draw(self.screen)   
        ##################################################################################
        
        enemy_gp.draw(self.screen)
        
        ##################################################################################
        self.enemy_bullet_collide(enemy_gp)
        
        ####################################################################################
        self.score_label.draw(self.screen)
        self.score_label.update(f"SCORE: {player.score}")
        
        self.lives_label.draw(self.screen)
        self.lives_label.update(f"LIVES: {player.health}")
        ######################################################################################
        
        for enemy in enemy_gp.sprites(): #FIXME - Bullets are not displaying on screen.
            fire = random.choices([1,0], [0.1, 99.9])[0]
            
            if fire == 1:
                enemy_bullet.add(EnemyBullet(enemy.rect.x + enemy.image.get_width() // 2, enemy.rect.y + enemy.image.get_height() // 2))
                
        
        enemy_bullet.update()
        enemy_bullet.draw(self.screen)
        
        ###########################################################################################
        
        if len(enemy_gp.sprites()) == 0:
            player.is_win = True
            self.save_state = True
            pause.change_pause_state()
            sounds.play_victory_sound()
            insert_values(player.name ,player.score)
            
        #########################################################################################
        
        # if pg.sprite.groupcollide(player_group, enemy_gp, False, False):
        #     player.death()
        #     pause.change_pause_state() #FIXME - Fix the issue with the collide the player with the enemies which gives error
        
        ###########################################################################################################
        
        if len(mystery_gp.sprites()) == 0:
            trigger = random.choices([1,0], [0.5, 99.5])[0]
            
            if trigger and player.unlimited_gun == False:
                mystery_gp.add(Mystery())
                sounds.play_mystery_sound()
                
        mystery_gp.update()
        mystery_gp.draw(self.screen)
        
        self.enemy_bullet_collide(mystery_gp)
        
        ############################################################################################################
        
        
game = GameScreen(screen.display(),
                  screen.get_width(),
                  screen.get_height())
        
    