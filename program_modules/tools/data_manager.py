from .string_manager import read_string

class DataManager():
    def __init__(self):
        self.data = {
            "shoot_coord": [],
            "defeated_ship": [],
            "player_handle": []
        }
    
    def load_data(self, data):
        data = read_string(data)
        self.data[f"{data[0]}"].append(data[1:])