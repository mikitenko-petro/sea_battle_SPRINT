import json

def write_json(json_path : str):
    with open(json_path, "w") as file:
        json.dump(json_path, file)

def read_json(json_path : str):
    with open(json_path, "r") as file:
        data = json.load(file)
        return data