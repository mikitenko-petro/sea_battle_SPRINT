from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_text_input import PygameTextInput
from ..widgets.pygame_button import PygameButton
from ..tools.pygame_storage import pygame_storage
from ..game_widgets.last_choise_button import LastChoiceButton
from ..game_modules.grid import Grid
from ..game_modules.ship import Ship
from ..widgets.pygame_rect import PygameRect

#Створюємо клас для створення екрану для під'єднання до серверу
class ConectToServerScreenScene():
    def __init__(self, screen : object, scene_manager : object):
        self.scene_manager = scene_manager
        self.screen = screen
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

        self.last_sesion_ip = LastChoiceButton(
            screen = self.screen,
            x = 610,
            y = 260-96,
            content_type = "IP",
            event = event
        )
        
        self.last_sesion_ip.show_button(600, 250, 384, 96)
        
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

        self.last_sesion_port = LastChoiceButton(
            screen = self.screen,
            x = 610,
            y = 460-96,
            content_type = "PORT",
            event = event
        )
        
        self.last_sesion_port.show_button(600, 450, 384, 96)

    def connect_to_server(self):
        try:
            pygame_storage.storage_dict["GAME"].client.ip = pygame_storage.storage_dict['IP']
            pygame_storage.storage_dict["GAME"].client.port = int(pygame_storage.storage_dict['PORT'])
            pygame_storage.storage_dict["GAME"].client.join()
            pygame_storage.storage_dict["GAME"].client.get_data_func.start()

            self.last_sesion_ip.create_json(pygame_storage.storage_dict['IP'])
            self.last_sesion_port.create_json(pygame_storage.storage_dict['PORT'])

            self.prepare_to_game()

            self.scene_manager.change_scene(scene = "prepare_to_game")
        except Exception as error:
            print(error)

    def prepare_to_game(self):
        pygame_storage.add_variable({"PLAYER_GRID" : None})
        pygame_storage.storage_dict["PLAYER_GRID"] = Grid(
            coordinates = (350, 150),
            type = "player",
            scene_manager = self.scene_manager
        )

        pygame_storage.add_variable({"ship_list" : None})
        pygame_storage.storage_dict["ship_list"] = []

        for i in range(10):
            if i < 4:
                pygame_storage.storage_dict["ship_list"].append(Ship(type = "1x1", id = i))
            elif i < 7:
                pygame_storage.storage_dict["ship_list"].append(Ship(type = "2x1", id = i))
            elif i < 9:
                pygame_storage.storage_dict["ship_list"].append(Ship(type = "3x1", id = i))
            else:
                pygame_storage.storage_dict["ship_list"].append(Ship(type = "4x1", id = i))

        pygame_storage.add_variable({"collision_list" : None})

        pygame_storage.storage_dict["collision_list"] = [
            PygameRect((350, 100), (500, 50), screen=self.screen),
            PygameRect((850, 150), (50, 500), screen=self.screen),
            PygameRect((350, 650), (500, 50), screen=self.screen),
            PygameRect((300, 150), (50, 500), screen=self.screen)
        ]