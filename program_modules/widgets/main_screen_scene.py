import pygame
from .pygame_image import PygameImage
from .pygame_button import PygameButton

class MainScreenScene():
    def __init__(self, screen, event):
        background_image = PygameImage(screen, "static/images/great_sea_battle_bg.png", (0, 0), (800, 600))
        start_button = PygameButton(screen, "static/images/start_button.png", (100, 100), (64*5, 16*7), event, lambda: print(2232), "Start")