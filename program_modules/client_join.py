import socket
import pickle
import io
import time

sea = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",]]
def client(cell: tuple):
    with socket.socket(family= socket.AF_INET, type= socket.SOCK_STREAM) as client_socket:
        client_socket.connect(("192.168.0.196", 8082))
        #data = client_socket.recv(1024)
        row, column = cell
        sea[row-1][column-1] = "X"
        message = pickle.dumps(sea)
        #client_socket.sendall("check".encode("utf-8"))
        while True:
            data = client_socket.recv(1024)
            if data:
                print(pickle.loads(data))
            if input('Go?') == "yes":
                client_socket.sendall(message)
                print(f"send: {sea}" )
client((2, 2))   