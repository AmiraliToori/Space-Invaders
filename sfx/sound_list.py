
import pygame as pg
from .sfx import Sound


SELECT_SOUND = "material/sounds/effects/SelectBtn.wav"
CLICK_SOUND = "material/sounds/effects/ClickBtn.wav"

class SoundList:
    
    
    def __init__(self) -> None:
        self.select_sound = Sound(SELECT_SOUND)
        self.click_sound = Sound(CLICK_SOUND)
        self.sounds_list = [self.select_sound, self.click_sound]
    
    def play_select_sound(self) -> None:
        self.select_sound.play_sound()
        
    def play_click_sound(self) -> None:
        self.click_sound.play_sound()
        
    def change_sound_volume(self,
                            value: float) -> None:
        for x_sound in self.sounds_list:
            x_sound.change_volume(value)

pg.mixer.init()
sounds = SoundList()
    