from ...pygame_storage import pygame_storage
from ...widgets.pygame_button import PygameButton

class TurnButton():
    def __init__(self, screen : object, coordinates : tuple, event : object, id : int):
        turn_button = PygameButton(
            coordinates = coordinates, 
            size = (50, 50),
            event = event, 
            function = lambda : self.rotate(id = id),
            path = "static/images/turn_button.png",
            screen = screen
        )
        
    def rotate(self, id : int):
        match pygame_storage.storage_dict["ship_list"][id].direction:
            case "right":
                pygame_storage.storage_dict["ship_list"][id].direction = "bottom"
            case "bottom":
                pygame_storage.storage_dict["ship_list"][id].direction = "left"
            case "left":
                pygame_storage.storage_dict["ship_list"][id].direction = "top"
            case "top":
                pygame_storage.storage_dict["ship_list"][id].direction = "right"

        pygame_storage.storage_dict["ship_list"][id].change_direction()