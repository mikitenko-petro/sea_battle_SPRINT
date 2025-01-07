from ...tools.storage import storage
from ...widgets.pygame_button import PygameButton

class ReturnButton():
    def __init__(self, coordinates : tuple, event : object, id : int):
        turn_button = PygameButton(
            coordinates = coordinates, 
            size = (50, 50),
            event = event, 
            function = lambda : self.ship_return(id = id),
            path = "static/images/return_button.png",
        )
        
    def ship_return(self, id : int):
        storage.storage_dict["selected_row"] = -1
        storage.storage_dict["selected_column"] = -1

        storage.storage_dict["ship_list"][id].row = -1
        storage.storage_dict["ship_list"][id].column = -1
        storage.storage_dict["ship_list"][id].status = "unplaced"
        storage.storage_dict["ship_list"][id].direction = "right"
        storage.storage_dict["ship_list"][id].highlight_ship()
        storage.storage_dict["ship_list"][id].change_direction()