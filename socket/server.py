import socket
import threading


def get_host_ip():
    global s
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


PORT = 6060
SERVER = get_host_ip()
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = 'UTF-8'
DISCONNECT_MSG = 'QUIT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f'{addr} connected...')
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False
            print(f'Receive msg :{msg} from {addr}')

    conn.close()


def start():
    server.listen()
    print(f'Server is listening on {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client(conn, addr))
        thread.start()
        print(f'Active thread:{threading.activeCount() - 1}')


print("Server is starting")
start()
