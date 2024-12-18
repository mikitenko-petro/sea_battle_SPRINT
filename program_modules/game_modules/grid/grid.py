from ...pygame_storage import pygame_storage as ps
from .cell import Cell
from ...widgets.pygame_hitbox import PygameHitBox

#Робим клас для створення сітки
class Grid(PygameHitBox):
    def __init__(self, coordinates, type, scene_manager):
        self.grid = [
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ]

        PygameHitBox.__init__(self, coordinates, (0,0))

        ps.add_variable({"selected_row" : -1})
        ps.add_variable({"current_coumn" : -1})

        self.type = type
        self.scene_manager = scene_manager

    def place_ship(self):
        if ps.storage_dict["picked_ship"] != -1:
            if ps.storage_dict["ship_list"][ps.storage_dict["picked_ship"]].status == "unplaced":
                if ps.storage_dict["selected_row"] != -1:
                    if ps.storage_dict["selected_column"] != -1:
                        ps.storage_dict["ship_list"][ps.storage_dict["picked_ship"]].row = ps.storage_dict["selected_row"]
                        ps.storage_dict["ship_list"][ps.storage_dict["picked_ship"]].column = ps.storage_dict["selected_column"]

                        ps.storage_dict["ship_list"][ps.storage_dict["picked_ship"]].status = "placed"
                        ps.storage_dict["ship_list"][ps.storage_dict["picked_ship"]].highlight_ship()
                        ps.storage_dict["picked_ship"] = -1
                        ps.storage_dict["selected_row"] = -1
                        ps.storage_dict["selected_column"] = -1
    
    def show_grid(self, screen, event):
        self.cell_list = []

        cell_x = 0
        cell_y = 0
        cell_index = 0

        for row in self.grid:
            for type in row:
                self.cell_list.append(Cell(
                    screen = screen,
                    coordinates = (cell_x, cell_y),
                    size = (50,50),
                    initial_x = self.x,
                    initial_y = self.y,
                    type = type,
                    grid_type = self.type,
                    scene_manager = self.scene_manager
                ))
                self.cell_list[cell_index].click_checking(event)

                cell_index += 1
                cell_x += 50
            cell_y += 50
            cell_x = 0
    