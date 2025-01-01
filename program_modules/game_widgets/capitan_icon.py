from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_hitbox import PygameHitBox
from ..tools.pygame_storage import pygame_storage
from pygame.time import wait

class CapitanIcon():
    def __init__(self, color, coordinates, size):
        PygameHitBox.__init__(self, coordinates, size)
        self.color = color

    def draw(self):
        self.status = "base"
        self.path = ""
        
        if pygame_storage.storage_dict["hit_status"] == "destroyed_ship":
            self.status = "angry"
            wait(5000)
            pygame_storage.storage_dict["hit_status"] = ""
            
        elif pygame_storage.storage_dict["hit_status"] == "hit_ship":
            self.status = "strange"
            wait(5000)
            pygame_storage.storage_dict["hit_status"] = ""

        elif pygame_storage.storage_dict["hit_status"] == "hit":
            self.status = "scared"
            wait(5000)
            pygame_storage.storage_dict["hit_status"] = ""

        else:
            self.status = "base"
        
        match self.status:
            case "base":
                self.path = "static/images/Base_capitan.png"

            case "angry":
                self.path = "static/images/angry_capitan.png"

            case "strange":
                self.path = "static/images/strange_capitan.png"

            case "scared":
                self.path = "static/images/scared_capitan.png"

        capitan_image = PygameImage(
            path = self.path,
            coordinates = (self.x, self.y),
            size = (self.width, self.height)
        )
