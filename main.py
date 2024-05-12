import pyxel
from model.player import Player

TITLE_TEXT = "Space Invaders"
YEAR_TEXT = "2024"
START_TEXT = "(S)TART"
QUIT_TEXT = "(Q)UIT"
SCREEN_WIDTH = 128
SCREEN_HEIGHT = 100
COLOR_BACKGROUND = 0

class Mainscreen:
    
    def __init__(self) -> None:
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title = TITLE_TEXT)
        pyxel.run(self.update, self.draw)
        
        
    def update(self) -> None:
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_S):
            Game()
    
    def draw(self) -> None:
        pyxel.cls(COLOR_BACKGROUND)
        pyxel.text(38, 30, TITLE_TEXT, pyxel.frame_count % 16)
        pyxel.text(1, 95, YEAR_TEXT, 2)
        pyxel.text(52, 50, START_TEXT, 7)
        pyxel.text(53, 60, QUIT_TEXT, 8)
        
        
class Game:
    
    def __init__(self) -> None:
        pyxel.load("assets/design.pyxres")
        
        self.player = Player()
        
        pyxel.run(self.update, self.draw)
        
    def update(self) -> None:
        
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
            
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player.move_right()
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.player.move_left()
            
        elif pyxel.btnp(pyxel.KEY_SPACE):
            self.player.shoot()
        
         
    def draw(self) -> None:
        pyxel.cls(0)
        
        pyxel.blt(self.player.x,
                  self.player.y,
                  self.player.PLAYER_IMG, 
                  self.player.U,
                  self.player.V,
                  self.player.PLAYER_WIDTH, 
                  self.player.PLAYER_HEIGHT)
        
    
Mainscreen()