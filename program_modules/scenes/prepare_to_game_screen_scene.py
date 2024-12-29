from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_button import PygameButton
from ..game_modules.grid import Grid
from ..game_modules.ship_manager import ShipManager
from ..tools.pygame_storage import pygame_storage

from ..game_widgets.random_placement_button import RandomPlacementButton

#Робим клас для підготовки гри
class PrepareToGameScreenScene():
    def __init__(self, screen : object, scene_manager : object):
        self.screen = screen
        self.scene_manager = scene_manager
        pygame_storage.add_variable({"check_placement" : False})

    #Робим метод для створення єкрану для підготовки гри
    def run(self, event : object):
        #Робим фон
        background_image = PygameImage(
            screen = self.screen,
            path = "static/images/sea_bg.png",
            coordinates = (0, 0),
            size = (1200, 700)
        )

        pygame_storage.storage_dict["PLAYER_GRID"].show_grid(self.screen, event)

        ship_manager = ShipManager(
            event = event,
            screen = self.screen,
            scene_manager = self.scene_manager
        )
        
        ship_manager.show_label(coordinates = (50, 150))
        
        pygame_storage.storage_dict["PLAYER_GRID"].place_ship()
        
        check_placement = True

        placed_ships = 0

        for ship in pygame_storage.storage_dict["ship_list"]:
            if ship.status == "placed":
                placed_ships += 1
        
        if placed_ships == len(pygame_storage.storage_dict["ship_list"]) and not pygame_storage.storage_dict["check_placement"]:
            check_placement = True
        else:
            check_placement = False

        if check_placement == True:
            move_to_scene = PygameButton(
                screen = self.screen,
                path = "static/images/blue_button.png",
                text = "start game",
                font_size = 40,
                coordinates = (472, 10),
                size = (128*2, 32*2),
                event = event,
                function = self.move_to_scene
            )
            
        random_button = RandomPlacementButton(
            event = event, 
            screen = self.screen
        )
    
    def move_to_scene(self):
        pygame_storage.add_variable({"ENEMY_GRID" : None})

        pygame_storage.storage_dict["ENEMY_GRID"] = Grid(
            coordinates = (650, 150),
            type = "enemy",
            scene_manager = self.scene_manager
        )
        
        self.scene_manager.change_scene(scene = "game")