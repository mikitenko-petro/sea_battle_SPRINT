from ...tools.storage import storage
from ...widgets.pygame_image import PygameImage

class ShieldWidget():
    def __init__(self):
        #I HAVE PLAYED THIS GAME BEFORE
        for cell in storage.storage_dict["PLAYER_GRID"].cell_list:
            if cell.type == "O":
                image = PygameImage(
                    path = "static/images/shield_tile.png",
                    coordinates = (storage.storage_dict["PLAYER_GRID"].x + cell.column*50, storage.storage_dict["PLAYER_GRID"].y + cell.row*50),
                    size = (50, 50)
                )