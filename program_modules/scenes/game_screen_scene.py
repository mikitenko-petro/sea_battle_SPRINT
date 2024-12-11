from ..widgets.pygame_image import PygameImage
from ..game_modules.grid.grid import Grid
from ..pygame_storage import pygame_storage
from ..game_modules.ship_manager import ShipManager
from ..game_modules.main_game_manager import MainGameManager

#Робим клас для ігрвого вікна
class GameScreneScene():
    #Робим метод ініт для задання пареммрів та модулів
    def __init__(self, screen : object, scene_manager : object, client : object):
        self.screen = screen
        self.scene_manager = scene_manager
        pygame_storage.add_variable(
            {"ENEMY_GRID" : Grid(
                    coordinates = (650, 150),
                    type = "enemy",
                    scene_manager = scene_manager
                )
            }
        )
         
    #Робим метод для створення екрану гри
    def run(self, event : object):
        pygame_storage.storage_dict["collision_list"] = []

        pygame_storage.add_variable(
            {"MainGameManager" : MainGameManager(client = self.scene_manager)}
        )
        pygame_storage.storage_dict["MainGameManager"].shoot("123")
        #Робим фон
        background_image = PygameImage(
        screen = self.screen,
        path = "static/images/sea_bg.png",
        coordinates = (0, 0),
        size = (1200, 700))

        pygame_storage.storage_dict["PLAYER_GRID"].show_grid(self.screen, event)
        pygame_storage.storage_dict["PLAYER_GRID"].x = 50
        pygame_storage.storage_dict["PLAYER_GRID"].y = 150

        pygame_storage.storage_dict["ENEMY_GRID"].show_grid(self.screen, event)

        ship_manager = ShipManager(
            event = event,
            screen = self.screen,
            scene_manager = self.scene_manager
        )
        