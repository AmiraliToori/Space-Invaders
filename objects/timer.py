

import pygame as pg

ENEMIES_MOVEMENT_ID = 1
ENEMIES_MOVEMENT_TIMING = 700

class Timer:
    
    def __init__(self,
                 id: int) -> None:
        self.timer_id = pg.USEREVENT + id
        
    def set_timer_event(self,
                        milliseconds: int,
                        loop: int = 0) -> None:
        pg.time.set_timer(self.timer_id, milliseconds, loop)
    
    def get_timer_id(self) -> int:
        return self.timer_id
    
enemies_move_timer = Timer(ENEMIES_MOVEMENT_ID)
enemies_move_timer.set_timer_event(ENEMIES_MOVEMENT_TIMING)
