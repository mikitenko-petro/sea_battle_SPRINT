import pygame
from .pygame_image import PygameImage

class GameScreneScene():
    def __init__(self, screen):
        background_image = PygameImage(screen, "static/images/sea_bg.png", (0, 0), (800, 600))