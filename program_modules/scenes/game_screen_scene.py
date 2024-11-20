import pygame
from ..widgets.pygame_image import PygameImage
from ..game_modules.grid import Grid

class GameScreneScene():
    def __init__(self, screen : object, scene_manager : object):
        self.screen = screen
        self.scene_manager = scene_manager
        self.player_grid = Grid()
        self.enemy_grid = Grid()
    def run(self, event : object):
        background_image = PygameImage(
        screen = self.screen,
        path = "static/images/sea_bg.png",
        coordinates = (0, 0),
        size = (1200, 700))
        
        enemy_cell_x = 0
        enemy_cell_y = 0

        player_cell_x = 0
        player_cell_y = 0


        for row in self.player_grid.grid:
            for column in row:
                if column == '':
                    cell = PygameImage(
                        screen = self.screen,
                        path = "static/images/cell.png",
                        coordinates = (50 + player_cell_x, 150 + player_cell_y),
                        size = (50, 50))
                    
                player_cell_x += 50
            player_cell_y += 50
            player_cell_x = 0

        for row in self.enemy_grid.grid:
            for column in row:
                if column == '':
                    cell = PygameImage(
                        screen = self.screen,
                        path = "static/images/cell.png",
                        coordinates = (650 + enemy_cell_x, 150 + enemy_cell_y),
                        size = (50, 50))
                    
                enemy_cell_x += 50
            enemy_cell_y += 50
            enemy_cell_x = 0

        for ship_x in range(4): 
            ship = PygameImage(
                coordinates = (150 + ship_x*50, 50),
                size = (50, 50),
                screen = self.screen,
                path ="static/images/ship1X1.png"
            )

            