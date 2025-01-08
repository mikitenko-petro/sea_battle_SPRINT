from .parent_ability_class import Ability
from ...tools.storage import storage
from ...tools.string_manager import write_string

class Shield(Ability):
    def __init__(self):
        Ability.__init__(self)
        
        self.title = "Shield"
        self.image_path = "static/images/shield.png"
        self.description = "Protect one tile of ship"

        self.amount = 0
        self.price = 3

    @Ability.usage
    def use_ability(self, row, column):
        storage.storage_dict["PLAYER_GRID"].grid[row][column] = "O"
        storage.storage_dict["Client"].send_data(write_string("shoot_coord", "shield_placed"))