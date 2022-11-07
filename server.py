import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 2134))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been estabilished!")
    clientsocket.send(bytes("Welcome to this server", "utf-8"))
