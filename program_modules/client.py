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
        client_socket.connect(("192.168.0.196", 8081))
        #data = client_socket.recv(1024)
        row, column = cell
        sea[row-1][column-1] = "X"
        message = pickle.dumps(sea)
        while True:
            if input('Go?') == "yes":
                client_socket.sendall(message)
                print(f"send: {sea}" )
client((3, 5))            