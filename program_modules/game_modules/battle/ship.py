from ...widgets.pygame_image import PygameImage
from ...widgets.pygame_hitbox import PygameHitBox
from ...widgets.pygame_button import PygameButton
from ...tools.music_manager import music_manager
from ...tools.storage import storage
from ...game_widgets.ship_buttons.turn_button import TurnButton
from ...game_widgets.ship_buttons.return_button import ReturnButton
from ...widgets.pygame_rect import PygameRect
from ...tools.string_manager import write_string

class Ship():
    def __init__(self, type, id):
        self.type = type
        self.status = "unplaced"
        self.direction = "right"
        self.is_picked = False
        self.row = -1
        self.column = -1
        self.path = ""
        self.id = id
        self.delta_x = 0
        self.delta_y = 0
        
        PygameHitBox.__init__(self, (0,0), (50,50))

        self.change_direction()

    def change_direction(self):
        match self.type:
            case "1x1":
                self.path = "static/images/ship1X1.png"

            case "2x1":
                self.path = "static/images/ship2X1.png"

            case "3x1":
                self.path = "static/images/ship3X1.png"

            case "4x1":
                self.path = "static/images/ship4X1.png"

        match self.direction:
            case "top":
                self.delta_x = 0

                self.angle = 0

                match self.type:
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

                self.angle = 180

            case "right":
                self.delta_y = 0
                self.delta_x = 0
        
                self.angle = 90

            case "left":
                self.delta_y = 0

                self.angle = 270

                match self.type:
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
            match self.type:
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
            match self.type:
                case "1x1":
                    self.width = 50

                case "2x1":
                    self.width = 100

                case "3x1":
                    self.width = 150

                case "4x1":
                    self.width = 200
    
    def show_ship(self, event, x, y):
        self.x = x
        self.y = y

        self.image_width = 50

        if self.is_picked == True:
            match self.type:
                case "1x1":
                    self.path = "static/images/ship1X1selected.png"

                case "2x1":
                    self.path = "static/images/ship2X1selected.png"

                case "3x1":
                    self.path = "static/images/ship3X1selected.png"

                case "4x1":
                    self.path = "static/images/ship4X1selected.png"

        else:
            match self.type:
                case "1x1":
                    self.path = "static/images/ship1X1.png"

                case "2x1":
                    self.path = "static/images/ship2X1.png"

                case "3x1":
                    self.path = "static/images/ship3X1.png"

                case "4x1":
                    self.path = "static/images/ship4X1.png"

        if self.status == "defeated":
            match self.type:
                case "1x1":
                    self.path = "static/images/ship1X1defeated.png"

                case "2x1":
                    self.path = "static/images/ship2X1defeated.png"

                case "3x1":
                    self.path = "static/images/ship3X1defeated.png"

                case "4x1":
                    self.path = "static/images/ship4X1defeated.png"

        match self.type:
            case "1x1":
                self.image_height = 50

            case "2x1":
                self.image_height = 100

            case "3x1":
                self.image_height = 150

            case "4x1":
                self.image_height = 200

        self.ship_image = PygameImage(
            path = self.path,
            coordinates = (x - self.delta_x, y - self.delta_y),
            size = (self.image_width, self.image_height),
            angle = self.angle
        )
        
        self.ship_collision_rect = PygameRect(
            coordinates = (x - self.delta_x + 2, y - self.delta_y + 2),
            size = (self.width - 4, self.height - 4),
            color = (255, 0, 0)
        )

        if storage.storage_dict["SceneManager"].current_scene == "prepare_to_game":
            if self.status == "placed":
                self.buffer_rect = PygameRect(
                    coordinates = (x - self.delta_x - 50 + 2, y - self.delta_y - 50 + 2),
                    size = (self.width + 100 - 4, self.height + 100 - 4),
                )
            else:
                if hasattr(self, "buffer_rect") == True:
                    delattr(self, "buffer_rect")

            self.draw_buttons(event = event)

        else:
            if hasattr(self, "buffer_rect") == True:
                delattr(self, "buffer_rect")
        
    def highlight_ship(self):
        if storage.storage_dict["SceneManager"].current_scene == "prepare_to_game":
            if self.is_picked == False and storage.storage_dict["picked_ship"] == -1:
                self.is_picked = True
                storage.storage_dict["picked_ship"] = self.id

            elif self.is_picked == True:
                self.is_picked = False
                storage.storage_dict["picked_ship"] = -1

    def select_ship(self, event):
        ship_button = PygameButton(
            coordinates = (self.x - self.delta_x, self.y - self.delta_y),
            size = (self.width, self.height),
            event = event,
            function = self.highlight_ship
        )

    def draw_buttons(self, event):
        if self.is_picked == True and self.status == "placed":
            x = self.x + 50
            y = self.y - 50
            turn_button = TurnButton((x, y), event, self.id)

            x = self.x + 100
            y = self.y - 50
            return_button = ReturnButton((x, y), event, self.id)
            
    def check_collide(self):
        collision_list = []
        
        for collision in storage.storage_dict["collision_list"]:
            collision_list.append(collision)

        try:
            if self.ship_collision_rect.collidelist(collision_list) != -1:
                self.ship_collision_rect.draw(2)
                storage.storage_dict["check_placement"] = True
        except:
            pass

        collision_list = []

        for ship in storage.storage_dict["ship_list"]:
            if hasattr(ship, "buffer_rect") == True:
                if ship.id != self.id:
                    collision_list.append(ship.buffer_rect)

        for collision in collision_list:
            if self.ship_collision_rect.collidelist(collision_list) != -1:
                self.ship_collision_rect.draw(2)
                storage.storage_dict["check_placement"] = True

        collision_list = []

        for cell in storage.storage_dict["PLAYER_GRID"].cell_list:
            if cell.type == "X":
                collision_list.append(cell.collision)

        collisions = [hitbox for hitbox in collision_list if self.ship_collision_rect.colliderect(hitbox)]
        
        for collision in collision_list:
            if self.ship_collision_rect.collidelist(collision_list) != -1:
                match self.type:
                    case "1x1":
                        if len(collisions) == 1:
                            self.status = "defeated"
                            self.add_defeated_ship()
                    case "2x1":
                        if len(collisions) == 2:
                            self.status = "defeated"
                            self.add_defeated_ship()
                    case "3x1":
                        if len(collisions) == 3:
                            self.status = "defeated"
                            self.add_defeated_ship()
                    case "4x1":
                        if len(collisions) == 4:
                            self.status = "defeated"
                            self.add_defeated_ship()

    def add_defeated_ship(self):
        is_found = False

        for id in storage.storage_dict["defeated_ship_list"]:
            if id != self.id:
                is_found = False
            else:
                is_found = True
                break
        
        #
        if not is_found:
            storage.storage_dict["defeated_ship_list"].append(self.id)
            storage.storage_dict["Client"].send_data(
                write_string("defeated_ship", self.id, self.type, self.direction, self.row, self.column)
            )