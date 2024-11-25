class PygameStorage():
    def __init__(self):
        self.storage_dict = {}

    def add_variable(self, storage_object : object):
        is_found = False
        value_key = list(storage_object.keys())

        for item in self.storage_dict.keys():
            if item != value_key[0]:
                is_found = False
            else:
                is_found = True
                break

        if is_found == False:    
            self.storage_dict.update(storage_object)
