import pygame
from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_text_input import PygameTextInput

class ConectToServerScreenScene():
    def __init__(self, screen, scene_manager, pygame_storage):
        self.screen = screen
        self.pygame_storage = pygame_storage

    def run(self, event):
        background_image = PygameImage(
        screen = self.screen,
        path = "static/images/lighthouse_bg.png",
        coordinates = (0, 0),
        size = (1200, 700))

        text_input = PygameTextInput(
        size = (384, 96),
        coordinates = (600, 400),
        event = event,
        screen = self.screen,
        pygame_storage = self.pygame_storage)
    
    
