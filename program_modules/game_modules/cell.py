from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_hitbox import PygameHitBox
from ..widgets.pygame_button import PygameButton
from .game_widgets.collision import Collision
from ..pygame_storage import pygame_storage
import pygame

class Cell(PygameHitBox):
    def __init__(
            self,
            screen : object,
            coordinates: tuple,
            size: tuple,
            initial_x : int,
            initial_y : int,
            type : str,
            grid_type : str,
            scene_manager : object):
        
        PygameHitBox.__init__(self, coordinates, size)

        self.initial_x = initial_x
        self.initial_y = initial_y

        self.row = self.x // 50
        self.column = self.y // 50

        self.path = ""
        self.scene_manager = scene_manager

        match type:
            case '  ':
                self.path = "static/images/cell.png"

            case 'x':
                self.path = "static/images/wrong_cell.png"

            case 'X':
                self.path = "static/images/right_cell.png"
                self.collision = Collision(
                    screen = screen,
                    coordinates = (initial_x + self.x + 1, initial_y + self.y + 1),
                    size = (self.width-2, self.height-2),
                    type = "cell"
                )
            
        cell = PygameImage(
            screen = screen,
            path = self.path,
            coordinates = (initial_x + self.x, initial_y + self.y),
            size = size
        )

        self.grid_type = grid_type

    def click_checking(self, event):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        for pygame_event in event: 
            if not (mouse_x >= self.initial_x and mouse_x <= self.initial_x + 500 and mouse_y >= self.initial_y and mouse_y <= self.initial_y + 500):
                if pygame_event.type == pygame.MOUSEBUTTONDOWN:
                    pygame_storage.storage_dict["selected_row"] = -1
                    pygame_storage.storage_dict["selected_column"] = -1

        cell_button = PygameButton(
            coordinates = (self.initial_x + self.x, self.initial_y + self.y),
            size = (self.width, self.height),
            event = event,
            function = self.set_current_cell
        )
    
    def set_current_cell(self):
        if self.scene_manager.current_scene == "prepare_to_game":
            pygame_storage.storage_dict["selected_row"] = self.row
            pygame_storage.storage_dict["selected_column"] = self.column
        else:
            if self.grid_type == "enemy":
                if pygame_storage.storage_dict["player_turn"] == True:
                    pygame_storage.storage_dict["selected_row"] = self.row
                    pygame_storage.storage_dict["selected_column"] = self.column
                    pygame_storage.storage_dict["ENEMY_GRID"].grid[self.column][self.row] = "x"
                    pygame_storage.storage_dict["MainGameManager"].shoot(self.column, self.row)
                    pygame_storage.storage_dict["player_turn"] = False