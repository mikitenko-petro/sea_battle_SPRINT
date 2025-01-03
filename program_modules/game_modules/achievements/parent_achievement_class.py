class Achievement():
    def __init__(self):
        self.name = ""
        self.description = ""
        self.is_complete = False
        self.complete_count = 0

    def change_complete(self):
        self.is_complete = True