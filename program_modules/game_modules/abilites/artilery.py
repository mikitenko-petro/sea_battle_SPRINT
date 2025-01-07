from .parent_ability_class import Ability
from ...tools.storage import storage
from ...tools.string_manager import write_string
import random
from time import sleep

class Artilery(Ability):
    def __init__(self):
        Ability.__init__(self)
        
        self.title = "Artilery"
        self.image_path = "static/images/rocket_artilery.png"
        self.description = "Land 3 shots on 3x3 area"

        self.amount = 0
        self.price = 3

    @Ability.usage
    def use_ability(self, row, column):
        for i in range(3):
            sleep(0.1)
            storage.storage_dict["Client"].send_data(
                write_string(
                    "shoot_coord",
                    random.randint(row-1, row+1), 
                    random.randint(column-1, column+1)
                )
            )