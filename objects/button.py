

import pygame as pg
from sfx import sound_list

MAIN_FONT_PATH = "material/font/Pixelify_Sans/PixelifySans-VariableFont_wght.ttf"
FONT_SIZE = 40
ANTI_ALIAS = True

class Button:
    
    def __init__(self,
                 text_input: str,
                 color: str,
                 x_pos: int,
                 y_pos: int) -> None:
        
        self.x_pos = x_pos
        self.y_pos = y_pos
        
        self.color = "white"
        
        self.text_input = text_input
        
        self.text = pg.font.Font(MAIN_FONT_PATH, FONT_SIZE)
        self.text_box = self.text.render(text_input,
                                     ANTI_ALIAS,
                                     color)
        self.rect = self.text_box.get_rect(center = (self.x_pos, self.y_pos))
        self.clicked = False
        self.play_one_time = False
        
    def draw(self, screen, hover_color) -> bool:
        target = False
        
        
        pos = pg.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            
            self.text_box = self.text.render(self.text_input, ANTI_ALIAS, hover_color)
            
            if self.play_one_time == False:
                sound_list.SoundList().play_select_sound()
                self.play_one_time = True
            
            
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                sound_list.SoundList().play_click_sound()
                self.clicked = True
                target = True
                
            elif pg.mouse.get_pressed()[0] == 0:
                self.clicked = False
                
        else:
            self.text_box = self.text.render(self.text_input, ANTI_ALIAS, self.color)
            self.play_one_time = False
            
        screen.blit(self.text_box, self.rect)
        
        return target
        