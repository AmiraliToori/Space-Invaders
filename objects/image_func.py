

import pygame as pg

def create_image(image_path: str,
                 scale: float = 1):
    
    image = pg.image.load(image_path)
    
    image_width = image.get_width()
    image_height = image.get_height()
    
    return pg.transform.scale(image, (image_width * scale, image_height * scale))