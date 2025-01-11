from ..scenes.main_screen_scene import MainScreenScene
from ..scenes.game_screen_scene import GameScreneScene
from ..scenes.prepare_to_game_screen_scene import PrepareToGameScreenScene
from ..scenes.conect_to_server_screen_scene import ConectToServerScreenScene
from ..scenes.end_screen_scene import EndScreenScene
from ..scenes.achievement_screen_scene import AchievementScreenScene

#Робим клас для перемикання між сценами
class SceneManager():
    def __init__(self):
        self.scene_list = {
            "main": MainScreenScene(),
            "prepare_to_game": PrepareToGameScreenScene(),
            "game": GameScreneScene(),
            "conect_to_server": ConectToServerScreenScene(),
            "end": EndScreenScene(),
            "achievement": AchievementScreenScene()
        }

        #Задається початкова сцена
        self.current_scene = "main"
    
    #Робимо метод зміни сцени        
    def change_scene(self, scene : str):
        self.current_scene = scene

    #Робимо функцію для показу сцени
    def show(self, event):
        return self.scene_list[self.current_scene].run(event = event)

    