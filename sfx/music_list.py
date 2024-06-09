
import pygame as pg

from .sfx import Music


MAIN_TITLE_THEME = "material/sounds/musics/main_theme.mp3"
COMBAT_THEME = "material/sounds/musics/combat_theme.mp3"

class Musics:
    
    def __init__(self) -> None:
        self.main_title = MAIN_TITLE_THEME
        self.music = Music(MAIN_TITLE_THEME)
        
    def play_music(self) -> None:
        self.music.play_music(-1)
    
    def stop_music(self) -> None:
        self.music.stop_music()
    
    def get_busy(self) -> bool:
        return self.music.get_busy()
    
    def load_music(self, value) -> None:
        self.unload_music()
        self.music = Music(value)
    
    def reset_music(self) -> None:
        self.unload_music()
        self.music = Music(self.main_title)
    
    @staticmethod
    def unload_music() -> None:
        pg.mixer.music.unload()
        
        
    

musics = Musics()


# class CombatTheme(MainTheme):
    
#     def __init__(self) -> None:
        
#         super().__init__()
#         self.music = Music(COMBAT_THEME)
        
# combat_theme = CombatTheme()