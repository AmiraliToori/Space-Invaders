
import pygame as pg
import display

from menu import menu_screen

# Font
FONT_PATH = "material/font/Pixelify_Sans/PixelifySans-VariableFont_wght.ttf"
DEFAULT_FONT_COLOR = "white"
BACKGROUND_COLOR = "black"

# Main Screen
TITLE_FONT_SIZE = 50

GREEN_HOVER = "green"
RED_HOVER = "red"


def main():
    
    pg.init()
    pg.mixer.init()
    screen = display.set_screen_display()
    display.set_desktop_icon()
    
    
    run = True
    screen_number = 1 # Start screen
    width, height = screen.get_width(), screen.get_height()
    
    
    
    
    while run:
        
        match screen_number:
            
            # First screen
            case 1:
                
                menu_screen.main_screen(screen,
                                        width,
                                        height,
                                        screen_number)
                
                
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
                
        pg.display.flip()


if __name__ == "__main__":
    main()
    pg.quit()