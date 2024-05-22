
import sys

# sys.path.insert(0,"./objects")

# from objects import button, text



sys.path.append('/home/glados/Documents/AmirAli Toori/Lessons/Python/Space-Invaders')


from objects.button import Button
from objects.text import Text

# Font
FONT_PATH = "material/font/Pixelify_Sans/PixelifySans-VariableFont_wght.ttf"
DEFAULT_FONT_COLOR = "white"
BACKGROUND_COLOR = "black"

# Main Screen
TITLE_FONT_SIZE = 50

GREEN_HOVER = "green"
RED_HOVER = "red"


def main_screen(screen,
                width: int,
                height: int, 
                screen_number: int) -> int:
    
    Title_screen = Text("SPACE INVADERS",
                                FONT_PATH,
                                TITLE_FONT_SIZE,
                                DEFAULT_FONT_COLOR,
                                BACKGROUND_COLOR,
                                width // 2,
                                height * 1 // 5)
        
    start_btn = Button("Start",
                                DEFAULT_FONT_COLOR,
                                width // 2,
                                height * 4 // 12)

    setting_btn = Button("Setting",
                                DEFAULT_FONT_COLOR,
                                width // 2,
                                height * 5 // 12)

    leaderboard_btn = Button("Leaderboard",
                                    DEFAULT_FONT_COLOR,
                                    width // 2,
                                    height * 6 // 12)

    exit_btn = Button("EXIT",
                                DEFAULT_FONT_COLOR,
                                width // 2,
                                height * 9 // 12)
    
    
    
    screen.fill(BACKGROUND_COLOR)
    Title_screen.draw(screen)
    
    if start_btn.draw(screen, GREEN_HOVER):
        screen_number = 2
    
    if setting_btn.draw(screen, GREEN_HOVER):
        screen_number = 3
        
    if leaderboard_btn.draw(screen, GREEN_HOVER):
        screen_number = 4
    
    if exit_btn.draw(screen, RED_HOVER):
        screen_number = 5
        
    return screen_number