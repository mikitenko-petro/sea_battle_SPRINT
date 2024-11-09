import socket
import io

with socket.socket(family= socket.AF_INET, type= socket.SOCK_STREAM) as client_socket:
    client_socket.connect(("192.168.0.196", 8081))
    message = "I am connect"
    client_socket.sendall(message.encode('utf-8'))
    