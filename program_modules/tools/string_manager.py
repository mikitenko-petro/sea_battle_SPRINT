def read_string(string : str) -> list:
    try:
        return string.split(";")[:-1]
    except:
        return []

def write_string(*args) -> str:
    string = ""
    for argument in args:
        string += f"{argument};"
    return string