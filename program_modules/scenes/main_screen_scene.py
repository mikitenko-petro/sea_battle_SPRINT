import pygame
from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_button import PygameButton

class MainScreenScene():
    def __init__(self, screen : object, event : object):
        background_image = PygameImage(
        screen = screen,
        path = "static/images/great_sea_battle_bg.png",
        coordinates = (0, 0),
        size = (1200, 700))

        start_button = PygameButton(
        screen = screen,
        path = "static/images/start_button.png",
        coordinates = (100, 100),
        size = (64*5, 16*5),
        event = event,
        function = lambda: print(2232),
        text = "Start",
        font_size = 40)