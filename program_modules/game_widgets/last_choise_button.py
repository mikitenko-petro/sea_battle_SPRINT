from ..tools.pygame_storage import pygame_storage
from ..tools.json_manager import read_json, write_json
from ..widgets.pygame_button import PygameButton
import pygame

class LastChoiceButton():
    def __init__(self, content_type, screen, x, y, event):
        self.screen = screen
        self.content_type = content_type
        self.x = x
        self.y = y
        self.event = event
        pygame_storage.add_variable({"show_last_button_type" : None})

        if pygame_storage.storage_dict["show_last_button_type"] == content_type:
            try:
                data = read_json("static/json/ip_and_port.json")

                button = PygameButton(
                    coordinates = (self.x, self.y),
                    size = (364, 76),
                    event = self.event,
                    function = lambda : self.text(),
                    text = data[self.content_type],
                    path = "static/images/grey_label.png",
                    screen = self.screen,
                    font_size = 50
                )

            except Exception as error:
                if pygame_storage.storage_dict["debug"]: 
                    print(error)
    
    def show_button(self, x, y, width, height):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        for pygame_event in self.event: 
            if mouse_x >= x and mouse_x <= x + width:
                if mouse_y >= y and mouse_y <= y + height:
                    if pygame_event.type == pygame.MOUSEBUTTONDOWN:
                        if self.content_type == "IP":
                            pygame_storage.storage_dict["show_last_button_type"] = "IP"
                        elif self.content_type == "PORT":
                            pygame_storage.storage_dict["show_last_button_type"] = "PORT"
        
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
    
    def text(self):
        data = read_json("static/json/ip_and_port.json")
        
        if self.content_type == "IP":
            pygame_storage.storage_dict['IP'] = data[self.content_type]

        elif self.content_type == "PORT":
            pygame_storage.storage_dict['PORT'] = data[self.content_type]

        pygame_storage.storage_dict["show_last_button_type"] = None