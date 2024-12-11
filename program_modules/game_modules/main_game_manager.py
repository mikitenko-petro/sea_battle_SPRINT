from ..pygame_storage import pygame_storage

from ..string_manager import read_string, write_string

class MainGameManager():
    def __init__(self, client):
        self.client = client
        self.queue_join = pygame_storage.storage_dict["number_client"]
        if self.queue_join == "1":
            self.turn = True
        else:
            self.turn = False

        print(self.turn)
    
    def shoot(self, data : str):
        if self.turn == True:
            self.client.send_data(data)
            self.turn = False
        else:
            data = self.client.get_data()
            self.turn = True

    def run(self):
        ...