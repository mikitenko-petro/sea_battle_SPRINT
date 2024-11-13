# create pygame screen 800x600
import pygame
from .widgets.pygame_image import PygameImage
from .widgets.pygame_button import PygameButton

class Game():
    def __init__(self) -> None:

        self = pygame.init()
        game = True
        screen = pygame.display.set_mode(size = (800, 600))
        background_image = PygameImage(screen, "static/images/great_sea_battle_bg.png", (0, 0), (800, 600))
        start_button = PygameImage(screen, "static/images/start_button.png", (100, 100), (100, 40))
        

        # start_button = PygameButton(screen, "static/images/start_button.png", (150, 50))
        pygame.display.update()

        while game:
            action_list = [background_image.draw(), start_button.draw()]
            
            for event in pygame.event.get():
                # start_button.click_checking(event)
                if event.type == pygame.QUIT:
                    game = False
            
            pygame.display.flip()
        

def start_game():
    game = Game()

