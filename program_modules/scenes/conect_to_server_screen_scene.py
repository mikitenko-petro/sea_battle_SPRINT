from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_text_input import PygameTextInput
from ..widgets.pygame_button import PygameButton
from ..pygame_storage import pygame_storage

#Створюємо клас для створення екрану для під'єднання до серверу
class ConectToServerScreenScene():
    def __init__(self, screen : object, scene_manager : object, client : object):
        self.scene_manager = scene_manager
        self.screen = screen
        self.client = client
        pygame_storage.add_variable({"IP" : "enter your ip"})
        pygame_storage.add_variable({"PORT" : "enter your port"})

    #Створюємо метод для створення підключення до сервера
    def run(self, event):
        background_image = PygameImage(
            screen = self.screen,
            path = "static/images/lighthouse_bg.png",
            coordinates = (0, 0),
            size = (1200, 700)
        )
        
        #Робимо строку вводу для айпі
        connect_to_server_button = PygameButton(
            screen = self.screen,
            path = "static/images/hollow_label.png",
            coordinates = (365, 320),
            size = (128*1.5, 32*1.5),
            font_size = 30,
            event = event,
            function = self.connect_to_server,
            text = "connect to server"
        )

        text_input_ip = PygameTextInput(
            size = (384, 96),
            coordinates = (600, 250),
            event = event,
            screen = self.screen,
            name = "ip",
            store_to = "IP",
            initial_text = "enter your ip"
        )
        
        #Робимо строку вводу для порту
        text_input_port = PygameTextInput(
            size = (384, 96),
            coordinates = (600, 450),
            event = event,
            screen = self.screen,
            name = "port",
            store_to = "PORT",
            initial_text = "enter your port"
        )

    def connect_to_server(self):
        try:
            self.client.ip = pygame_storage.storage_dict['IP']
            self.client.port = int(pygame_storage.storage_dict['PORT'])
            self.client.join()
            self.client.get_data_func.start()

            self.scene_manager.change_scene(scene = "prepare_to_game")
            
        except Exception as error:
            print(error)