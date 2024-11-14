# create pygame screen 800x600
import pygame
from .widgets.pygame_image import PygameImage
from .widgets.pygame_button import PygameButton
from .widgets.main_screen_scene import MainScreenScene

class Game():
    def __init__(self) -> None:

        self = pygame.init()
        game = True
        screen = pygame.display.set_mode(size = (800, 600))

        while game:
            event = pygame.event.get()
            main_screen = MainScreenScene(screen, event)

            for pygame_event in event:
                if pygame_event.type == pygame.QUIT:
                    game = False

            pygame.display.update()
            pygame.display.flip()
        

def start_game(): 
    game = Game()

