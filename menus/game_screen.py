
from graphic.resolution_setting import screen
from objects.player import players


class GameScreen:
    
    
    def __init__(self,
                 screen,
                 width: int,
                 height: int) -> None:
        
        self.screen = screen
        self.width = width
        self.height = height
    
    
    def draw(self):
        self.screen.fill('black')
        players.update()
        players.draw(self.screen)
        
game = GameScreen(screen.display(),
                  screen.get_width(),
                  screen.get_height())
        
    