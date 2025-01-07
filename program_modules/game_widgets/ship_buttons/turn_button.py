from ...tools.storage import storage
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
        match storage.storage_dict["ship_list"][id].direction:
            case "right":
                storage.storage_dict["ship_list"][id].direction = "bottom"
            case "bottom":
                storage.storage_dict["ship_list"][id].direction = "left"
            case "left":
                storage.storage_dict["ship_list"][id].direction = "top"
            case "top":
                storage.storage_dict["ship_list"][id].direction = "right"

        storage.storage_dict["ship_list"][id].change_direction()