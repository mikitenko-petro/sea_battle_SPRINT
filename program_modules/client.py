import socket

#Робимо клас для клієнта
class Client():
    def __init__(self, ip : str, port : int):
        self.client_socket = socket.socket(family= socket.AF_INET, type= socket.SOCK_STREAM)
        self.ip = ip    
        self.port = port
        self.player_type = 0
    
    #Робимо метод для під'єднання клієнта
    def join(self):
        self.client_socket.connect((self.ip, self.port))

        #Робимо змінну для зберігання клієнтів
        check_list = self.client_socket.recv(1024).decode("utf-8")

        #Робимо умову
        if check_list == "1":
            self.player_type = "1"
        else:
            self.player_type = "2"

    #Робимо метод для отримання даних         
    def get_data(self):
        data = self.client_socket.recv(1024)
        if data:
            return data.decode("utf-8")

    #Робимо метод для відправлення даних
    def send_data(self, data : str):
        self.client_socket.sendall(data.encode("utf-8"))