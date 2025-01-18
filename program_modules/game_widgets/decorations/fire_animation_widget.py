from ...tools.storage import storage
from ...widgets.pygame_animation import PygameAnimation

class FireAnimationWidget():
    def __init__(self):
        for cell in storage.storage_dict["PLAYER_GRID"].cell_list:
            if cell.type == "X":
                storage.add_variable({f"fire_animation_{cell.row}_{cell.column}_player":
                        PygameAnimation(
                            animation_name = "fire",
                            coordinates = (
                                storage.storage_dict["PLAYER_GRID"].x + cell.column*50,
                                storage.storage_dict["PLAYER_GRID"].y + cell.row*50 - 25),
                            size = (50,50),
                            speed = 0.15
                        )
                    }
                )

                storage.storage_dict[f"fire_animation_{cell.row}_{cell.column}_player"].display()

        for cell in storage.storage_dict["ENEMY_GRID"].cell_list:
            if cell.type == "X":
                storage.add_variable({f"fire_animation_{cell.row}_{cell.column}_enemy":
                        PygameAnimation(
                            animation_name = "fire",
                            coordinates = (
                                storage.storage_dict["ENEMY_GRID"].x + cell.column*50,
                                storage.storage_dict["ENEMY_GRID"].y + cell.row*50 - 25),
                            size = (50,50),
                            speed = 0.15
                        )
                    }
                )

                storage.storage_dict[f"fire_animation_{cell.row}_{cell.column}_enemy"].display()