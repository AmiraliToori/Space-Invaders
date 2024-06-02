

from objects.text import Text
from objects.button import Button
from objects.image import Image
from graphic import resolution_setting

# Font
FONT_PATH = "material/font/Pixelify_Sans/PixelifySans-VariableFont_wght.ttf"
DEFAULT_FONT_COLOR = "white"
BACKGROUND_COLOR = "black"

# Main Screen
TITLE_FONT_SIZE = 50

GREEN_HOVER = "green"
RED_HOVER = "red"


MYSTERY_IMG = "material/Icons/enemy/mystery/mystery-frame1.png"
ENEMY_TYPE_1_IMG = "material/Icons/enemy/enemy_type1/enemy-type1-frame1.png"
ENEMY_TYPE_2_IMG = "material/Icons/enemy/enemy_type2/enemy-type2-frame1.png"
ENEMY_TYPE_3_IMG = "material/Icons/enemy/enemy_type3/enemy-type3-frame1.png"


class IntroScreen:
    
    
    
    def __init__(self,
                 screen,
                 width: int,
                 height: int) -> None:
        
        self.screen = screen
        self.width = width
        self.height = height
        self.screen_number = 2
                
        self.score_advance_label = Text("*SCORE ADVANCE TABLE*",
                                        FONT_PATH,
                                        TITLE_FONT_SIZE,
                                        DEFAULT_FONT_COLOR,
                                        BACKGROUND_COLOR,
                                        width // 2,
                                        height * 4 // 48)

        ####################################################################
        
        self.mystery = Image(MYSTERY_IMG,
                             width * 8 // 48,
                             height * 8 // 48)
        
        self.mystery_label = Text("=   ?  MYSTERY",
                                  FONT_PATH,
                                  TITLE_FONT_SIZE,
                                  DEFAULT_FONT_COLOR,
                                  BACKGROUND_COLOR,
                                  width * 30 // 48,
                                  height * 10 // 48)
        
        #########################################################################3
        
        self.enemy_type_3 = Image(ENEMY_TYPE_3_IMG,
                                  width * 10 // 48,
                                  height * 13 // 48)
        
        self.enemy_type_3_label = Text("=    30   POINTS",
                                  FONT_PATH,
                                  TITLE_FONT_SIZE,
                                  DEFAULT_FONT_COLOR,
                                  BACKGROUND_COLOR,
                                  width * 30 // 48,
                                  height * 15 // 48)
        
        ###############################################################
        
        self.enemy_type_2 = Image(ENEMY_TYPE_2_IMG,
                                  width * 9 // 48,
                                  height * 18 // 48)
        
        self.enemy_type_2_label = Text("=    20   POINTS",
                                  FONT_PATH,
                                  TITLE_FONT_SIZE,
                                  DEFAULT_FONT_COLOR,
                                  BACKGROUND_COLOR,
                                  width * 30 // 48,
                                  height * 20 // 48)
        
        #################################################################
        
        self.enemy_type_1 = Image(ENEMY_TYPE_1_IMG,
                                  width * 9 // 48,
                                  height * 23 // 48)
        
        self.enemy_type_1_label = Text("=    10   POINTS",
                                  FONT_PATH,
                                  TITLE_FONT_SIZE,
                                  DEFAULT_FONT_COLOR,
                                  BACKGROUND_COLOR,
                                  width * 30 // 48,
                                  height * 25 // 48)
        
        #####################################################################
        
        self.play_button = Button("CLICK HERE TO PLAY!",
                                  DEFAULT_FONT_COLOR,
                                  width * 24 // 48,
                                  height * 32 // 48)
        
        #######################################################################
        
        self.back_button = Button("<<",
                                  DEFAULT_FONT_COLOR,
                                  25,
                                  25)
        
        
    def draw(self) -> None:
        
        self.screen.fill('black')
        
        self.score_advance_label.draw(self.screen)
        
        ########################################################
        
        self.mystery.draw_image(self.screen, 0.1)
        self.mystery_label.draw(self.screen)
        
        ##########################################################
        
        self.enemy_type_3.draw_image(self.screen, 0.1)
        self.enemy_type_3_label.draw(self.screen)
        
        ##########################################################
        
        self.enemy_type_2.draw_image(self.screen, 0.1)
        self.enemy_type_2_label.draw(self.screen)
        
        ##########################################################
        
        self.enemy_type_1.draw_image(self.screen, 0.1)
        self.enemy_type_1_label.draw(self.screen)
        
        ##############################################################
        
        play_button = self.play_button.draw(self.screen, GREEN_HOVER)
        
        ################################################################
        
        back_button = self.back_button.draw(self.screen, RED_HOVER)
        
        
        if play_button:
            self.screen_number = 6
        if back_button:
            self.screen_number = 1
    
    
    def update(self) -> int:
            temp = self.screen_number
            self.screen_number = 2
            return temp

game_intro = IntroScreen(resolution_setting.screen.display(),
                         resolution_setting.screen.get_width(),
                         resolution_setting.screen.get_width())









