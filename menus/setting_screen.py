
import sys
from icecream import ic

sys.path.append('/home/glados/Documents/AmirAli Toori/Lessons/Python/Space-Invaders')


from objects.tools.button import SettingButton, Button
from objects.tools.text import Text

from objects.user import user_list

from sfx import configuration_volume

from graphic import resolution_setting

# Font
FONT_PATH = "material/font/Pixelify_Sans/PixelifySans-VariableFont_wght.ttf"
FONT_SIZE = 40
DEFAULT_FONT_COLOR = "white"
BACKGROUND_COLOR = "black"

# Setting Screen
SETTING_TITLE_FONT_SIZE = 40

GREEN_HOVER = "green"
RED_HOVER = "red"

VOLUME_BUTTON_OFFSET = 70
USER_BUTTON_OFFSET = 140


volume_adjuster = configuration_volume.ConfigurationVolume()

class SettingScreen:
    
    
    def __init__(self,
                 screen,
                 width: int,
                 height: int) -> None:
        
        self.screen = screen
        self.width = width
        self.height = height
        self.screen_number = 3
        
        
        self.setting_title = Text("Settings",
                                    FONT_PATH,
                                    SETTING_TITLE_FONT_SIZE,
                                    DEFAULT_FONT_COLOR,
                                    BACKGROUND_COLOR,
                                    width // 2,
                                    height * 2 // 12)
        
        #########################################################################################
        
        self.music_volume_label = Text("Music Volume:",
                                    FONT_PATH,
                                    SETTING_TITLE_FONT_SIZE,
                                    DEFAULT_FONT_COLOR,
                                    BACKGROUND_COLOR,
                                    width * 1 // 4,
                                    height * 8 // 12)
        
        
        self.current_music_volume = Text(f"{volume_adjuster.get_current_music_volume()}",
                                    FONT_PATH,
                                    SETTING_TITLE_FONT_SIZE,
                                    DEFAULT_FONT_COLOR,
                                    BACKGROUND_COLOR,
                                    width * 3 // 4,
                                    height * 8 // 12)
        
        self.volume_up_music = SettingButton(f">",
                                             FONT_SIZE,
                                    DEFAULT_FONT_COLOR,
                                    width * 3 // 4 + VOLUME_BUTTON_OFFSET,
                                    height * 8 // 12)
        
        self.volume_down_music = SettingButton(f"<",
                                               FONT_SIZE,
                                    DEFAULT_FONT_COLOR,
                                    width * 3 // 4 - VOLUME_BUTTON_OFFSET,
                                    height * 8 // 12)
        #############################################################################################################
        
        self.sound_volume_label = Text("Sound Volume:",
                                    FONT_PATH,
                                    SETTING_TITLE_FONT_SIZE,
                                    DEFAULT_FONT_COLOR,
                                    BACKGROUND_COLOR,
                                    width * 1 // 4,
                                    height * 10 // 12)
        
        self.current_sound_volume = Text(f"{volume_adjuster.get_current_sound_volume()}",
                                    FONT_PATH,
                                    SETTING_TITLE_FONT_SIZE,
                                    DEFAULT_FONT_COLOR,
                                    BACKGROUND_COLOR,
                                    width * 3 // 4,
                                    height * 10 // 12)
        
        
        self.volume_up_sound = SettingButton(f">",
                                             FONT_SIZE,
                                    DEFAULT_FONT_COLOR,
                                    width * 3 // 4 + VOLUME_BUTTON_OFFSET,
                                    height * 10 // 12)
        
        self.volume_down_sound = SettingButton(f"<",
                                               FONT_SIZE,
                                    DEFAULT_FONT_COLOR,
                                    width * 3 // 4 - VOLUME_BUTTON_OFFSET,
                                    height * 10 // 12)
        
        #################################################################################################3
        
        self.user_preset_label = Text("Current User:",
                                    FONT_PATH,
                                    SETTING_TITLE_FONT_SIZE,
                                    DEFAULT_FONT_COLOR,
                                    BACKGROUND_COLOR,
                                    width * 1 // 4,
                                    height * 4 // 12)
        
        self.user_preset = Text(f"{user_list.get_current_value()}",
                                    FONT_PATH,
                                    SETTING_TITLE_FONT_SIZE,
                                    DEFAULT_FONT_COLOR,
                                    BACKGROUND_COLOR,
                                    width * 3 // 4,
                                    height * 4 // 12)
        
        
        self.next_user = SettingButton(f">",
                                                 40,
                                    DEFAULT_FONT_COLOR,
                                    width * 3 // 4 + USER_BUTTON_OFFSET,
                                    height * 4 // 12)
        
        self.prev_user = SettingButton(f"<",
                                                 40,
                                    DEFAULT_FONT_COLOR,
                                    width * 3 // 4 - USER_BUTTON_OFFSET,
                                    height * 4 // 12)
        
        ############################################################################################
        
        self.user_menu_btn = Button(f"<USERS>",
                                      FONT_SIZE,
                                      DEFAULT_FONT_COLOR,
                                      width // 2,
                                      height * 6 // 12)
        
        
        #############################################################################################
        
        
        self.back_button = Button(f"<<",
                                  FONT_SIZE,
                                DEFAULT_FONT_COLOR,
                                25,
                                25)
        
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
        
        ##########################################################################################################################
        
        self.user_preset_label.draw(self.screen)
        
        self.user_preset.draw(self.screen)
        self.user_preset.update(f"{user_list.get_current_value()}")
        
        self.next_user.draw(self.screen, GREEN_HOVER, user_list.next_user)
        self.prev_user.draw(self.screen, GREEN_HOVER, user_list.perv_user)
        
        ################################################################################################################################
        
        back_button_flag = self.back_button.draw(self.screen, RED_HOVER)
        
        if back_button_flag:
            self.screen_number = 1
            
        ##########################################################################################################################
        
        user_menu_flag = self.user_menu_btn.draw(self.screen, GREEN_HOVER)
        
        if user_menu_flag:
            self.screen_number = 7
    
    def update(self) -> int:
        temp = self.screen_number
        self.screen_number = 3
        return temp
        
        
        
setting = SettingScreen(resolution_setting.screen.display(),
                        resolution_setting.screen.get_width(),
                        resolution_setting.screen.get_height())