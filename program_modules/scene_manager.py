from .scenes.main_screen_scene import MainScreenScene
from .scenes.game_screen_scene import GameScreneScene
from .scenes.prepare_to_game_screen_scene import PrepareToGameScreenScene
from .scenes.conect_to_server_screen_scene import ConectToServerScreenScene
from .scenes.end_screen_scene import EndScreenScene

#Робим клас для перемикання між сценами
class SceneManager():
    def __init__(self, screen : object, client : object):
        main_screen_scene = MainScreenScene(
            screen = screen,
            scene_manager = self
        )

        #Створюємо змінну до якої присвоюємо клас сцени підготовки гри
        prepare_to_game_screen_scene = PrepareToGameScreenScene(
            client = client,
            screen = screen,
            scene_manager = self
        )

        #Створюємо змінну до якої присвоюємо клас сцени основної гри
        game_screen_scene = GameScreneScene(
            screen = screen,
            scene_manager = self,
            client = client
        )

        #Створюємо змінну до якої присвоюємо клас сцени підключення до сервера
        conect_to_server_screen_scene = ConectToServerScreenScene(
            client = client,
            screen = screen,
            scene_manager = self
        )
        
        end_screen_scene = EndScreenScene(
            screen = screen,
            client = client,
            scene_manager = self
        )

        #Створюємо список де вказуємо наші змінні
        self.scene_list = {
            "main": main_screen_scene,
            "conect_to_server": conect_to_server_screen_scene,
            "prepare_to_game": prepare_to_game_screen_scene,
            "game": game_screen_scene,
            "end": end_screen_scene
        }

        #Задається початкова сцена
        self.current_scene = "main"
    
    #Робимо метод зміни сцени        
    def change_scene(self, scene : str):
        self.current_scene = scene

    #Робимо функцію для показу сцени
    def show(self, event):
        return self.scene_list[self.current_scene].run(event = event)

    