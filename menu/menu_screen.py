
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


class Main_screen:

    
    def __init__(self,
                 screen,
                 width: int,
                 height: int,
                 screen_number: int) -> None:
    
        self.screen = screen
        self.width = width
        self.height = height
        self.screen_number = screen_number
        self.title_screen = Text("SPACE INVADERS",
                                    FONT_PATH,
                                    TITLE_FONT_SIZE,
                                    DEFAULT_FONT_COLOR,
                                    BACKGROUND_COLOR,
                                    width // 2,
                                    height * 1 // 5)
        
        self.start_btn = Button("Start",
                                    DEFAULT_FONT_COLOR,
                                    width // 2,
                                    height * 4 // 12)
        
        self.setting_btn = Button("Setting",
                                    DEFAULT_FONT_COLOR,
                                    width // 2,
                                    height * 5 // 12)
        
        self.leaderboard_btn = Button("Leaderboard",
                                        DEFAULT_FONT_COLOR,
                                        width // 2,
                                        height * 6 // 12)
        
        self.exit_btn = Button("EXIT",
                                    DEFAULT_FONT_COLOR,
                                    width // 2,
                                    height * 9 // 12)