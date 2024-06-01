
from graphic.resolution_setting import screen

from objects.player import player_group
from objects.bullet import player_bullet

class GameScreen:
    
    
    def __init__(self,
                 screen,
                 width: int,
                 height: int) -> None:
        
        self.screen = screen
        self.width = width
        self.height = height
    
    
    def draw(self) -> None:
        self.screen.fill('black')
        
        player_group.update()
        player_group.draw(self.screen)
        
        player_bullet.update()
        player_bullet.draw(self.screen)
        
game = GameScreen(screen.display(),
                  screen.get_width(),
                  screen.get_height())
        
    