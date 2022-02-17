import socket
import threading

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM  # TCP/IP
)

server.bind(
    ("127.0.0.1", 1234)  # localhost
)

server.listen(10)  # 10 active connections
users = []
print("Server is ready")

def listen_user(user):
    while True:
        try:
            message = user.recv(2048)
            print("Got message from " + f"{message}")
            send_all(message)

        # put an exception to show that someone left chatroom
        except ConnectionResetError:
            users.remove(user)
            print("Someone left chat")
            return

def send_all(data):
    for user in users:
        user.send(data)

def start_server():
    while True:
        user_socket, address = server.accept()
        print(f"User <{address[0]}> connected")  # get client's IP address
        user_socket.send("CONNECTED \n"
                         "===========================================================\n"
                         "= Welcome to the smallest anonymous chat around Internet! =\n"
                         "===========================================================\n".encode("utf-8"))
        users.append(user_socket)
        listen_accepted_user = threading.Thread(
            target=listen_user,
            args=(user_socket,)
        )

        listen_accepted_user.start()

if __name__ == '__main__':
    start_server()