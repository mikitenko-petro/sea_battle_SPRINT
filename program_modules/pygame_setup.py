# create pygame screen 800x600
import pygame

def start_game():
    pygame.init()
    game = True
    screen = pygame.display.set_mode(size = (800, 600))
    background_image = pygame.image.load("static/images/great_sea_battle_bg.png")
    background_image = pygame.transform.scale(background_image, (800, 600))
    bg_rect = background_image.get_rect()
    screen.blit(background_image, bg_rect)
    pygame.display.update()


    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        
        pygame.display.flip()

