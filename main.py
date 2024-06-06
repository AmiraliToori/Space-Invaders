
import pygame as pg
import random

from menus import main_screen, setting_screen, intro_screen, game_screen, game_popup, leaderboard_surface, user_surface

from objects.player import player
from objects.player_bullet import player_bullet, PlayerBullet
from objects.enemy import enemy_gp, enemy_box, Enemy
from objects.user import user_list


from objects.tools.timer import enemies_move_timer, enemies_spawn_timer
from objects.tools.pause import pause
from objects.tools.custom_timer import unlimited_gun_power_timer

from sfx.sound_list import sounds

from graphic.resolution_setting import screen

from icecream import ic



# MUSIC FILES PATH
MAIN_SCREEN_THEME_PATH = "material/sounds/musics/main_menu_theme.mp3"


def main():
    
    
    leaderboard_window = None
    
    pg.init()
    pg.mixer.init()
    
    clock = pg.time.Clock()
    run = True
    screen_number = 1 # Start screen
    # music_list.MusicList().play_main_title()
    
    while run:
        
        user_list.update_user_preset()
        
        match screen_number:
            
            # First screen
            case 1:
                main_screen.main.draw()
                screen_number = main_screen.main.update()
                
            # enter intro of game
            case 2:
                intro_screen.game_intro.draw()
                screen_number = intro_screen.game_intro.update()
    
            # enter Settings
            case 3:
                setting_screen.setting.draw()
                screen_number = setting_screen.setting.update()
            
            # enter leaderboard
            case 4:
                leaderboard_surface.leaderboard_screen.draw()
                screen_number = leaderboard_surface.leaderboard_screen.update()
                
            # exit button
            case 5:
                run = False
                
            # the game itself
            case 6:
                if not pause.pause_state:
                    game_screen.game.draw()
                elif pause.pause_state and player.is_win == False and player.is_lost == False:
                    game_popup.pause_popup.draw()
                    screen_number = game_popup.pause_popup.update()
                    
                if player.is_win:
                    game_popup.victory_popup.draw()
                    screen_number = game_popup.victory_popup.update()
                
                elif player.is_lost:
                    game_popup.gameover_popup.draw()
                    screen_number = game_popup.gameover_popup.update()
            
            # Add user button
            case 7:
                user_surface.user_setting.draw()
                screen_number = user_surface.user_setting.update()
                
        
        keys = pg.key.get_pressed()
                   
        if keys[pg.K_q]:
            run = False
            
        if keys[pg.K_LEFT]:
            player.move_left()
            
        if keys[pg.K_RIGHT]:
            player.move_right()
        
    
        elif enemy_box.move_to_down == True and not pause.pause_state and screen_number == 6:
                enemy_type_random = random.choices([1,2,3])[0]
                
                if enemies_move_timer.timing - 100 > 0:
                    enemies_move_timer.change_timing_event(enemies_move_timer.timing - 100)
                
                
                if enemy_box.move_to_left_toggle:
                    for x in range(17, 50, 3):
                        enemy_gp.add(Enemy(screen.get_width() * x // 50, screen.get_height() * 9 // 48, enemy_type_random))
                    enemy_box.move_to_down = False
                    
                    
                else:
                    for x in range(2, 35, 3):
                        enemy_gp.add(Enemy(screen.get_width() * x // 50, screen.get_height() * 9 // 48, enemy_type_random))
                    enemy_box.move_to_down = False
        
        
        
        event_list = pg.event.get()
        
        for event in event_list:
        
            if event.type == pg.KEYDOWN:
            
                if event.key == pg.K_SPACE and screen_number == 6 and not pause.pause_state:
                    
                    if len(player_bullet) == 0 or player.unlimited_gun: 
                        sounds.play_shoot_sound()
                        player_bullet.add(PlayerBullet())
                        
                elif event.key == pg.K_ESCAPE and screen_number == 6:
                    pause.change_pause_state()
        
            
            elif event.type == enemies_move_timer.get_timer_id() and not pause.pause_state and screen_number == 6:
                
                enemy_gp.update()
                
                
                enemy_box.update_group(enemy_gp)
                enemy_box.box_movement()
                
            
            elif player.unlimited_gun:
                
                unlimited_gun_power_timer.update()
                if not unlimited_gun_power_timer.active:
                    player.unlimited_gun = False 
            
            elif event.type == pg.QUIT:
                run = False
                
        clock.tick(60)
        pg.display.flip()


if __name__ == "__main__":
    main()
    pg.quit()
