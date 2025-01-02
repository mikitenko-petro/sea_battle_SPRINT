from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_button import PygameButton
from ..game_modules.battle.grid import Grid
from ..game_modules.battle.ship_manager import ShipManager
from ..tools.pygame_storage import pygame_storage
from ..game_widgets.random_placement_button import RandomPlacementButton

#Робим клас для підготовки гри
class PrepareToGameScreenScene():
    def __init__(self):
        pygame_storage.add_variable({"check_placement" : False})
        pygame_storage.add_variable({"PLAYER_GRID" : None})
        pygame_storage.add_variable({"ship_list" : None})
        pygame_storage.add_variable({"collision_list" : None})

    #Робим метод для створення єкрану для підготовки гри
    def run(self, event : object):
        #Робим фон
        background_image = PygameImage(
            path = "static/images/sea_bg.png",
            coordinates = (0, 0),
            size = (1200, 700)
        )

        decoration_image = PygameImage(
            path = "static/images/decoration1.png",
            coordinates = (0, 250),
            size = (512, 512)
        )

        pygame_storage.storage_dict["PLAYER_GRID"].show_grid(event = event)

        ship_manager = ShipManager(
            event = event,
        )
        
        ship_manager.show_label(coordinates = (0, 0))
        
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
            coordinates = (10, 620),
            size = (128*1.5, 32*1.5)
        )
    
    def move_to_scene(self):
        pygame_storage.storage_dict["ENEMY_GRID"] = Grid(
            coordinates = (650, 180),
            type = "enemy",
        )

        pygame_storage.add_variable({"player_turn" : None})

        if pygame_storage.storage_dict["number_client"] == "1":
            pygame_storage.storage_dict["player_turn"] = True
        else:
            pygame_storage.storage_dict["player_turn"] = False
        
        pygame_storage.storage_dict["SceneManager"].change_scene(scene = "game")