from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_text import PygameText
from ..widgets.pygame_label import PygameLabel
from ..widgets.pygame_text_input import PygameTextInput

#Створюємо клас для створення екрану для під'єднання до серверу
class ConectToServerScreenScene():
    #Робим метод
    def __init__(self, screen, scene_manager, pygame_storage):
        self.screen = screen
        self.pygame_storage = pygame_storage
        self.pygame_storage.add_variable({"IP" : ""})
    #Створюємо метод для створення підключення до сервера
    def run(self, event):
        #Робим фон для екрану підключення до сервера
        background_image = PygameImage(
        screen = self.screen,
        path = "static/images/lighthouse_bg.png",
        coordinates = (0, 0),
        size = (1200, 700))
        #Робимо строку вводу для айпі
        text_input_ip = PygameTextInput(
        size = (384, 96),
        coordinates = (600, 250),
        event = event,
        screen = self.screen,
        pygame_storage = self.pygame_storage,
        name = "ip",
        store_to = "IP",
        initial_text = "enter your ip")
        #Відображуємо айпі
        ip_label = PygameLabel(
        screen = self.screen,
        path = "static/images/casual_label.png",
        coordinates = (10, 250),
        size = (128*2.5, 32*2),
        text = f"your IP: {self.pygame_storage.storage_dict['IP']}",
        font = None,
        font_size = 40)
        #Робимо строку вводу для порту
        text_input_port = PygameTextInput(
        size = (384, 96),
        coordinates = (600, 450),
        event = event,
        screen = self.screen,
        pygame_storage = self.pygame_storage,
        name = "port",
        store_to = "PORT",
        initial_text = "enter your port")
        #Відображуємо порт
        port_label = PygameImage(
        screen = self.screen,
        path = "static/images/casual_label.png",
        coordinates = (10, 450),
        size = (128*2.5, 32*2))
        #Текст для порту
        port_text = PygameText(
        screen = self.screen,
        text = f"your PORT: {self.pygame_storage.storage_dict['PORT']}",
        font = None,
        font_size = 40,
        x = 10 + 10,
        y = 250 + 220)