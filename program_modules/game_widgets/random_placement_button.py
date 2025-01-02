import random
import threading
import time
from ..tools.pygame_storage import pygame_storage
from ..game_modules.battle.check_random_ship_collision import check_random_ship_collision
from ..widgets.pygame_button import PygameButton

class RandomPlacementButton():
    def __init__(self, coordinates, size, event):
        self.thread_auto_place_ships = threading.Thread(target = self.auto_place_ships)

        button = PygameButton(
            coordinates = coordinates, 
            size = size, 
            event = event, 
            function = lambda : self.thread_auto_place_ships.start(), 
            path = "static/images/hollow_label.png",
            text = "AUTO",
            font_size = 40,
        )
        
    def auto_place_ships(self):
        self.placed_ships = 0

        for ship in pygame_storage.storage_dict["ship_list"]:
            if ship.status == "placed":
                ship.status = "unplaced"

        while self.placed_ships < len(pygame_storage.storage_dict["ship_list"]):
            time.sleep(0.1)
            for ship in pygame_storage.storage_dict["ship_list"][::-1]:
                if ship.status == "unplaced":
                    direction = random.choice(["top", "bottom", "left", "right"])
                    row = random.randint(0, 9)
                    column = random.randint(0, 9)

                    if not check_random_ship_collision(
                        direction = direction,  
                        row = row, 
                        column = column,
                        type = ship.type,
                        id = ship.id):
                        
                        ship.direction = direction
                        ship.row = row
                        ship.column = column
                        ship.change_direction()
                        ship.status = "placed"
                        self.placed_ships += 1

                    break