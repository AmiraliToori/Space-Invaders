

import pygame as pg

MAIN_FONT_PATH = "material/font/Pixelify_Sans/PixelifySans-VariableFont_wght.ttf"
FONT_SIZE = 40

HOVER_SOUND = "material/sounds/effects/SelectBtn.wav"
CLICK_SOUND = "material/sounds/effects/ClickBtn.wav"
MAX_TIME_PLAY_SOUND = 1

ANTI_ALIAS = True

class Button:
    
    def __init__(self,
                 text_input: str,
                 color: str,
                 x_pos: int,
                 y_pos: int) -> None:
        self.x = x_pos
        self.y = y_pos
        self.color = "white"
        self.text_input = text_input
        self.text = pg.font.Font(MAIN_FONT_PATH, FONT_SIZE)
        self.text_box = self.text.render(text_input,
                                     ANTI_ALIAS,
                                     color)
        self.rect = self.text_box.get_rect(center = (self.x, self.y))
        self.clicked = False
        self.hover_sound = pg.mixer.Sound(HOVER_SOUND)
        self.click_sound = pg.mixer.Sound(CLICK_SOUND)
        self.abravesh_flag = False
        self.just_one_time_play = True
    
        
    def draw(self, screen, color: str) -> bool:
        
        action = False
        pos = pg.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            
            self.abravesh_flag = True
            self.hover_sound.play(0, MAX_TIME_PLAY_SOUND)       
                
            
            self.text_box = self.text.render(self.text_input,ANTI_ALIAS, color)
            
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.click_sound.play()
                self.clicked = True
                self.abravesh_flag = True
                action = True
            
            if pg.mouse.get_pressed()[0] == 0:
                self.clicked = False
        
        else:
            self.abravesh_flag = True
            self.text_box = self.text.render(self.text_input,ANTI_ALIAS, self.color)
        
        screen.blit(self.text_box, self.rect)
        
        return action
        