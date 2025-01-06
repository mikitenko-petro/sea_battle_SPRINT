from ...tools.pygame_storage import pygame_storage as ps
from .cell import Cell
from ...widgets.pygame_hitbox import PygameHitBox
from ...widgets.pygame_text import PygameText

#Робим клас для створення сітки
class Grid(PygameHitBox):
    def __init__(self, coordinates, type):
        self.grid = [
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
        ]

        self.text_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        self.number_list = [1, 2, 3, 4, 5, 6, 7 , 8, 9, 10]

        PygameHitBox.__init__(self, coordinates, (0,0))

        ps.add_variable({"selected_row" : -1})
        ps.add_variable({"current_coumn" : -1})

        self.type = type

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
    
    def show_grid(self, event):
        self.cell_list = []
        cell_index = 0

        for i in range(10):
            text_word = PygameText(
                text = self.text_list[i],
                font_size = 40,
                x = self.x-35,
                y = self.y+i*50+10,
                font = "static/fonts/alagard.ttf"
            )
            
            text_number = PygameText(
                text = f"{self.number_list[i]}",
                font_size = 40,
                x = self.x+i*50+10,
                y = self.y-35,
                font = "static/fonts/alagard.ttf"
            )

        for y, row in enumerate(self.grid):
            for x, type in enumerate(row):
                self.cell_list.append(
                    Cell(
                        coordinates = (x*50, y*50),
                        size = (50,50),
                        initial_x = self.x,
                        initial_y = self.y,
                        type = type,
                        grid_type = self.type,
                    )
                )
                
                self.cell_list[cell_index].click_checking(event)
                cell_index += 1