import pygame
from ..widgets.pygame_image import PygameImage
from ..widgets.text_input import TextInput

class ConectToServerScreenScene():
    def __init__(self, screen):
        self.screen = screen

    def run(self, event):
        background_image = PygameImage(
        screen = self.screen,
        path = "static/images/lighthouse_bg.png",
        coordinates = (0, 0),
        size = (1200, 700))

        text_input = TextInput(
        size = (128, 32),
        coordinates = (500, 500),
        event = event,
        screen = self.screen
        )

    
    
