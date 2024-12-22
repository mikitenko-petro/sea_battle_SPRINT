from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_button import PygameButton
from ..pygame_storage import pygame_storage

#Створюємо клас для створення екрану для під'єднання до серверу
class ConectToServerScreenScene():
    def __init__(self, screen : object, scene_manager : object, client : object):
        self.scene_manager = scene_manager
        self.screen = screen
        self.client = client

    #Створюємо метод для створення підключення до сервера
    def run(self, event):
        background_image = PygameImage(
            screen = self.screen,
            path = "static/images/lighthouse_bg.png",
            coordinates = (0, 0),
            size = (1200, 700)
        )

