import pygame
from ..widgets.pygame_image import PygameImage

class GameScreneScene():
    def __init__(self, screen):
        background_image = PygameImage(
        screen = screen,
        path = "static/images/sea_bg.png",
        coordinates = (0, 0),
        size = (1200, 700))