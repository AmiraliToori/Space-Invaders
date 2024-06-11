

import pygame as pg

from objects.tools.text import Text
from objects.tools.button import Button, SettingButton

from graphic.resolution_setting import screen

from extra.database import read_score_table


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
        
        self.my_font = pg.sysfont.SysFont(FONT_PATH, 25)
        
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
        
        self.next_btn = SettingButton(">",
                             CLOSE_BUTTON_FONT_SIZE,
                             DEFAULT_FONT_COLOR,
                             width * 59 // 64,
                             height // 2)
        
        self.previous_btn = SettingButton("<",
                             CLOSE_BUTTON_FONT_SIZE,
                             DEFAULT_FONT_COLOR,
                             width * 5 // 64,
                             height // 2)
        
        self.scores_lst = read_score_table()
        
        
        
    def draw(self) -> None:
        
        self.screen.blit(self.surface, (0, 0))
        
        pg.draw.rect(self.surface,
                     "#06ff06",
                     (self.width * 1 // 24, self.height * 1 // 24, self.width * 22 // 24, self.height * 22 // 24), 2)
        
        self.leaderboard_title.draw(self.surface)
        
        close_flag = self.close_btn.draw(self.surface, RED_HOVER)
        
        if close_flag:
            self.screen_number = 1
        
        # self.next_btn.draw(self.surface, GREEN_HOVER, None)
        
        # self.previous_btn.draw(self.surface, GREEN_HOVER, None)
        
        
    def update(self) -> None:
        x_pos = 15
        y_pos = 10
        
        self.scores_lst = read_score_table()
        
        for tuple in self.scores_lst:
            text = self.my_font.render(f"{tuple[0]} : {tuple[1]}",
                                True,
                                DEFAULT_FONT_COLOR,
                                BACKGROUND_COLOR)
            self.surface.blit(text, (self.width * y_pos // 100, self.height * x_pos // 100))
            x_pos += 4
            if x_pos >= 90:
                x_pos = 15
                y_pos += 25
                            
    
    def update_btn(self) -> int:
        temp = self.screen_number
        self.screen_number = 4
        return temp
            
        
leaderboard_screen = LeaderBoard(screen.display(),
                                 screen.get_width(),
                                 screen.get_height())
        
        