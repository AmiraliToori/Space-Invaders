

import pygame as pg
from icecream import ic


class Sound:
    
    def __init__(self,
                 file_name: str) -> None:
        
        self.file_name = file_name
        self.sound = pg.mixer.Sound(self.file_name)
        
    def play_sound(self,
                   loops: int = 0,
                   max_time: int = 0,
                   fade_out: int = 0) -> None:
        
        self.sound.play(loops, max_time, fade_out)
        
        
    def stop_sound(self) -> None:
        self.sound.stop()




class Music:
    
    def __init__(self,
                 file_name: str) -> None:
        
        self.file_name = file_name
        self.music = pg.mixer.music.load(self.file_name)
        
    
    def play_music(self,
                   loops: int = 0,
                   max_time: int = 0,
                   fade_out: int = 0):
        
        pg.mixer.music.play(loops, max_time, fade_out)
        
    def stop_music(self):
        pg.mixer.music.stop()
        
        
def mapping_volume():
    pass


temp = [i / 10 for i in range(0, 11)]
VOLUMES_PRESETS = {i:p for i, p in enumerate(temp, 0)}

ic(VOLUMES_PRESETS)
class ConfigurationMusic:
    
    
    
    def __init__(self) -> None:
        self.current_volume = 8
    
    
    def get_current_volume(self) -> float:
        ic(VOLUMES_PRESETS[self.current_volume])
        return VOLUMES_PRESETS[self.current_volume]
    
    def volume_up(self) -> None:
        
        if self.current_volume < 10:
            self.current_volume += 1
            
            # ic(VOLUMES_PRESETS[self.current_volume])
            
            pg.mixer.music.set_volume(VOLUMES_PRESETS[self.current_volume])
            
        
            
            
    def volume_down(self) -> None:
        if self.current_volume > 0:
            
            self.current_volume -= 1
            
            # ic(VOLUMES_PRESETS[self.current_volume])
            
            pg.mixer.music.set_volume(VOLUMES_PRESETS[self.current_volume])
            
        
    
