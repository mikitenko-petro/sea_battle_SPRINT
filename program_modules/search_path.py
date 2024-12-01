import os

#Робим функцію для пошуку абсолютного шляху
def search_path(file_name : str):
    base_path = os.path.abspath(".")
    path = os.path.join(base_path, file_name)
    return path