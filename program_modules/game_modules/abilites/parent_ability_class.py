from ...tools.storage import storage

class Ability():
    def __init__(self):
        self.title = None
        self.image_path = None
        self.description = None
        self.name = self.__class__.__name__
        self.amount = 0
        self.price = 0
    
    def buy(self):
        if storage.storage_dict["medals"] >= self.price:
            self.amount += 1
            storage.storage_dict["medals"] -= self.price

    def usage(func):
        def handle(self, **kwargs):
            if self.amount > 0:
                if kwargs.get("row") and kwargs.get("column"):
                    func(self, kwargs["row"], kwargs["column"])
                else:
                    func(self)

                self.amount -= 1
                storage.storage_dict["player_turn"] = False
                storage.storage_dict["AbilityManager"].picked_ability = None

        return handle