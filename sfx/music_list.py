
from .sfx import Music


MAIN_TITLE_THEME = "material/sounds/musics/main_menu_theme.mp3"

class MusicList:
    
    def __init__(self) -> None:
        self.main_title_theme = Music(MAIN_TITLE_THEME)
        
    def play_main_title(self) -> None:
        self.main_title_theme.play_music()