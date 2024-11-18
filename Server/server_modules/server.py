import socket
import pickle
import io
import os

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

def start_server(cell: tuple):
    with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as server_socket:
        # зв'язуємо socket з IP та портом
        server_socket.bind(("SERVER_IP", 8082))
        #Переводить socket в режим очікування
        
        
        server_socket.listen()
        print("connecting ... ")
        # Очікує та приймає підключення клієнту
        client_socket, adress = server_socket.accept()
        print("connected", adress)
        row, column = cell
        sea[row-1][column-1] = "X"
        message = pickle.dumps(sea)
        data = client_socket.recv(1024)
        if data:
            print(data.decode("utf-8"))
        while True:
            data = client_socket.recv(1024)
            if data:
                print(pickle.loads(data))
            if input('Go?') == "yes":
                client_socket.sendall(message)
                print(f"send: {sea}" )
start_server((1, 1))