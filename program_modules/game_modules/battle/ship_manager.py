from ...tools.storage import storage

class ShipManager():
    def __init__(self, event):
        self.event = event
        storage.add_variable({"picked_ship" : -1})
        storage.add_variable({"defeated_ship_list" : []})

        for i in range(len(storage.storage_dict["ship_list"])):
            storage.storage_dict["ship_list"][i].select_ship(event = self.event)

            if storage.storage_dict["ship_list"][i].status == "placed" or storage.storage_dict["ship_list"][i].status == "defeated":
                storage.storage_dict["ship_list"][i].show_ship(
                    event = event,
                    x = storage.storage_dict["PLAYER_GRID"].x + storage.storage_dict["ship_list"][i].column*50,
                    y = storage.storage_dict["PLAYER_GRID"].y + storage.storage_dict["ship_list"][i].row*50,
                )
            
            storage.storage_dict["ship_list"][i].check_collide()

    def show_label(self, coordinates):
        self.x, self.y = coordinates
        for i in range(len(storage.storage_dict["ship_list"])):
            if storage.storage_dict["ship_list"][i].status == "unplaced":
                storage.storage_dict["ship_list"][i].show_ship(
                    self.event,
                    x = self.x,
                    y = self.y + i*45,
                )