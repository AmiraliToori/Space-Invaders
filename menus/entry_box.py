

import pygame_textinput
import pygame as pg

from graphic.resolution_setting import screen

from objects.tools.text import Text
from objects.tools.button import Button
from objects.tools.timer import enemies_move_timer
from objects.tools.temp import temp2

from icecream import ic

FONT_PATH = "material/font/Pixelify_Sans/PixelifySans-VariableFont_wght.ttf"

DEFAULT_FONT_COLOR = "white"
BACKGROUND_COLOR = "black"

FONT_OBJECT = pg.font.Font(FONT_PATH, 30)

# Setting Screen
SETTING_TITLE_FONT_SIZE = 40

GREEN_HOVER = "green"
RED_HOVER = "red"


class Entry:
    
    
    def __init__(self,
                 screen
                 ,width
                 ,height) -> None:
        
        self.screen = screen
        self.width = width
        self.height = height
        self.screen_number = 9
        
        self.surface = pg.Surface((self.width, self.height))
        
        self.text = Text("Enter interval time of enemy movement(ms):",
                         FONT_PATH,
                         30,
                         "white",
                         "black",
                         self.width // 2,
                         self.height // 2)
        
        
        self.textinput = pygame_textinput.TextInputVisualizer(font_object = FONT_OBJECT,
                                                              font_color = DEFAULT_FONT_COLOR,
                                                              antialias = True,
                                                              cursor_color = DEFAULT_FONT_COLOR)
        
        self.button = Button("<ENTER>",
                             30,
                             "green",
                             self.width // 2,
                             self.height * 40 // 60)
        
        
    def draw(self) -> None:
        
        self.screen.blit(self.surface, (0, 0))
        
        self.screen.blit(self.textinput.surface, (self.width * 22 // 50, self.height * 33 // 60))
        
        self.text.draw(self.screen)
        
        button_flag = self.button.draw(self.screen, GREEN_HOVER)
        
        if button_flag:
            temp = int(self.textinput.value)
            enemies_move_timer.change_timing_event(temp)
            
            self.textinput.value = ""
            self.screen_number = 10
    
    def update(self) -> int:
        temp = self.screen_number
        self.screen_number = 9
        return temp
    
entry_1 = Entry(screen.display(),
                screen.get_width(),
                screen.get_height())


class Entry2(Entry):
    
    def __init__(self,
                 screen,
                 width: int,
                 height: int) -> None:
        super().__init__(screen, width, height)

        self.screen_number = 10
        
        self.text = Text("Enter the minimum value possible for time interval:",
                         FONT_PATH,
                         30,
                         "white",
                         "black",
                         self.width // 2,
                         self.height // 2)
        
        self.button = Button("<ENTER>",
                             30,
                             "green",
                             self.width // 2,
                             self.height * 45 // 60)
        
    def draw(self) -> None:
        
        self.screen.blit(self.surface, (0, 0))
        
        self.screen.blit(self.textinput.surface, (self.width * 22 // 50, self.height * 33 // 60))
        
        self.text.draw(self.screen)
        
        button_flag = self.button.draw(self.screen, GREEN_HOVER)
        
        if button_flag:
            temp = int(self.textinput.value)
            temp2.change_value(temp)
            self.textinput.value = ""
            self.screen_number = 6
    
    def update(self) -> int:
        temp = self.screen_number
        self.screen_number = 10
        return temp
    
entry_2 = Entry2(screen.display(),
                screen.get_width(),
                screen.get_height())
        
        