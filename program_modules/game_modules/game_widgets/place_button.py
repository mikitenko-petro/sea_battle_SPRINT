from ...pygame_storage import pygame_storage
from ...widgets.pygame_button import PygameButton

class PlaceButton():
    def __init__(self, screen : object, coordinates : tuple, event : object, id : int):
        self.path = ""

        if True:
            self.path = "static/images/accept_button.png"
        
        place_button = PygameButton(
            coordinates = coordinates, 
            size = (50, 50),
            event = event, 
            function = lambda : self.place(id = id),
            path = "static/images/return_button.png",
            screen = screen
        )
        
    def place(self, id : int):
        ...