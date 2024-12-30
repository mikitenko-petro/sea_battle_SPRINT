from ..tools.pygame_storage import pygame_storage
from ..widgets.pygame_animation import PygameAnimation

class FireAnimationWidget():
    def __init__(self, type):
        if type == "player":
            self.grid = pygame_storage.storage_dict["PLAYER_GRID"]

        elif type == "enemy":
            self.grid = pygame_storage.storage_dict["ENEMY_GRID"]
    
    def create_fire_animation(self):
        for cell in self.grid.cell_list:
            if cell.type == "X":
                pygame_storage.add_variable({f"fire_animation_{cell.row}_{cell.column}_{self.grid.type}":
                        PygameAnimation(
                            animation_name = "fire",
                            coordinates = (self.grid.x + cell.row*50, self.grid.y + cell.column*50 - 25),
                            size = (50,50),
                            speed = 0.15
                        )
                    }
                )

                pygame_storage.storage_dict[f"fire_animation_{cell.row}_{cell.column}_{self.grid.type}"].display()