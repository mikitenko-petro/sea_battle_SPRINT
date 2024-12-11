from ...pygame_storage import pygame_storage
from ...widgets.pygame_button import PygameButton

class ReturnButton():
    def __init__(self, screen : object, coordinates : tuple, event : object, id : int):
        turn_button = PygameButton(
            coordinates = coordinates, 
            size = (50, 50),
            event = event, 
            function = lambda : self.ship_return(id = id),
            path = "static/images/return_button.png",
            screen = screen
        )
        
    def ship_return(self, id : int):
        pygame_storage.storage_dict["selected_row"] = -1
        pygame_storage.storage_dict["selected_column"] = -1

        pygame_storage.storage_dict["ship_list"][id].row = -1
        pygame_storage.storage_dict["ship_list"][id].column = -1
        pygame_storage.storage_dict["ship_list"][id].status = "unplaced"
        pygame_storage.storage_dict["ship_list"][id].direction = "right"
        pygame_storage.storage_dict["ship_list"][id].highlight_ship()
        pygame_storage.storage_dict["ship_list"][id].change_direction()