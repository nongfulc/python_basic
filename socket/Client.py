import socket

PORT = 6060
HEADER = 64
FORMAT = 'UTF-8'
DISCONNECT_MSG = 'QUIT'
SERVER = '172.17.30.26'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


send("Hello Server")
send(DISCONNECT_MSG)
