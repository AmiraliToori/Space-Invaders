

class Pause:
    
    
    def __init__(self) -> None:
        self.pause_state = False
        
    def change_pause_state(self) -> None:
        self.pause_state = not(self.pause_state)
        

pause = Pause()

