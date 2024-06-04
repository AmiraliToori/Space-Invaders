

import pygame as pg

def create_image(image_path: str,
                 scale: float = 1):
    
    image = pg.image.load(image_path)
    
    image_width = image.get_width()
    image_height = image.get_height()
    
    return pg.transform.smoothscale(image, (int(image_width * scale), int(image_height * scale))).convert_alpha()