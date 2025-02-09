from .parent_ability_class import Ability
from ...widgets.pygame_animation import PygameAnimation
from ...tools.music_manager import music_manager
from ...tools.storage import storage
from ...tools.string_manager import write_string
from time import sleep

class RadioSet(Ability):
    def __init__(self):
        Ability.__init__(self)
        
        self.title = "Radio Set"
        self.image_path = "static/images/radio_set.png"
        self.description = "Scan 3x3 area for ships"

        self.amount = 0
        self.price = 7

    @Ability.usage
    def use_ability(self, row, column):
        storage.storage_dict["radio_set_animation_list"].append(
            PygameAnimation(
                    animation_name = "radar_animation",
                    coordinates = (
                        storage.storage_dict["ENEMY_GRID"].x + (column - 1)*50,
                        storage.storage_dict["ENEMY_GRID"].y + (row - 1)*50,
                    ),
                    size = (150, 150),
                    speed = 0.2,
                    loop = False,
                )
        )
        music_manager.sfx["radio_set"].play()

        storage.storage_dict["Client"].send_data(write_string("shoot_coord", "radio_set", row, column))

    def scan_area(self, row, column):
        for i in range(-1, 2):
            for j in range(-1, 2):
                sleep(0.1)
                if storage.storage_dict["PLAYER_GRID"].grid[row + i][column + j] == "~":
                    storage.storage_dict["Client"].send_data(
                        write_string("shoot_coord", "radio_set", "o", row + i, column + j)
                    )

                elif storage.storage_dict["PLAYER_GRID"].grid[row + i][column + j] == "":
                    storage.storage_dict["Client"].send_data(
                        write_string("shoot_coord", "radio_set", "*", row + i, column + j)
                    )