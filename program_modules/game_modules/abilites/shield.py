from .parent_ability_class import Ability
from ..battle.check_hit_collision import check_hit_collision
from ...tools.pygame_storage import pygame_storage

class Shield(Ability):
    def __init__(self):
        Ability.__init__(self)
        
        self.title = "Shield"
        self.image_path = "static/images/shield.png"
        self.description = "Protect one tile of ship"

        self.amount = 0
        self.price = 3

    @Ability.usage
    def use_ability(self):
        row = pygame_storage.storage_dict["selected_row"]
        column = pygame_storage.storage_dict["selected_column"]
        
        if check_hit_collision(column, row, enemy = False):
            if pygame_storage.storage_dict["PLAYER_GRID"].grid[row][column] == "~":
                pygame_storage.storage_dict["PLAYER_GRID"].grid[row][column] = "O"