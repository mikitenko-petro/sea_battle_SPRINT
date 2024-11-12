# create pygame screen 800x600
import pygame
from .widgets.pygame_image import PygameImage
from .widgets.pygame_button import PygameButton

def start_game():
    pygame.init()
    game = True
    screen = pygame.display.set_mode(size = (800, 600))
    background_image = PygameImage(screen, "sea_battle_SPRINT/static/images/great_sea_battle_bg.png", (800, 600))
    start_button = PygameButton(screen, "sea_battle_SPRINT/static/images/start_button.png", (150, 50))
    pygame.display.update()

    while game:
        #print("work")
        
        for event in pygame.event.get():
            start_button.click_checking(event)
            if event.type == pygame.QUIT:
                game = False
        
        pygame.display.flip()

