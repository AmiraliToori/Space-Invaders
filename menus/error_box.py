

import pygame as pg

from objects.tools.text import Text
from objects.tools.button import Button

from graphic.resolution_setting import screen

FONT_PATH = "material/font/Pixelify_Sans/PixelifySans-VariableFont_wght.ttf"

RED_HOVER = "red"

FONT_SIZE = 30

class ErrorBox:
    
    
    def __init__(self,
                 screen,
                 width: int,
                 height: int) -> None:
        
        self.screen = screen
        self.width = width
        self.height = height
        self.screen_number = 8
        
        self.surface = pg.Surface((self.width, self.height))
        
        self.error = Text("The entered user name is currently in the database.",
                          FONT_PATH,
                          FONT_SIZE,
                          "white",
                          "black",
                          self.width // 2,
                          self.height // 2)
        
        
        self.button = Button("<OK>",
                             FONT_SIZE,
                             "white",
                             self.width // 2,
                             self.height * 55 // 100)
        
    def draw(self) -> None:
        
        self.screen.blit(self.surface, (0, 0))
        
        self.error.draw(self.screen)
        
        ok_btn_flag = self.button.draw(self.screen, RED_HOVER)
        
        if ok_btn_flag:
            self.screen_number = 7
            
    def update(self) -> int:
        temp = self.screen_number
        self.screen_number = 8
        return temp
        
        
repeated_entry = ErrorBox(screen.display(),
                          screen.get_width(),
                          screen.get_height())




        
        