from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_button import PygameButton
from ..widgets.pygame_text import PygameText
from ..tools.storage import storage
from ..tools.music_manager import music_manager
from ..client import Client

#Створюємо клас для створення екрану для під'єднання до серверу
class EndScreenScene():
    def __init__(self):
        pass

    #Створюємо метод для створення підключення до сервера
    def run(self, event):
        if storage.storage_dict['win']:
            win_background_image = PygameImage(
                path = "static/images/victory_bg.png",
                coordinates = (0, 0),
                size = (1200, 700)
            )

            win_text = PygameText(
                text = "VICTORY",
                font_size = 200,
                x = 200,
                y = 300,
                font = "static/fonts/alagard.ttf",
                color = (251, 228, 76)
            )
            
        else:
            defeat_background_image = PygameImage(
                path = "static/images/defeat_bg.png",
                coordinates = (0, 0),
                size = (1200, 700)
            )

            defeat_text = PygameText(
                text = "DEFEAT",
                font_size = 200,
                x = 220,
                y = 300,
                font = "static/fonts/alagard.ttf",
                color = (69, 69, 69)
            )

        return_to_home_button = PygameButton(
            path = "static/images/green_button.png",
            text = "return",
            font_size = 50,
            coordinates = (460, 600),
            size = (128*2, 32*2),
            event = event,
            function = self.end_of_work
        )

    def end_of_work(self):
        storage.storage_dict["Client"].listening = False
        storage.storage_dict["Client"].client_socket.close()
        storage.storage_dict["Client"] = Client()

        storage.storage_dict["defeated_ship"] = 0
        storage.storage_dict["defeated_cells"] = 0

        if storage.storage_dict["win"]:
            storage.storage_dict["StatsManager"].stats_dict["winned_games"] += 1

        storage.storage_dict['win'] = None
        storage.storage_dict["dummy_ship_list"] = []
        storage.storage_dict["defeated_ship_list"] = []
        storage.storage_dict["moves"] = 0

        storage.storage_dict['DataManager'].data["shoot_coord"] = []
        storage.storage_dict["DataManager"].data["defeated_ship"] = []

        storage.storage_dict['medals'] = 0

        for ability in storage.storage_dict["AbilityManager"].ability_dict:
            storage.storage_dict["AbilityManager"].ability_dict[ability].amount = 0

        for quest in storage.storage_dict["QuestManager"].quests_list:
            quest.quest_complite = False

        music_manager.music["battle_music"].stop()
        music_manager.music["background_music"].play(loops=-1)
        storage.storage_dict["SceneManager"].change_scene(scene = "main")