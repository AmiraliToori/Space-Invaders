
import pygame as pg
from menus import main_screen
from sfx import music_list 

# Main Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE_FONT_SIZE = 50

# Hover Color button
GREEN_HOVER = "green"
RED_HOVER = "red"

# MUSIC FILES PATH
MAIN_SCREEN_THEME_PATH = "material/sounds/musics/main_menu_theme.mp3"


def main():
    
    pg.init()
    pg.mixer.init()
    
    screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    
    run = True
    screen_number = 1 # Start screen
    width, height = screen.get_width(), screen.get_height()
    
    menu = main_screen.MainScreen(screen,
                                    width,
                                    height,
                                    screen_number)
    
    # music_list.MusicList().play_main_title()
    while run:
        
        match screen_number:
            
            # First screen
            case 1:
                menu.draw()
                
                
            # enter intro of game
            case 2:
                screen.fill("black")
            
            
            # enter Settings
            case 3:
                screen.fill("black")
                
            
            
            # enter leaderboard
            case 4:
                screen.fill("yellow")
            
            
            # exit button
            case 5:
                pass
                
                
        
        keys = pg.key.get_pressed()
        
        if keys[pg.K_q]:
            run = False
        if keys[pg.K_SPACE]:
            screen_number = 2
        
        for event in pg.event.get():
            
            if event.type == pg.QUIT:
                run = False
                
        pg.display.flip()


if __name__ == "__main__":
    main()
    pg.quit()
