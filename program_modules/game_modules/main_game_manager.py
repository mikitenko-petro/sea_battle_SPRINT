from ..tools.storage import storage
from ..tools.music_manager import music_manager
from ..tools.string_manager import write_string
from .battle.dummy_ship import DummyShip

class MainGameManager():
    def __init__(self):
        storage.add_variable({"last_row" : -1})
        storage.add_variable({"last_column" : -1})
        storage.add_variable({"defeated_ship" : 0})
        storage.add_variable({"defeated_cells" : 0})

        storage.add_variable({"win" : None}) 

        storage.add_variable({"dummy_ship_list" : []})

        storage.add_variable({"moves": 0})
        storage.add_variable({"hits": 0})

    def check_hit(self):
        if len(storage.storage_dict["DataManager"].data["shoot_coord"]) > 0:
            data = storage.storage_dict["DataManager"].data["shoot_coord"][0]

            print(data)
            if len(data) == 2:
                row = int(data[0])
                column = int(data[1])

                if storage.storage_dict["PLAYER_GRID"].grid[row][column] == "~":
                    storage.storage_dict["Client"].send_data(write_string("shoot_coord","hit", row, column))
                    storage.storage_dict["PLAYER_GRID"].grid[row][column] = "X"
                    music_manager.sfx["hit_effect"].play()

                elif storage.storage_dict["PLAYER_GRID"].grid[row][column] == "O":
                    storage.storage_dict["Client"].send_data(write_string("shoot_coord","shield", row, column))
                    storage.storage_dict["PLAYER_GRID"].grid[row][column] = "~"
                    storage.storage_dict["player_turn"] = True

                else:
                    storage.storage_dict["Client"].send_data(write_string("shoot_coord","miss", row, column))
                    storage.storage_dict["PLAYER_GRID"].grid[row][column] = "x"
                    storage.storage_dict["player_turn"] = True

            elif len(data) == 3:
                status = str(data[0])
                row = int(data[1])
                column = int(data[2])

                match status:
                    case "hit":
                        storage.storage_dict["ENEMY_GRID"].grid[row][column] = "X"
                        storage.storage_dict["player_turn"] = True
                        music_manager.sfx["hit_effect"].play()

                    case "shield":
                        storage.storage_dict["ENEMY_GRID"].grid[row][column] = "o"
                        music_manager.sfx["shield4"].play()

                    case "radio_set":
                        storage.storage_dict["AbilityManager"].ability_dict["RadioSet"].scan_area(
                            row = row,
                            column = column
                        )
                        storage.storage_dict["player_turn"] = True

                storage.storage_dict["hits"] += 1

            elif len(data) == 4:
                status = str(data[1])
                row = int(data[2])
                column = int(data[3])
                
                storage.storage_dict["ENEMY_GRID"].grid[row][column] = status

            elif len(data) == 1:
                if data[0] == "shield_placed":
                    storage.storage_dict["player_turn"] = True
                    music_manager.sfx["shield1"].play()

            storage.storage_dict["DataManager"].data["shoot_coord"].pop(0)
                 
    def check_lose(self):
        storage.storage_dict["defeated_ship"] = 0
        for ship in storage.storage_dict["ship_list"]:
            if ship.status == "defeated":
                storage.storage_dict["defeated_ship"] += 1
                       
        if storage.storage_dict["defeated_ship"] == 10:
            storage.storage_dict["win"] = False
            storage.storage_dict["SceneManager"].change_scene(scene = "end")

        storage.storage_dict["defeated_cells"] = 0
        if hasattr(storage.storage_dict["ENEMY_GRID"], "cell_list") == True:
            for cell in storage.storage_dict["ENEMY_GRID"].cell_list:
                if cell.type == "X":
                    storage.storage_dict["defeated_cells"] += 1
                       
        if storage.storage_dict["defeated_cells"] == 20:
            storage.storage_dict["win"] = True
            storage.storage_dict["SceneManager"].change_scene(scene = "end")
        
    def check_destroy(self):
        if len(storage.storage_dict["DataManager"].data["defeated_ship"]) > 0:
            data = storage.storage_dict["DataManager"].data["defeated_ship"][0]

            storage.storage_dict["dummy_ship_list"].append(
                DummyShip(
                    id = data[0],
                    type = data[1],
                    direction = data[2],
                    row = int(data[3]),
                    column = int(data[4]),
                )
            )
            music_manager.sfx["kill_effect"].play()

            storage.storage_dict["DataManager"].data["defeated_ship"].pop(0)

        for dummy in storage.storage_dict["dummy_ship_list"]:
            dummy.show_ship()

    def event_manager(self):
        self.check_lose()
        self.check_hit()
        self.check_destroy()