


import pygame as pg



class CustomTimer:
    
    def __init__(self,
                 duration: int) -> None:
        
        self.start_time = 0
        self.duration = duration
        self.active = False
        
    
    def activate(self) -> None:
        if self.active == False:
            self.active = True
            self.start_time = pg.time.get_ticks()
        
    def deactivate(self) -> None:
        self.active = False
        self.start_time = 0
    
    def update(self) -> None:
        if self.active:
            current_time = pg.time.get_ticks()
            if current_time - self.start_time >= self.duration:
                self.deactivate()

ENEMY_DEATH_DURATION = 300

enemy_death_frame_timer = CustomTimer(ENEMY_DEATH_DURATION)