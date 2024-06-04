

import pygame as pg

from objects.tools.text import Text
from objects.tools.button import Button

from graphic.resolution_setting import screen

FONT_PATH = "material/font/Pixelify_Sans/PixelifySans-VariableFont_wght.ttf"
DEFAULT_FONT_COLOR = "white"
BACKGROUND_COLOR = "black"


TITLE_FONT_SIZE = 40
CLOSE_BUTTON_FONT_SIZE = 40

GREEN_HOVER = "green"
RED_HOVER = "red"

class LeaderBoard:
    
    
    def __init__(self,
                 screen,
                 width: int,
                 height: int) -> None:
        
        self.screen = screen
        self.width = width
        self.height = height
        
        self.screen_number = 4
        
        self.surface = pg.Surface((self.screen.get_width(), self.screen.get_height()))
        
        self.leaderboard_title = Text("Leaderboard",
                                      FONT_PATH,
                                      TITLE_FONT_SIZE,
                                      DEFAULT_FONT_COLOR,
                                      BACKGROUND_COLOR,
                                      width // 2,
                                      height * 9 // 96)
        
        self.close_btn = Button("<<",
                                CLOSE_BUTTON_FONT_SIZE,
                                DEFAULT_FONT_COLOR,
                                width * 2 // 24,
                                height * 2 // 24)
        
    def draw(self) -> None:
        
        self.screen.blit(self.surface, (0, 0))
        
        pg.draw.rect(self.surface,
                     "#06ff06",
                     (self.width * 1 // 24, self.height * 1 // 24, self.width * 22 // 24, self.height * 22 // 24), 2)
        
        self.leaderboard_title.draw(self.surface)
        
        close_flag = self.close_btn.draw(self.surface, RED_HOVER)
        
        if close_flag:
            self.screen_number = 1
            
    def update(self) -> int:
        temp = self.screen_number
        self.screen_number = 4
        return temp
            
        
leaderboard_screen = LeaderBoard(screen.display(),
                                 screen.get_width(),
                                 screen.get_height())
        
        