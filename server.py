import socket

HEADERSIZE = 1000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 2134))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been estabilished!")

    msg = "Welcome to the server!"
    msg = f'{len(msg):<{HEADERSIZE}}' + msg

    clientsocket.send(bytes(msg, "utf-8"))
    #clientsocket.close()
