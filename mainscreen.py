import pyxel
import main

class App():
    
    
    def __init__(self) -> None:
        pyxel.init(128, 100, title = "Space Invaders!")
        # pyxel.images[0].load(0, 0,"assets/design.pyxres")
        pyxel.run(self.update, self.draw)
        
    def update(self) -> None:
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_S):
            pyxel.quit()
            main()
        
    def draw(self) -> None:
        pyxel.cls(0)
        pyxel.text(38, 30, "Space Invaders", pyxel.frame_count % 16)
        pyxel.text(1, 95, "2024", 2)
        pyxel.text(52, 50, "(S)TART", 7)
        pyxel.text(53, 60, "(Q)UIT", 8)
        # pyxel.blt(61, 66, 0, 0, 0, 38, 16)
        
App()