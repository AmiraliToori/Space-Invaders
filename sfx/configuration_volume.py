
import pygame as pg
# from .sound_list import SoundList
from .sound_list import sounds


temp = [i / 10 for i in range(0, 11)]
VOLUMES_PRESETS = {i:p for i, p in enumerate(temp, 0)}

class ConfigurationVolume:
    
        
    def __init__(self) -> None:
        self.current_volume_music = 1
        self.current_volume_sound = 1
    
    def get_current_music_volume(self) -> float:
        return VOLUMES_PRESETS[self.current_volume_music]
    
    def get_current_sound_volume(self) -> float:
        return VOLUMES_PRESETS[self.current_volume_sound]
    
    ############################################################################################
    
    def volume_up_music(self) -> None:
        if self.current_volume_music < 10:
            self.current_volume_music += 1
            pg.mixer.music.set_volume(VOLUMES_PRESETS[self.current_volume_music])
            
    def volume_down_music(self) -> None:
        if self.current_volume_music > 0:
            self.current_volume_music -= 1
            pg.mixer.music.set_volume(VOLUMES_PRESETS[self.current_volume_music])
            
    ######################################################################################################3
            
    def volume_up_sound(self) -> None:
        if self.current_volume_sound < 10:
            self.current_volume_sound += 1
            sounds.change_sound_volume(VOLUMES_PRESETS[self.current_volume_sound])
            
    def volume_down_sound(self) -> None:
        if self.current_volume_sound > 0:
            self.current_volume_sound -= 1
            sounds.change_sound_volume(VOLUMES_PRESETS[self.current_volume_sound])