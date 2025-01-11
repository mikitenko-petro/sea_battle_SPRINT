import pygame
import os
from .search_path import search_path

class ImageContainer():
    def __init__(self):
        self.images = {}
        self.load_images()

    def load_images(self):
        for filename in os.listdir(search_path('static/images')):
            if filename.endswith('.png'):
                image = pygame.image.load(search_path(f'static/images/{filename}')).convert_alpha()
                self.images.update({f"static/images/{filename}": image})
                
            elif filename.endswith("") and not filename.endswith(".ico"):
                for image_name in os.listdir(search_path(f'static/images/{filename}')):
                    image = pygame.image.load(search_path(f'static/images/{filename}/{image_name}')).convert_alpha()
                    self.images.update({f"static/images/{filename}/{image_name}": image})