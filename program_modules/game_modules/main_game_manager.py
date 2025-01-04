from ..tools.pygame_storage import pygame_storage
from ..tools.music_manager import music_manager
from ..tools.string_manager import write_string
from .battle.check_hit_collision import check_hit_collision
from .battle.dummy_ship import DummyShip

class MainGameManager():
    def __init__(self):
        pygame_storage.add_variable({"last_row" : -1})
        pygame_storage.add_variable({"last_column" : -1})
        pygame_storage.add_variable({"defeated_ship" : 0})
        pygame_storage.add_variable({"defeated_cells" : 0})

        pygame_storage.add_variable({"win" : None}) 

        pygame_storage.add_variable({"dummy_ship_list" : []})

        pygame_storage.add_variable({"moves": 0})
        pygame_storage.add_variable({"hits": 0})

    def shoot(self, row, column):
        if pygame_storage.storage_dict["player_turn"]:
            pygame_storage.storage_dict["Client"].send_data(write_string("shoot_coord", row, column))
            pygame_storage.storage_dict["player_turn"] = False
            pygame_storage.storage_dict["last_row"] = row
            pygame_storage.storage_dict["last_column"] = column
            pygame_storage.storage_dict["moves"] += 1

    def check_hit(self):
        data = pygame_storage.storage_dict["DataManager"].data["shoot_coord"]
        if not pygame_storage.storage_dict["player_turn"] and data:
            if len(data) == 2:
                row = int(data[0])
                column = int(data[1])

                if check_hit_collision(row, column) == True:
                    pygame_storage.storage_dict["Client"].send_data(write_string("shoot_coord","you don't missed"))
                    pygame_storage.storage_dict["PLAYER_GRID"].grid[row][column] = "X"

                    music_manager.music_dict["kill_effect"].play()
                else:
                    pygame_storage.storage_dict["PLAYER_GRID"].grid[row][column] = "x"
                    pygame_storage.storage_dict["player_turn"] = True

            elif len(data) == 1:
                pygame_storage.storage_dict["ENEMY_GRID"].grid[pygame_storage.storage_dict["last_row"]][pygame_storage.storage_dict["last_column"]] = "X"
                pygame_storage.storage_dict["player_turn"] = True
                pygame_storage.storage_dict["hits"] += 1

            pygame_storage.storage_dict["DataManager"].data["shoot_coord"] = None
                 
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
        
    def check_destroy(self):
        data = pygame_storage.storage_dict["DataManager"].data["defeated_ship"]
        if data:
            pygame_storage.storage_dict["dummy_ship_list"].append(
                DummyShip(
                    id = data[0],
                    type = data[1],
                    direction = data[2],
                    row = int(data[3]),
                    column = int(data[4]),
                )
            )

            pygame_storage.storage_dict["DataManager"].data["defeated_ship"] = None

        for dummy in pygame_storage.storage_dict["dummy_ship_list"]:
            dummy.show_ship()

    def event_manager(self):
        self.check_lose()
        self.check_hit()
        self.check_destroy()