class Player:
    IMG = 0
    U = 0
    V = 0 
    WIDTH = 8
    HEIGHT = 8
    DX = 2
    
    
    def __init__(self):
        self.x = 70
        self.y = 100
        self.lives = 3
        
    def move_left(self):
        self.x -= self.DX
        
    def move_right(self):
        self.x += self.DX
   
    def health(self):
        self.lives = self.lives
        
   
    
    