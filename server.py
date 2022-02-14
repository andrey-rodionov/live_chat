import socket
from threading import Thread

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM # TCP/IP
)

server.bind(
    ("127.0.0.1", 1234) # localhost
)

server.listen(10) # 10 active connections
users = []
print("Server is listening")

def start_server():
    while True:
        user_socket, address = server.accept()
        print(f"User <{address[0]}> connected") # get client's IP address
        users.append(user_socket)
        listen_accepted_user = Thread(
            target=listen_user,
            args=(user_socket,)
        )

        listen_accepted_user.start()
        listen_accepted_user.join()

def listen_user(user):
    while True:
        data = user.recv(2048)
        print(f"User sent {data}")
        send_all(data)

def send_all(data):
    for user in users:
        user.send(data)




if __name__ == '__main__':
    start_server()