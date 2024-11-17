import pygame
from ..widgets.pygame_image import PygameImage

class GameScreneScene():
    def __init__(self, screen, event):
        background_image = PygameImage(
        screen = screen,
        path = "static/images/sea_bg.png",
        coordinates = (0, 0),
        size = (1200, 700))

def game_screen_scene(screen, event):
    scene = GameScreneScene(screen = screen, event = event)