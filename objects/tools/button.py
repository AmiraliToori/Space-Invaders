

import pygame as pg
from sfx import sound_list



MAIN_FONT_PATH = "material/font/Pixelify_Sans/PixelifySans-VariableFont_wght.ttf"
ANTI_ALIAS = True

class Button:
    
    def __init__(self,
                 text_input: str,
                 font_size: int,
                 color: str,
                 x_pos: int,
                 y_pos: int) -> None:
        
        self.x_pos = x_pos
        self.y_pos = y_pos
        
        self.color = color
        self.font_size = font_size
        self.text_input = text_input
        
        self.text = pg.font.Font(MAIN_FONT_PATH, self.font_size)
        self.text_box = self.text.render(text_input,
                                     ANTI_ALIAS,
                                     color)
        self.rect = self.text_box.get_rect(center = (self.x_pos, self.y_pos))
        self.clicked = False
        self.play_one_time = False
        
    def draw(self,
             screen,
             hover_color: str,) -> bool:
        target = False
        
        
        pos = pg.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            
            self.text_box = self.text.render(self.text_input, ANTI_ALIAS, hover_color)
            
            if self.play_one_time == False:
                sound_list.sounds.play_select_sound()
                self.play_one_time = True
            
            
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                sound_list.sounds.play_click_sound()
                self.clicked = True
                target = True
                
            elif pg.mouse.get_pressed()[0] == 0:
                self.clicked = False
                
        else:
            self.text_box = self.text.render(self.text_input, ANTI_ALIAS, self.color)
            self.play_one_time = False
            
        screen.blit(self.text_box, self.rect)
        
        return target
    


class SettingButton(Button):
    
    def __init__(self,
                 text_input: str,
                 font_size: int,
                 color: str,
                 x_pos: int,
                 y_pos: int) -> None:
        super().__init__(text_input, font_size,color, x_pos, y_pos)
        
    def draw(self, screen, hover_color, command) -> None:
        
        pos = pg.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            
            self.text_box = self.text.render(self.text_input, ANTI_ALIAS, hover_color)
            
            if self.play_one_time == False:
                
                sound_list.sounds.play_select_sound()
                self.play_one_time = True
            
            
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                command()
                sound_list.sounds.play_click_sound()
                self.clicked = True
                
                
            elif pg.mouse.get_pressed()[0] == 0:
                self.clicked = False
                
        else:
            self.text_box = self.text.render(self.text_input, ANTI_ALIAS, self.color)
            self.play_one_time = False
            
        screen.blit(self.text_box, self.rect)

        
        
        
            
        