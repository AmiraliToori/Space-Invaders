

import pygame as pg




DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600

WINDOW_ICON_PATH = "material/Icons/desktop-icons8-space-invaders-48.png"
WINDOW_ICON_IMG = pg.image.load(WINDOW_ICON_PATH)

BACKGROUND_COLOR = 'black'


def set_screen_display():
    return pg.display.set_mode([DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT])


def set_desktop_icon() -> None:
    pg.display.set_icon(WINDOW_ICON_IMG)
    
def fill_screen(screen, color: str) -> None:
    screen.fill(color)

def draw_box(screen,
             color: str,
             height: int,
             width: int,
             line_width: int) -> None:
    
    pg.draw.line(screen, color, (0, 0), (width, 0), line_width)
    
    pg.draw.line(screen, color, (0, 0), (0, height), line_width)
    
    pg.draw.line(screen, color, (0, height), (width, height), line_width)

    pg.draw.line(screen, color, (0, width), (width, height), line_width)