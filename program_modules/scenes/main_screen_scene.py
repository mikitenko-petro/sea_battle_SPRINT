import pygame
from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_button import PygameButton

class MainScreenScene():
    def __init__(self, screen : object, scene_manager : object):
        self.screen = screen
        self.scene_manager = scene_manager

    def run(self, event : object):
        background_image = PygameImage(
        screen = self.screen,
        path = "static/images/great_sea_battle_bg.png",
        coordinates = (0, 0),
        size = (1200, 700))

        start_button = PygameButton(
        screen = self.screen,
        path = "static/images/start_button.png",
        coordinates = (100, 100),
        size = (64*5, 16*5),
        event = event,
        function = lambda: self.change_scene(),
        text = "Start",
        font_size = 40)

    def change_scene(self):
        self.scene_manager.change_scene(scene = "game")