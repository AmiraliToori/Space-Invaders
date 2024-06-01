
import pygame as pg
from menus import main_screen, setting_screen, intro_screen
from sfx import music_list




# MUSIC FILES PATH
MAIN_SCREEN_THEME_PATH = "material/sounds/musics/main_menu_theme.mp3"


def main():
    
    pg.init()
    pg.mixer.init()
    
    # screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT], pg.RESIZABLE)
    # screen = pg.transform.scale(screen, (windoWidth,windowHeight)) 
    # window.blit(screen, (0, 0))
    # screen = resolution_setting.screen.display()
    run = True
    screen_number = 1 # Start screen
    # music_list.MusicList().play_main_title()
    
    while run:
        
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
                screen.fill("yellow")
                
            
            # exit button
            case 5:
                pg.quit()
                
            # the game itself
            case 6:
                pass
                
                
        
        keys = pg.key.get_pressed()
        
        if keys[pg.K_q]:
            run = False
        # if keys[pg.K_SPACE]:
        #     screen_number = 2
        
        for event in pg.event.get():
            
            if event.type == pg.VIDEORESIZE:
                # screen = resolution_setting.screen.set_custom_display(event.w, event.h)
                screen = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)
                
            if event.type == pg.QUIT:
                run = False
                
        pg.display.flip()


if __name__ == "__main__":
    main()
    pg.quit()
