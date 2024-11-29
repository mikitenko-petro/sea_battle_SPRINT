import pygame
from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_text import PygameText
from ..widgets.pygame_text_input import PygameTextInput

#Створюємо клас для створення екрану для під'єднання до серверу
class ConectToServerScreenScene():
    #Робим метод
    def __init__(self, screen, scene_manager, pygame_storage):
        self.screen = screen
        self.pygame_storage = pygame_storage
        self.pygame_storage.add_variable({"IP" : ""})

    def run(self, event):
        background_image = PygameImage(
        screen = self.screen,
        path = "static/images/lighthouse_bg.png",
        coordinates = (0, 0),
        size = (1200, 700))

        text_input_ip = PygameTextInput(
        size = (384, 96),
        coordinates = (600, 250),
        event = event,
        screen = self.screen,
        pygame_storage = self.pygame_storage,
        name = "ip")

        ip_label = PygameImage(
        screen = self.screen,
        path = "static/images/start_button.png",
        coordinates = (10, 250),
        size = (128*2.5, 32*2))

        ip_text = PygameText(
        screen = self.screen,
        text = f"your IP: {self.pygame_storage.storage_dict['IP']}",
        font = None,
        font_size = 40,
        x = 10 + 10,
        y = 250 + 20)

        text_input_port = PygameTextInput(
        size = (384, 96),
        coordinates = (600, 450),
        event = event,
        screen = self.screen,
        pygame_storage = self.pygame_storage,
        name = "port")

        port_label = PygameImage(
        screen = self.screen,
        path = "static/images/start_button.png",
        coordinates = (10, 450),
        size = (128*2.5, 32*2))

        port_text = PygameText(
        screen = self.screen,
        text = f"your PORT: {self.pygame_storage.storage_dict['PORT']}",
        font = None,
        font_size = 40,
        x = 10 + 10,
        y = 250 + 220)

        