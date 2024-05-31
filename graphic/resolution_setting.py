
from icecream import ic

import pygame as pg

DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 600


RESOLUTIONS_OPTIONS = [(800, 600), (1280, 720), (1600, 900), (1920, 1080)]
RESOLUTIONS_PRESETS = {number:option for number, option in enumerate(RESOLUTIONS_OPTIONS, 1)}

class Resolution:
    
    def __init__(self) -> None:
        
        self.width = DEFAULT_WIDTH
        self.height = DEFAULT_HEIGHT
        self.current_preset = 1
        self.is_change = False
        
        
        pg.display.set_caption("Space Invaders")
        pg.display.set_icon(pg.image.load("material/Icons/window_icon.png"))
    
    def display(self):
        return pg.display.set_mode((self.width, self.height))
    
    def update(self):
        if self.is_change:
            self.is_change = False
            return pg.display.set_mode((self.width, self.height))
            
    def increase_resolution(self):
        if self.current_preset < 4:
            self.current_preset += 1
            self.width, self.height = RESOLUTIONS_PRESETS[self.current_preset]
            self.is_change = True
            
    def decrease_resolution(self):
        if self.current_preset > 1:
            self.current_preset -= 1
            self.width, self.height = RESOLUTIONS_PRESETS[self.current_preset]
            self.is_change = True
            
    def get_width(self) -> int:
        return self.width
    
    def get_height(self) -> int:
        return self.height
            
            
screen = Resolution()