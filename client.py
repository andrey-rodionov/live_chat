import socket
from datetime import datetime
from os import system
import threading

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM  #TCP/IP
)

def setup_connection():
    try:
        client.connect(
            ("127.0.0.1", 1234)  # localhost
        )

    # put an exception to show users that server is not ready to work, and they should run server.py first
    except OSError:
        print("Sorry, our tiny server is not available\n"
              "Please, try later")
        exit(0)

def listen_server():
    messages = ""
    while True:
        try:
            data = client.recv(2048)
            messages += f"{datetime.now().date()}" + ": " + data.decode('utf-8') + "\n"
            system("cls") # "cls" helps us to avoid duplicate lines
            print(messages)

        # put an exception to inform users about server's disconnect
        except ConnectionResetError:
            print("\n"
                  "Oops! Server is not available anymore....\n"
                  "Please, restart server and try again")
            return

def send_all():
    listen_thread = threading.Thread(target=listen_server)
    listen_thread.start()

    while True:
        client.send(input("").encode("utf-8"))

if __name__ == '__main__':
    setup_connection()
    send_all()
