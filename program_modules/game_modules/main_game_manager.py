from ..pygame_storage import pygame_storage
from ..music_manager import music_manager
from ..string_manager import read_string, write_string
from .check_hit_collision import check_hit_collision

class MainGameManager():
    def __init__(self, client, screen):
        self.client = client
        self.screen = screen
        pygame_storage.add_variable({"last_row" : -1})
        pygame_storage.add_variable({"last_column" : -1})
        pygame_storage.add_variable({"defeated_ship" : 0})

        if pygame_storage.storage_dict["number_client"] == "1":
            pygame_storage.add_variable({"player_turn" : True})
        else:
            pygame_storage.add_variable({"player_turn" : False})

    def shoot(self, row, column):
        if pygame_storage.storage_dict["player_turn"] == True:
            data = write_string(row, column)
            self.client.send_data(data)
            pygame_storage.storage_dict["player_turn"] = False
            pygame_storage.storage_dict["last_row"] = row
            pygame_storage.storage_dict["last_column"] = column

    def check_hit(self):
        data = self.client.data
        if pygame_storage.storage_dict["player_turn"] == False:
            if data != None:
                if len(read_string(data)) == 2:
                    row, column = read_string(data)
                    if check_hit_collision(self.screen, int(row), int(column)) == True:
                        self.client.send_data(write_string("you don't missed"))
                        pygame_storage.storage_dict["PLAYER_GRID"].grid[int(row)][int(column)] = "X"
                        music_manager.music_dict["kill_effect"].play()
                    else:
                        pygame_storage.storage_dict["PLAYER_GRID"].grid[int(row)][int(column)] = "x"
                        pygame_storage.storage_dict["player_turn"] = True
                else:
                    pygame_storage.storage_dict["ENEMY_GRID"].grid[pygame_storage.storage_dict["last_row"]][pygame_storage.storage_dict["last_column"]] = "X"
                    pygame_storage.storage_dict["player_turn"] = True
                
                self.client.data = None
                
    def check_lose(self):
        data = self.client.data
        if data != None:
            if data == "win":
                print("win")
                self.client.data = None

        pygame_storage.storage_dict["defeated_ship"] = 0
        for ship in pygame_storage.storage_dict["ship_list"]:
            if ship.status == "defeated":
                pygame_storage.storage_dict["defeated_ship"] += 1
                       
        if pygame_storage.storage_dict["defeated_ship"] == 9:
            self.client.send_data("win")