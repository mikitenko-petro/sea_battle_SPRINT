from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_label import PygameLabel
from ..game_widgets.fire_animation_widget import FireAnimationWidget
from ..tools.pygame_storage import pygame_storage
from ..game_modules.ship_manager import ShipManager
from ..game_modules.main_game_manager import MainGameManager
from ..game_widgets.capitan_icon import CapitanIcon

#Робим клас для ігрвого вікна
class GameScreneScene():
    #Робим метод ініт для задання пареммрів та модулів
    def __init__(self):
        pygame_storage.storage_dict["can_highlight_ship"] = False
        pygame_storage.add_variable({"ENEMY_GRID" : None})
        
        # self.blue_capitan = CapitanIcon(
        #     color = "blue",
        #     coordinates = (0, 0),
        #     size = (128, 128)
        # )

    #Робим метод для створення екрану гри
    def run(self, event : object):
        pygame_storage.storage_dict["collision_list"] = []

        pygame_storage.add_variable(
            {"MainGameManager" : MainGameManager()}
        )

        #Робим фон
        background_image = PygameImage(
            path = "static/images/sea_bg.png",
            coordinates = (0, 0),
            size = (1200, 700)
        )

        # self.blue_capitan.draw()

        pygame_storage.storage_dict["PLAYER_GRID"].show_grid(event)
        pygame_storage.storage_dict["PLAYER_GRID"].x = 50
        pygame_storage.storage_dict["PLAYER_GRID"].y = 150

        pygame_storage.storage_dict["ENEMY_GRID"].show_grid(event)

        ship_manager = ShipManager(
            event = event
        )

        pygame_storage.storage_dict["MainGameManager"].event_manager()

        player_fire_animation_widget = FireAnimationWidget(type = "player")
        player_fire_animation_widget.create_fire_animation()
        
        enemy_fire_animation_widget = FireAnimationWidget(type = "enemy")
        enemy_fire_animation_widget.create_fire_animation()

        turn_label = PygameLabel(
            path = "static/images/blue_button.png",
            coordinates = (500, 10),
            size = (128*2, 32*2),
            text = (lambda: "your turn" if pygame_storage.storage_dict["player_turn"] else "enemy turn")(),
            font_size = 40
        )