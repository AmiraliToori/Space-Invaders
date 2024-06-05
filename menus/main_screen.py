

import sys


sys.path.append('/home/glados/Documents/AmirAli Toori/Lessons/Python/Space-Invaders')

import pygame as pg
from objects.tools.button import Button
from objects.tools.text import Text
from graphic import resolution_setting

# Font
FONT_PATH = "material/font/Pixelify_Sans/PixelifySans-VariableFont_wght.ttf"
FONT_SIZE = 40
DEFAULT_FONT_COLOR = "white"
BACKGROUND_COLOR = "black"

# Main Screen
TITLE_FONT_SIZE = 50

GREEN_HOVER = "green"
RED_HOVER = "red"


class MainScreen:

    def __init__(self,
                 screen,
                 width: int,
                 height: int) -> None:
    
        self.screen = screen
        self.width = width
        self.height = height
        self.screen_number = 1
        
        self.title_screen = Text("SPACE INVADERS",
                                    FONT_PATH,
                                    TITLE_FONT_SIZE,
                                    DEFAULT_FONT_COLOR,
                                    BACKGROUND_COLOR,
                                    width // 2,
                                    height * 1 // 5)
        
        self.start_btn = Button("Start",
                                FONT_SIZE,
                                    DEFAULT_FONT_COLOR,
                                    width // 2,
                                    height * 4 // 12)
        
        self.setting_btn = Button("Setting",
                                  FONT_SIZE,
                                    DEFAULT_FONT_COLOR,
                                    width // 2,
                                    height * 5 // 12)
        
        self.leaderboard_btn = Button("Leaderboard",
                                      FONT_SIZE,
                                        DEFAULT_FONT_COLOR,
                                        width // 2,
                                        height * 6 // 12)
        
        
        self.exit_btn = Button("EXIT",
                               FONT_SIZE,
                                    DEFAULT_FONT_COLOR,
                                    width // 2,
                                    height * 9 // 12)
        
        
    def draw(self) -> None:
        
        self.screen.fill('black')
        
        self.title_screen.draw(self.screen)
        
        start_flag = self.start_btn.draw(self.screen, GREEN_HOVER)
        
        setting_flag = self.setting_btn.draw(self.screen, GREEN_HOVER)
            
        leaderboard_flag = self.leaderboard_btn.draw(self.screen, GREEN_HOVER)
    
        exit_flag = self.exit_btn.draw(self.screen, RED_HOVER)
        
        
        if start_flag:
            self.screen_number = 2
        if setting_flag:
            self.screen_number = 3
        if leaderboard_flag:
            self.screen_number = 4
        if exit_flag:
            self.screen_number = 5
        
        
    def update(self) -> int:
        temp = self.screen_number
        self.screen_number = 1
        return temp
        
pg.init()
main = MainScreen(resolution_setting.screen.display(),
                         resolution_setting.screen.get_width(),
                         resolution_setting.screen.get_height())