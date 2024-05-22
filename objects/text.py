

import pygame as pg


class Text:
    
    
    def __init__(self,
                 text_input: str,
                 font_name: str,
                 font_size: int,
                 color: str,
                 background_color: str,
                 x_pos: int,
                 y_pos: int) -> None:
        
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.text_input = text_input
        self.font_name = font_name
        self.font_size = font_size
        self.ANTI_ALIAS = True
        self.color = color
        self.background_color = background_color
        
        self.font = pg.font.Font(self.font_name, self.font_size)
        self.text = self.font.render(self.text_input,
                                     self.ANTI_ALIAS,
                                     color,
                                     background_color)
        
        self.text_box = self.text.get_rect(center = (x_pos, y_pos))

    
    def draw(self, screen):
        screen.blit(self.text, self.text_box)