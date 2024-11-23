import pygame
from .main_screen_scene import MainScreenScene
from .game_screen_scene import GameScreneScene
from .prepare_to_game_screen_scene import PrepareToGameScreenScene
from .conect_to_server_screen_scene import ConectToServerScreenScene

class SceneManager():
    def __init__(self, screen : object):
        main_screen_scene = MainScreenScene(screen = screen, scene_manager = self)
        prepare_to_game_screen_scene = PrepareToGameScreenScene(screen=screen)
        game_screen_scene = GameScreneScene(screen = screen, scene_manager = self)
        conect_to_server_screen_scene = ConectToServerScreenScene(screen=screen)

        self.scene_list = {"main": main_screen_scene, "conect_to_server": conect_to_server_screen_scene, "prepare_to_game": prepare_to_game_screen_scene,  "game": game_screen_scene}

        self.current_scene = "main"
        
    def change_scene(self, scene):
        self.current_scene = scene

    def show(self, event):
        return self.scene_list[self.current_scene].run(event = event)

    