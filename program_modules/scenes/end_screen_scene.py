from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_button import PygameButton
from ..widgets.pygame_text import PygameText
from ..pygame_storage import pygame_storage


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
                x = 300,
                y = 200,
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
                x = 300,
                y = 200,
                font = "static/fonts/alagard.ttf",
                color = (192, 192, 192)
            )

        return_to_home_button = PygameButton(
            path = "static/images/green_button.png",
            text = "Home",
            font_size = 50,
            coordinates = (460, 230),
            size = (128*2, 32*2),
            event = event,
            function = None
        )

    