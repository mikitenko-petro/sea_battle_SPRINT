from ..pygame_storage import pygame_storage

class ShipManager():
    def __init__(self, screen, event, scene_manager):
        self.screen = screen
        self.scene_manager = scene_manager
        self.event = event
        pygame_storage.add_variable({"picked_ship" : -1})

        for i in range(len(pygame_storage.storage_dict["ship_list"])):
            pygame_storage.storage_dict["ship_list"][i].select_ship(event = self.event)

            if pygame_storage.storage_dict["ship_list"][i].status == "placed":
                pygame_storage.storage_dict["ship_list"][i].show_ship(
                    self.screen,
                    event,
                    x = pygame_storage.storage_dict["PLAYER_GRID"].x + pygame_storage.storage_dict["ship_list"][i].row*50,
                    y = pygame_storage.storage_dict["PLAYER_GRID"].y + pygame_storage.storage_dict["ship_list"][i].column*50,
                    scene_manager = scene_manager
                )
            
            pygame_storage.storage_dict["ship_list"][i].check_collide(screen)

    def show_label(self, coordinates):
        self.x, self.y = coordinates
        for i in range(len(pygame_storage.storage_dict["ship_list"])):

            if pygame_storage.storage_dict["ship_list"][i].status == "unplaced":
                pygame_storage.storage_dict["ship_list"][i].show_ship(
                    self.screen,
                    self.event,
                    x = self.x,
                    y = self.y + i*50,
                    scene_manager = self.scene_manager
                )