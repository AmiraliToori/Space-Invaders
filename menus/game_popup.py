
import pygame as pg

from graphic.resolution_setting import screen

from objects.tools.text import Text
from objects.tools.button import Button
from objects.tools.pause import pause

from objects.player import player

# Font
FONT_PATH = "material/font/Pixelify_Sans/PixelifySans-VariableFont_wght.ttf"
FONT_SIZE = 30
DEFAULT_FONT_COLOR = "white"
BACKGROUND_COLOR = "black"

# Main Screen
TITLE_FONT_SIZE = 50

GREEN_HOVER = "green"
RED_HOVER = "red"

class PauseSurface:
    
    
    def __init__(self,
                 screen,
                 width,
                 height) -> None:
        
        self.screen = screen
        self.width = width
        self.height = height
        self.screen_number = 6
        
        self.surface = pg.Surface((self.screen.get_width(), self.screen.get_height()), pg.SRCALPHA)
        
        
        
        self.pause_label = Text("The Game is Paused, Press ESC button to unpause.",
                                FONT_PATH,
                                FONT_SIZE,
                                DEFAULT_FONT_COLOR,
                                BACKGROUND_COLOR,
                                width // 2,
                                height * 1 // 2
                                )

        self.exit_button = Button("<EXIT>",
                                FONT_SIZE,
                                DEFAULT_FONT_COLOR,
                                width // 2,
                                height * 14 // 24)
        
    def draw(self) -> None:
        
        self.screen.blit(self.surface, (0, 0))
        
        self.black_rect = pg.draw.rect(self.surface,
                                       '#06ff06',
                                       (30, self.height // 2 - 20, self.width - 58, self.height * 8 // 48), 2)
        
        self.pause_label.draw(self.surface)
        
        exit_flag = self.exit_button.draw(self.surface, RED_HOVER)
        
        if exit_flag:
            self.screen_number = 5
            pause.pause_state = False
    
    
    def update(self) -> int:
        temp = self.screen_number
        self.screen_number = 6
        return temp
        

pause_popup = PauseSurface(screen.display(),
                           screen.get_width(),
                           screen.get_height())


####################################################################################################################

class GameOverSurface(PauseSurface):
    
    
    def __init__(self,
                 screen,
                 width: int,
                 height: int) -> None:
        super().__init__(screen, width, height)
        
        
        self.label = Text("GAME-OVER",
                                FONT_PATH,
                                FONT_SIZE,
                                DEFAULT_FONT_COLOR,
                                BACKGROUND_COLOR,
                                width // 2,
                                height * 21 // 48
                                )

        self.details = Text(f"{player.name}       SCORE: {player.score}",
                            FONT_PATH,
                            FONT_SIZE,
                            "#06ff06",
                            BACKGROUND_COLOR,
                            width // 2,
                            height * 27 // 48)
        
        self.exit_button = Button("<EXIT>",
                                FONT_SIZE,
                                DEFAULT_FONT_COLOR,
                                width // 2,
                                height * 31 // 48)
        
        
    
    def draw(self) -> None:
        
        self.screen.blit(self.surface, (0, 0))
        
        self.black_rect = pg.draw.rect(self.surface,
                                       '#06ff06',
                                       (30, self.height // 2 - 20, self.width - 58, self.height * 11 // 48), 2)
        self.label.draw(self.surface)
        exit_flag = self.exit_button.draw(self.surface, RED_HOVER)
        
        self.details.draw(self.surface)
        self.details.update(f"{player.name}       SCORE: {player.score}")
        
        if exit_flag:
            self.screen_number = 5
            pause.pause_state = False
      
gameover_popup = GameOverSurface(screen.display(),
                                 screen.get_width(),
                                 screen.get_height())
      
##########################################################################################################  
      
      
class VictorySurface(GameOverSurface):
    
    
    def __init__(self,
                 screen,
                 width: int,
                 height: int) -> None:
        super().__init__(screen, width, height)
        
        
        self.label = Text("VICTORY",
                                FONT_PATH,
                                FONT_SIZE,
                                DEFAULT_FONT_COLOR,
                                BACKGROUND_COLOR,
                                width // 2,
                                height * 24 // 48
                                )
        
            
victory_popup = VictorySurface(screen.display(),
                               screen.get_width(),
                               screen.get_height())
