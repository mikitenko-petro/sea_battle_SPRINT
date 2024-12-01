from .scenes.main_screen_scene import MainScreenScene
from .scenes.game_screen_scene import GameScreneScene
from .scenes.prepare_to_game_screen_scene import PrepareToGameScreenScene
from .scenes.conect_to_server_screen_scene import ConectToServerScreenScene

class SceneManager():
    def __init__(self, screen : object, pygame_storage : object, client : object):
        main_screen_scene = MainScreenScene(
        screen = screen,
        scene_manager = self)

        prepare_to_game_screen_scene = PrepareToGameScreenScene(
        screen = screen)

        game_screen_scene = GameScreneScene(
        screen = screen,
        scene_manager = self)

        conect_to_server_screen_scene = ConectToServerScreenScene(
        client = client,
        screen = screen,
        scene_manager = self,
        pygame_storage = pygame_storage)

        self.scene_list = {
        "main": main_screen_scene,
        "conect_to_server": conect_to_server_screen_scene,
        "prepare_to_game": prepare_to_game_screen_scene,
        "game": game_screen_scene}

        self.current_scene = "main"
        
    def change_scene(self, scene : str):
        self.current_scene = scene

    def show(self, event):
        return self.scene_list[self.current_scene].run(event = event)

    