from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_text_input import PygameTextInput
from ..widgets.pygame_button import PygameButton
from ..widgets.pygame_rect import PygameRect
from ..game_widgets.tools.last_choise_button import LastChoiceButton
from ..game_modules.battle.grid import Grid
from ..game_modules.battle.ship import Ship
from ..tools.storage import storage

#Створюємо клас для створення екрану для під'єднання до серверу
class ConectToServerScreenScene():
    def __init__(self):
        storage.add_variable({"IP" : "enter your ip"})
        storage.add_variable({"PORT" : "enter your port"})

    #Створюємо метод для створення підключення до сервера
    def run(self, event):
        background_image = PygameImage(
            path = "static/images/lighthouse_bg.png",
            coordinates = (0, 0),
            size = (1200, 700)
        )

        return_button = PygameButton(
            coordinates = (0, 0),
            size = (50, 50),
            event = event,
            path = "static/images/apply_button.png",
            function = lambda: storage.storage_dict["SceneManager"].change_scene(scene = "main")
        )
        
        #Робимо строку вводу для айпі
        connect_to_server_button = PygameButton(
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
            name = "ip",
            store_to = "IP",
            initial_text = "enter your ip"
        )

        self.last_sesion_ip = LastChoiceButton(
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
            name = "port",
            store_to = "PORT",
            initial_text = "enter your port"
        )

        self.last_sesion_port = LastChoiceButton(
            x = 610,
            y = 460-96,
            content_type = "PORT",
            event = event
        )
        
        self.last_sesion_port.show_button(600, 450, 384, 96)

    def connect_to_server(self):
        try:
            storage.storage_dict["Client"].ip = storage.storage_dict['IP']
            storage.storage_dict["Client"].port = int(storage.storage_dict['PORT'])
            storage.storage_dict["Client"].join()
            storage.storage_dict["Client"].get_data_func.start()

            self.last_sesion_ip.create_json(storage.storage_dict['IP'])
            self.last_sesion_port.create_json(storage.storage_dict['PORT'])

            self.prepare_to_game()

            storage.storage_dict["SceneManager"].change_scene(scene = "prepare_to_game")
        except Exception as error:
            print(error)

    def prepare_to_game(self):
        storage.storage_dict["PLAYER_GRID"] = Grid(
            coordinates = (350, 150),
            type = "player",
        )

        storage.storage_dict["ship_list"] = []

        for i in range(10):
            if i < 4:
                storage.storage_dict["ship_list"].append(Ship(type = "1x1", id = i))
            elif i < 7:
                storage.storage_dict["ship_list"].append(Ship(type = "2x1", id = i))
            elif i < 9:
                storage.storage_dict["ship_list"].append(Ship(type = "3x1", id = i))
            else:
                storage.storage_dict["ship_list"].append(Ship(type = "4x1", id = i))

        storage.storage_dict["collision_list"] = [
            PygameRect((350, 100), (500, 50)),
            PygameRect((850, 150), (50, 500)),
            PygameRect((350, 650), (500, 50)),
            PygameRect((300, 150), (50, 500))
        ]