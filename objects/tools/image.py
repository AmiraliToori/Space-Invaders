
import pygame as pg


class Image:
    
    def __init__(self, file_name, x_pos, y_pos) -> None:
        
        self.file_name = file_name
        
        self.x_pos = x_pos
        self.y_pos = y_pos
        
        
    def draw_image(self,
                   screen,
                   scale: float = 1) -> None:
        
        self.image = pg.image.load(self.file_name).convert_alpha()
        image_width = self.image.get_width()
        image_height = self.image.get_height()
        
        self.image = pg.transform.scale(self.image, (int(image_width * scale), int(image_height * scale)))
        
        screen.blit(self.image, (self.x_pos, self.y_pos))
        
        