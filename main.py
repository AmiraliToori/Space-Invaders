import pyxel

from model.player import Player

class App:
    
    def __init__(self):
        pyxel.init(160, 120,title = "Space Invaders!")
        pyxel.load("design/player.pyxres")
        
        self.player = Player()
        
        pyxel.run(self.update, self.draw)
        
        
    def update(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player.move_right()
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.player.move_left()
            
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        
    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.player.x,
                  self.player.y,
                  self.player.IMG,
                  self.player.U,
                  self.player.V,
                  self.player.WIDTH,
                  self.player.HEIGHT
                  )
        
App()