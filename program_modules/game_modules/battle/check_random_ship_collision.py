from ...widgets.pygame_rect import PygameRect
from ...tools.pygame_storage import pygame_storage

class CheckRandomShipCollision():
    def __init__(self, direction, x, y, type, id):
        self.type = type
        self.direction = direction
        self.delta_x = 0
        self.delta_y = 0
        self.id = id
        
        match self.direction:
            case "top":
                self.delta_x = 0 
                match type:
                    case "1x1":
                        self.delta_y = 0 
                    case "2x1":
                        self.delta_y = 50    
                    case "3x1":
                        self.delta_y = 100   
                    case "4x1":
                        self.delta_y = 150   
            case "bottom":
                self.delta_y = 0
                self.delta_x = 0 
            case "right":
                self.delta_y = 0
                self.delta_x = 0
            case "left":
                self.delta_y = 0 
                match type:
                    case "1x1":
                        self.delta_x = 0 
                    case "2x1":
                        self.delta_x = 50    
                    case "3x1":
                        self.delta_x = 100   
                    case "4x1":
                        self.delta_x = 150
            
        if self.direction == "top" or self.direction == "bottom":
            self.width = 50
            match type:
                case "1x1":
                    self.height = 50
                case "2x1":
                    self.height = 100
                case "3x1":
                    self.height = 150
                case "4x1":
                    self.height = 200
        elif self.direction == "left" or self.direction == "right":
            self.height = 50
            match type:
                case "1x1":
                    self.width = 50
                case "2x1":
                    self.width = 100
                case "3x1":
                    self.width = 150
                case "4x1":
                    self.width = 200
    
        self.ship_collision_rect = PygameRect(
            coordinates = (x - self.delta_x + 2, y - self.delta_y + 2),
            size = (self.width - 4, self.height - 4),
            color = (255, 0, 0)
        )
        
        self.ship_buffer_rect = PygameRect(
            coordinates = (x - self.delta_x - 50 + 2, y - self.delta_y - 50 + 2),
            size = (self.width + 100 - 4, self.height + 100 - 4),
            color = (255, 0, 0)
        )

    def check_ship_collision(self):
        collision_list = []

        for collision in pygame_storage.storage_dict["collision_list"]:
            collision_list.append(collision)

        try:
            if self.ship_collision_rect.collidelist(collision_list) != -1:
                return True
        except:
            pass

        collision_list = []

        for ship in pygame_storage.storage_dict["ship_list"]:
            if hasattr(ship, "buffer_rect") == True:
                if ship.id != self.id:
                    collision_list.append(ship.buffer_rect)

        for collision in collision_list:
            if self.ship_collision_rect.collidelist(collision_list) != -1:
                return True
            
        return False
            
def check_random_ship_collision(direction, row, column, type, id):
    x = pygame_storage.storage_dict["PLAYER_GRID"].x + column*50
    y = pygame_storage.storage_dict["PLAYER_GRID"].y + row*50

    random_ship_collision = CheckRandomShipCollision(direction, x, y, type, id)

    is_hit = random_ship_collision.check_ship_collision()
    
    del random_ship_collision
    return is_hit