from .game_widgets.collision import Collision
from ..pygame_storage import pygame_storage
from ..music_manager import music_manager

def check_hit_collision(screen, row, column):
    check_collision = Collision(
        screen = screen,
        coordinates = (
            pygame_storage.storage_dict["PLAYER_GRID"].x + column*50 + 25,
            pygame_storage.storage_dict["PLAYER_GRID"].y + row*50 + 25
            ),
        size = (1,1),
        type = "check_collision"
    )

    collision_list = []
    is_hit = False

    for ship in pygame_storage.storage_dict["ship_list"]:
        collision_list.append(ship.ship_collision_rect)

    for collision in collision_list:
        if check_collision.rect.colliderect(collision):
            music_manager.music_dict["hit_effect"].play()
            is_hit = True
            break

    del check_collision

    print(is_hit)
    return is_hit