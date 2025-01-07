from ...widgets.pygame_image import PygameImage
from ...tools.storage import storage

class DummyShip():
    def __init__(self, id, direction, row, column, type):
        self.id = id
        self.direction = direction
        self.x = storage.storage_dict["ENEMY_GRID"].x + column*50
        self.y = storage.storage_dict["ENEMY_GRID"].y + row*50
        self.type = type

    def show_ship(self):    
        match self.direction:
            case "top":
                delta_x = 0
                angle = 0
                match self.type:
                    case "1x1":
                        delta_y = 0
                    case "2x1":
                        delta_y = 50
                    case "3x1":
                        delta_y = 100
                    case "4x1":
                        delta_y = 150

            case "bottom":
                delta_y = 0
                delta_x = 0
                angle = 180

            case "right":
                delta_y = 0
                delta_x = 0
                angle = 90
                
            case "left":
                delta_y = 0
                angle = 270
                match self.type:
                    case "1x1":
                        delta_x = 0
                    case "2x1":
                        delta_x = 50
                    case "3x1":
                        delta_x = 100
                    case "4x1":
                        delta_x = 150

        image_width = 50
        match self.type:
            case "1x1":
                path = "static/images/ship1X1defeated.png"
            case "2x1":
                path = "static/images/ship2X1defeated.png"
            case "3x1":
                path = "static/images/ship3X1defeated.png"
            case "4x1":
                path = "static/images/ship4X1defeated.png"

        match self.type:
            case "1x1":
                image_height = 50
            case "2x1":
                image_height = 100
            case "3x1":
                image_height = 150
            case "4x1":
                image_height = 200
                
        ship_image = PygameImage(
            path = path,
            coordinates = (self.x - delta_x, self.y - delta_y),
            size = (image_width, image_height),
            angle = angle
        )