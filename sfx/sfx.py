

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

    def change_volume(self,
                value: float) -> None:
        self.sound.set_volume(value)
        
    

class Music:
    
    def __init__(self,
                 file_name: str) -> None:
        
        self.file_name = file_name
        self.music = pg.mixer.music.load(self.file_name)
        
    
    def play_music(self,
                   loops: int = 0,
                   max_time: int = 0,
                   fade_out: int = 0) -> None:
        
        pg.mixer.music.play(loops, max_time, fade_out)
    
    
    def get_busy(self) -> bool:
        return pg.mixer.music.get_busy()
        
    def stop_music(self) -> None:
        pg.mixer.music.stop()
        
        







            
        
    
