from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_button import PygameButton
from ..widgets.pygame_text import PygameText
from ..pygame_storage import pygame_storage
from ..client import Client

#Створюємо клас для створення екрану для під'єднання до серверу
class EndScreenScene():
    def __init__(self, screen : object, scene_manager : object, client : object):
        self.scene_manager = scene_manager
        self.screen = screen
        self.client = client

    #Створюємо метод для створення підключення до сервера
    def run(self, event):
        if pygame_storage.storage_dict['win'] == True:
            win_background_image = PygameImage(
                screen = self.screen,
                path = "static/images/victory_bg.png",
                coordinates = (0, 0),
                size = (1200, 700)
            )

            win_text = PygameText(
                screen = self.screen,
                text = "VICTORY",
                font_size = 200,
                x = 200,
                y = 300,
                font = "static/fonts/alagard.ttf",
                color = (251, 228, 76)
            )
            
        else:
            defeat_background_image = PygameImage(
                    screen = self.screen,
                    path = "static/images/defeat_bg.png",
                    coordinates = (0, 0),
                    size = (1200, 700)
                )

            defeat_text = PygameText(
                screen = self.screen,
                text = "DEFEAT",
                font_size = 200,
                x = 220,
                y = 300,
                font = "static/fonts/alagard.ttf",
                color = (69, 69, 69)
            )

        return_to_home_button = PygameButton(
            screen = self.screen,
            path = "static/images/green_button.png",
            text = "return",
            font_size = 50,
            coordinates = (460, 600),
            size = (128*2, 32*2),
            event = event,
            function = self.end_of_work
        )

    def end_of_work(self):
        self.client.listening = False
        self.client.client_socket.close()
        pygame_storage.storage_dict["GAME"].client = Client(ip = "", port = 0)


        pygame_storage.storage_dict['win'] = None

        pygame_storage.storage_dict["PLAYER_GRID"].grid = [
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
        ]

        pygame_storage.storage_dict["PLAYER_GRID"].grid = pygame_storage.storage_dict["ENEMY_GRID"].grid

        pygame_storage.storage_dict["ship_list"] = []

        self.scene_manager.change_scene(scene = "main")