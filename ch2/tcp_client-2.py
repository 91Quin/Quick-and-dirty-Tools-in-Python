import socket

# for test
import time


Host = "1.15.148.126"
Port = 9998


def client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((Host, Port))
    str = "Now time is: " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    client.send(bytes(str.encode("utf-8")))  # I feel that I am coooool!
    response, address = client.recvfrom(4096)
    client.close()
    print(response.decode("utf-8"))


while True:
    client()
