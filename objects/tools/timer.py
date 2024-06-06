

import pygame as pg

ENEMIES_MOVEMENT_ID = 1
ENEMIES_MOVEMENT_TIMING = 700

ENEMIES_SPAWN_ID = 2
ENEMIES_SPAWN_TIMING = 15000

class Timer:
    
    def __init__(self,
                 id: int,
                 timing: int) -> None:
        self.timer_id = pg.USEREVENT + id
        self.timing = timing
        
    def set_timer_event(self,
                        loop: int = 0) -> None:
        pg.time.set_timer(self.timer_id, self.timing, loop)
    
    def change_timing_event(self,
                            new_time: int,
                            loop = 0) -> None:
        self.timing = new_time
        pg.time.set_timer(self.timer_id, new_time, loop)
    
    
    def get_timer_id(self) -> int:
        return self.timer_id
    
    
    
enemies_move_timer = Timer(ENEMIES_MOVEMENT_ID, ENEMIES_MOVEMENT_TIMING)
enemies_move_timer.set_timer_event(ENEMIES_MOVEMENT_TIMING)

enemies_spawn_timer = Timer(ENEMIES_SPAWN_ID, ENEMIES_SPAWN_TIMING)
enemies_spawn_timer.set_timer_event(ENEMIES_SPAWN_TIMING)


