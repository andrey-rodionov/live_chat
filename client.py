import socket
import threading

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM #TCP/IP
)

client.connect(
    ("127.0.0.1", 1234)  # localhost
)

def listen_server():
    while True:
        data = client.recv(2048)
        print(data.decode("utf-8"))


def send_all():
    listen_thread = threading.Thread(target=listen_server)
    listen_thread.start()

    while True:
        client.send(input("Me:").encode("utf-8"))

if __name__ == '__main__':
    send_all()