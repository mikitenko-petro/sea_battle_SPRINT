import pygame

#
class PygameImage():
    def __init__(self, screen, path, size):
        image = pygame.image.load(path)
        image = pygame.transform.scale(image, size)
        image_rect = image.get_rect()
        screen.blit(image, image_rect)
        
