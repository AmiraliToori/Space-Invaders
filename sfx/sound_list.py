

from .sfx import Sound


SELECT_SOUND = "material/sounds/effects/SelectBtn.wav"
CLICK_SOUND = "material/sounds/effects/ClickBtn.wav"

class SoundList:
    
    
    def __init__(self) -> None:
        
        self.select_sound = Sound(SELECT_SOUND)
        self.click_sound = Sound(CLICK_SOUND)
    
    
    def play_select_sound(self) -> None:
        self.select_sound.play_sound()
        
    def play_click_sound(self) -> None:
        self.click_sound.play_sound()
    