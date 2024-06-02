
import pygame as pg
from .sfx import Sound


SELECT_SOUND = "material/sounds/effects/SelectBtn.wav"
CLICK_SOUND = "material/sounds/effects/ClickBtn.wav"
SHOOT_SOUND = "material/sounds/effects/Shoot.wav"
INVADER_KILLED_SOUND = "material/sounds/effects/InvaderKilled.wav"

class SoundList:
    
    
    def __init__(self) -> None:
        self.select_sound = Sound(SELECT_SOUND)
        self.click_sound = Sound(CLICK_SOUND)
        self.shoot_sound = Sound(SHOOT_SOUND)
        self.invader_killed_sound = Sound(INVADER_KILLED_SOUND)
        
        self.sounds_list = [self.select_sound, self.click_sound, self.shoot_sound, self.invader_killed_sound]
    
    def play_select_sound(self) -> None:
        self.select_sound.play_sound()
        
    def play_click_sound(self) -> None:
        self.click_sound.play_sound()
        
    def play_shoot_sound(self) -> None:
        self.shoot_sound.play_sound()
        
    def play_invader_killed(self) -> None:
        self.invader_killed_sound.play_sound()
        
    def change_sound_volume(self,
                            value: float) -> None:
        for x_sound in self.sounds_list:
            x_sound.change_volume(value)

pg.mixer.init()
sounds = SoundList()
    