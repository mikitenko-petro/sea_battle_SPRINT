from ...tools.storage import storage

class RadioSetAnimation():
    def __init__(self):
        storage.add_variable({"radio_set_animation_list": []})

    def show(self):
        for animation in storage.storage_dict["radio_set_animation_list"]:
            animation.display()