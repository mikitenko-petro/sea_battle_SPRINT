from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_button import PygameButton

#Робимо клас для Основної сцени гри
class MainScreenScene():
    #Робимо функцію ініт для задання параметрів та основних модулів
    def __init__(self, screen : object, scene_manager : object):
        self.screen = screen
        self.scene_manager = scene_manager

    #Робим метод для початкогово екрану
    def run(self, event : object):
        #Робим фон для початкової сцени
        background_image = PygameImage(
            screen = self.screen,
            path = "static/images/great_sea_battle_bg.png",
            coordinates = (0, 0),
            size = (1200, 700)
        )

        #Робим кнопку старт
        move_to_scene = PygameButton(
            screen = self.screen,
            path = "static/images/green_button.png",
            text = "Start",
            font_size = 50,
            coordinates = (460, 230),
            size = (128*2, 32*2),
            event = event,
            function = lambda: self.scene_manager.change_scene(scene = "conect_to_server")
        )