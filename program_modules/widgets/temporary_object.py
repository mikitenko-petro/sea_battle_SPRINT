from ..tools.storage import storage

class TemporaryObject():
    def __init__(
        self,
        miliseconds : int,
        object_list : list):

        self.miliseconds = miliseconds
        self.object_list = object_list
        self.step = 0
        
    def show(self):
        if self.step <= self.miliseconds:
            for object in self.object_list:
                object.display()
            
            self.step += storage.storage_dict["clock"].get_time()