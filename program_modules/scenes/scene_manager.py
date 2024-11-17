import pygame
from .main_screen_scene import MainScreenScene
from .game_screen_scene import GameScreneScene


class SceneManager():
    def __init__(self, screen, *scenes):
        self.scene_list = []
        self.screen = screen
        for scene in scenes:
            self.scene_list.append(scene)

    def show(self, scene_index):
        return self.scene_list[scene_index(self.screen)]


scenes = SceneManager(MainScreenScene, GameScreneScene)