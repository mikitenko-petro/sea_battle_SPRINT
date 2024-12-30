from .pygame_image import PygameImage
from .pygame_hitbox import PygameHitBox
from ..tools.pygame_storage import pygame_storage
import os

class PygameAnimation(PygameHitBox):
    def __init__(
        self,
        animation_name : str,
        coordinates : tuple,
        size : tuple,
        speed : float = 1.0):

        PygameHitBox.__init__(self, coordinates, size)

        self.animation_name = animation_name

        self.image_list = []
        self.step = 0
        self.speed = speed

        for image in os.listdir(f"static/images/{self.animation_name}"):
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
            self.step = 0

        else:
            self.image_list[int(self.step)].display()
            self.step += self.speed * 60 / pygame_storage.storage_dict["FPS"]