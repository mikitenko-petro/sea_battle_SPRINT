from ..tools.pygame_storage import pygame_storage
from ..tools.music_manager import music_manager
from ..tools.string_manager import read_string, write_string
from .check_hit_collision import check_hit_collision

class MainGameManager():
    def __init__(self):
        pygame_storage.add_variable({"last_row" : -1})
        pygame_storage.add_variable({"last_column" : -1})
        pygame_storage.add_variable({"defeated_ship" : 0})
        pygame_storage.add_variable({"defeated_cells" : 0})

        pygame_storage.add_variable({"win" : None})

        if pygame_storage.storage_dict["number_client"] == "1":
            pygame_storage.add_variable({"player_turn" : True})
        else:
            pygame_storage.add_variable({"player_turn" : False})

    def shoot(self, row, column):
        if pygame_storage.storage_dict["player_turn"]:
            data = write_string(row, column)
            pygame_storage.storage_dict["Client"].send_data(data)
            pygame_storage.storage_dict["player_turn"] = False
            pygame_storage.storage_dict["last_row"] = row
            pygame_storage.storage_dict["last_column"] = column

    def check_hit(self):
        data = pygame_storage.storage_dict["Client"].data
        if pygame_storage.storage_dict["player_turn"] == False:
            if data != None:
                if len(read_string(data)) == 2:
                    row, column = read_string(data)
                    if check_hit_collision(int(row), int(column)) == True:
                        pygame_storage.storage_dict["Client"].send_data(write_string("you don't missed"))
                        pygame_storage.storage_dict["PLAYER_GRID"].grid[int(row)][int(column)] = "X"
                        music_manager.music_dict["kill_effect"].play()
                    else:
                        pygame_storage.storage_dict["PLAYER_GRID"].grid[int(row)][int(column)] = "x"
                        pygame_storage.storage_dict["player_turn"] = True
                else:
                    pygame_storage.storage_dict["ENEMY_GRID"].grid[pygame_storage.storage_dict["last_row"]][pygame_storage.storage_dict["last_column"]] = "X"
                    pygame_storage.storage_dict["player_turn"] = True
                
                pygame_storage.storage_dict["Client"].data = None
                
    def check_lose(self):
        pygame_storage.storage_dict["defeated_ship"] = 0
        for ship in pygame_storage.storage_dict["ship_list"]:
            if ship.status == "defeated":
                pygame_storage.storage_dict["defeated_ship"] += 1
                       
        if pygame_storage.storage_dict["defeated_ship"] == 10:
            pygame_storage.storage_dict["win"] = False
            pygame_storage.storage_dict["SceneManager"].change_scene(scene = "end")

        pygame_storage.storage_dict["defeated_cells"] = 0
        if hasattr(pygame_storage.storage_dict["ENEMY_GRID"], "cell_list") == True:
            for cell in pygame_storage.storage_dict["ENEMY_GRID"].cell_list:
                if cell.type == "X":
                    pygame_storage.storage_dict["defeated_cells"] += 1
                       
        if pygame_storage.storage_dict["defeated_cells"] == 20:
            pygame_storage.storage_dict["win"] = True
            pygame_storage.storage_dict["SceneManager"].change_scene(scene = "end")
