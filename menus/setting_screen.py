
import sys
from icecream import ic

sys.path.append('/home/glados/Documents/AmirAli Toori/Lessons/Python/Space-Invaders')


from objects.button import SettingButton
from objects.text import Text
from sfx import sfx


# Font
FONT_PATH = "material/font/Pixelify_Sans/PixelifySans-VariableFont_wght.ttf"
DEFAULT_FONT_COLOR = "white"
BACKGROUND_COLOR = "black"

# Setting Screen
SETTING_TITLE_FONT_SIZE = 50

GREEN_HOVER = "green"
RED_HOVER = "red"

MUSIC_BUTTON_OFFSET = 70



music_adjuster = sfx.ConfigurationMusic()

class SettingScreen:
    
    
    def __init__(self,
                 screen,
                 width: int,
                 height: int,
                 screen_number: int) -> None:
        
        self.screen = screen
        self.width = width
        self.height = height
        self.screen_number = screen_number
        
        
        self.setting_title = Text("Settings",
                                    FONT_PATH,
                                    SETTING_TITLE_FONT_SIZE,
                                    DEFAULT_FONT_COLOR,
                                    BACKGROUND_COLOR,
                                    width // 2,
                                    height * 1 // 5)
        
        
        self.change_music_volume = Text("Music Volume:",
                                    FONT_PATH,
                                    SETTING_TITLE_FONT_SIZE,
                                    DEFAULT_FONT_COLOR,
                                    BACKGROUND_COLOR,
                                    width * 1 // 4,
                                    height * 2 // 5)
        
        self.current_volume = Text(f"{music_adjuster.get_current_volume()}",
                                    FONT_PATH,
                                    SETTING_TITLE_FONT_SIZE,
                                    DEFAULT_FONT_COLOR,
                                    BACKGROUND_COLOR,
                                    width * 3 // 4,
                                    height * 2 // 5)
        
        
        
        self.volume_up = SettingButton(f">",
                                    DEFAULT_FONT_COLOR,
                                    width * 3 // 4 + MUSIC_BUTTON_OFFSET,
                                    height * 2 // 5)
        
        self.volume_down = SettingButton(f"<",
                                    DEFAULT_FONT_COLOR,
                                    width * 3 // 4 - MUSIC_BUTTON_OFFSET,
                                    height * 2 // 5)
        
    def draw(self) -> None:
        
        self.screen.fill('black')
        
        self.setting_title.draw(self.screen)
        
        self.change_music_volume.draw(self.screen)
        
        self.current_volume.draw(self.screen)
        
        self.volume_up.draw(self.screen, GREEN_HOVER, music_adjuster.volume_up)
        
        self.volume_down.draw(self.screen, GREEN_HOVER, music_adjuster.volume_down)
            