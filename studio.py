

import pygame as pg

def play_music(file_name: str):
    # song = pg.mixer.music.load(file_name, "Main Screen Theme")
    # file_name.music.play()
    pass

def play_sound(file_name: str) -> None:
    sound = pg.mixer.Sound(file_name)
    sound.play()