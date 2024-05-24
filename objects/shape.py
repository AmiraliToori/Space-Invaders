


class Shape:
    
    def __init__(self, file_name, x_pos, y_pos) -> None:
        
        self.file_name = file_name
        self.x_pos = x_pos
        self.y_pos = y_pos
        
        
    def draw(self, screen):
        screen.draw(self.file_name, (self.x_pos, self.y_pos))
        
        