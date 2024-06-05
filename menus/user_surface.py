

import pygame as pg

from graphic.resolution_setting import screen

from objects.tools.button import SettingButton, Button
from objects.tools.text import Text

from objects.user import user_list

# Font
FONT_PATH = "material/font/Pixelify_Sans/PixelifySans-VariableFont_wght.ttf"
FONT_SIZE = 40
DEFAULT_FONT_COLOR = "white"
BACKGROUND_COLOR = "black"

# Setting Screen
SETTING_TITLE_FONT_SIZE = 40

GREEN_HOVER = "green"
RED_HOVER = "red"

class UserSetting:
    
    
    def __init__(self,
                 screen,
                 width: int,
                 height: int) -> None:
        
        self.screen = screen
        self.width = width
        self.height = height
        self.screen_number = 7
        
        
        self.surface = pg.Surface((self.width, self.height))
        
        self.title = Text("Users Settings",
                          FONT_PATH,
                          FONT_SIZE,
                          DEFAULT_FONT_COLOR,
                          BACKGROUND_COLOR,
                          width * 1 // 2,
                          height * 1 // 12)
        
        self.insert_user_btn = SettingButton("INSERT USER",
                                      30,
                                      DEFAULT_FONT_COLOR,
                                      width * 2 // 12,
                                      height * 16 // 24
                                      )
        
        self.delete_user_btn = SettingButton("DELETE USER",
                                         30,
                                         DEFAULT_FONT_COLOR,
                                         width * 6 // 12,
                                         height * 16 // 24)
        
        self.change_name_btn = SettingButton("CHANGE NAME",
                                             30,
                                             DEFAULT_FONT_COLOR,
                                             width * 10 // 12,
                                             height * 16 // 24 
                                             )
        
        self.back_btn = Button("<<",
                               FONT_SIZE,
                               DEFAULT_FONT_COLOR,
                               30,
                               30)
        
    def draw(self) -> None:
        
        self.screen.blit(self.surface, (0, 0))
        
        pg.draw.rect(self.surface, "#06ff06", (self.width * 2 // 60, self.height * 1 // 3, self.width * 56 // 60, self.height * 4 // 10)  ,2)
        
        self.title.draw(self.surface)
        
        self.insert_user_btn.draw(self.surface, GREEN_HOVER, user_list.insert_user)
        
        self.delete_user_btn.draw(self.surface, RED_HOVER, user_list.delete_user)
        
        self.change_name_btn.draw(self.surface, 'blue', user_list.change_user_name)

        back_btn_flag = self.back_btn.draw(self.surface, RED_HOVER)

        if back_btn_flag:
            self.screen_number = 3
    
    
    def update(self) -> int:
        temp = self.screen_number
        self.screen_number = 7
        return temp

user_setting = UserSetting(screen.display(),
                           screen.get_width(),
                           screen.get_height())





