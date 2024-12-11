def read_string(string : str):
    try:
        return string.split(";")[:-1]
    except:
        return []

def write_string(*args):
    string = ""
    for argument in args:
        string += f"{argument};"
    return string