from ...widgets.pygame_image import PygameImage
from ...widgets.pygame_hitbox import PygameHitBox
from ...widgets.pygame_button import PygameButton
from ...widgets.pygame_rect import PygameRect
from ...widgets.pygame_animation import PygameAnimation
from ...tools.storage import storage
from ...tools.music_manager import music_manager
from ...tools.string_manager import write_string
import pygame

class Cell(PygameHitBox):
    def __init__(
            self,
            coordinates: tuple,
            size: tuple,
            initial_x : int,
            initial_y : int,
            type : str,
            grid_type : str,):
        
        PygameHitBox.__init__(self, coordinates, size)

        self.initial_x = initial_x
        self.initial_y = initial_y

        self.row = self.y // 50
        self.column = self.x // 50

        self.path = ""
        self.type = type
        self.grid_type = grid_type

        cell = PygameImage(
            path = "static/images/cell.png",
            coordinates = (initial_x + self.x, initial_y + self.y),
            size = size
        )

        self.collision = PygameRect(
            coordinates = (initial_x + self.x + 1, initial_y + self.y + 1),
            size = (self.width-2, self.height-2),
        )

        if type == "x":
            storage.add_variable({f"bauble_animation_{self.row}_{self.column}_{self.grid_type}":
                    PygameAnimation(
                        animation_name = "baubles",
                        coordinates = (initial_x + self.x, initial_y + self.y),
                        size = size,
                        speed = 0.15
                    )
                }
            )

            storage.storage_dict[f"bauble_animation_{self.row}_{self.column}_{self.grid_type}"].display()

        elif type == "X":
            storage.add_variable({f"scrap_animation_{self.row}_{self.column}_{self.grid_type}":
                    PygameAnimation(
                        animation_name = "scrap",
                        coordinates = (initial_x + self.x, initial_y + self.y),
                        size = size,
                        speed = 0.05
                    )
                }
            )

            storage.storage_dict[f"scrap_animation_{self.row}_{self.column}_{self.grid_type}"].display()

        elif type == "o":
            cell = PygameImage(
                path = "static/images/right_cell.png",
                coordinates = (initial_x + self.x, initial_y + self.y),
                size = size
            )

        elif type == "*":
            cell = PygameImage(
                path = "static/images/radio_set_tile.png",
                coordinates = (initial_x + self.x, initial_y + self.y),
                size = size
            )  
             
    def click_checking(self, event):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        for pygame_event in event: 
            if not (mouse_x >= self.initial_x and mouse_x <= self.initial_x + 500 and mouse_y >= self.initial_y and mouse_y <= self.initial_y + 500):
                if pygame_event.type == pygame.MOUSEBUTTONDOWN:
                    storage.storage_dict["selected_row"] = -1
                    storage.storage_dict["selected_column"] = -1

        if not storage.storage_dict["show_quests"]:
            cell_button = PygameButton(
                coordinates = (self.initial_x + self.x, self.initial_y + self.y),
                size = (self.width, self.height),
                event = event,
                function = self.set_current_cell
            )
    
    def set_current_cell(self):
        enemy_cell = storage.storage_dict["ENEMY_GRID"].grid[self.row][self.column]
        
        if storage.storage_dict["SceneManager"].current_scene == "game" and storage.storage_dict["player_turn"]:
            match storage.storage_dict["AbilityManager"].picked_ability:
                case None:
                    if self.grid_type == "enemy" and (enemy_cell == "" or enemy_cell == "o"):
                        storage.storage_dict["Client"].send_data(
                            write_string("shoot_coord", self.row, self.column)
                        )
                        storage.storage_dict["ENEMY_GRID"].grid[self.row][self.column] = "x"

                        storage.storage_dict["moves"] += 1
                        storage.storage_dict["player_turn"] = False
                
                case "Shield":           
                    if self.grid_type == "player" and self.type == "~":
                        storage.storage_dict["AbilityManager"].ability_dict["Shield"].use_ability(
                            row = self.row,
                            column = self.column
                        )
                
                case "RadioSet":
                    if self.grid_type == "enemy":
                        if (0 < self.row < 9) and (0 < self.column < 9):
                            storage.storage_dict["AbilityManager"].ability_dict["RadioSet"].use_ability(
                                row = self.row,
                                column = self.column
                            )

                case "Artilery":
                    if self.grid_type == "enemy":
                        if (0 < self.row < 9) and (0 < self.column < 9):
                            storage.storage_dict["AbilityManager"].ability_dict["Artilery"].use_ability(
                                row = self.row,
                                column = self.column
                            )

    def check_for_ship(self):
        for ship in storage.storage_dict["ship_list"]:
            if self.collision.collidelist([ship.ship_collision_rect]) != -1:
                storage.storage_dict[f"{self.grid_type.upper()}_GRID"].grid[self.row][self.column] = "~"