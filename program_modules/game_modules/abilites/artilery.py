from .parent_ability_class import Ability
from ...tools.storage import storage
from ...tools.music_manager import music_manager
from ...tools.string_manager import write_string
import random
from time import sleep

class Artilery(Ability):
    def __init__(self):
        Ability.__init__(self)
        
        self.title = "Artilery"
        self.image_path = "static/images/rocket_artilery.png"
        self.description = "Land 3 shots on 3x3 area"
        self.last_coordinates = []

        self.amount = 0
        self.price = 5

    @Ability.usage
    def use_ability(self, row, column):
        music_manager.sfx["hit_effect"].play()
        for i in range(3):
            sleep(0.1)
            while True:
                coords = (random.randint(row-1, row+1), random.randint(column-1, column+1))

                if coords not in self.last_coordinates:
                    self.last_coordinates.append(coords)
                    break

            storage.storage_dict["Client"].send_data(
                write_string(
                    "shoot_coord",
                    coords[0], 
                    coords[1]
                )
            )