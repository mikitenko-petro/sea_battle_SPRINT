import pygame
from .main_screen_scene import main_screen_scene
from .game_screen_scene import game_screen_scene


class SceneManager():
    def __init__(self, screen, event):
        self.screen = screen
        self.event = event

        self.scene_list = [
        lambda: main_screen_scene(screen = screen, event = event),
        lambda: game_screen_scene(screen = screen, event = event)
        ]

    def show(self, scene_index):
        return self.scene_list[scene_index]()
