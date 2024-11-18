import pygame
from .main_screen_scene import MainScreenScene
from .game_screen_scene import GameScreneScene

class SceneManager():
    def __init__(self, screen : object):
        main_screen_scene = MainScreenScene(screen = screen, scene_manager = self)
        game_screen_scene = GameScreneScene(screen = screen, scene_manager = self)

        self.scene_list = {"main": main_screen_scene, "game": game_screen_scene}

        self.current_scene = "main"
        
    def change_scene(self, scene):
        self.current_scene = scene

    def show(self, event):
        return self.scene_list[self.current_scene].run(event = event)
