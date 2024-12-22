import pygame
import random
from ..pygame_storage import pygame_storage
from ..widgets.pygame_button import PygameButton

class RandomPlacementButton():
    def __init__(self, event, screen, grid):
        button = PygameButton(
            coordinates = (0, 0), 
            size = (50, 50), 
            event = event, 
            function = lambda : self.auto_place_ships(grid), 
            path = "static/images/turn_button.png", 
            screen = screen
        )

    def auto_place_ships(self, grid):
        for ship in pygame_storage.storage_dict["ship_list"]:
            if ship.status == "unplaced":
                ship.direction = random.choice(["top", "bottom", "left", "right"])
                ship.change_direction()
                ship.row = random.randint(0, len(grid.grid) - 1)
                ship.column = random.randint(0, len(grid.grid[0]) - 1)
                ship.status = "placed"
                
    