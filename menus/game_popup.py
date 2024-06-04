
import pygame as pg

from graphic.resolution_setting import screen
from objects.tools.text import Text
from objects.tools.button import Button
from objects.tools.pause import pause

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
        
        self.surface = pg.Surface((screen.get_width(), screen.get_height()), pg.SRCALPHA)
        
        
        
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
                                "black",
                                width // 2,
                                height * 14 // 24)
        
    def draw(self) -> None:
        
        self.screen.blit(self.surface, (0, 0))
        
        self.black_rect = pg.draw.rect(self.surface,
                                       '#06ff06',
                                       (30, self.height // 2 - 20, self.width - 58, self.height * 8 // 48))
        
        self.pause_label.draw(self.surface)
        
        exit_flag = self.exit_button.draw(self.surface, RED_HOVER)
        
        if exit_flag:
            self.screen_number = 5
            pause.pause_state = False
    
    
    def update(self) -> int:
        temp = self.screen_number
        self.screen_number = 6
        return temp
        

pause_screen = PauseSurface(screen.display(),
                           screen.get_width(),
                           screen.get_height())


####################################################################################################################

# class GameOverSurface(PauseSurface):
    
    
#     def __init__(self,
#                  screen,
#                  width: int,
#                  height: int) -> None:
#         super().__init__(screen, width, height)
        
        
#         self.game_over_label = Text("GAME-OVER",
#                                 FONT_PATH,
#                                 FONT_SIZE,
#                                 DEFAULT_FONT_COLOR,
#                                 BACKGROUND_COLOR,
#                                 width // 2,
#                                 height * 1 // 2
#                                 )

#         self.exit_button = Button("<EXIT>",
#                                 FONT_SIZE,
#                                 "black",
#                                 width // 2,
#                                 height * 14 // 24)
        
    
#     def draw(self) -> None:
        
#         self.screen.blit(self.surface, (0, 0))
        
#         self.black_rect = pg.draw.rect(self.surface,
#                                        '#06ff06',
#                                        (30, self.height // 2 - 20, self.width - 58, self.height * 8 // 48))
#         self.game_over_label.draw(self.surface)
#         exit_flag = self.exit_button.draw(self.surface, RED_HOVER)
        
#         if exit_flag:
#             self.screen_number = 5
#             pause.pause_state = False
#         self.screen.blit(self.surface, (0, 0))
        
#         self.black_rect = pg.draw.rect(self.surface,
#                                        '#06ff06',
#                                        (30, self.height // 2 - 20, self.width - 58, self.height * 8 // 48))
#         self.game_over_label.draw(self.surface)
#         exit_flag = self.exit_button.draw(self.surface, RED_HOVER)
        
#         if exit_flag:
#             self.screen_number = 5
#             pause.pause_state = False
      
      
      
##########################################################################################################  
      
      
            
# class VictorySurface(PauseSurface):
    
    
#     def __init__(self,
#                  screen,
#                  width: int,
#                  height: int) -> None:
#         super().__init__(screen, width, height)
        
        
#         self.victory_label = Text("GAME-OVER",
#                                 FONT_PATH,
#                                 FONT_SIZE,
#                                 DEFAULT_FONT_COLOR,
#                                 BACKGROUND_COLOR,
#                                 width // 2,
#                                 height * 1 // 2
#                                 )

#         self.exit_button = Button("<EXIT>",
#                                 FONT_SIZE,
#                                 "black",
#                                 width // 2,
#                                 height * 14 // 24)
        
    
#     def draw(self) -> None:
        
#         self.screen.blit(self.surface, (0, 0))
        
#         self.black_rect = pg.draw.rect(self.surface,
#                                        '#06ff06',
#                                        (30, self.height // 2 - 20, self.width - 58, self.height * 8 // 48))
#         self.victory_label.draw(self.surface)
#         exit_flag = self.exit_button.draw(self.surface, RED_HOVER)
        
#         if exit_flag:
#             self.screen_number = 5
#             pause.pause_state = False
