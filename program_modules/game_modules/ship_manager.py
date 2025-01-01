from ..tools.pygame_storage import pygame_storage

class ShipManager():
    def __init__(self, event):
        self.event = event
        pygame_storage.add_variable({"picked_ship" : -1})
        pygame_storage.add_variable({"defeated_ship_list" : []})

        for i in range(len(pygame_storage.storage_dict["ship_list"])):
            pygame_storage.storage_dict["ship_list"][i].select_ship(event = self.event)

            if pygame_storage.storage_dict["ship_list"][i].status == "placed" or pygame_storage.storage_dict["ship_list"][i].status == "defeated":
                pygame_storage.storage_dict["ship_list"][i].show_ship(
                    event = event,
                    x = pygame_storage.storage_dict["PLAYER_GRID"].x + pygame_storage.storage_dict["ship_list"][i].row*50,
                    y = pygame_storage.storage_dict["PLAYER_GRID"].y + pygame_storage.storage_dict["ship_list"][i].column*50,
                )
            
            pygame_storage.storage_dict["ship_list"][i].check_collide()

    def show_label(self, coordinates):
        self.x, self.y = coordinates
        for i in range(len(pygame_storage.storage_dict["ship_list"])):
            if pygame_storage.storage_dict["ship_list"][i].status == "unplaced":
                pygame_storage.storage_dict["ship_list"][i].show_ship(
                    self.event,
                    x = self.x,
                    y = self.y + i*45,
                )