
import pygame as pg
import display

from menu import menu_screen
from studio import play_sound, play_music

# Main Screen
TITLE_FONT_SIZE = 50

# Hover Color button
GREEN_HOVER = "green"
RED_HOVER = "red"

# MUSIC FILES PATH
MAIN_SCREEN_THEME_PATH = "material/sounds/musics/main_menu_theme.mp3"


def main():
    
    pg.init()
    pg.mixer.init()
    
    
    
    # main_screen_theme = play_music(MAIN_SCREEN_THEME_PATH)
    # pg.mixer.music.play(main_screen_theme)
    
    screen = display.set_screen_display()
    display.set_desktop_icon()
    
    
    run = True
    screen_number = 1 # Start screen
    width, height = screen.get_width(), screen.get_height()
    
    menu = menu_screen.Main_screen(screen,
                                    width,
                                    height,
                                    screen_number)
    
    while run:
        
        match screen_number:
            
            # First screen
            case 1:
                menu.title_screen.draw(screen)
                menu.start_btn.draw(screen, GREEN_HOVER)
                menu.setting_btn.draw(screen, GREEN_HOVER)
                menu.leaderboard_btn.draw(screen, GREEN_HOVER)
                menu.exit_btn.draw(screen, RED_HOVER)
                
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
                # width_surface = width // 3
                # height_surface = height // 4
                # LINE_WIDTH = 2
                # exit_surface = pg.surface.Surface((width_surface ,height_surface))
                
                # display.fill_screen(exit_surface, "black")
                
                # display.draw_box(exit_surface,
                #                  "white",
                #                  width_surface,
                #                  height_surface,
                #                  LINE_WIDTH)
                
        
        keys = pg.key.get_pressed()
        
        if keys[pg.K_q]:
            run = False
        if keys[pg.K_SPACE]:
            screen_number = 2
        
        for event in pg.event.get():
            
            if event.type == pg.QUIT:
                run = False
                
        # while menu_screen.main_screen.abravesh_flag:
        pg.display.flip()


if __name__ == "__main__":
    main()
    pg.quit()