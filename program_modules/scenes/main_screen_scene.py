from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_button import PygameButton
from ..widgets.pygame_text import PygameText
from ..tools.music_manager import music_manager
from ..tools.storage import storage

#Робимо клас для Основної сцени гри
class MainScreenScene():
    #Робимо функцію ініт для задання параметрів та основних модулів
    def __init__(self):
        music_manager.music["background_music"].play(loops=-1)

    #Робим метод для початкогово екрану
    def run(self, event : object):
        #Робим фон для початкової сцени
        background_image = PygameImage(
            path = "static/images/great_sea_battle_bg.png",
            coordinates = (0, 0),
            size = (1200, 700)
        )
        #Робим кнопку старт
        move_to_scene = PygameButton(
            path = "static/images/green_button.png",
            text = "Start",
            font_size = 50,
            coordinates = (460, 230),
            size = (128*2, 32*2),
            event = event,
            function = lambda: storage.storage_dict["SceneManager"].change_scene(scene = "conect_to_server")
        )
        move_to_achievement_scene = PygameButton(
            coordinates = (1150, 0),
            size = (50,50),
            event = event,
            function = self.move_to_achievement_scene,
            path = "static/images/achievements_icon.png"
        )
        logo_text1 = PygameText(
            text = "Great Sea",
            font_size = 150,
            x = 280,
            y = 330,
            font = "static/fonts/alagard.ttf",
            color = (34, 32, 52)
        )
        logo_text2 = PygameText(
            text = "Battle",
            font_size = 150,
            x = 400,
            y = 450,
            font = "static/fonts/alagard.ttf",
            color = (34, 32, 52)
        )
        

    def move_to_achievement_scene(self):  
        storage.storage_dict["SceneManager"].change_scene(scene = "achievement")    