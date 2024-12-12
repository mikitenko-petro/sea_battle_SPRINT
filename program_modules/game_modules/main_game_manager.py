from ..pygame_storage import pygame_storage
from ..string_manager import read_string, write_string

class MainGameManager():
    def __init__(self, client):
        self.client = client
        if pygame_storage.storage_dict["number_client"] == "1":
            self.turn = True
        else:
            self.turn = False

    def shoot(self, row, column):
        if self.turn == True:
            data = write_string(row, column)
            self.client.send_data(data)
            self.turn = False

    def check_hit(self):
        data = self.client.data
        if self.turn == False:
            if data != None:
                row, column = read_string(data)
                pygame_storage.storage_dict["PLAYER_GRID"].grid[int(row)][int(column)] = "x"
                self.turn = True

    def run(self):
        self.queue_join = pygame_storage.storage_dict["number_client"]
        if self.queue_join == "1":
            self.turn = True
        else:
            self.turn = False