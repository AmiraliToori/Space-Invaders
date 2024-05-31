

from objects.text import Text
from objects.button import Button
from objects.shape import Shape 
from graphic import resolution_setting

# Font
FONT_PATH = "material/font/Pixelify_Sans/PixelifySans-VariableFont_wght.ttf"
DEFAULT_FONT_COLOR = "white"
BACKGROUND_COLOR = "black"

# Main Screen
TITLE_FONT_SIZE = 50

GREEN_HOVER = "green"
RED_HOVER = "red"

class IntroScreen:
    
    
    
    def __init__(self) -> None:
        
        self.score_advance_label = Text("*SCORE ADVANCE TABLE*",
                                        FONT_PATH,
                                        TITLE_FONT_SIZE,
                                        DEFAULT_FONT_COLOR,
                                        BACKGROUND_COLOR,
                                        resolution_setting.screen.get_width(),
                                        resolution_setting.screen.get_height())
    
    
    
    
    def draw(self) -> None:
        self.score_advance_label.draw(resolution_setting.screen)











