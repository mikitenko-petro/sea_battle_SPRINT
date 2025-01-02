from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_button import PygameButton
from ..widgets.pygame_text import PygameText
from ..tools.pygame_storage import pygame_storage

#Робимо клас для Основної сцени гри
class AchievementScreenScene():
    #Робимо функцію ініт для задання параметрів та основних модулів
    def __init__(self):
        pass

    #Робим метод для початкогово екрану
    def run(self, event : object):
        #Робим фон для початкової сцени
        background_image = PygameImage(
            path = "static/images/great_sea_battle_bg.png",
            coordinates = (0, 0),
            size = (1200, 700)
        )

        return_button = PygameButton(
            coordinates = (0, 0),
            size = (50, 50),
            event = event,
            path = "static/images/apply_button.png",
            function = lambda: pygame_storage.storage_dict["SceneManager"].change_scene(scene = "main")
        )

        title = PygameText(
            text = "Achievements",
            font_size = 120,
            x = 240,
            y = 500,
            font = "static/fonts/alagard.ttf",
            color = (34, 32, 52)
        )