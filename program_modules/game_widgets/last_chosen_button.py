import pygame
from ..pygame_storage import pygame_storage
from ..json_manager import read_json, write_json
from ..widgets.pygame_button import PygameButton
from ..widgets.pygame_label import PygameLabel

class LastSessions():
    def __init__(self, content_type, screen, x, y, height, ip = None, port = None):
        self.ip = ip
        self.port = port
        self.json = "static/json/ip_and_port.json"
        self.screen = screen
        self.x = x
        self.y = y + height
        self.content_type = content_type
        if content_type == "ip":
            self.create_json(self.ip)
        if content_type == "port":
            self.create_json(self.ip)

    def create_last_sesion_lable(self, event):
        data = read_json(self.json)

        background_label = PygameLabel(
            screen = self.screen,
            path = "static/images/grey_label.png",
            coordinates = (self.x, self.y),
            size = (150, 300),
            text = "a"
        )
        
        for index in range(len(data[self.content_type])):
            button = PygameButton(
                coordinates = (self.x + 10, self.y + 10 + 90*index),
                size = (130, 90),
                event = event,
                fuction = None,
                text = data[self.content_type][index],
                path = "static/images/green_button.png",
                screen = self.screen
            )
        
    def create_json(self, ip, port):
        self.sesions = read_json(self.json)

        if self.content_type == "ip":            
            data = {"ip": [ip, ip, ip]}
            self.sesions["ip"] = data
            
        if self.content_type == "port":
            data = {"port": [port, port, port]}
            self.sesions["port"] = data

        if len(self.sesions) > 3:
            self.sesions = self.sesions[:3]

        write_json(self.json)