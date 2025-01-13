from ...widgets.pygame_animation import PygameAnimation
from ...tools.storage import storage

class RadioSetAnimation():
    def __init__(self):
        self.row = -1
        self.column = -1

    def show(self):
        if self.row != -1 and self.column != -1:
            storage.add_variable({f"RadioSetAnimation_{self.row}_{self.row}":
                    PygameAnimation(
                        animation_name = "radar_animation",
                        coordinates = (
                            storage.storage_dict["ENEMY_GRID"].y + (self.row - 1)*50,
                            storage.storage_dict["ENEMY_GRID"].x + (self.column - 1)*50
                        ),
                        size = (150, 150),
                        speed = 0.2,
                        loop = False
                    )
                }
            )
            storage.storage_dict[f"fire_animation_{self.row}_{self.row}"].display()