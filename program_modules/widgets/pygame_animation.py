from .pygame_image import PygameImage
from .pygame_hitbox import PygameHitBox
from ..tools.storage import storage
from ..tools.search_path import search_path
import os

class PygameAnimation(PygameHitBox):
    def __init__(
        self,
        animation_name : str,
        coordinates : tuple,
        size : tuple,
        speed : float = 1.0,
        loop : bool = True):

        PygameHitBox.__init__(self, coordinates, size)

        self.animation_name = animation_name

        self.image_list = []
        self.step = 0
        self.speed = speed
        self.loop = loop

        def sort_by_number(filename):
            number = ""
            for char in filename:
                if char.isdigit():
                    number += char
            return int(number)
        
        image_list = os.listdir(search_path(f"static/images/{self.animation_name}"))
        image_list.sort(key=sort_by_number)

        for image in image_list:
            self.image_list.append(
                PygameImage(
                    path = f"static/images/{self.animation_name}/{image}",
                    coordinates = (self.x, self.y),
                    size = (self.width, self.height),
                    already_display = False
            )
        )
        
    def display(self):
        if self.step >= len(self.image_list):
            self.image_list[0].display()
            if self.loop:
                self.step = 0

        else:
            self.image_list[int(self.step)].display()
            self.step += self.speed * 60 / storage.storage_dict["FPS"]