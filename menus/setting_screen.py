
import sys
from icecream import ic

sys.path.append('/home/glados/Documents/AmirAli Toori/Lessons/Python/Space-Invaders')


from objects.button import SettingButton
from objects.text import Text
from sfx import configuration_volume


# Font
FONT_PATH = "material/font/Pixelify_Sans/PixelifySans-VariableFont_wght.ttf"
DEFAULT_FONT_COLOR = "white"
BACKGROUND_COLOR = "black"

# Setting Screen
SETTING_TITLE_FONT_SIZE = 50

GREEN_HOVER = "green"
RED_HOVER = "red"

MUSIC_BUTTON_OFFSET = 70



volume_adjuster = configuration_volume.ConfigurationVolume()

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
        
        #########################################################################################
        
        self.music_volume_label = Text("Music Volume:",
                                    FONT_PATH,
                                    SETTING_TITLE_FONT_SIZE,
                                    DEFAULT_FONT_COLOR,
                                    BACKGROUND_COLOR,
                                    width * 1 // 4,
                                    height * 2 // 5)
        
        
        self.current_music_volume = Text(f"{volume_adjuster.get_current_music_volume()}",
                                    FONT_PATH,
                                    SETTING_TITLE_FONT_SIZE,
                                    DEFAULT_FONT_COLOR,
                                    BACKGROUND_COLOR,
                                    width * 3 // 4,
                                    height * 2 // 5)
        
        self.volume_up_music = SettingButton(f">",
                                    DEFAULT_FONT_COLOR,
                                    width * 3 // 4 + MUSIC_BUTTON_OFFSET,
                                    height * 2 // 5)
        
        self.volume_down_music = SettingButton(f"<",
                                    DEFAULT_FONT_COLOR,
                                    width * 3 // 4 - MUSIC_BUTTON_OFFSET,
                                    height * 2 // 5)
        #############################################################################################################
        
        self.sound_volume_label = Text("Sound Volume:",
                                    FONT_PATH,
                                    SETTING_TITLE_FONT_SIZE,
                                    DEFAULT_FONT_COLOR,
                                    BACKGROUND_COLOR,
                                    width * 1 // 4,
                                    height * 3 // 5)
        
        self.current_sound_volume = Text(f"{volume_adjuster.get_current_sound_volume()}",
                                    FONT_PATH,
                                    SETTING_TITLE_FONT_SIZE,
                                    DEFAULT_FONT_COLOR,
                                    BACKGROUND_COLOR,
                                    width * 3 // 4,
                                    height * 3 // 5)
        
        
        self.volume_up_sound = SettingButton(f">",
                                    DEFAULT_FONT_COLOR,
                                    width * 3 // 4 + MUSIC_BUTTON_OFFSET,
                                    height * 3 // 5)
        
        self.volume_down_sound = SettingButton(f"<",
                                    DEFAULT_FONT_COLOR,
                                    width * 3 // 4 - MUSIC_BUTTON_OFFSET,
                                    height * 3 // 5)
        
        
        
    def draw(self) -> None:
        
        self.screen.fill('black')
        
        self.setting_title.draw(self.screen)
        
        self.music_volume_label.draw(self.screen)
        
        self.current_music_volume.draw(self.screen)
        self.current_music_volume.update(f"{volume_adjuster.get_current_music_volume()}")
        
        self.volume_up_music.draw(self.screen, GREEN_HOVER, volume_adjuster.volume_up_music)
        self.volume_down_music.draw(self.screen, GREEN_HOVER, volume_adjuster.volume_down_music)
        
        ######################################################################################################################
        
        self.sound_volume_label.draw(self.screen)
        
        self.current_sound_volume.draw(self.screen)
        self.current_sound_volume.update(f"{volume_adjuster.get_current_sound_volume()}")
        
        self.volume_up_sound.draw(self.screen, GREEN_HOVER, volume_adjuster.volume_up_sound)
        self.volume_down_sound.draw(self.screen, GREEN_HOVER, volume_adjuster.volume_down_sound)
        