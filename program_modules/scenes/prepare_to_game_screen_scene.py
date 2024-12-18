from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_button import PygameButton
from ..game_modules.grid.grid import Grid
from ..game_modules.ship import Ship
from ..game_modules.ship_manager import ShipManager
from ..pygame_storage import pygame_storage
from ..game_modules.game_widgets.collision import Collision

#Робим клас для підготовки гри
class PrepareToGameScreenScene():
    def __init__(self, screen : object, scene_manager : object, client : object):
        self.screen = screen
        self.scene_manager = scene_manager
        pygame_storage.add_variable({"ship_list" : []})
        pygame_storage.add_variable({"PLAYER_GRID" : Grid(coordinates = (350, 150), type = "player", scene_manager = scene_manager)})
        pygame_storage.add_variable({"check_placement" : False})

        for i in range(10):
            if i < 4:
                pygame_storage.storage_dict["ship_list"].append(Ship(type = "1x1", id = i, client = client))
            elif i < 7:
                pygame_storage.storage_dict["ship_list"].append(Ship(type = "2x1", id = i, client = client))
            elif i < 9:
                pygame_storage.storage_dict["ship_list"].append(Ship(type = "3x1", id = i, client = client))
            else:
                pygame_storage.storage_dict["ship_list"].append(Ship(type = "4x1", id = i, client = client))

    #Робим метод для створення єкрану для підготовки гри
    def run(self, event : object):
        #Робим фон
        background_image = PygameImage(
        screen = self.screen,
        path = "static/images/sea_bg.png",
        coordinates = (0, 0),
        size = (1200, 700))

        pygame_storage.storage_dict["PLAYER_GRID"].show_grid(self.screen, event)

        collision_list = [
            Collision(self.screen, (350, 100), (500, 50), "buffer"),
            Collision(self.screen, (850, 150), (50, 500), "buffer"),
            Collision(self.screen, (350, 650), (500, 50), "buffer"),
            Collision(self.screen, (300, 150), (50, 500), "buffer")
        ]

        pygame_storage.add_variable({"collision_list" : collision_list})

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
                coordinates = (472, 50),
                size = (128*2, 32*2),
                event = event,
                function = lambda: self.scene_manager.change_scene(scene = "game")
            )
        