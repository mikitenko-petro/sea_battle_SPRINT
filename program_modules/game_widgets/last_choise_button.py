from ..pygame_storage import pygame_storage
from ..json_manager import read_json, write_json
from ..widgets.pygame_button import PygameButton

class LastChoiceButton():
    def __init__(self, content_type, screen, x, y):
        self.screen = screen
        self.content_type = content_type
        self.x = x
        self.y = y

    def show_button(self, event):
        try:
            data = read_json("static/json/ip_and_port.json")
        
            button = PygameButton(
                coordinates = (self.x + 10, self.y + 10 + 90),
                size = (130, 90),
                event = event,
                function = None,
                text = data[self.content_type],
                path = "static/images/grey_label.png",
                screen = self.screen
            )
            
        except Exception as error:
            print(error)
        
    def create_json(self, content):
        try:
            data: dict = read_json(path = "static/json/ip_and_port.json")
        except:
            data = {}

        if self.content_type == "IP":            
            data.update({"IP": content})
            
        if self.content_type == "PORT":
            data.update({"PORT": content})

        write_json(path = "static/json/ip_and_port.json", data = data)